---
description: Score DevCommX blog drafts on the 6-dimension rubric and build the validation workbook.
argument-hint: "[batch name, slug, or glob]"
---
# /devcommx:blog-validate

Validate: **$ARGUMENTS**

Load `devcommx-blog-ops` and read `references/validation-rubric.md`.

## Steps

1. **Hard rules first.** `scripts/check_draft.py` on every target. A draft that fails the
   hard rules does not need a rubric score, it needs a fix.
2. **Rubric pass.** One agent per blog, each scoring all 6 dimensions × 5 criteria and
   writing `devcommx/validation/{slug}.json`. Findings must **quote actual evidence from
   that blog**. Generic findings are unacceptable. Agents do **not** compute the verdict.
3. **Score in the main thread** — the agents mislabel verdicts:
   ```bash
   python3 .claude/skills/devcommx-blog-ops/scripts/score_findings.py devcommx/validation/*.json
   ```
4. **Workbook** (main thread only, openpyxl):
   ```bash
   python3 .claude/skills/devcommx-blog-ops/scripts/build_workbook.py \
       --out devcommx/validation/workbooks/DevCommX_{Batch}_Blog_Validation.xlsx \
       devcommx/validation/*.json
   ```

## Calibration

Do not inflate. No in-body images means Visual Elements is 2/5 at best. No pricing
discussion means Pricing Transparency is not 4–5. Verdicts: ≥3.9 PUBLISH, ≥2.75 REVISE,
below that HOLD.

## Output

The score table, the verdict split, the weakest criteria across the set, and the
workbook path. Call out any blog whose score moved a verdict boundary.
