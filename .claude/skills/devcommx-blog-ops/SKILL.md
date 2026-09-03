---
name: devcommx-blog-ops
version: 1.0.0
description: |
  Run the DevCommX SEO/AEO/GEO blog program in Webflow CMS end to end: turn keyword
  and topic sheets into long-form blog drafts against a strict spec, validate them on
  a 6-dimension rubric, push them into the Webflow Blog collection as drafts, audit
  internal links, embed on-brand figures, and compile review docs and validation
  workbooks.
  Use whenever the user mentions DevCommX blogs, DevCommX Webflow, blog drafts,
  blog batch, blog validation, the validation workbook, CMS items, post-body,
  schema-markup, the blog collection, "push to Webflow", "create the drafts",
  "validate the blogs", "audit the links", or names any DevCommX blog slug.
  Carries the Webflow collection IDs, the exact CMS field schema, the draft spec,
  the validation rubric, the proven batch pipeline, and the hard-won gotchas
  (CMS concurrency bug, /contact-us not /contact, internal-link liveness).
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebSearch
  - WebFetch
  - AskUserQuestion
  - Skill
---

# DevCommX blog operations

The operating manual for DevCommX's Webflow blog program. **Read the reference file
for the phase you are in before acting** — the details below are the index, not the
whole spec.

| Reference | Read it when |
|---|---|
| [references/webflow-cms.md](references/webflow-cms.md) | Any read or write against the Webflow CMS |
| [references/draft-spec.md](references/draft-spec.md) | Writing or editing a blog draft |
| [references/internal-links.md](references/internal-links.md) | Choosing internal links, before drafting anything |
| [references/validation-rubric.md](references/validation-rubric.md) | Scoring drafts, building a workbook |
| [references/pipeline.md](references/pipeline.md) | Running a whole batch start to finish |
| [references/schema-dates.md](references/schema-dates.md) | Anything touching schema, dates, or the two schema locations |
| [references/gotchas.md](references/gotchas.md) | **Always.** These are failures that already shipped. |
| [references/visuals.md](references/visuals.md) | Adding figures, heroes, screenshots |
| [references/state.md](references/state.md) | Picking up where the last session stopped |

Corpus and working state live in **`devcommx/`** at the repo root: 53 built drafts
(`devcommx/blogs/`), 53 validation findings (`devcommx/validation/`), 4 workbooks,
the slug inventory (`devcommx/data/_existing_slugs.txt`), and the original handoff.

---

## The account in one paragraph

DevCommX is a B2B agency that builds autonomous, signal-based **AI SDR and
GTM-engineering systems** (outbound, RevOps, Clay, cold email, LLMO/AEO). The
differentiator is that **clients own the infrastructure**, they are not renting a
managed campaign. The only sanctioned proof point is **"40+ qualified demos in
~6 weeks."** Every blog is authored by **Sumit Nautiyal, VP of Revenue Operations
& GTM Engineering, DevCommX**. Voice is practitioner, direct, no hype.

**Never invent DevCommX case-study numbers beyond the 40+ demos framing.**

---

## The five facts you cannot get wrong

1. **Blog collection ID:** `689c92652a4b35f0e9a14fc2`.
2. **The CTA URL is `/contact-us`.** `https://www.devcommx.com/contact` is a hard 404.
3. **Webflow CMS writes must be sequential.** Parallel creates double-create items and
   cross-wire responses. Drafting can fan out; writing never does.
4. **No em dashes or en dashes anywhere** in any field, prose or References list.
5. **Schema lives in TWO places** per blog: the `schema-markup` field and a JSON-LD
   script inside `post-body`. They drift. Fix both, and store bare JSON in the field.
6. **Internal links must be curl-verified 200 before use.** The CMS slug list includes
   unpublished drafts, so "exists in the CMS" does not mean "resolves on the site."

---

## Standard workflow

```
sheet/topics → dedup → verify link menu (200s) → draft (parallel, to disk)
   → check_draft.py (hard rules) → validate (rubric → findings JSON)
   → score_findings.py (weighted verdict) → build_workbook.py
   → push to Webflow SEQUENTIALLY as drafts → re-enumerate + dedupe → review doc
```

Publishing is **draft-only unless the user explicitly says publish.** An update to a
live item only *stages* the change; it needs `publish_collection_items` to go public.

---

## Scripts

Run from the repo root. All are dependency-light (`openpyxl` only for the workbook).

| Script | Purpose |
|---|---|
| `scripts/check_draft.py` | Hard-rules gate on a draft JSON: parse, dashes, `\"` anchors, schema close, FAQ mirror, table header colour, word count, link counts, CTA URL, References. **Run on every draft before pushing.** |
| `scripts/score_findings.py` | Weighted score and verdict from a validation findings JSON. The agents mislabel verdicts, always recompute. |
| `scripts/build_workbook.py` | Findings JSONs to a colour-coded multi-tab `.xlsx`. |
| `scripts/check_links.sh` | Curl-verify internal link targets return 200. |
| `scripts/fix_schema_dates.py` | Compute and verify schema date corrections across both schema locations. |
| `scripts/apply_schema_date_fix.py` | Apply that fix straight against the Webflow API, with backup, read-back and publish. |
| `scripts/excel_helpers.py` | openpyxl styling helpers used by `build_workbook.py`. |

```bash
python3 .claude/skills/devcommx-blog-ops/scripts/check_draft.py devcommx/blogs/traffic/*.json
python3 .claude/skills/devcommx-blog-ops/scripts/score_findings.py devcommx/validation/*.json
bash   .claude/skills/devcommx-blog-ops/scripts/check_links.sh slug-a slug-b
```

---

## Related skills

- **devcommx-keyword-governance** — run the 3-question rule and the exclusion list on
  every keyword **before** drafting. A brief without its classification block is not
  ready to write.
- **devcommx-brand** — colours, type, and the graphic devices for any figure or doc.
- **ai-seo**, **schema-markup**, **seo-audit** — general technique; this skill's specs win
  on anything DevCommX-specific.

## Commands

`/devcommx:blog-batch` `/devcommx:blog-draft` `/devcommx:blog-validate`
`/devcommx:blog-push` `/devcommx:blog-audit` `/devcommx:blog-status`
`/devcommx:blog-figures` `/devcommx:blog-review-doc`
