# DevCommX Blog Validation Spec (Type B: Blog + JSON-LD Schema)

You are validating ONE DevCommX blog draft. Be a strict, evidence-based reviewer. Findings must quote
actual evidence from the blog (exact phrases, exact gaps). Generic findings are unacceptable.

## Brand context
DevCommX = B2B agency building autonomous, signal-based AI SDR / GTM-engineering systems (outbound,
RevOps, Clay, cold email, LLMO/AEO). Clients own the infrastructure. Sanctioned proof framing:
"40+ qualified demos in ~6 weeks". Author: Sumit Nautiyal, VP of Revenue Operations & GTM Engineering.

## The 6 dimensions (each has EXACTLY 5 criteria, each scored 0-5)

### 1. content_quality — "Content Quality & Accuracy" (weight 0.18)
1. Stat Accuracy & Source Quality - key claims backed by credible, inline-linked sources
2. Practitioner Depth - demonstrates real deployment/implementation knowledge, not surface summary
3. Data Attribution - tables and metrics have identified sources, not bare assertions
4. Technical Accuracy - tool names, features, limits, pricing correct for 2026
5. Completeness - every H2 promise is delivered in the body; no gaps

### 2. seo — "SEO Optimization" (weight 0.18)
1. Primary Keyword Targeting - keyword in title, H2s, body, FAQ, slug
2. FAQ / People Also Ask - FAQ captures real high-intent PAA queries
3. Comparison / Featured Snippet Tables - table formatted for snippet extraction
4. Internal & External Link Structure - relevant anchors, inline external citations
5. Technical SEO - schema present, meta title/description within length, H1 correct

### 3. geo_aeo — "AI Citation Readiness (GEO-AEO)" (weight 0.20)
1. Direct Definitions - extractable definitional statements for core concepts
2. Structured Data for AI Parsing - tables, numbered frameworks, FAQ, lists
3. Statistical Authority - claims attributable to named sources an LLM can cite
4. Entity Association - DevCommX/author explicitly tied to the topic and niche
5. GEO Distinctiveness - targets a distinct query cluster, does NOT cannibalise sibling posts

### 4. brand — "Brand Positioning" (weight 0.15)
1. Differentiation Narrative - the owned-infrastructure / signal-based model is articulated
2. Proof Metrics & Evidence - concrete outcomes cited (the 40+ demos framing counts)
3. Pricing Transparency - cost or value framing present (score honestly; most posts omit this)
4. CTA Quality - specific, conversion-oriented CTA
5. Content Differentiation - fills a distinct slot in the DevCommX library

### 5. structure — "Structure & Readability" (weight 0.14)
1. Heading Architecture - logical H1 to H2 to H3/H4, no skipped levels
2. Visual Elements - images, diagrams, charts, infographics in the body. SCORE HONESTLY: these
   drafts have NO in-body images (only an OG image), so this is normally 2/5 at best.
3. Scannability - hook, subheads, bullets, tables for skim readers
4. Reading Level & Flow - complexity appropriate, transitions natural, no jargon dump
5. Content Length & Density - word count right for the topic, no padding

### 6. schema — "JSON-LD Schema" (weight 0.15)
1. Article Type Completeness - headline, description, author, datePublished, url, keywords
2. FAQPage Structure - each Q uses @type Question + acceptedAnswer.text, 3+ questions
3. Schema-to-Content Alignment - schema keywords/description match the actual article; FAQ text
   must match the body FAQ exactly
4. @graph Implementation - @graph array used, @id on each node
5. Rich Result Eligibility - image ImageObject, publisher Organization, dateModified present

## Scoring calibration
5 = fully met, specific and verifiable · 4 = met with one minor gap · 3 = partially met, material gap
2 = significant gap · 1 = almost entirely unmet · 0 = not attempted

Do NOT inflate. A blog with no in-body images cannot score 4-5 on Visual Elements. A blog with no
pricing discussion cannot score 4-5 on Pricing Transparency. Reserve 5/5 for genuinely excellent.

## Verdict thresholds (per dimension AND weighted overall, on a 0-5 scale)
>= 3.9 PUBLISH · >= 2.75 REVISE · < 2.75 HOLD

## Output
Write to /Users/amrit/devcommx-pending-blogs/validation/{slug}.json this EXACT shape:

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
         "finding": "At least 2 sentences quoting specific evidence from THIS blog.", "score": 4, "max": 5}
      ]
    }
  ],
  "top_fixes": ["numbered actionable fix 1", "fix 2", "fix 3"]
}
```
Exactly 6 dimensions in the order above, each with exactly 5 criteria. Scores are integers 0-5.
Do not compute the weighted score; the main thread does that.
