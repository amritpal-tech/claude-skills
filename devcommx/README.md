# DevCommX blog operations — corpus and working state

Working data for the DevCommX Webflow SEO/AEO/GEO blog program. The **operating manual**
is the skill at `.claude/skills/devcommx-blog-ops/`; this directory is the state it acts on.

| Path | What it is |
|---|---|
| `blogs/{batch}/{slug}.json` | 53 built drafts as Webflow CMS items, ready to `create_collection_items` |
| `validation/{slug}.json` | 53 rubric findings, one per blog |
| `validation/workbooks/` | 4 colour-coded validation workbooks |
| `data/_existing_slugs.txt` | 149 slugs from the collection. **Includes unpublished drafts** — never treat as a live-link menu. |
| `data/_longtail_candidates.json` | un-drafted long-tail candidates |
| `figures/contact_sheet.html` | the 6 embedded SVG figures |
| `handoff-original/` | the source handoff verbatim: `HANDOFF.md`, `SKILLS_USED.md`, the 3 original specs, the 2 learned-rule notes |

## Batches

| Batch | Dir | N | Mean score |
|---|---|---|---|
| Long-tail | `blogs/longtail/` | 25 | 3.73 |
| Traffic sheet | `blogs/traffic/` | 16 | 4.26 |
| Pillars | `blogs/batch10/` | 4 | 4.29 (with tier1 + commercial) |
| Tier-1 vendor selection | `blogs/tier1/` | 4 | ↑ |
| Commercial | `blogs/commercial/` | 2 | ↑ |
| Rest | `blogs/rest/` | 2 | 4.06 |

53 blogs, mean **4.01**, 34 PUBLISH / 19 REVISE / 0 HOLD.

## Known state of the corpus

Verified by re-running the scripts against these files:

- **37 of 53 drafts have no `<h3>References</h3>` section.** The References requirement was
  added partway through the source session, so only the 16 traffic blogs carry it. This is
  a real content gap, not a tooling artifact.
- **`brand-mentions-vs-backlinks-ai-search` contains an em dash** in its References list
  ("arXiv 2311.09735 — evidence that..."). Exactly the failure mode the gotchas warn about.
  Fix before any republish.
- **The weakest criteria across all 53**, from the findings: Visual Elements 1.96/5,
  Pricing Transparency 2.25, Data Attribution 2.66, Stat Accuracy 2.70, Statistical
  Authority 2.89. The first is the missing-images gap; the rest are one problem —
  **sources sit in the References footer instead of being anchored inline at the claim.**

## Reproducing the numbers

```bash
python3 .claude/skills/devcommx-blog-ops/scripts/check_draft.py    devcommx/blogs/*/*.json
python3 .claude/skills/devcommx-blog-ops/scripts/score_findings.py devcommx/validation/*.json
```

## Publish state

**Unknown until re-enumerated.** The SEO team publishes independently, so what is draft
and what is live drifts. Run `/devcommx:blog-status` before acting on any of this.
