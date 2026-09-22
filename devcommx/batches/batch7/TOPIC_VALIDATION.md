# Batch 7 topic validation — 12 proposed topics

Scored on the 5-check topic rubric (25 points -> /5). VALID at 3.5+.
Cannibalisation checked against the live CMS inventory of 223 published pages
(`devcommx/data/_published_slugs.txt`, generated 2026-09-22), not against the
stale `_existing_slugs.txt`, which covers only 149 of them.

Keyword decisions run through `devcommx-keyword-governance`: the 3-question rule,
the standing exclusion list, and the protected-terms list.

## Governance findings that apply across the batch

1. `generative engine optimization` (4,400/mo, KD 75) and `answer engine
   optimization` (2,400/mo, KD 66) are BOTH on the standing exclusion list, cut as
   informational head terms. The recorded remedy is to take the `agency` and
   `services` variants. Topics 1 and 4 do exactly that and are on-strategy.
2. Tool queries are an exclusion category (19 terms). The recorded reason:
   `clay vs apollo` produced 27 clicks from 25,824 impressions. This lands on topic 3.
3. Every supporting blog must link into a money page. Confirmed service pages:
   `/ai-sdr`, `/revenue-operations`, `/gtm-engineering`, plus `/aeo-services` and
   the `/aeo-services/{city}` set. There is NO demand-generation service page and
   NO marketing-automation service page. That blocks topics 6, 7 and 11 from
   satisfying the rule, and is a business decision rather than a writing problem.
4. Internal fragmentation: topics 1, 2 and 12 all pull on GEO services/agency, and
   topics 2 and 5 are the same "X vs SEO" article twice. Shipping them as proposed
   would split one keyword across three or four URLs.

## Scores

| # | Topic | Clarity | Audience | Search fit | Originality | Depth | Total | Score | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | GEO agency, what it does | 4 | 5 | 4 | 5 | 4 | 22 | 4.4 | VALID |
| 2 | GEO services vs traditional SEO | 4 | 4 | 3 | 2 | 3 | 16 | 3.2 | REVISE |
| 3 | GEO tools for tracking citations | 4 | 3 | 2 | 2 | 3 | 14 | 2.8 | REWORK |
| 4 | AEO agency, what it does | 4 | 5 | 4 | 3 | 4 | 20 | 4.0 | VALID |
| 5 | AEO services vs SEO services | 4 | 4 | 3 | 2 | 3 | 16 | 3.2 | REVISE |
| 6 | B2B demand gen agency, what it does | 5 | 4 | 5 | 5 | 4 | 23 | 4.6 | VALID, money page missing |
| 7 | Demand gen 2026, quality over volume | 4 | 4 | 3 | 1 | 3 | 15 | 3.0 | REWORK |
| 8 | RevOps consulting, broken handoffs | 5 | 5 | 3 | 3 | 4 | 20 | 4.0 | VALID |
| 9 | Sales automation process, 8 steps | 5 | 4 | 3 | 3 | 4 | 19 | 3.8 | VALID |
| 10 | CRM automation services, 10 workflows | 5 | 4 | 4 | 3 | 4 | 20 | 4.0 | VALID |
| 11 | Marketing automation implementation | 4 | 3 | 4 | 4 | 4 | 19 | 3.8 | VALID, money page missing |
| 12 | GEO services for brand mentions | 3 | 4 | 3 | 2 | 3 | 15 | 3.0 | REWORK |

Mean 3.65. VALID 7, REVISE 2, REWORK 3.

## Primary keywords

| # | Primary keyword | 3-question | Format | Money page | Exclusion check |
|---|---|---|---|---|---|
| 1 | `generative engine optimization agency` | Q1 hire-now | Service-adjacent blog | /aeo-services | clear (head term excluded, this variant is the prescribed one) |
| 2 | `geo vs seo` | Q2 learning | Supporting blog | /aeo-services | clear, but cannibalises two live pages |
| 3 | `ai citation tracking tools` | Q2 learning | DO NOT BUILD as proposed | - | tool-query category |
| 4 | `answer engine optimization agency` | Q1 hire-now | Service-adjacent blog | /aeo-services | clear (same variant rule) |
| 5 | `aeo vs seo` | Q2 learning | Merge into 2 | /aeo-services | clear, but duplicates topic 2 |
| 6 | `b2b demand generation agency` | Q1 hire-now | Service page, not a blog | NEEDS ONE | clear |
| 7 | `demand generation lead quality` | Q2 learning | Merge into live page | - | clear, but duplicates a live page |
| 8 | `sales and marketing handoff` | Q2 learning | Supporting blog | /revenue-operations | clear |
| 9 | `sales automation process` | Q2 learning | Supporting blog | /gtm-engineering | clear |
| 10 | `crm automation services` | Q1 hire-now | Service-adjacent blog | /revenue-operations | clear |
| 11 | `marketing automation implementation` | Q1 hire-now | Service-adjacent blog | NEEDS ONE | clear |
| 12 | `brand mentions ai search` | Q2 learning | Merge into live page | /aeo-services | clear, but duplicates a live page |

## The four collisions, named

- **Topic 2 + topic 5** are one article. Both are "our discipline vs SEO". Merge.
- **Topics 2/5 vs live** `llmo-vs-seo-vs-geo-vs-aeo` and `aeo-vs-geo-difference-strategy-guide`
  already own the comparison. A third and fourth page splits it further.
- **Topic 7 vs live** `lead-quality-vs-quantity-b2b` is the same argument, already published.
- **Topic 12 vs live** `brand-mentions-vs-backlinks-ai-search` already owns brand mentions
  in AI search. Topic 12 restates it with a service framing.
- **Topic 3 vs live** `llmo-checklist-best-llmo-tools-2026` and
  `how-to-measure-llmo-ai-visibility-tracking` cover the tooling and the measurement.

## Recommended batch: 7 topics, not 12

Build 1, 4, 6, 8, 9, 10, 11. Merge 5 into 2 and reframe as a decision page rather than
another explainer. Fold 7 and 12 into the live pages they duplicate as new sections.
Rework 3 away from a tool roundup toward a measurement method, or drop it.

Topics 6 and 11 need a service page to exist before they can be written to the rule.

---

# Blog structure — unchanged from previous batches

Canonical source: `.claude/skills/devcommx-blog-ops/references/draft-spec.md`.
Every batch-7 post follows it exactly, as sheet12 and batch 4 did.

`post-body` HTML, in this order:

1. **Extractable answer paragraph.** First `<p>` answers the target keyword in the
   first one or two sentences, 40-70 words, quotable standalone, key terms in
   `<strong>`. Highest-leverage element for AEO.
2. **Intro `<p>`** with DevCommX practitioner framing and exactly ONE internal link.
3. **Five to eight `<h2>` sections**, each 2-4 `<p>`, `<strong>` sub-labels where useful.
4. **ONE comparison table** as a Webflow embed, after an intro `<h2>`. Every `<th>`
   must carry `color:#1f2937` or the header renders white on grey.
5. **CTA section**: `<h2>` plus one `<p>` ending at
   `https://www.devcommx.com/contact-us` (never `/contact`, that is a hard 404).
   Service topics also link the live service page in the body.
6. **`<h3>Further Reading</h3>`** with 3 external links, each
   `target="_blank" rel="noopener noreferrer"`.
7. **`<h3>References</h3>`** listing EVERY external source cited, 3 minimum, 4-6
   preferred, each a real anchor naming what it supports. Required on every post.
8. **`<h3>FAQ</h3>`** with 5-6 `<h4>` questions, each answered in 40-80 words,
   mirrored word-for-word into the FAQPage schema.

Length 2,300-2,800 words standard, 2,600-3,200 pillar.
`add-blog-reading-time` = round(words / 220), as a string.

Links: minimum 3 internal plus 3 external. Internal targets must come from the
verified-live menu only. As of 2026-09-22 that means the 223 slugs in
`devcommx/data/_published_slugs.txt`. The 12 slugs listed as unpublished in
`published_slugs.json` are drafts and will render as 404s if linked.

Keyword placement: primary keyword in H1/`name`, `meta-title`, first 100 words, at
least two `<h2>`s, the body, one FAQ question, and the slug.

Schema goes in BOTH locations and they must be byte-identical: the `schema-markup`
field, and a `<script type="application/ld+json">` inside `post-body` wrapped in
`<div data-rt-embed-type='true'>`. `datePublished` must never predate the article's
existence, and `dateModified` moves whenever the body changes.
