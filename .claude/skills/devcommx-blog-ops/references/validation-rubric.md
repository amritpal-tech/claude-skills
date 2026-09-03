# Validation rubric (Type B: blog + JSON-LD schema)

You are validating ONE DevCommX blog draft. Be a strict, evidence-based reviewer.
**Findings must quote actual evidence from the blog** — exact phrases, exact gaps.
Generic findings are unacceptable.

6 dimensions, exactly 5 criteria each, each scored 0–5 as an integer.

## 1. content_quality — Content Quality & Accuracy (weight 0.18)
1. **Stat Accuracy & Source Quality** — key claims backed by credible, inline-linked sources
2. **Practitioner Depth** — real deployment knowledge, not a surface summary
3. **Data Attribution** — tables and metrics have identified sources, not bare assertions
4. **Technical Accuracy** — tool names, features, limits, pricing correct for 2026
5. **Completeness** — every H2 promise is delivered in the body

## 2. seo — SEO Optimization (weight 0.18)
1. **Primary Keyword Targeting** — keyword in title, H2s, body, FAQ, slug
2. **FAQ / People Also Ask** — FAQ captures real high-intent PAA queries
3. **Comparison / Featured Snippet Tables** — table formatted for snippet extraction
4. **Internal & External Link Structure** — relevant anchors, inline external citations
5. **Technical SEO** — schema present, meta title/description in length, H1 correct

## 3. geo_aeo — AI Citation Readiness (weight 0.20)
1. **Direct Definitions** — extractable definitional statements for core concepts
2. **Structured Data for AI Parsing** — tables, numbered frameworks, FAQ, lists
3. **Statistical Authority** — claims attributable to named sources an LLM can cite
4. **Entity Association** — DevCommX and the author explicitly tied to the topic
5. **GEO Distinctiveness** — a distinct query cluster, does not cannibalise sibling posts

## 4. brand — Brand Positioning (weight 0.15)
1. **Differentiation Narrative** — the owned-infrastructure, signal-based model articulated
2. **Proof Metrics & Evidence** — concrete outcomes cited (the 40+ demos framing counts)
3. **Pricing Transparency** — cost or value framing present. Score honestly, most posts omit this.
4. **CTA Quality** — specific, conversion-oriented CTA
5. **Content Differentiation** — fills a distinct slot in the library

## 5. structure — Structure & Readability (weight 0.14)
1. **Heading Architecture** — logical H1 → H2 → H3/H4, no skipped levels
2. **Visual Elements** — images, diagrams, charts in the body. **Score honestly:** a draft
   with no in-body images (only an OG image) is 2/5 at best.
3. **Scannability** — hook, subheads, bullets, tables for skim readers
4. **Reading Level & Flow** — complexity appropriate, transitions natural
5. **Content Length & Density** — word count right for the topic, no padding

## 6. schema — JSON-LD Schema (weight 0.15)
1. **Article Type Completeness** — headline, description, author, datePublished, url, keywords
2. **FAQPage Structure** — each Q uses `@type Question` + `acceptedAnswer.text`, 3+ questions
3. **Schema-to-Content Alignment** — schema keywords/description match the article; FAQ text
   matches the body FAQ exactly
4. **@graph Implementation** — `@graph` array used, `@id` on each node
5. **Rich Result Eligibility** — image `ImageObject`, publisher `Organization`, `dateModified`

---

## Scoring calibration

`5` fully met, specific and verifiable · `4` met with one minor gap · `3` partially met,
material gap · `2` significant gap · `1` almost entirely unmet · `0` not attempted.

**Do not inflate.** A blog with no in-body images cannot score 4–5 on Visual Elements. A
blog with no pricing discussion cannot score 4–5 on Pricing Transparency. Reserve 5/5 for
genuinely excellent.

## Verdict thresholds

Applied to the weighted overall and to each dimension, on a 0–5 scale:

| Score | Verdict |
|---|---|
| ≥ 3.9 | PUBLISH |
| ≥ 2.75 | REVISE |
| < 2.75 | HOLD |

## Findings output

Write to `devcommx/validation/{slug}.json`:

```json
{
  "slug": "...",
  "title": "...",
  "words": 0,
  "dimensions": [
    {
      "key": "content_quality",
      "title": "Content Quality & Accuracy",
      "weight": 0.18,
      "flag": "one-line summary of the most important finding for this dimension",
      "flag_type": "pass|warn|critical",
      "criteria": [
        {"category": "Sources", "criterion": "Stat Accuracy & Source Quality",
         "finding": "At least 2 sentences quoting specific evidence from THIS blog.",
         "score": 4, "max": 5}
      ]
    }
  ],
  "top_fixes": ["actionable fix 1", "fix 2", "fix 3"]
}
```

Exactly 6 dimensions in the order above, each with exactly 5 criteria.
**The agent does not compute the weighted score.** The main thread does, with
`scripts/score_findings.py`, because agents mislabel verdicts.

## Workbook

`scripts/build_workbook.py` turns a set of findings JSONs into an Exec Summary tab plus
one tab per blog. It uses `scripts/excel_helpers.py`, whose helpers **return** style
objects — assign them (`c.fill = fill(x)`), do not call them for effect.

Build the workbook in the main thread; subagents cannot run openpyxl reliably.

## Benchmark results from the handoff session

| Batch | Blogs | Mean weighted |
|---|---|---|
| Long-tail | 25 | 3.73 |
| Recent | 10 | 4.29 |
| Rest | 2 | 4.06 |
| Traffic | 16 | 4.26 |

**The cross-cutting gap in every batch is Visual Elements at ~2/5** — no in-body images.
Second is inline stat attribution: sources sitting in the References footer instead of
anchored at the claim.
