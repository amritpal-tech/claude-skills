#!/usr/bin/env python3
"""
Verify a draft carries the keywords its brief requires, in the places that matter.

The house draft spec demands the PRIMARY keyword appear verbatim in the H1 (`name`),
the meta-title, the first 100 words, at least two H2s, one FAQ question and the slug.
Every SECONDARY keyword must appear at least once in the body. check_draft.py enforces
structure; this enforces keyword coverage.

Usage:
    check_keywords.py --map keywords.json devcommx/blogs/sheet12/*.json

`keywords.json` maps slug -> {"primary": "...", "secondary": ["...", ...]}.
Exit 1 if any REQUIRED placement is missing. Secondary misses are warnings.
"""
import sys, json, re, html, argparse


def text_of(h):
    """Visible prose only: drop script/style blocks, then tags."""
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h or "", flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def norm(s, slash=" "):
    """Lowercase, drop varying punctuation, collapse space.

    `slash` controls how "/" reads. Both readings are legitimate and which one a
    writer used cannot be known in advance:
      " "  ->  "SPF/DKIM"      reads as "spf dkim"   (matches "SPF, DKIM")
      ""   ->  "A/B testing"   reads as "ab testing" (matches "AB testing")
    `has` tries both, so either spelling counts.
    """
    s = html.unescape(s or "").lower()
    s = s.replace("/", slash).replace("-", " ").replace("&amp;", "and")
    # punctuation to space FIRST, then collapse: otherwise "AI Overviews, B2B"
    # normalises to a double space and fails to match "AI Overviews B2B".
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()


def has(hay, needle):
    """Whole-phrase match on normalised text, tolerant of punctuation and hyphens."""
    for slash in (" ", ""):
        h, n = norm(hay, slash), norm(needle, slash)
        if n and re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", h):
            return True
    return False


def check(path, kw):
    fd = json.load(open(path, encoding="utf-8"))["fieldData"]
    body = fd.get("post-body", "") or ""
    primary = kw["primary"]
    secondary = kw.get("secondary", [])
    errs, warns = [], []

    prose = text_of(body)
    first100 = " ".join(prose.split()[:100])
    h2s = re.findall(r"<h2\b[^>]*>(.*?)</h2>", body, re.S | re.I)
    h4s = re.findall(r"<h4\b[^>]*>(.*?)</h4>", body, re.S | re.I)

    checks = [
        ("H1 / name",      has(fd.get("name", ""), primary)),
        ("meta-title",     has(fd.get("meta-title", ""), primary)),
        ("first 100 words", has(first100, primary)),
        ("slug",           has(fd.get("slug", "").replace("-", " "), primary)),
        (">=2 H2s",        sum(1 for h in h2s if has(h, primary)) >= 2),
        ("an FAQ question", any(has(q, primary) for q in h4s)),
    ]
    for label, ok in checks:
        if not ok:
            errs.append(f"primary keyword {primary!r} missing from {label}")

    body_norm = prose + " " + " ".join(h2s) + " " + " ".join(h4s)
    missing = [s.strip() for s in secondary if s.strip() and not has(body_norm, s)]
    for m in missing:
        warns.append(f"secondary keyword not found verbatim: {m!r}")

    n_primary = len(re.findall(re.escape(norm(primary)), norm(body_norm)))
    return errs, warns, {
        "slug": fd.get("slug", ""),
        "primary_hits": n_primary,
        "h2_hits": sum(1 for h in h2s if has(h, primary)),
        "secondary_ok": len(secondary) - len(missing),
        "secondary_total": len(secondary),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--map", required=True)
    a = ap.parse_args()
    kwmap = json.load(open(a.map))

    failed = 0
    for p in a.files:
        slug = json.load(open(p, encoding="utf-8"))["fieldData"].get("slug", "")
        kw = kwmap.get(slug)
        if not kw:
            print(f"[SKIP] {slug or p}: no keyword entry")
            continue
        errs, warns, st = check(p, kw)
        mark = "FAIL" if errs else ("warn" if warns else "PASS")
        if errs:
            failed += 1
        print(f"[{mark}] {st['slug']}  primary x{st['primary_hits']} "
              f"(H2 x{st['h2_hits']})  secondary {st['secondary_ok']}/{st['secondary_total']}")
        for e in errs:
            print(f"    ERROR  {e}")
        for w in warns:
            print(f"    warn   {w}")
    print(f"\n{len(a.files) - failed}/{len(a.files)} pass required keyword placement.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
