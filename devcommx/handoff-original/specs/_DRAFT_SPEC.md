# DevCommX Blog Draft Spec (Batch: emerging + tools how-to)

You are drafting ONE long-form blog for DevCommX and writing it as a Webflow CMS item JSON to disk.

## Brand
DevCommX = B2B agency building **autonomous, signal-based AI SDR / GTM-engineering systems** (outbound, RevOps, Clay, cold email, LLMO/AEO). Clients **own the infrastructure**, not a managed campaign. Typical proof point: setup to **40+ qualified demos in ~6 weeks** because systems trigger on real buying signals, not static lists. Voice: practitioner, direct, no hype, no em/en dashes (use commas or periods). Author is always **Sumit Nautiyal, VP of Revenue Operations & GTM Engineering, DevCommX**.

## Output
Write a single JSON file to: `/Users/amrit/devcommx-pending-blogs/longtail/{slug}.json`
It MUST be valid JSON (parseable) with this EXACT top-level shape and fixed reference values:

```json
{
  "collection_id": "689c92652a4b35f0e9a14fc2",
  "isDraft": true,
  "isArchived": false,
  "fieldData": {
    "name": "<H1 / full post title>",
    "slug": "<the assigned slug>",
    "meta-title": "<=60 chars, keyword-first",
    "meta-description": "150-160 chars, keyword in first half, ends with benefit",
    "post-summary": "2-3 sentence summary (40-60 words) of what the post covers",
    "post-body": "<HTML string, see structure>",
    "schema-markup": "<JSON string, see schema>",
    "date": "2026-07-01T00:00:00.000Z",
    "last-updated": "2026-07-01T00:00:00.000Z",
    "author-name": "Sumit Nautiyal",
    "author-title": "VP of Revenue Operations & GTM Engineering, DevCommX",
    "add-blog-reading-time": "<integer as string, e.g. 11>",
    "blog-list": "https://www.devcommx.com/blogs/{slug}",
    "og-image": {
      "fileId": "69ce06f820d4562027a83191",
      "url": "https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"
    },
    "author": "677194290c472080e6cd6c06",
    "authors-collection": "69d8f4fd2475affd96f68115",
    "category": ["689c9183e68cf0a3029741d1"]
  }
}
```

## post-body structure (HTML string, 2,300-2,800 words)
1. **Extractable answer paragraph** — very first `<p>` directly answers the target keyword in the first 1-2 sentences (40-70 words), quotable standalone. Bold the key terms with `<strong>`.
2. **Intro `<p>`** — context + DevCommX practitioner framing + exactly ONE internal link (`https://www.devcommx.com/blogs/<existing-slug>`).
3. **`<h2>` sections** — 5 to 8 of them, each with 2-4 `<p>`. Use `<strong>` sub-labels where useful. Concrete, specific, no filler.
4. **ONE comparison/summary table** as a Webflow embed, placed after an intro `<h2>`. Use this EXACT wrapper (note `color:#1f2937` on every `<th>` — required, fixes white-on-grey):
```html
<div data-rt-embed-type='true'><div style="overflow-x:auto;"><table style="width:100%; border-collapse:collapse; font-family:Arial, sans-serif; font-size:14px; line-height:1.7;"><thead><tr><th style="border:1px solid #ddd; padding:12px; text-align:left; background:#f5f5f5; color:#1f2937;">Col A</th><th style="border:1px solid #ddd; padding:12px; text-align:left; background:#f5f5f5; color:#1f2937;">Col B</th></tr></thead><tbody><tr><td style="border:1px solid #ddd; padding:12px;">...</td><td style="border:1px solid #ddd; padding:12px;">...</td></tr></tbody></table></div></div>
```
5. **CTA section** — an `<h2>` then one `<p>`. For sales-intent topics use a **SALES CTA**; for AI-search/AEO topics use an **AEO CTA** (offer the free AI Visibility Checker angle). End the CTA `<p>` with an internal link to `https://www.devcommx.com/contact-us` (NOTE: the correct contact URL is `/contact-us`, NOT `/contact` which is a 404). Example sales CTA:
   `<h2>Build This With DevCommX</h2><p>DevCommX builds autonomous, signal-based AI SDR systems that your team owns... <a href="https://www.devcommx.com/contact-us">Book a GTM strategy call</a> to map this to your pipeline.</p>`
   For **vendor-selection / service topics**, ALSO link the relevant live service page in the body: `https://www.devcommx.com/ai-sdr` (AI SDR), `https://www.devcommx.com/revenue-operations` (RevOps), `https://www.devcommx.com/gtm-engineering` (GTM engineering). These count as internal links.
6. **Further Reading** — `<h3>Further Reading</h3>` + `<ul>` with **3 external links**, each `target="_blank" rel="noopener noreferrer"` to a real authoritative source (Gartner, Forrester, official docs, Google/Anthropic docs, FCC, etc.).
7. **FAQ** — `<h3>FAQ</h3>` then **5-6** `<h4>` questions, each followed by one `<p>` answer (40-80 words). These MUST be mirrored EXACTLY (same question text, same answer text) in the FAQPage schema.

**Links total:** at least **3 internal** (devcommx.com/blogs/... or /contact) + **3 external** (target=_blank). Internal links must point to REAL existing slugs from the menu below.

## Internal link menu (real existing slugs — pick 3+ relevant)
agentic-gtm-ai-agents-gtm-engineering, gtm-engineering-stack, best-gtm-engineering-agencies, definitive-guide-to-ai-sdrs, ai-sdr-system-cost, ai-sdr-pricing, human-in-the-loop-ai-sdr-orchestration, hybrid-ai-sdr-model-account-split, b2b-buying-signals-guide-signal-based-prospecting, abm-campaign-strategy-signal-based-targeting, clay-data-enrichment-fields-integrations-guide, clay-hubspot-integration-guide, clay-pricing-breakdown, clay-alternatives-data-enrichment-tools, b2b-email-deliverability-guide-2026, cold-email-domain-setup-checklist, best-email-warmup-tools-deliverability, email-deliverability-rules-2026-spf-dkim-dmarc-compliance, b2b-outbound-automation-guide, b2b-outbound-tool-stack, how-to-get-cited-by-chatgpt, how-to-optimize-content-for-llms-llmo-playbook, how-to-measure-llmo-ai-visibility-tracking, how-clay-uses-clay-seo-aeo-strategy, mcp-for-sales-model-context-protocol-revenue-stack, company-news-sales-outreach-event-based-outbound, contextual-outreach-playbook-buying-signals-meetings

## schema-markup (JSON string) — MUST be valid, MUST end correctly
Full `@graph` with a `BlogPosting` and a `FAQPage`. The whole value is a JSON STRING (escape internal quotes). It MUST end with the sequence `... ] } ] }` — i.e. close mainEntity array `]`, close FAQPage obj `}`, close @graph array `]`, close root obj `}`. Do NOT drop the final `}` (this was a live bug — five blogs shipped missing it).

Template (fill in, keep author = Sumit Nautiyal):
```
{"@context":"https://schema.org","@graph":[{"@type":"BlogPosting","@id":"https://www.devcommx.com/blogs/{slug}#article","headline":"...","description":"...","url":"https://www.devcommx.com/blogs/{slug}","datePublished":"2026-07-01","dateModified":"2026-07-01","keywords":"...","image":{"@type":"ImageObject","url":"https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png","width":1200,"height":630},"author":{"@type":"Person","name":"Sumit Nautiyal","jobTitle":"VP of Revenue Operations & GTM Engineering, DevCommX","url":"https://www.linkedin.com/company/devcommx"},"publisher":{"@type":"Organization","name":"DevCommX","url":"https://www.devcommx.com","logo":{"@type":"ImageObject","url":"https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":"https://www.devcommx.com/blogs/{slug}"}},{"@type":"FAQPage","@id":"https://www.devcommx.com/blogs/{slug}#faq","mainEntity":[{"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}]}]}
```

## Hard rules
- Valid JSON file (test mentally: no trailing commas, all quotes escaped inside strings).
- No em dashes or en dashes anywhere. Use commas/periods.
- FAQ in body == FAQPage in schema (exact match).
- All facts must be defensible; do not invent DevCommX case-study numbers beyond the "40+ demos in ~6 weeks" framing. Cite external stats generally (per the whyNow note) without fake precision.
- Reading time = round(words / 220).
- Write the file, then reply with just: the slug, word count, and confirmation the JSON parses.


## References section (REQUIRED, in addition to Further Reading)
End every blog with an explicit `<h3>References</h3>` followed by a `<ul>` that lists EVERY external source cited in the post, each as a real `<a href="..." target="_blank" rel="noopener noreferrer">Source name — what it supports</a>`. This is a formal reference list (min 3, ideally 4-6). It may reuse the same external links as inline citations. Place it after the FAQ (order: CTA -> References -> FAQ is also acceptable, but References must appear near the end and list all external links).

## Keyword + AEO + GEO targeting (REQUIRED in every blog)
- KEYWORD: the primary keyword appears in the H1/name, the meta-title, the first 100 words, at least two H2s, the body, one FAQ question, and the URL slug. Include 2-3 secondary/long-tail variants naturally.
- AEO (answer engine optimization): first paragraph is a direct, extractable 40-60 word answer to the title question; use clear definitional sentences; structure with tables, numbered frameworks, and the FAQ so answer engines can lift a clean answer.
- GEO (generative engine optimization): cite named, authoritative sources inline (so LLMs can attribute); state DevCommX as the entity tied to the topic; use specific numbers with sources. The References section reinforces this.
