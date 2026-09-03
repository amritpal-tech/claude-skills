# The batch pipeline

The proven sequence. Repeat per batch. Deviating from the ordering is what caused every
gotcha in `gotchas.md`.

---

## 0. Preconditions

- Webflow MCP connector authorized on this account. Call `webflow_guide_tool` once.
- `devcommx-keyword-governance` run on every candidate keyword. A brief without its
  classification block is not ready to write.

## 1. Read the source sheet

Google Sheet or Doc via the Drive connector (`read_file_content`), or a pasted list.
**Apply the sheet's own tier, skip and consolidation verdicts — they are authoritative.**

## 2. Dedup

Check every candidate against:
- `devcommx/data/_existing_slugs.txt`
- everything already in `devcommx/blogs/`
- the live site

Never draft a duplicate. Where two topics overlap, differentiate the angles and
cross-link them.

## 3. Verify the internal-link menu

Curl every candidate internal target for a 200 and keep only those.
`scripts/check_links.sh`. Hand the drafting agents **only the verified menu**.
See `internal-links.md`.

## 4. Draft in parallel

Fan out, one agent per blog, general-purpose type. **Cap the batch at ~13 agents** — a
31-agent run tripped an org token cap mid-flight.

Each agent:
1. reads `references/draft-spec.md`,
2. researches with WebSearch,
3. writes the `fieldData` JSON to `devcommx/blogs/{batch}/{slug}.json`,
4. self-validates and reports slug, word count, JSON parses.

**Write the file first, create in Webflow later.** This is what makes the batch resumable.

## 5. Validate the hard rules independently

In the main thread, **do not trust the agents' self-reports**:

```bash
python3 .claude/skills/devcommx-blog-ops/scripts/check_draft.py devcommx/blogs/{batch}/*.json
```

Checks: JSON parses, schema-markup parses and closes `] } ] }`, word count in range,
FAQ body mirrors FAQ schema, table `<th>` colour, References present, no em/en dashes,
no `\"` anchors, ≥3 internal and ≥3 external links, `/contact-us` CTA, reading time,
author fields. Fix everything it flags before step 6.

## 6. Create in Webflow, STRICTLY SEQUENTIALLY

One `create_collection_items` call at a time. `isDraft: true`. After each, **verify the
returned slug has no random `-xxxxx` suffix**. If a call drops mid-response, enumerate
before retrying. See `gotchas.md` #1.

## 7. Re-enumerate and dedupe

Paginate the collection (offsets 0, 100, 200), match by slug prefix, confirm clean
singletons. Delete duplicates only with explicit user approval — deletion is permanent.

## 8. Score the batch

Fan out validation agents against `references/validation-rubric.md`, each writing
`devcommx/validation/{slug}.json`. Then, in the main thread:

```bash
python3 .claude/skills/devcommx-blog-ops/scripts/score_findings.py devcommx/validation/*.json
python3 .claude/skills/devcommx-blog-ops/scripts/build_workbook.py \
    --out devcommx/validation/workbooks/DevCommX_{Batch}_Blog_Validation.xlsx \
    devcommx/validation/*.json
```

## 9. Compile the review doc

Standalone HTML, then `.docx` via pandoc. The HTML review-doc design system used for
these is navy `#213065` plus coral `#D22B27`, theme-aware tokens.

## 10. Publish decisions are the user's

Everything is created as a **draft**. Publishing is a separate, explicit instruction.
An update to a live item only *stages* the change; it needs `publish_collection_items`.

**Hub sets publish together.** A group of posts that link to each other (e.g. the
Sales-Ops hub of 6) must be published as a set, or the inter-hub links 404.
