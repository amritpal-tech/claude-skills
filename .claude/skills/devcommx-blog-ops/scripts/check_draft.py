#!/usr/bin/env python3
"""
Hard-rules gate for a DevCommX blog draft JSON.

Usage:
    python3 check_draft.py devcommx/blogs/traffic/*.json
    python3 check_draft.py --json devcommx/blogs/**/*.json    # machine-readable

Exit code is 1 if any file has an ERROR. WARN does not fail the run.
Every rule here corresponds to something that shipped broken at least once.
"""
import sys, os, json, re, html, argparse

CONTACT_OK   = "https://www.devcommx.com/contact-us"
CONTACT_BAD  = "devcommx.com/contact\""
COLLECTION   = "689c92652a4b35f0e9a14fc2"
AUTHOR       = "Sumit Nautiyal"
WORDS_MIN, WORDS_MAX = 2300, 3200

REQUIRED_FIELDS = [
    "name", "slug", "meta-title", "meta-description", "post-summary", "post-body",
    "schema-markup", "date", "last-updated", "author-name", "author-title",
    "add-blog-reading-time", "blog-list", "og-image", "author",
    "authors-collection", "category",
]


def strip_tags(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def norm(s):
    """Normalise text for the FAQ body-vs-schema comparison."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip().lower()


def check(path):
    errs, warns = [], []
    E, W = errs.append, warns.append
    raw = open(path, encoding="utf-8").read()

    try:
        item = json.loads(raw)
    except Exception as e:
        return [f"JSON does not parse: {e}"], [], {}

    fd = item.get("fieldData") or {}
    if item.get("collection_id") != COLLECTION:
        E(f"collection_id is {item.get('collection_id')!r}, expected {COLLECTION}")
    if item.get("isDraft") is not True:
        W("isDraft is not true (intentional only if pushing a live update)")

    for f in REQUIRED_FIELDS:
        if f not in fd:
            E(f"fieldData missing required field: {f}")

    body   = fd.get("post-body", "") or ""
    slug   = fd.get("slug", "") or ""
    schema = fd.get("schema-markup", "") or ""

    # --- dashes, anywhere in the whole payload -------------------------------
    for dash, label in (("—", "em dash"), ("–", "en dash")):
        if dash in raw:
            spots = []
            for k, v in fd.items():
                if isinstance(v, str) and dash in v:
                    i = v.index(dash)
                    spots.append(f"{k}: ...{v[max(0,i-40):i+40]}...")
            E(f"{label} found. " + (spots[0] if spots else ""))

    # --- the backslash-quote anchor bug --------------------------------------
    if '\\"' in body:
        E('post-body contains a literal \\" (backslash-quote) - breaks the HTML anchors')

    # --- CTA -----------------------------------------------------------------
    if CONTACT_OK not in body:
        E(f"CTA link {CONTACT_OK} not found in post-body")
    if re.search(r"devcommx\.com/contact(?![-\w])", body):
        E("post-body links /contact which is a hard 404. Use /contact-us")

    # --- table embed ---------------------------------------------------------
    ths = re.findall(r"<th\b[^>]*>", body)
    if not ths:
        E("no <th> found - the required comparison table embed is missing")
    else:
        bad = [t for t in ths if "color:#1f2937" not in t.replace(" ", "")]
        if bad:
            E(f"{len(bad)}/{len(ths)} <th> tags missing color:#1f2937 (white-on-grey header)")
    if "data-rt-embed-type" not in body:
        E("table is not wrapped in a data-rt-embed-type Webflow embed")
    for m in re.finditer(r"<div data-rt-embed-type=['\"]true['\"]>", body):
        # walk the div nesting to find where this embed actually closes
        depth, i = 0, m.start()
        for t in re.finditer(r"<div\b[^>]*>|</div>", body[m.start():]):
            depth += 1 if t.group(0).startswith("<div") else -1
            if depth == 0:
                i = m.start() + t.end()
                break
        size = i - m.start()
        if size >= 10000:
            W(f"an embed block is {size} chars, near/over the ~10,000 Webflow limit")
            break

    # --- required sections ---------------------------------------------------
    if not re.search(r"<h3[^>]*>\s*References\s*</h3>", body, re.I):
        E("missing <h3>References</h3> section")
    if not re.search(r"<h3[^>]*>\s*Further Reading\s*</h3>", body, re.I):
        E("missing <h3>Further Reading</h3> section")
    if not re.search(r"<h3[^>]*>\s*FAQ\s*</h3>", body, re.I):
        E("missing <h3>FAQ</h3> section")

    h2s = re.findall(r"<h2\b[^>]*>(.*?)</h2>", body, re.S | re.I)
    if not 5 <= len(h2s) <= 9:
        W(f"{len(h2s)} h2 sections (spec wants 5-8)")

    # --- links ---------------------------------------------------------------
    hrefs = re.findall(r'href="([^"]+)"', body)
    internal = [h for h in hrefs if "devcommx.com" in h]
    external = [h for h in hrefs if h.startswith("http") and "devcommx.com" not in h]
    if len(internal) < 3:
        E(f"only {len(internal)} internal links (need >= 3)")
    if len(external) < 3:
        E(f"only {len(external)} external links (need >= 3)")
    for a in re.finditer(r'<a\b[^>]*href="(https?://(?!www\.devcommx\.com)[^"]+)"[^>]*>', body):
        if 'target="_blank"' not in a.group(0):
            W(f"external link without target=_blank: {a.group(1)[:60]}")
            break

    # --- word count / reading time -------------------------------------------
    words = len(strip_tags(body).split())
    if not WORDS_MIN <= words <= WORDS_MAX:
        (E if words < 2000 or words > 3600 else W)(
            f"word count {words} outside {WORDS_MIN}-{WORDS_MAX}")
    try:
        rt = int(str(fd.get("add-blog-reading-time", "")).strip())
        if abs(rt - round(words / 220)) > 1:
            W(f"reading time {rt} but round({words}/220) = {round(words/220)}")
    except (ValueError, TypeError):
        E(f"add-blog-reading-time is not an integer string: {fd.get('add-blog-reading-time')!r}")

    # --- author / slug consistency -------------------------------------------
    if fd.get("author-name") != AUTHOR:
        E(f"author-name is {fd.get('author-name')!r}, expected {AUTHOR!r}")
    if slug and fd.get("blog-list") != f"https://www.devcommx.com/blogs/{slug}":
        W(f"blog-list does not match the slug: {fd.get('blog-list')!r}")
    if slug and os.path.basename(path) != f"{slug}.json":
        W(f"filename does not match slug {slug!r}")
    mt = fd.get("meta-title", "") or ""
    if len(mt) > 60:
        W(f"meta-title is {len(mt)} chars (<= 60)")
    md = fd.get("meta-description", "") or ""
    if not 140 <= len(md) <= 170:
        W(f"meta-description is {len(md)} chars (want 150-160)")

    # --- schema ---------------------------------------------------------------
    faq_schema = []
    if not schema.rstrip().endswith("]}]}") and not re.sub(r"\s", "", schema).endswith("]}]}"):
        E("schema-markup does not end with the required ] } ] } sequence")
    try:
        sch = json.loads(schema)
    except Exception as e:
        E(f"schema-markup does not parse: {e}")
    else:
        graph = sch.get("@graph") or []
        types = [n.get("@type") for n in graph]
        if "BlogPosting" not in types:
            E("schema @graph has no BlogPosting node")
        if "FAQPage" not in types:
            E("schema @graph has no FAQPage node")
        for n in graph:
            if not n.get("@id"):
                W(f"schema node {n.get('@type')} has no @id")
            if n.get("@type") == "BlogPosting":
                for k in ("headline", "description", "author", "datePublished",
                          "dateModified", "url", "keywords", "image", "publisher"):
                    if k not in n:
                        W(f"BlogPosting missing {k}")
                if (n.get("author") or {}).get("name") != AUTHOR:
                    E("schema author is not Sumit Nautiyal")
            if n.get("@type") == "FAQPage":
                for q in n.get("mainEntity") or []:
                    faq_schema.append((q.get("name", ""),
                                       (q.get("acceptedAnswer") or {}).get("text", "")))

    # --- FAQ body vs schema, exact mirror -------------------------------------
    tail = body[body.lower().rindex("<h3") if "<h3" in body.lower() else 0:]
    m = re.search(r"<h3[^>]*>\s*FAQ\s*</h3>(.*)$", body, re.S | re.I)
    faq_body = []
    if m:
        blk = m.group(1)
        for q in re.finditer(r"<h4\b[^>]*>(.*?)</h4>\s*<p\b[^>]*>(.*?)</p>", blk, re.S | re.I):
            faq_body.append((q.group(1), q.group(2)))
    if not 5 <= len(faq_body) <= 6:
        W(f"{len(faq_body)} FAQ Q/A pairs in the body (spec wants 5-6)")
    if faq_schema:
        if len(faq_body) != len(faq_schema):
            E(f"FAQ mismatch: {len(faq_body)} in body, {len(faq_schema)} in schema")
        for i, (bq, ba) in enumerate(faq_body):
            if i >= len(faq_schema):
                break
            sq, sa = faq_schema[i]
            if norm(bq) != norm(sq):
                E(f"FAQ Q{i+1} text differs between body and schema")
            elif norm(ba) != norm(sa):
                E(f"FAQ A{i+1} text differs between body and schema")

    return errs, warns, {"slug": slug, "words": words,
                         "internal": len(internal), "external": len(external),
                         "h2": len(h2s), "faq": len(faq_body)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()

    results, failed = [], 0
    for p in a.files:
        errs, warns, stats = check(p)
        results.append({"file": p, "errors": errs, "warnings": warns, **stats})
        if errs:
            failed += 1

    if a.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            name = r.get("slug") or os.path.basename(r["file"])
            mark = "FAIL" if r["errors"] else ("warn" if r["warnings"] else "PASS")
            extra = ""
            if "words" in r:
                extra = (f"  {r['words']}w  h2:{r['h2']}  faq:{r['faq']}  "
                         f"int:{r['internal']}  ext:{r['external']}")
            print(f"[{mark}] {name}{extra}")
            for e in r["errors"]:
                print(f"    ERROR  {e}")
            for w in r["warnings"]:
                print(f"    warn   {w}")
        clean = len(results) - failed
        print(f"\n{clean}/{len(results)} pass the hard rules.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
