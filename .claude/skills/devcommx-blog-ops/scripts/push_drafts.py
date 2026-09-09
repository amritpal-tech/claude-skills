#!/usr/bin/env python3
"""
Create DevCommX blog drafts in Webflow from the JSON files on disk.

Why this exists: the Webflow MCP connector needs every field value retyped as a
literal tool argument. A single blog is ~30KB of HTML, which the tool layer now
truncates to a file, so pushing a batch by hand costs many round trips and risks
silently corrupting a post. This moves the same bytes mechanically.

    export WEBFLOW_TOKEN=...        # Site settings > Apps & integrations > API access
    python3 push_drafts.py --dry-run devcommx/blogs/sheet12/*.json
    python3 push_drafts.py --apply  devcommx/blogs/sheet12/*.json

Safety properties, all learned the hard way:
  - Creates SEQUENTIALLY. The CMS is not concurrency safe: parallel creates
    double-create items and cross-wire responses.
  - Skips any slug that already exists, so a re-run after a partial failure
    resumes instead of duplicating. Idempotent.
  - Verifies the returned slug has no random "-xxxxx" suffix, which is Webflow's
    tell that the clean slug was taken and a duplicate was just made.
  - Reads each item back and compares post-body and schema-markup byte for byte.
  - Creates as drafts. Publishing is always a separate, explicit decision.
"""
import os, sys, json, time, argparse, urllib.request, urllib.error

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
            with urllib.request.urlopen(r, timeout=90) as resp:
                return json.loads(resp.read() or "{}")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                wait = 2 ** attempt
                print(f"    {e.code}, retrying in {wait}s", file=sys.stderr)
                time.sleep(wait); continue
            raise SystemExit(f"HTTP {e.code} on {method} {path}: {e.read().decode()[:500]}")
    raise SystemExit(f"gave up on {method} {path}")


def existing_slugs(token):
    slugs, offset = {}, 0
    while True:
        r = req("GET", f"/collections/{COLLECTION}/items?limit=100&offset={offset}", token)
        for it in r.get("items", []):
            slugs[it["fieldData"].get("slug")] = it["id"]
        total = r.get("pagination", {}).get("total", len(slugs))
        offset += 100
        if offset >= total or not r.get("items"):
            break
    return slugs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    token = os.environ.get("WEBFLOW_TOKEN")
    if not token:
        raise SystemExit("set WEBFLOW_TOKEN (Webflow > Site settings > Apps & integrations > API access)")

    drafts = []
    for f in sorted(a.files):
        d = json.load(open(f, encoding="utf-8"))
        assert d["collection_id"] == COLLECTION, f"{f}: wrong collection_id"
        drafts.append((f, d))

    print("fetching current collection ...")
    have = existing_slugs(token)
    print(f"  {len(have)} items already in the collection\n")

    todo, skip = [], []
    for f, d in drafts:
        (skip if d["fieldData"]["slug"] in have else todo).append((f, d))
    for f, d in skip:
        print(f"  SKIP (already exists) {d['fieldData']['slug']}")
    for f, d in todo:
        print(f"  PUSH {d['fieldData']['slug']}")
    print(f"\n{len(todo)} to create, {len(skip)} already present")

    if not a.apply:
        print("\ndry run, nothing written. re-run with --apply")
        return

    created, failed = [], []
    for n, (f, d) in enumerate(todo, 1):
        fd = d["fieldData"]
        print(f"[{n}/{len(todo)}] {fd['slug']}", flush=True)
        r = req("POST", f"/collections/{COLLECTION}/items", token,
                {"isDraft": True, "isArchived": False, "fieldData": fd})
        got = r.get("fieldData", {}).get("slug", "")
        if got != fd["slug"]:
            print(f"    SLUG CHANGED to {got!r}: a duplicate was likely created. Stopping.",
                  file=sys.stderr)
            failed.append(fd["slug"]); break
        back = req("GET", f"/collections/{COLLECTION}/items/{r['id']}", token)["fieldData"]
        bad = [k for k in ("post-body", "schema-markup") if back.get(k) != fd[k]]
        if bad:
            print(f"    MISMATCH on {bad}", file=sys.stderr); failed.append(fd["slug"])
        else:
            created.append((fd["slug"], r["id"]))

    print(f"\ncreated {len(created)}, failed {len(failed)}")
    for s, i in created:
        print(f"  {s}  id={i}")
    if failed:
        print("failed:", ", ".join(failed)); sys.exit(1)
    print("\nAll created as DRAFTS. Publishing is a separate, explicit step.")


if __name__ == "__main__":
    main()
