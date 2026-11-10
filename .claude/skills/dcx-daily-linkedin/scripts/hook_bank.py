#!/usr/bin/env python3
"""Convert a Scripe "Top 100 Hooks" sheet (.xlsx) into the desk's hook bank files.

    python3 hook_bank.py SHEET.xlsx                       # writes references/hook-bank/<pulled>-scripe-top100.{md,txt}
    python3 hook_bank.py SHEET.xlsx --pulled 2026-11-10   # if the sheet doesn't say when it was pulled
    python3 hook_bank.py SHEET.xlsx --out-dir /some/dir

The .md is for drafting: hooks by niche, pattern scoreboard, formulas, freshness.
The .txt is for the gate: every hook and formula, one block each, fed to
check_post.py --bank so a post can never share a six-word run with a bank line.

Expected sheets (as in the 10 Nov 2026 sheet): "Top 100 Hooks" with columns
#, Category, Hook (opening lines), Hook pattern, Author, Posted, Reactions, Comments,
Total engagement, Comment ratio; optionally "Hook Formulas" (Pattern, Template, Proven by)
and "Consistent Performers" (Author, Hooks in Top 100, Total engagement, Avg engagement / post, Topics).
"""
import argparse
import collections
import datetime as dt
import os
import re
import sys

try:
    import openpyxl
except ImportError:
    sys.exit("openpyxl is needed: pip install openpyxl")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, "..", "references", "hook-bank"))

# niche in the sheet -> desk profile
PROFILE_FOR = {"SEO / AEO": "Amritpal", "GTM": "Sumit", "RevOps": "Pankaj"}
NICHE_ORDER = ["SEO / AEO", "GTM", "RevOps"]
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def rows_of(ws):
    return [r for r in ws.iter_rows(values_only=True) if r and any(c not in (None, "") for c in r)]


def find_header(rows, first_cell):
    for i, r in enumerate(rows):
        if r and str(r[0]).strip() == first_cell:
            return i
    return None


def age_days(posted):
    """'4 days ago' -> 4, 'a month ago' -> 30, '3 months ago' -> 90, '—' -> None."""
    s = str(posted or "").strip().lower()
    m = re.match(r"(a|an|\d+)\s+(hour|day|week|month|year)s?\s+ago", s)
    if not m:
        return None
    n = 1 if m.group(1) in ("a", "an") else int(m.group(1))
    return n * {"hour": 0, "day": 1, "week": 7, "month": 30, "year": 365}[m.group(2)]


def pulled_date(rows, override):
    if override:
        return dt.date.fromisoformat(override)
    for r in rows[:4]:
        m = re.search(r"pulled\s+(\d{1,2})\s+([A-Za-z]{3})[a-z]*\s+(\d{4})", " ".join(str(c) for c in r if c))
        if m:
            return dt.date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1)))
    sys.exit("can't find the pull date in the sheet; pass --pulled YYYY-MM-DD")


def one_line(s):
    return " / ".join(p.strip() for p in str(s or "").splitlines() if p.strip()).replace("|", "\\|")


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet")
    ap.add_argument("--pulled", help="YYYY-MM-DD the hooks were pulled from Scripe")
    ap.add_argument("--out-dir", default=DEFAULT_OUT)
    a = ap.parse_args()

    wb = openpyxl.load_workbook(a.sheet, read_only=True, data_only=True)
    top = rows_of(wb[wb.sheetnames[0]] if "Top 100 Hooks" not in wb.sheetnames else wb["Top 100 Hooks"])
    pulled = pulled_date(top, a.pulled)
    title = str(top[0][0] or "Scripe hooks").strip()
    source = str(top[1][0] or "").strip() if len(top) > 1 else ""
    h = find_header(top, "#")
    if h is None:
        sys.exit("no header row starting with '#' in the hooks sheet")
    hooks = []
    for r in top[h + 1:]:
        if not isinstance(r[0], (int, float)):
            continue
        r = list(r) + [None] * 10
        d = age_days(r[5])
        hooks.append({
            "n": int(r[0]), "niche": str(r[1] or "").strip(), "hook": str(r[2] or "").strip(),
            "pattern": str(r[3] or "").strip(), "author": str(r[4] or "").strip(),
            "posted": str(r[5] or "—").strip(), "age": d, "fresh": d is not None and d <= 14,
            "reactions": num(r[6]), "comments": num(r[7]), "eng": num(r[8]), "ratio": num(r[9]),
        })

    formulas, performers = [], []
    if "Hook Formulas" in wb.sheetnames:
        fr = rows_of(wb["Hook Formulas"])
        fh = find_header(fr, "Pattern")
        formulas = [r for r in fr[fh + 1:]] if fh is not None else []
    if "Consistent Performers" in wb.sheetnames:
        pr = rows_of(wb["Consistent Performers"])
        ph = find_header(pr, "Author")
        performers = [r for r in pr[ph + 1:]] if ph is not None else []

    os.makedirs(a.out_dir, exist_ok=True)
    stem = os.path.join(a.out_dir, f"{pulled.isoformat()}-scripe-top100")

    # ---- .txt for the gate
    with open(stem + ".txt", "w", encoding="utf-8") as f:
        f.write(f"# Gate text for check_post.py --bank. Source: {title}, pulled {pulled.isoformat()}.\n\n")
        for x in hooks:
            f.write(x["hook"] + "\n\n")
        for r in formulas:
            f.write(str(r[1] or "").strip() + "\n\n")

    # ---- .md for drafting
    niches = collections.OrderedDict((n, [x for x in hooks if x["niche"] == n]) for n in NICHE_ORDER)
    for x in hooks:
        niches.setdefault(x["niche"], [])
        if x not in niches[x["niche"]]:
            niches[x["niche"]].append(x)
    L = []
    L.append(f"# Hook bank · {title}")
    L.append("")
    L.append(f"Pulled **{pulled.isoformat()}**. {source}")
    L.append("")
    L.append("Generated by `scripts/hook_bank.py` from the team's Scripe sheet. Use it the way "
             "`post-formats.md` (\"Using the Scripe hook bank\") says: borrow the **pattern**, never the words, "
             "facts or numbers. The gate fails any post sharing a six-word run with the matching `.txt`.")
    L.append("")
    L.append(f"**Fresh** = posted within 14 days of the pull date ({sum(x['fresh'] for x in hooks)} of {len(hooks)}). "
             "Fresh hooks show what is working this fortnight; the rest are proven patterns. "
             "Post ages are relative to the pull date, as Scripe shows them.")
    L.append("")
    L.append("| Niche | Profile | Hooks | Fresh | Total engagement |")
    L.append("|---|---|---|---|---|")
    for n, xs in niches.items():
        L.append(f"| {n} | {PROFILE_FOR.get(n, '?')} | {len(xs)} | {sum(x['fresh'] for x in xs)} | {int(sum(x['eng'] for x in xs)):,} |")
    L.append("")
    for n, xs in niches.items():
        if not xs:
            continue
        L.append(f"## {n} · for {PROFILE_FOR.get(n, '?')}")
        L.append("")
        pats = collections.defaultdict(list)
        for x in xs:
            pats[x["pattern"]].append(x)
        board = sorted(pats.items(), key=lambda kv: -sum(x["eng"] for x in kv[1]))
        L.append("**Pattern scoreboard** (by total engagement; comment ratio is comments ÷ engagement):")
        L.append("")
        L.append("| Pattern | Hooks | Total eng. | Avg comment ratio | Fresh |")
        L.append("|---|---|---|---|---|")
        for p, ps in board[:10]:
            L.append(f"| {p} | {len(ps)} | {int(sum(x['eng'] for x in ps)):,} | "
                     f"{sum(x['ratio'] for x in ps) / len(ps):.0%} | {sum(x['fresh'] for x in ps)} |")
        L.append("")
        L.append("| # | Pattern | Hook (opening lines) | Posted | Eng. | Comments | Fresh |")
        L.append("|---|---|---|---|---|---|---|")
        for x in sorted(xs, key=lambda x: -x["eng"]):
            L.append(f"| {x['n']} | {x['pattern']} | {one_line(x['hook'])} | {x['posted']} | "
                     f"{int(x['eng']):,} | {int(x['comments']):,} | {'yes' if x['fresh'] else ''} |")
        L.append("")
    if formulas:
        L.append("## Hook formulas (fill-in-the-blank, from the sheet)")
        L.append("")
        L.append("Templates are mechanics. Fill them with our facts and rewrite the fixed words in the "
                 "profile's voice; the gate checks the fixed words too.")
        L.append("")
        L.append("| Pattern | Template | Proven by |")
        L.append("|---|---|---|")
        for r in formulas:
            r = list(r) + [None] * 3
            L.append(f"| {one_line(r[0])} | {one_line(r[1])} | {one_line(r[2])} |")
        L.append("")
    if performers:
        L.append("## Consistent performers (3+ hooks in the Top 100)")
        L.append("")
        L.append("| Author | Hooks | Total eng. | Avg / post | Topics |")
        L.append("|---|---|---|---|---|")
        for r in performers:
            r = list(r) + [None] * 5
            L.append(f"| {one_line(r[0])} | {int(num(r[1]))} | {int(num(r[2])):,} | {int(num(r[3])):,} | {one_line(r[4])} |")
        L.append("")
    with open(stem + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"pulled {pulled}: {len(hooks)} hooks, {len(formulas)} formulas, {len(performers)} performers")
    for n, xs in niches.items():
        print(f"  {n:10} {len(xs):3} hooks, {sum(x['fresh'] for x in xs):2} fresh")
    print(f"wrote {stem}.md and {stem}.txt")


if __name__ == "__main__":
    main()
