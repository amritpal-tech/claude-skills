---
name: content-validator
description: >
  Validates any marketing or sales content (blog posts, X/Twitter posts, LinkedIn posts or
  event briefs, social captions, email copy) by generating a color-coded multi-tab Excel
  workbook that scores the content across quality, SEO, GEO/AI-readiness, brand positioning,
  structure, and (for blogs) JSON-LD schema. Use this skill whenever the user pastes content
  or uploads a doc and says anything like: "validate this", "validate this blog / post / brief",
  "score this content", "audit this", "check this before we publish", or asks for a validation
  report. Also trigger when the user submits a blog draft + JSON-LD schema together. Works for
  DevCommX content and any other brand — just adapt the brand criteria to the brand at hand.
---

# Content Validator Skill

You produce a professional, color-coded Excel validation workbook for any marketing content
the user shares. The output is always an `.xlsx` file saved to the outputs folder.

---

## Quick-start checklist

1. **Identify the content type** (see Content Type Detection below)
2. **Select the right tab structure** for that type (see Tab Structures)
3. **Write the validation script** using the excel_helpers.py pattern
4. **Run it** and save to `/sessions/cool-eloquent-thompson/mnt/outputs/`
5. **Share the link** — no long explanation needed

---

## Content Type Detection

Read the content carefully and classify it:

| Type | Signals | Tab count |
|---|---|---|
| **Blog post** | Long-form article, headings, FAQ section, word count > 400 | 5–6 tabs |
| **Blog + Schema** | Blog with attached JSON-LD | 6 tabs (add Schema tab) |
| **X / Twitter post** | Short text, hashtags, character count concerns, thread format | 4 tabs |
| **LinkedIn post** | Professional narrative, 1,300 char range, no hashtag overload | 4 tabs |
| **LinkedIn event brief** | Structured doc: event name, date, speakers, CTA, cover image | 5 tabs |
| **Email copy** | Subject line, preview text, body, CTA, unsubscribe | 4 tabs |
| **Case study / resource** | Client story, metrics, outcomes, quote, CTA | 5 tabs |

If unsure, ask the user one question: "Is this a blog post, a social post, or a document?"

---

## Tab Structures by Content Type

### A. Blog Post (5 tabs, no schema)

| # | Tab name | Weight | Tab color |
|---|---|---|---|
| 1 | Content Quality & Accuracy | 22% | TAB_TEAL |
| 2 | SEO Optimization | 22% | TAB_GREEN |
| 3 | AI Citation Readiness (GEO-AEO) | 22% | TAB_TEAL |
| 4 | Brand Positioning | 18% | TAB_TEAL |
| 5 | Structure & Readability | 16% | TAB_TEAL |

### B. Blog Post + JSON-LD Schema (6 tabs) ← most common

| # | Tab name | Weight | Tab color |
|---|---|---|---|
| 1 | Content Quality & Accuracy | 18% | TAB_TEAL |
| 2 | SEO Optimization | 18% | TAB_GREEN |
| 3 | AI Citation Readiness (GEO-AEO) | 20% | TAB_TEAL |
| 4 | Brand Positioning | 15% | TAB_TEAL |
| 5 | Structure & Readability | 14% | TAB_TEAL |
| 6 | JSON-LD Schema | 15% | TAB_PURPLE |

### C. X / Twitter Post (4 tabs, unequal weights)

| # | Tab name | Weight | Tab color |
|---|---|---|---|
| 1 | Hook & Narrative Flow | 25% | TAB_TEAL |
| 2 | Factual Accuracy | 35% | TAB_NAVY (or TAB_RED if issues) |
| 3 | Format & Platform Fit | 20% | TAB_TEAL |
| 4 | Thought Leadership Signal | 20% | TAB_PURPLE |

> Factual Accuracy carries extra weight because unverified claims on X cause reputational damage
> quickly. Use a red flag bar with `flag_type="critical"` if any fact is unverified.

### D. LinkedIn Post (4 tabs)

| # | Tab name | Weight | Tab color |
|---|---|---|---|
| 1 | Hook & Narrative Flow | 25% | TAB_TEAL |
| 2 | Credibility & Claims | 30% | TAB_NAVY |
| 3 | Format & Platform Fit | 25% | TAB_TEAL |
| 4 | Thought Leadership & CTA | 20% | TAB_PURPLE |

### E. LinkedIn Event Brief (5 tabs)

| # | Tab name | Weight | Tab color |
|---|---|---|---|
| 1 | Platform Compliance | 20% | TAB_TEAL |
| 2 | Description Copy | 20% | TAB_TEAL |
| 3 | Visual & Brand | 20% | TAB_PURPLE |
| 4 | Conversion Architecture | 20% | TAB_GREEN |
| 5 | Executability | 20% | TAB_NAVY |

---

## Standard Criteria per Tab

Below are the default criteria sets. Adapt scores and findings to the actual content.

### Content Quality & Accuracy (5 criteria × max 5 pts each = 25 max)

1. **Stat Accuracy & Source Quality** — Key claims backed by credible, inline-linked sources
2. **Practitioner Depth** — Content demonstrates direct deployment/implementation knowledge
3. **Data Attribution** — Tables and metrics have identified sources (not bare assertions)
4. **Technical Accuracy** — Tool names, features, pricing, and positioning are correct for the current year
5. **Completeness** — All stated topics covered; no gaps between H2 promises and body content

### SEO Optimization (5 criteria × max 5 pts each = 25 max)

1. **Primary Keyword Targeting** — Target keyword in title, H2s, body, FAQ, URL slug
2. **FAQ / People Also Ask** — FAQ structured to capture high-intent PAA queries
3. **Comparison / Featured Snippet Tables** — Tables formatted for Google featured snippet extraction
4. **Internal & External Link Structure** — Internal links with relevant anchors; external citations inline
5. **Technical SEO** — Schema present; meta description and H1 confirmable

### AI Citation Readiness / GEO-AEO (5 criteria × max 5 pts each = 25 max)

1. **Direct Definitions** — Extractable definitional statements for core concepts
2. **Structured Data for AI Parsing** — Tables, numbered frameworks, FAQ, and lists for LLM extraction
3. **Statistical Authority** — Claims backed by named sources AI models can attribute
4. **Entity Association** — Brand/author explicitly associated with the topic and niche
5. **GEO Distinctiveness** — Blog targets a distinct query cluster (not cannibalising other brand content)

### Brand Positioning (5 criteria × max 5 pts each = 25 max)

1. **Differentiation Narrative** — Brand's unique model or approach clearly articulated
2. **Proof Metrics & Evidence** — Client data, deployment counts, case outcomes cited
3. **Pricing Transparency** — Brand's service cost or value framing present
4. **CTA Quality** — Calls to action are specific, time-bound, and conversion-oriented
5. **Content Differentiation** — Article fills a distinct topic slot in the brand's content library

### Structure & Readability (5 criteria × max 5 pts each = 25 max)

1. **Heading Architecture** — H1→H2→H3 hierarchy logical; no skipped levels
2. **Visual Elements** — Images, diagrams, charts, or infographics present
3. **Scannability** — Intro hook, subheadings, bullet lists, pull quotes for skim readers
4. **Reading Level & Flow** — Appropriate complexity; no jargon overload; transitions natural
5. **Content Length & Density** — Word count appropriate for topic depth; no padding

### JSON-LD Schema (5 criteria × max 5 pts each = 25 max)

1. **Article Type Completeness** — headline, description, author, datePublished, url, keywords all present
2. **FAQPage Structure** — Each Q&A uses `@type: Question` + `acceptedAnswer.text`; 3+ questions
3. **Schema-to-Content Alignment** — Schema keywords/description match actual article content
4. **@graph Implementation** — `@graph` array used; `@id` on each node for cross-referencing
5. **Rich Result Eligibility** — `image` (ImageObject), `publisher` (Organization), `dateModified` present

---

## Verdict Thresholds

Apply to every tab and to the weighted overall score:

| Score / 5.0 | Verdict | Color |
|---|---|---|
| ≥ 3.9 (≥78%) | PUBLISH / APPROVED | Green (`C_PASS`) |
| ≥ 2.75 (≥55%) | REVISE | Amber (`C_WARN`) |
| < 2.75 (<55%) | HOLD / BLOCKED | Red (`C_FAIL`) |

---

## Exec Summary Tab (always first or last)

Always include an **Exec Summary** tab. Put it first in the workbook (insert before other tabs)
or as the last tab — user preference; first is recommended.

The exec summary must include:
- **Overall weighted score** and verdict (color-coded title bar)
- **Tab-by-tab score table** — tab name, score/5.0, verdict, top finding per tab
- **Top 3–5 fixes** before publishing, numbered and actionable
- **Recurring gaps section** — if this is one of multiple validated pieces, surface cross-piece patterns

---

## Script Template

```python
"""
Validation: [Content title]
Output: [Filename].xlsx
"""

import sys, os
sys.path.insert(0, "/sessions/cool-eloquent-thompson/blog-validator/scripts")
# OR if running from the skill's own scripts/ dir:
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import openpyxl
from openpyxl.utils import get_column_letter
from excel_helpers import (
    fill, font, border, align, section, score_bg,
    set_col_widths, freeze, col_headers,
    write_criterion_row, write_score_summary_row, write_title_bar,
    C_NAVY, C_TEAL, C_SLATE, C_WHITE, C_OFFWH, C_LTGREY,
    C_PASS, C_LTGREEN, C_WARN, C_LTAMBER, C_FAIL, C_LTRED,
    C_INFO, C_LTBLUE, C_PURPLE, C_LTPURP,
    TAB_NAVY, TAB_TEAL, TAB_GREEN, TAB_RED, TAB_PURPLE,
)

OUT_PATH = "/sessions/cool-eloquent-thompson/mnt/outputs/[Filename].xlsx"

NCOLS  = 6
WIDTHS = [26, 38, 52, 10, 10, 12]
COL_HDRS = ["CATEGORY", "CRITERION", "VALIDATION FINDING", "SCORE", "MAX", "RATING"]
COL_BGS  = [C_NAVY, C_SLATE, C_TEAL, C_TEAL, C_SLATE, C_TEAL]

V_PUBLISH = ("PUBLISH",  C_PASS, C_WHITE)
V_REVISE  = ("REVISE",   C_WARN, C_WHITE)
V_HOLD    = ("HOLD",     C_FAIL, C_WHITE)

TABS = [
    {
        "id":        1,
        "title":     "Tab Title Here",
        "tab_color": TAB_TEAL,
        "verdict":   V_PUBLISH,   # or V_REVISE or V_HOLD
        "flag":      "One-line summary of the most important finding for this tab.",
        "flag_type": "pass",      # "pass", "warn", or "critical"
        "criteria": [
            (
                "Category Label",   # shown bold in col 1
                "Criterion name",   # col 2
                "Detailed finding — specific evidence from the content. Quote exact phrases, name exact gaps. Minimum 2 sentences.",
                4,   # score out of 5
                5    # max
            ),
            # ... 4 more criteria
        ]
    },
    # ... more tabs
]
```

Then call `build_workbook(wb, TABS)` using the pattern below.

---

## Building the Workbook — Exact Pattern

```python
wb = openpyxl.Workbook()
wb.remove(wb.active)  # remove default Sheet

for tab in TABS:
    title     = tab["title"]
    tab_color = tab["tab_color"]
    verdict_label, verdict_bg, verdict_fc = tab["verdict"]
    flag      = tab["flag"]
    flag_type = tab["flag_type"]
    criteria  = tab["criteria"]

    # Sanitise tab name for Excel
    safe_title = (title.replace(":", "").replace("/", "-")
                       .replace("?", "").replace("'", "")
                       .replace("(", "").replace(")", ""))

    ws = wb.create_sheet(safe_title)
    ws.sheet_properties.tabColor = tab_color
    set_col_widths(ws, WIDTHS)

    row = 1
    # Title bar (verdict colour)
    write_title_bar(ws, f"Tab {tab['id']}: {title} — {verdict_label}", verdict_bg, NCOLS, 30)
    ws.row_dimensions[row].height = 30

    row = 2
    # Column headers
    col_headers(ws, row, COL_HDRS, COL_BGS)
    ws.row_dimensions[row].height = 18
    freeze(ws, "A3")

    row = 3
    # Flag row
    flag_colours = {
        "pass":     (C_LTGREEN,  C_PASS),
        "warn":     (C_LTAMBER,  C_WARN),
        "critical": (C_LTRED,    C_FAIL),
    }
    flag_bg, flag_fc = flag_colours.get(flag_type, (C_LTBLUE, C_INFO))
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=NCOLS)
    fc = ws.cell(row, 1)
    fc.value     = flag
    fc.fill      = fill(flag_bg)
    fc.font      = font(True, flag_fc, 9)
    fc.alignment = align("left")
    fc.border    = border()
    ws.row_dimensions[row].height = 36

    row = 4
    section(ws, row, f"🔍 Validation Criteria — {title}", C_NAVY, NCOLS)
    ws.row_dimensions[row].height = 18

    row = 5
    for cat, crit, finding, score, mx in criteria:
        write_criterion_row(ws, row, cat, crit, finding, score, mx, NCOLS)
        ws.row_dimensions[row].height = 55
        row += 1

    # Summary row
    total_score = sum(r[3] for r in criteria)
    total_max   = sum(r[4] for r in criteria)
    write_score_summary_row(ws, row, total_score, total_max, f"Tab {tab['id']} verdict: {verdict_label}", NCOLS)
    ws.row_dimensions[row].height = 22

wb.save(OUT_PATH)
print(f"Saved: {OUT_PATH}")
```

---

## Exec Summary Tab — Building Pattern

Insert the exec summary as the first sheet. Build it after computing all tab scores.

```python
# Insert exec summary at position 0
ws_exec = wb.create_sheet("📊 Exec Summary", 0)
ws_exec.sheet_properties.tabColor = TAB_NAVY

# Compute weighted overall score
weights = [0.18, 0.18, 0.20, 0.15, 0.14, 0.15]  # adjust per content type
tab_scores = [...]  # list of (tab_score_out_of_5) computed from criteria

weighted_total = sum(s * w for s, w in zip(tab_scores, weights))
overall_verdict = "PUBLISH" if weighted_total >= 3.9 else ("REVISE" if weighted_total >= 2.75 else "HOLD")
overall_bg = C_LTGREEN if weighted_total >= 3.9 else (C_LTAMBER if weighted_total >= 2.75 else C_LTRED)
overall_fc = C_PASS if weighted_total >= 3.9 else (C_WARN if weighted_total >= 2.75 else C_FAIL)
```

The exec summary should contain:
1. Title bar with overall verdict and score
2. Tab-by-tab score table (merge cols 1-2 for tab name, col 3 for score, col 4 for verdict, col 5-6 for key finding)
3. Numbered fixes section (use `section()` for the header, then rows with fix number, description, priority)
4. Recurring gaps section if applicable

---

## Critical Rules (avoid these bugs)

**MergedCell write error** — When you write a header row and then iterate over columns using a loop,
Excel may mark columns 2+ of a merged range as "MergedCell" objects that are read-only. To avoid this:
- Write the merged cell first: `ws.merge_cells(...)`, then `c = ws.cell(row, 1)` (top-left only)
- Write non-merged cells to specific column indices: `c2 = ws.cell(row, 3)` etc.
- Never write to a cell inside a merged range except the top-left

**Tab name sanitisation** — Excel rejects `/ : ? ' ( )` in sheet names. Always sanitise:
```python
safe = title.replace(":", "").replace("/", "-").replace("?", "").replace("'", "").replace("(", "").replace(")", "")
```

**Slack scheduling** — Use `slack_schedule_message` with `post_at = int(time.time()) + 180`.
Never hardcode a Unix timestamp — it will be in the past by the time you use it.

**Slack private channels** — `slack_search_channels` defaults to public only. Always pass
`channel_types=public_channel,private_channel` if the channel might be private.

---

## Scoring Calibration

These rough benchmarks help calibrate scores when the content is ambiguous:

- **5/5** — Fully meets the criterion; evidence is specific and verifiable
- **4/5** — Meets the criterion with one minor gap; still strong
- **3/5** — Partially meets; a material gap exists that affects quality or credibility
- **2/5** — Significant gap; the criterion is largely unmet but some effort is present
- **1/5** — Criterion almost entirely unmet
- **0/5** — Not attempted at all

When in doubt, err toward being specific in the finding text. A finding like
"HubSpot listed in References but never cited inline — same gap from the previous blog"
is more useful than "citation gaps exist."

---

## Output Naming Convention

| Content type | Filename pattern |
|---|---|
| Blog (by brand) | `[Brand]_[TopicSlug]_Blog_Validation.xlsx` |
| Blog re-validation | `[Brand]_[TopicSlug]_Blog_Validation_v2.xlsx` |
| X post | `[Author]_XPost_[Topic]_Validation.xlsx` |
| LinkedIn post | `[Author]_LinkedIn_[Topic]_Validation.xlsx` |
| LinkedIn event brief | `[EventName]_LinkedIn_Brief_Validation.xlsx` |
| Generic | `[Brand]_[ContentType]_Validation.xlsx` |

---

## References

- `scripts/excel_helpers.py` — Core styling helpers. Always add this to `sys.path` before importing.
- See the skill description for trigger conditions.
