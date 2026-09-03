---
description: Run a full DevCommX blog batch end to end — sheet to validated Webflow drafts.
argument-hint: "[sheet URL, topic list, or batch name]"
---
# /devcommx:blog-batch

Run the whole pipeline for: **$ARGUMENTS**

Load the `devcommx-blog-ops` skill and read `references/pipeline.md` and
`references/gotchas.md` before starting. Do not skip a step or reorder them; the
ordering is what prevents the known failure modes.

## Steps

1. **Preconditions** — confirm the Webflow connector is authorized (`webflow_guide_tool`
   once). Confirm which batch directory this writes to (`devcommx/blogs/{batch}/`).
2. **Keyword gate** — run every candidate through `devcommx-keyword-governance`. Emit the
   classification block per topic. Drop anything that is excluded or answers "do not build".
3. **Dedup** — against `devcommx/data/_existing_slugs.txt`, everything in `devcommx/blogs/`,
   and the live collection. Report overlaps and how you are differentiating them.
4. **Link menu** — verify internal targets return 200 (`scripts/check_links.sh`). If the
   session cannot reach the domain, say so and use only targets the user confirms.
5. **Draft** — fan out, **max ~13 agents**, one blog each, against `references/draft-spec.md`.
   Every agent writes JSON to disk and reports slug, word count, parse status.
6. **Gate** — `scripts/check_draft.py` on every file. Fix every ERROR before step 7.
   Do not trust the agents' self-reports.
7. **Push** — `/devcommx:blog-push`. **Sequential only.** Drafts unless told otherwise.
8. **Re-enumerate** — confirm clean singletons, no `-xxxxx` suffixed duplicates.
9. **Validate** — `/devcommx:blog-validate` for findings, scores and the workbook.
10. **Review doc** — `/devcommx:blog-review-doc`.

## Output

A batch report: topics accepted and rejected with reasons, drafts written, hard-rule
results, what was created in Webflow with its item IDs, the weighted scores, and the
open items. State plainly anything you could not verify.
