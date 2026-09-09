# DevCommX Sheet-12 batch spec (2026-09-08)

Read this in full, then your brief in `briefs/topic-<N>.md`. Write ONE blog.

## Output
Write valid JSON to `/home/user/claude-skills/devcommx/blogs/sheet12/{slug}.json`.
Start from this exact shape. Only `name, slug, meta-title, meta-description,
post-summary, post-body, schema-markup, add-blog-reading-time, blog-list` vary.

```json
{
  "collection_id": "689c92652a4b35f0e9a14fc2",
  "isDraft": true,
  "isArchived": false,
  "fieldData": {
    "name": "", "slug": "", "meta-title": "", "meta-description": "",
    "post-summary": "", "post-body": "", "schema-markup": "",
    "date": "2026-09-08T00:00:00.000Z", "last-updated": "2026-09-08T00:00:00.000Z",
    "author-name": "Sumit Nautiyal",
    "author-title": "VP of Revenue Operations & GTM Engineering, DevCommX",
    "add-blog-reading-time": "", "blog-list": "https://www.devcommx.com/blogs/{slug}",
    "og-image": {"fileId":"69ce06f820d4562027a83191","url":"https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"},
    "author": "677194290c472080e6cd6c06",
    "authors-collection": "69d8f4fd2475affd96f68115",
    "category": ["689c9183e68cf0a3029741d1"]
  }
}
```

## Brand
DevCommX builds autonomous, signal-based **AI SDR / GTM-engineering systems**. Clients
**own the infrastructure**, they are not renting a managed campaign. Voice: practitioner,
direct, no hype. Author is always Sumit Nautiyal.

**The ONLY sanctioned DevCommX proof point is "40+ qualified demos in ~6 weeks."**
Invent no other DevCommX metric, client name, or case study. Ever.

## post-body structure, in this exact order
1. **Extractable answer paragraph** — the very first `<p>`, 40 to 70 words, answers the
   primary keyword directly and stands alone as a quote. Bold key terms with `<strong>`.
2. **Intro `<p>`** — context plus DevCommX practitioner framing, containing exactly ONE
   internal link.
3. **5 to 8 `<h2>` sections**, 2 to 4 `<p>` each. Follow your brief's outline. Concrete,
   specific, no filler.
4. **ONE comparison table** as a Webflow embed, after an early `<h2>`. Use this wrapper
   verbatim; every `<th>` MUST carry `color:#1f2937`:
```html
<div data-rt-embed-type='true'><div style="overflow-x:auto;"><table style="width:100%; border-collapse:collapse; font-family:Arial, sans-serif; font-size:14px; line-height:1.7;"><thead><tr><th style="border:1px solid #ddd; padding:12px; text-align:left; background:#f5f5f5; color:#1f2937;">Col A</th><th style="border:1px solid #ddd; padding:12px; text-align:left; background:#f5f5f5; color:#1f2937;">Col B</th></tr></thead><tbody><tr><td style="border:1px solid #ddd; padding:12px;">...</td><td style="border:1px solid #ddd; padding:12px;">...</td></tr></tbody></table></div></div>
```
5. **CTA** — an `<h2>` then one `<p>` ending with a link to
   `https://www.devcommx.com/contact-us`. Use the CTA angle named in your brief.
6. **Further Reading** — `<h3>Further Reading</h3>` + `<ul>` of exactly 3 external links,
   each `target="_blank" rel="noopener noreferrer"`.
7. **References** — `<h3>References</h3>` + `<ul>` listing EVERY external source you cited,
   4 to 6 entries, each a real anchor with `target="_blank" rel="noopener noreferrer"`.
   Format: `Source name, what it supports`. **No dashes in these lines.**
8. **FAQ** — `<h3>FAQ</h3>` then 5 or 6 `<h4>` questions each followed by one `<p>` answer
   of 40 to 80 words. Use your brief's PAA targets.

## Word count
**2,300 to 2,800 words** of body prose. This is the DevCommX house standard and it
OVERRIDES any lower figure in the source sheet. Pillars may reach 3,000.
`add-blog-reading-time` = round(words / 220), as a string.

## Keyword rules
The **primary keyword must appear verbatim** in: the `name` (H1), the `meta-title`, the
first 100 words, **at least two `<h2>`s**, the body, **one FAQ question**, and the slug.
Work every **secondary keyword** in your brief into the body at least once, naturally.

## Sources and honesty
- Every statistic must come from a **named, linked, third-party source**, cited **inline
  at the claim** with an `<a>` anchor, not only in the References list. This is the single
  biggest scoring gap in the existing library, so fix it here.
- Research with WebSearch. Use real, currently-live sources: Google, Anthropic, OpenAI and
  vendor documentation, Gartner, Forrester, McKinsey, HubSpot, government data.
- **If your brief asks for DevCommX-proprietary data that you do not have, do NOT invent
  it.** Write the method, cite a third-party benchmark for scale, and mark the gap inline
  exactly as: `<!-- DATA GAP: <what the client must supply> -->`. List every gap in your
  final reply.

## Hard rules, all enforced by an automated gate
1. Valid JSON, no trailing commas.
2. **No em dashes or en dashes anywhere in any field.** Use commas, colons, periods.
   They slip into References lines most often. Check the whole file.
3. **Anchors use plain double quotes.** Never `href=\"...\"` with a backslash.
4. FAQ in the body must match the FAQPage schema **exactly**, same question and answer text.
5. `schema-markup` must parse and must end with the sequence `] } ] }`.
6. Internal links: at least 3, ONLY from the menu in your brief. Never invent a slug.
7. External links: at least 3, all `target="_blank"`.
8. CTA points to `/contact-us`. `/contact` is a hard 404.
9. `meta-title` <= 60 chars. `meta-description` 150 to 160 chars.

## schema-markup
A JSON **string** holding an `@graph` with a `BlogPosting` and a `FAQPage`. Keep this
house shape (it overrides the sheet's HowTo/ItemList/Service suggestions). Dates are
`2026-09-08`. FAQ entries must mirror the body FAQ exactly.

**Schema goes in TWO places and they must be byte identical.** The template renders the
`schema-markup` field, and every DevCommX post also carries the same JSON-LD as a script
inside `post-body`. Append this as the LAST thing in `post-body`, with the identical
schema string, bare JSON inside the script tag (never nest a second `<script>`):

```html
<div data-rt-embed-type='true'><script type="application/ld+json">

{the same schema string}
  </script></div>
```

```
{"@context":"https://schema.org","@graph":[{"@type":"BlogPosting","@id":"https://www.devcommx.com/blogs/{slug}#article","headline":"...","description":"...","url":"https://www.devcommx.com/blogs/{slug}","datePublished":"2026-09-08","dateModified":"2026-09-08","keywords":"...","image":{"@type":"ImageObject","url":"https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png","width":1200,"height":630},"author":{"@type":"Person","name":"Sumit Nautiyal","jobTitle":"VP of Revenue Operations & GTM Engineering, DevCommX","url":"https://www.linkedin.com/company/devcommx"},"publisher":{"@type":"Organization","name":"DevCommX","url":"https://www.devcommx.com","logo":{"@type":"ImageObject","url":"https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":"https://www.devcommx.com/blogs/{slug}"}},{"@type":"FAQPage","@id":"https://www.devcommx.com/blogs/{slug}#faq","mainEntity":[{"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}]}]}
```

## When done
Reply with ONLY: slug, word count, "JSON parses", the internal slugs you linked, and any
`DATA GAP` markers you left.
