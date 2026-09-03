#!/usr/bin/env python3
"""
Apply the DevCommX blog schema date fix directly against the Webflow API.

Self-contained: fetches every item in the Blog collection, computes the correct
dates, patches BOTH schema locations, verifies each write round-trips, and
publishes the live items it changed.

Why this exists: the Webflow MCP connector is the only write path from a Claude
session, and it needs every field value retyped as a literal tool argument. That
is ~1.8MB of blog HTML for this fix, which is slow and risks silently corrupting a
live post. This script moves the same bytes mechanically instead.

    export WEBFLOW_TOKEN=...        # Site token with CMS read/write
    python3 apply_schema_date_fix.py --dry-run     # audit + show the plan
    python3 apply_schema_date_fix.py --apply       # patch, verify, publish

What it changes, per item, and nothing else:
    schema-markup   datePublished / dateModified values only
    post-body       the same two values inside the embedded JSON-LD script
                    (adds the embed if missing, resyncs it if it had drifted)
    last-updated    set equal to dateModified so the page cannot contradict schema

Rules:
    datePublished = the item's CMS `date` field, the real publish date
    dateModified  = the item's real last modification (lastPublished / lastUpdated);
                    where that equals the publish date, meaning the post was never
                    edited after publishing, today is used so the two dates differ
"""
import os, sys, json, time, argparse, datetime, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fix_schema_dates import build, verify   # single source of truth for the logic

API = "https://api.webflow.com/v2"
COLLECTION = "689c92652a4b35f0e9a14fc2"


def req(method, path, token, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(API + path, data=data, method=method, headers={
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "content-type": "application/json",
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read() or "{}")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                wait = 2 ** attempt
                print(f"    {e.code}, retrying in {wait}s", file=sys.stderr)
                time.sleep(wait); continue
            raise SystemExit(f"HTTP {e.code} on {method} {path}: {e.read().decode()[:400]}")
    raise SystemExit(f"gave up on {method} {path}")


def fetch_all(token):
    items, offset = [], 0
    while True:
        r = req("GET", f"/collections/{COLLECTION}/items?limit=100&offset={offset}", token)
        batch = r.get("items", [])
        items += batch
        total = r.get("pagination", {}).get("total", len(items))
        offset += 100
        if offset >= total or not batch:
            break
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write to Webflow (default is dry run)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--no-publish", action="store_true", help="stage changes without publishing")
    ap.add_argument("--limit", type=int, help="only process the first N items (for a cautious first run)")
    a = ap.parse_args()

    token = os.environ.get("WEBFLOW_TOKEN")
    if not token:
        raise SystemExit("set WEBFLOW_TOKEN (Webflow > Site settings > Apps & integrations > API access)")

    print("fetching collection ...")
    items = fetch_all(token)
    print(f"  {len(items)} items")

    payloads, skipped = build(items, a.today)
    if a.limit:
        payloads = payloads[:a.limit]

    bad = verify(payloads, {i["id"]: i for i in items})
    if bad:
        print(f"PRE-FLIGHT VERIFY FAILED ({len(bad)}), nothing written:")
        for s, m in bad[:40]:
            print(f"  {s}: {m}")
        raise SystemExit(1)
    print(f"pre-flight verify passed: {len(payloads)} items to fix, {len(skipped)} skipped")

    for p in payloads:
        print(f"  {p['slug'][:56]:<56} {p['was']} -> pub {p['pub']} / mod {p['mod']}  [{p['embed']}]")

    if not a.apply:
        print("\ndry run, nothing written. re-run with --apply")
        return

    backup = f"webflow-blogs-backup-{a.today}.json"
    json.dump(items, open(backup, "w"))
    print(f"\nbackup of all {len(items)} items written to {backup}")

    # Sequential writes. The CMS is not concurrency safe: parallel writes
    # double-create items and cross-wire responses.
    published, failed = [], []
    for n, p in enumerate(payloads, 1):
        fd = p["fieldData"]
        patch = {"schema-markup": fd["schema-markup"],
                 "post-body": fd["post-body"],
                 "last-updated": fd["last-updated"]}
        print(f"[{n}/{len(payloads)}] {p['slug']}", flush=True)
        req("PATCH", f"/collections/{COLLECTION}/items/{p['id']}", token,
            {"isDraft": p["isDraft"], "isArchived": p["isArchived"], "fieldData": patch})

        # read back and prove the bytes landed
        got = req("GET", f"/collections/{COLLECTION}/items/{p['id']}", token)["fieldData"]
        for f in ("schema-markup", "post-body"):
            if got.get(f) != fd[f]:
                print(f"    MISMATCH on {f}, not publishing this item", file=sys.stderr)
                failed.append(p["slug"]); break
        else:
            if not p["isDraft"]:
                published.append(p["id"])

    if published and not a.no_publish:
        print(f"\npublishing {len(published)} live items ...")
        for i in range(0, len(published), 100):
            req("POST", f"/collections/{COLLECTION}/items/publish", token,
                {"itemIds": published[i:i + 100]})

    print(f"\ndone: {len(payloads) - len(failed)} patched, {len(failed)} failed, "
          f"{len(published) if not a.no_publish else 0} published")
    if failed:
        print("failed:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
