---
description: Audit DevCommX blogs for broken links, hard-rule violations, and spec drift.
argument-hint: "[batch, slug, glob, or 'live' for the whole collection]"
---
# /devcommx:blog-audit

Audit: **$ARGUMENTS**

Load `devcommx-blog-ops` and read `references/gotchas.md`.

## Steps

1. **Hard rules across the corpus:**
   ```bash
   python3 .claude/skills/devcommx-blog-ops/scripts/check_draft.py devcommx/blogs/*/*.json
   ```
   Known baseline: the 37 drafts predating the References requirement fail on
   `missing <h3>References</h3>`. That is a real gap, not a script bug. Report new
   failures separately from that known set.

2. **Every href in every post:**
   ```bash
   bash .claude/skills/devcommx-blog-ops/scripts/check_links.sh --drafts devcommx/blogs/*/*.json
   ```
   Internal targets must return 200. A CMS slug that exists but is an unpublished draft
   is a live 404.

   **If the session's network blocks devcommx.com** (curl 403 on CONNECT, WebFetch
   `EGRESS_BLOCKED`), the run reports everything DEAD and is worthless. Say so and stop
   rather than "fixing" working links.

3. **The specific defects to grep for:**
   - `devcommx.com/contact` without `-us` — a hard 404
   - `\"` inside `post-body` — broken anchors
   - em dash `—` or en dash `–` anywhere in fieldData, References lists especially
   - `<th>` missing `color:#1f2937` — white-on-grey header
   - `schema-markup` not ending `] } ] }`
   - FAQ body text diverging from the FAQPage schema

4. **External 403s** from Gartner, Apollo KB, SEC.gov, DOL.gov, Perplexity are anti-bot,
   not broken. Verify in a browser before changing anything.

## Fixing live items

Full fieldData, `isDraft` pinned to its current value, sequential updates, then
`publish_collection_items` for anything already live. See `/devcommx:blog-push`.

## Output

A defect table: slug, defect, whether it is live or draft, and the fix. Separate the
known baseline gaps from new regressions.
