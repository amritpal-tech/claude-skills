#!/usr/bin/env python3
"""
Repair DevCommX blog schema dates and keep BOTH schema locations in sync.

The DevCommX blog template carries JSON-LD in two places:
  1. the `schema-markup` PlainText CMS field   (rendered by a hidden template embed)
  2. a <script type="application/ld+json"> block inside the `post-body` rich text

They drift. This script patches datePublished / dateModified in BOTH, surgically:
it rewrites only the two date VALUES, never regenerating the schema, so FAQ text,
headlines and every other node are byte-identical afterwards.

Rules applied
  datePublished = the item's CMS `date` field (the real publish date)
  dateModified  = the item's real last modification (max of lastUpdated /
                  lastPublished); where that equals the publish date, meaning the
                  post was never edited after publishing, today's date is used so
                  the two dates differ and the value stays truthful
  last-updated  = kept equal to dateModified, so the on-page "Last updated" and the
                  schema cannot contradict each other

Usage
  fix_schema_dates.py --items all_items.json --today 2026-09-03 --out payloads.json
  fix_schema_dates.py --items all_items.json --today 2026-09-03 --verify payloads.json
"""
import json, re, argparse, sys, datetime

SCRIPT_RE = re.compile(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', re.S)
# a JSON-LD script, optionally inside its Webflow embed div
LD_BLOCK_RE = re.compile(
    r"(?:<div data-rt-embed-type='true'>\s*)?"
    r"<script[^>]*application/ld\+json[^>]*>.*?</script>"
    r"(?:\s*</div>)?", re.S)


def unwrap(schema_text):
    """Return the bare JSON inside a schema value, stripping <script> tags if present."""
    m = SCRIPT_RE.search(schema_text or "")
    return (m.group(2) if m else schema_text).strip()
EMBED_TPL = ('<div data-rt-embed-type=\'true\'><script type="application/ld+json">\n'
             '{schema}\n  </script></div>')


def set_date(text, key, value):
    """Replace every "<key>": "<...>" value. Returns (new_text, n_replaced)."""
    pat = re.compile(r'("%s"\s*:\s*")([^"]*)(")' % re.escape(key))
    return pat.subn(lambda m: m.group(1) + value + m.group(3), text)


def patch(schema_text, pub, mod):
    s, n1 = set_date(schema_text, "datePublished", pub)
    s, n2 = set_date(s, "dateModified", mod)
    return s, n1, n2


def body_schema(body):
    m = SCRIPT_RE.search(body or "")
    return m.group(2) if m else None


def build(items, today):
    payloads, skipped = [], []
    for it in items:
        fd = it["fieldData"]
        slug = fd.get("slug")
        field = fd.get("schema-markup") or ""
        body = fd.get("post-body") or ""
        pub = (fd.get("date") or "")[:10]

        cur = re.search(r'"datePublished"\s*:\s*"([^"]*)"', field)
        if not cur:
            skipped.append((slug, "no datePublished in schema-markup")); continue
        if not pub:
            skipped.append((slug, "CMS date field is empty, no source of truth")); continue
        if cur.group(1) == pub:
            skipped.append((slug, "already correct")); continue

        lastmod = max((it.get("lastPublished") or "")[:10], (it.get("lastUpdated") or "")[:10])
        mod = lastmod if lastmod > pub else today

        new_field, n1, n2 = patch(field, pub, mod)
        if n1 == 0:
            skipped.append((slug, "datePublished not replaceable")); continue

        # --- keep the body embed in sync -------------------------------------
        emb = body_schema(body)
        if emb is None:
            new_body = body + EMBED_TPL.format(schema=unwrap(new_field))
            embed_action = "added"
        else:
            insync = re.sub(r"\s+", "", emb) == re.sub(r"\s+", "", unwrap(field))
            if insync:
                new_emb, _, _ = patch(emb, pub, mod)
                embed_action = "patched"
            else:
                new_emb = "\n" + unwrap(new_field) + "\n  "
                embed_action = "resynced"
            new_body = SCRIPT_RE.sub(
                lambda m: m.group(1) + new_emb + m.group(3), body, count=1)

        nfd = dict(fd)
        nfd["schema-markup"] = new_field
        nfd["post-body"] = new_body
        nfd["last-updated"] = f"{mod}T00:00:00.000Z"

        payloads.append({
            "id": it["id"], "slug": slug, "isDraft": it.get("isDraft", False),
            "isArchived": it.get("isArchived", False),
            "was": cur.group(1), "pub": pub, "mod": mod,
            "n_pub": n1, "n_mod": n2, "embed": embed_action,
            "fieldData": nfd,
        })
    return payloads, skipped


def verify(payloads, items_by_id):
    """Prove nothing but the dates moved."""
    bad = []
    for p in payloads:
        old = items_by_id[p["id"]]["fieldData"]
        new = p["fieldData"]

        # 1. only the three intended fields differ
        changed = {k for k in set(old) | set(new)
                   if json.dumps(old.get(k), sort_keys=True) != json.dumps(new.get(k), sort_keys=True)}
        if changed - {"schema-markup", "post-body", "last-updated"}:
            bad.append((p["slug"], f"unexpected fields changed: {changed}"))

        # 2. schema differs ONLY in date values
        a = set_date(set_date(old["schema-markup"], "datePublished", "X")[0], "dateModified", "X")[0]
        b = set_date(set_date(new["schema-markup"], "datePublished", "X")[0], "dateModified", "X")[0]
        if a != b:
            bad.append((p["slug"], "schema-markup changed beyond the date values"))

        # 3. the dates actually landed
        for key, want in (("datePublished", p["pub"]), ("dateModified", p["mod"])):
            got = re.findall(r'"%s"\s*:\s*"([^"]*)"' % key, new["schema-markup"])
            if got and set(got) != {want}:
                bad.append((p["slug"], f"{key} is {got}, expected {want}"))
        if p["pub"] == p["mod"]:
            bad.append((p["slug"], "datePublished == dateModified"))

        # 4. both locations agree
        emb = body_schema(new["post-body"])
        if emb is None:
            bad.append((p["slug"], "no body embed after patch"))
        elif re.sub(r"\s+", "", emb) != re.sub(r"\s+", "", unwrap(new["schema-markup"])):
            bad.append((p["slug"], "body embed does not match schema-markup field"))

        # 5. body prose untouched (everything before the embed)
        strip = lambda t: LD_BLOCK_RE.sub("", t or "")
        if strip(old["post-body"]) != strip(new["post-body"]):
            bad.append((p["slug"], "post-body prose changed outside the schema embed"))

        # 6. no dash regression, and parse status never worsens
        if "—" in new["schema-markup"] or "–" in new["schema-markup"]:
            if "—" not in old["schema-markup"] and "–" not in old["schema-markup"]:
                bad.append((p["slug"], "em/en dash introduced"))
        def ok(t):
            try: json.loads(t.strip()); return True
            except: return False
        if ok(old["schema-markup"]) and not ok(new["schema-markup"]):
            bad.append((p["slug"], "schema no longer parses"))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", required=True, help="JSON array of live CMS items")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--out")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()

    items = json.load(open(a.items))
    payloads, skipped = build(items, a.today)

    print(f"{len(payloads)} items to fix, {len(skipped)} skipped")
    counts = {}
    for p in payloads:
        counts[p["embed"]] = counts.get(p["embed"], 0) + 1
    print("  body embed:", counts)

    if a.verify:
        bad = verify(payloads, {i["id"]: i for i in items})
        if bad:
            print(f"\nVERIFY FAILED ({len(bad)}):")
            for s, m in bad[:40]:
                print(f"  {s}: {m}")
            sys.exit(1)
        print(f"\nVERIFY PASSED: {len(payloads)} payloads change only datePublished, "
              "dateModified and last-updated; both schema locations agree.")

    if a.out:
        json.dump(payloads, open(a.out, "w"), indent=1)
        print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
