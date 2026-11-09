#!/usr/bin/env python3
"""
Hard-rules gate for DevCommX LinkedIn posts. Every rule maps to the house style in
Notion "DevCommX — LinkedIn HQ", the 360Brew Playbook, and the dcx-humanizer skill.

Two ways to run it:

  1) On a daily brief that marks its posts (the normal case):
       python3 check_post.py devcommx/linkedin-daily/2026-11-04.md

     The brief marks each post and first comment like this:
       <!-- post:sumit format:text ask:sharp-question type:news -->
       ...post body...
       <!-- /post -->
       <!-- comment:sumit -->
       ...first comment...
       <!-- /comment -->

  2) On a single post file:
       python3 check_post.py post.txt --profile pankaj --format carousel \
           --ask save-this --type news --comment comment.txt

Exit code 1 if any ERROR. WARN never fails the run but must be read.
"""
import argparse
import re
import sys
import unicodedata

PROFILES = {"amritpal", "sumit", "pankaj"}
FORMATS = {"text", "listicle", "carousel", "single-image", "reference-map", "video", "document"}
ASKS = {"save-this", "repost-if", "sharp-question", "comment-gate"}
TYPES = {"news", "evergreen", "receipts", "curation"}

BANNED_WORDS = [
    "leverage", "leveraging", "unlock", "unlocks", "unlocking", "elevate", "elevates",
    "delve", "delves", "empower", "empowers", "empowering", "supercharge", "seamless",
    "seamlessly", "robust", "game-changer", "game changer", "gamechanger", "tapestry",
    "testament", "underscore", "underscores", "foster", "fosters", "harness",
    "harnessing", "revolutionize", "revolutionise", "cutting-edge", "cutting edge",
    "in today's fast-paced", "ever-evolving", "navigate the", "dive into", "let's dive",
    "buckle up", "here's the kicker", "game-changing", "paradigm shift",
]
BAIT = [
    r"\blike if\b", r"\blike and (comment|share|repost)\b", r"\bcomment below if you agree\b",
    r"\bagree\?\s*$", r"\bthoughts\?\s*$", r"\blike,? comment,? (and|&) (repost|share)\b",
    r"\bsmash (the|that) like\b", r"\btag someone who\b",
]
# symmetrical negation, the house's most-banned construction
NEGATION = [
    r"\bnot (just |only |merely )?[^.\n?!]{1,60}?, (it'?s|it is|but|they'?re|we'?re)\b",
    r"\bit'?s not [^.\n?!]{1,60}?[.;] ?it'?s\b",
    r"\bit is not [^.\n?!]{1,60}?[.;] ?it is\b",
    r"\bisn'?t (about )?[^.\n?!]{1,50}?, it'?s (about )?\b",
    r"\b(this|that) is not [^.\n?!]{1,50}?\. (this|that|it) is\b",
]


def is_emoji(ch):
    if not ch:
        return False
    cp = ord(ch)
    return (0x1F300 <= cp <= 0x1FAFF) or (0x2600 <= cp <= 0x27BF and ch not in "→↳✓") or cp in (0x2B50, 0x2B55, 0x203C, 0x2049)


def words(s):
    return re.findall(r"[A-Za-z0-9$%'’.\-/]+", s)


def first_sentence(body):
    for line in body.splitlines():
        line = line.strip()
        if line:
            m = re.split(r"(?<=[.?!])\s", line, maxsplit=1)
            return m[0]
    return ""


LOWERCASE_OK = {"n8n", "iphone", "ios", "ebay", "macos"}
ABBREV = {"vs", "e.g", "i.e", "etc", "approx", "no"}


def sentence_case_misses(text):
    """Line starts and sentence starts that begin with a lowercase letter.

    List markers (1. / ↳ / → / - / •) are skipped. Domains (chatgpt.com) and a few
    brands that are lowercase by design (n8n) are allowed.
    """
    def ok(word):
        w = word.strip("\"'“‘(")
        if not w[:1].isalpha() or w[:1].isupper():
            return True
        bare = w.lower().rstrip(".,:;!?")
        return bare in LOWERCASE_OK or bool(re.match(r"^[a-z0-9-]+\.[a-z]{2,}", bare))

    misses = []
    for line in text.splitlines():
        s = re.sub(r"^\s*(\d+[.)]|↳|→|-|•)\s*", "", line).strip()
        if not s:
            continue
        first = s.split()[0]
        if not ok(first):
            misses.append(first)
        for m in re.finditer(r"(\S+)[.?!]\s+(\S+)", s):
            prev, nxt = m.group(1).lower().rstrip("."), m.group(2)
            if prev in ABBREV or re.search(r"\.[a-z]{2,}$", m.group(1).lower()):
                continue
            if not ok(nxt):
                misses.append(nxt)
    return misses


def ngrams(text, n=6):
    toks = re.findall(r"[a-z0-9$%']+", text.lower().replace("’", "'"))
    return {" ".join(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def check_post(body, profile, fmt, ask, typ, comment, bank_grams=None):
    errs, warns = [], []
    E, W = errs.append, warns.append
    text = body.strip()
    low = text.lower()

    if not text:
        return ["empty post body"], []

    # 1 dashes: absolute
    for label, s in (("post", text), ("first comment", comment or "")):
        n = s.count("—") + s.count("–")
        if n:
            E(f"{label}: {n} em/en dash(es). Rewrite with a period, comma or parentheses.")

    # 2 banned vocabulary
    for w in BANNED_WORDS:
        if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
            E(f"banned word/phrase: '{w}'")

    # 3 symmetrical negation
    for pat in NEGATION:
        m = re.search(pat, low)
        if m:
            E(f"'not X, it's Y' construction: \"...{m.group(0)}...\". Say the plain thing in one clause.")
            break

    # 4 engagement bait / triple ask
    for pat in BAIT:
        if re.search(pat, low, flags=re.M):
            E(f"engagement bait matched /{pat}/")

    # 5 links belong in the first comment
    if re.search(r"https?://|www\.", text):
        E("link in post body. Move it to the first comment (body links cost 40-60% reach).")
    elif re.search(r"\b[a-z0-9-]+\.(com|io|ai|co|org|net)/\S", low):
        W("looks like a bare URL path in the body. If it is a link, move it to the first comment.")

    # 6 hashtags: zero, except reference maps (which carry the tag/hashtag set)
    tags = re.findall(r"(?<![\w&])#[A-Za-z][\w]*", text)
    if tags and fmt != "reference-map":
        E(f"hashtags in body ({', '.join(tags[:5])}). House rule is zero hashtags outside Reference Maps.")

    # 7 emoji-led lines are banned; emoji anywhere is a warning
    for line in text.splitlines():
        s = line.strip()
        if s and is_emoji(s[0]):
            E(f"emoji-led line: '{s[:40]}'")
            break
    if any(is_emoji(c) for c in text):
        W("emoji in body. The house voice almost never uses them.")

    # 8 length band (360Brew: 1,200-1,900 chars gets 2.9x)
    n = len(text)
    if n > 3000:
        E(f"{n} characters, over LinkedIn's 3,000 limit")
    elif n < 900:
        E(f"{n} characters. Too thin for the 1,200-1,900 band; add the mechanism or the steps.")
    elif not (1200 <= n <= 1900):
        W(f"{n} characters, outside the 1,200-1,900 target band")

    # 9 hook: first sentence short, and cashable
    hook = first_sentence(text)
    hw = len(words(hook))
    if hw > 16:
        E(f"hook is {hw} words. First line must stop the scroll in under ~10 words: '{hook[:80]}'")
    elif hw > 10:
        W(f"hook is {hw} words (target under 10): '{hook[:80]}'")
    if re.match(r"(?i)(in today's|in the world of|as (a|an) |have you ever|did you know|i'?m excited|i'?m thrilled|big news)", hook):
        E(f"soft wind-up hook: '{hook[:60]}'")

    # 10 whitespace: one idea per line, no walls
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]

    def is_list(p):
        lines = [l.strip() for l in p.splitlines() if l.strip()]
        return len(lines) > 1 and all(re.match(r"(\d+[.)]|↳|→|-|•)\s", l) for l in lines)

    walls = [p for p in paras if len(p) > 320 and not is_list(p)]
    if walls:
        W(f"{len(walls)} paragraph(s) over 320 characters. Break them up; one idea per line.")
    if len(paras) < 6:
        W(f"only {len(paras)} blocks. House format is a blank line between lines.")

    # 11 casing: sentence case for every profile (Amritpal's call, 2026-11-04)
    if profile in ("amritpal", "sumit", "pankaj"):
        misses = sentence_case_misses(text)
        if misses:
            msg = f"sentence case: {len(misses)} line/sentence start(s) in lowercase, e.g. {misses[:3]}"
            (W if profile == "pankaj" else E)(msg)

    # 12 exactly one explicit ask, matching the declared type
    last = paras[-1].lower() if paras else ""
    tail = " ".join(p.lower() for p in paras[-2:])
    if ask == "sharp-question" and "?" not in last:
        E("ask is sharp-question but the last block has no question")
    if ask == "save-this" and "save" not in tail:
        E("ask is save-this but the close never says save")
    if ask == "repost-if" and "repost" not in tail:
        E("ask is repost-if but the close never says repost")
    if ask == "comment-gate" and "comment" not in tail:
        E("ask is comment-gate but the close never names the comment action")
    asks_found = sum([
        "save this" in low or "save it" in low,
        bool(re.search(r"\brepost (if|this|it)\b", low)),  # "reposts" as a metric name is not an ask
        bool(re.search(r"\bcomment (the word |your |[A-Z]{3,})", text, flags=re.I)),
        bool(re.search(r"\bfollow (me|for)\b", low)),
    ])
    if asks_found > 1:
        W("more than one ask detected (save / repost / comment / follow). Exactly one per post.")
    if "thoughts?" in low:
        E("'thoughts?' is not a sharp question")

    # 13 placeholders and honesty flags
    needs = re.findall(r"\[NEEDS:[^\]]*\]", text + "\n" + (comment or ""))
    if needs:
        W(f"{len(needs)} [NEEDS:] flag(s). Cannot publish until a human resolves them: {needs[:3]}")
    if re.search(r"\[(TBD|TODO|XX|INSERT)[^\]]*\]", text, flags=re.I):
        E("unfilled placeholder in body")

    # 14 news posts must carry their source in the first comment
    if typ == "news":
        if not comment or not re.search(r"https?://", comment):
            E("news post with no source URL in the first comment")

    # 15 hook bank: borrow the mechanic, never the words
    if bank_grams:
        shared = sorted(ngrams(text) & bank_grams)
        if shared:
            E(f"shares {len(shared)} six-word run(s) with the Scripe hook bank, e.g. \"{shared[0]}\". Rewrite in the profile's own words.")

    # 16 first comment hygiene
    if comment:
        if len(comment) > 1250:
            W(f"first comment is {len(comment)} characters; keep it tight")
        if re.search(r"(?<![\w&])#[A-Za-z]", comment):
            W("hashtags in first comment")

    return errs, warns


MARK_POST = re.compile(r"<!--\s*post:(\w+)([^>]*)-->(.*?)<!--\s*/post\s*-->", re.S)
MARK_COMMENT = re.compile(r"<!--\s*comment:(\w+)\s*-->(.*?)<!--\s*/comment\s*-->", re.S)


def attrs(s):
    return dict(re.findall(r"(\w+):([\w-]+)", s))


def run_brief(raw):
    posts = MARK_POST.findall(raw)
    comments = {k: v.strip() for k, v in MARK_COMMENT.findall(raw)}
    results = []
    for profile, a, body in posts:
        at = attrs(a)
        results.append((profile, at, body.strip(), comments.get(profile, "")))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--profile", choices=sorted(PROFILES))
    ap.add_argument("--format", dest="fmt", choices=sorted(FORMATS), default="text")
    ap.add_argument("--ask", choices=sorted(ASKS))
    ap.add_argument("--type", dest="typ", choices=sorted(TYPES), default="news")
    ap.add_argument("--comment")
    ap.add_argument("--bank", help="text export of the Scripe hook bank; fails any post sharing a six-word run with it")
    a = ap.parse_args()
    bank_grams = ngrams(open(a.bank, encoding="utf-8").read()) if a.bank else None

    raw = open(a.file, encoding="utf-8").read()
    jobs = run_brief(raw)
    if not jobs:
        if not a.profile or not a.ask:
            sys.exit("no <!-- post:... --> markers found; pass --profile and --ask for a single post file")
        comment = open(a.comment, encoding="utf-8").read() if a.comment else ""
        jobs = [(a.profile, {"format": a.fmt, "ask": a.ask, "type": a.typ}, raw, comment)]

    failed = False
    for profile, at, body, comment in jobs:
        fmt, ask, typ = at.get("format", "text"), at.get("ask"), at.get("type", "news")
        problems = []
        if profile not in PROFILES:
            problems.append(f"unknown profile '{profile}'")
        if fmt not in FORMATS:
            problems.append(f"unknown format '{fmt}'")
        if ask not in ASKS:
            problems.append(f"missing or unknown ask '{ask}' (one of {sorted(ASKS)})")
        errs, warns = check_post(body, profile, fmt, ask, typ, comment, bank_grams)
        errs = problems + errs
        status = "FAIL" if errs else ("PASS with warnings" if warns else "PASS")
        failed |= bool(errs)
        print(f"== {profile} · {fmt} · {ask} · {typ} · {len(body)} chars · {status}")
        for e in errs:
            print(f"   ERROR {e}")
        for w in warns:
            print(f"   WARN  {w}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
