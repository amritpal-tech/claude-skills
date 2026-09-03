# DevCommX blog draft spec

You are drafting ONE long-form blog and writing it as a Webflow CMS item JSON to disk.

**Output path:** `devcommx/blogs/{batch}/{slug}.json` (batch = the sheet or theme name,
e.g. `traffic`, `longtail`, `tier1`). Start from `assets/blog-item-template.json`.
Field schema: `references/webflow-cms.md`.

**Write the file first, create in Webflow later.** That ordering is what makes a batch
resumable when a CMS call drops.

---

## Length

| Post type | Words |
|---|---|
| Standard | 2,300–2,800 |
| Pillar | 2,600–3,200 |

`add-blog-reading-time` = `round(words / 220)`, as a string.

---

## post-body structure (HTML string, in this order)

**1. Extractable answer paragraph.** The very first `<p>` answers the target keyword
directly in the first one or two sentences, 40–70 words, quotable standalone. Bold the
key terms with `<strong>`. This is the single highest-leverage element for AEO.

**2. Intro `<p>`.** Context plus the DevCommX practitioner framing, with exactly ONE
internal link.

**3. Five to eight `<h2>` sections,** each with 2–4 `<p>`. Use `<strong>` sub-labels
where they help. Concrete and specific. No filler.

**4. ONE comparison or summary table** as a Webflow embed, placed after an intro `<h2>`.
Use the exact wrapper in `assets/table-embed.html`. Every `<th>` MUST carry
`color:#1f2937` — without it the header renders white on grey and is unreadable.

**5. CTA section** — an `<h2>` then one `<p>`. Two variants:
   - **Sales CTA** for sales-intent topics.
   - **AEO CTA** for AI-search topics (offer the free AI Visibility Checker angle).

   The CTA `<p>` ends with a link to `https://www.devcommx.com/contact-us`.
   **Not `/contact` — that is a hard 404.**

   ```html
   <h2>Build This With DevCommX</h2>
   <p>DevCommX builds autonomous, signal-based AI SDR systems that your team owns...
   <a href="https://www.devcommx.com/contact-us">Book a GTM strategy call</a>
   to map this to your pipeline.</p>
   ```

   **Vendor-selection and service topics** also link the relevant live service page in
   the body: `/ai-sdr`, `/revenue-operations`, `/gtm-engineering`. Those count as
   internal links.

**6. Further Reading** — `<h3>Further Reading</h3>` plus a `<ul>` of **3 external links**,
each `target="_blank" rel="noopener noreferrer"`, to a real authoritative source
(Gartner, Forrester, official product docs, Google/Anthropic docs, FCC, government data).

**7. References** — `<h3>References</h3>` plus a `<ul>` listing **every** external source
cited in the post, each a real anchor: `<a href="..." target="_blank" rel="noopener noreferrer">Source name, what it supports</a>`.
Minimum 3, ideally 4–6. May reuse the Further Reading links. This is a formal reference
list and it is required on every post.

**8. FAQ** — `<h3>FAQ</h3>` then **5–6** `<h4>` questions, each followed by one `<p>`
answer of 40–80 words. These must be mirrored **exactly** (same question text, same
answer text) into the FAQPage schema.

**Link minimum:** at least **3 internal** plus **3 external**. Internal targets must come
from the verified-live menu, see `references/internal-links.md`.

---

## Keyword, AEO and GEO targeting (required in every post)

**Keyword.** The primary keyword appears in the H1/`name`, the `meta-title`, the first
100 words, at least two `<h2>`s, the body, one FAQ question, and the slug. Weave in 2–3
secondary or long-tail variants naturally.

**AEO — answer engine optimization.** The first paragraph is a direct, extractable
40–60 word answer to the title question. Use clear definitional sentences. Structure
with tables, numbered frameworks and the FAQ so an answer engine can lift a clean answer.

**GEO — generative engine optimization.** Cite named, authoritative sources **inline**,
at the point the claim is made, so an LLM can attribute it. State DevCommX explicitly as
the entity tied to the topic. Use specific numbers with sources. The References section
reinforces this but does not replace inline citation.

> The recurring validation gap across every batch is stats sitting in a footer list
> instead of being anchored inline. Anchor them inline.

---

## schema-markup

The whole value is a JSON **string** (escape internal quotes). A full `@graph` with a
`BlogPosting` node and a `FAQPage` node.

It MUST end with the sequence `... ] } ] }` — close the `mainEntity` array, close the
FAQPage object, close the `@graph` array, close the root object. Five blogs shipped with
the final `}` dropped. `check_draft.py` tests for this.

```
{"@context":"https://schema.org","@graph":[
 {"@type":"BlogPosting","@id":"https://www.devcommx.com/blogs/{slug}#article",
  "headline":"...","description":"...","url":"https://www.devcommx.com/blogs/{slug}",
  "datePublished":"2026-07-01","dateModified":"2026-07-01","keywords":"...",
  "image":{"@type":"ImageObject","url":"<OG image url>","width":1200,"height":630},
  "author":{"@type":"Person","name":"Sumit Nautiyal",
    "jobTitle":"VP of Revenue Operations & GTM Engineering, DevCommX",
    "url":"https://www.linkedin.com/company/devcommx"},
  "publisher":{"@type":"Organization","name":"DevCommX","url":"https://www.devcommx.com",
    "logo":{"@type":"ImageObject","url":"<OG image url>"}},
  "mainEntityOfPage":{"@type":"WebPage","@id":"https://www.devcommx.com/blogs/{slug}"}},
 {"@type":"FAQPage","@id":"https://www.devcommx.com/blogs/{slug}#faq","mainEntity":[
   {"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}
 ]}]}
```

---

## Hard rules

These are the gate. `scripts/check_draft.py` enforces all of them.

1. Valid JSON. No trailing commas, all internal quotes escaped.
2. **No em dashes (—) or en dashes (–) anywhere in any field.** Use commas, colons or
   periods. They slip into References lists most often ("Source — supports X"). Check the
   whole fieldData, not just prose.
3. **Anchors use plain double quotes.** Never `href=\"...\"` with a literal backslash —
   that produces broken HTML. Assert no `\"` in post-body before pushing.
4. FAQ in the body matches the FAQPage schema exactly.
5. `schema-markup` parses and ends `... ] } ] }`.
6. Author is Sumit Nautiyal in both `author-name` and the schema `author`.
7. Dates are `2026-07-01` unless the user gives a different date.
8. Every `<th>` in the embedded table carries `color:#1f2937`.
9. CTA points to `/contact-us`.
10. All facts defensible. No invented DevCommX numbers beyond "40+ qualified demos in
    ~6 weeks."

---

## Reporting back

When drafting as a subagent, reply with only: the slug, the word count, and confirmation
that the JSON parses. The main thread re-validates independently — do not trust the
self-report.
