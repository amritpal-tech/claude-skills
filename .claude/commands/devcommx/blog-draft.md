---
description: Draft one or more DevCommX blogs to the spec and write them to disk.
argument-hint: "[keyword, topic, or slug list]"
---
# /devcommx:blog-draft

Draft: **$ARGUMENTS**

Load `devcommx-blog-ops` and read `references/draft-spec.md` in full first. Start from
`assets/blog-item-template.json`.

## Before writing a word

1. Run the topic through `devcommx-keyword-governance`. A brief without its
   classification block is not ready to write.
2. Dedup against `devcommx/data/_existing_slugs.txt` and `devcommx/blogs/`.
3. Get the verified-live internal-link menu (`references/internal-links.md`).

## Writing

- 2,300–2,800 words, pillars 2,600–3,200.
- Structure in order: extractable answer paragraph, intro with one internal link,
  5–8 H2 sections, one table embed, CTA to `/contact-us`, Further Reading,
  References, FAQ of 5–6 Q/A mirrored exactly into the FAQPage schema.
- Keyword in H1, meta-title, first 100 words, ≥2 H2s, one FAQ question, the slug.
- **Cite named sources inline, at the claim**, not only in the References footer. This
  is the single biggest recurring scoring gap in the library.
- No em or en dashes. No `\"` in anchors. Every `<th>` carries `color:#1f2937`.

Write to `devcommx/blogs/{batch}/{slug}.json`. **Write the file before touching Webflow.**

## Then

```bash
python3 .claude/skills/devcommx-blog-ops/scripts/check_draft.py devcommx/blogs/{batch}/{slug}.json
```

Fix every ERROR. Report the slug, word count, hard-rule result, and the internal and
external links used.
