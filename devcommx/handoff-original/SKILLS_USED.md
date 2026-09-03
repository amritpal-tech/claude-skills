# Skills & tools used this session

## Skills (Claude Skill tool)

| Skill | What it is | How it was used here | In this zip |
|---|---|---|---|
| **anthropic-skills:content-validator** | Generates a color-coded multi-tab Excel validation workbook scoring content across quality/SEO/GEO-AEO/brand/structure/schema. | The 6-dimension rubric for every validation pass; produced the 4 `.xlsx` workbooks. Rubric captured in `specs/_VALIDATION_SPEC.md`. | `skills/content-validator/` (SKILL.md + scripts/excel_helpers.py) |
| **devcommx-brand** | DevCommX Brand Book v3.1 (logo-first): canonical colors, type, layout, voice, the 6 graphic devices, checklist. | Source of truth for the 6 on-brand SVG figures. Colors: Electric Blue `#2F5BFF`, Ink `#0C0F1A`, Mist `#EEF1F8`, Signal Red `#FF3B1F`, Signal Green `#1F8F3A`; Inter + JetBrains Mono; flat fills, hairlines, semantic color. | `skills/devcommx-brand/` (full copy) |
| **anthropic-skills:docx** | Create/read/edit Word docs. | Every `.docx` review compilation was produced with pandoc following this skill's guidance (docx-js gotchas, pandoc for HTML→docx). | rubric/notes in HANDOFF |
| **anthropic-skills:xlsx** | Spreadsheet create/edit. | Backstop for the validation workbooks (openpyxl). | — |
| **artifact-design** | Design guidance for published Artifacts. | The web review docs (HTML artifacts) were designed per this: navy `#213065` + coral `#D22B27` review-doc system, theme-aware tokens. | — |
| **anthropic-skills:pdf** | PDF read/render. | Rendering docx→PDF→JPG to visually verify Word/Excel output. | — |
| **devcommx-keyword-governance** (available) | DevCommX keyword filter + exclusion list, 3-question rule. | The dedup/skip discipline mirrors this (draft only GREENLIGHT/REFINE; skip off-vertical/duplicate/off-service-line). | — |

## MCP tools / connectors used

- **Webflow** (`data_cms_tool`, server `mcp__2b3254d1-…`): list/create/update/publish CMS items. **Requires authorization on the target account.**
- **Google Drive** (`read_file_content`): reading the keyword/topic Google Sheets & Docs.
- **Slack** (`slack_read_channel`, `slack_search_public`): reading `#devcommx-website-seo-team` (channel `C08GHET487R`) for the suggested keywords + blog fixes.
- **Browser pane** (`preview_start`, `computer`): rendering/verifying HTML docs and SVG figures; opening live pages.
- **Artifact tool:** publishing the web review docs.
- **Workflow tool:** the fan-out engine — parallel drafting/validation, strictly-sequential creation. Scripts followed the `workflow-authoring` reference.

## Reusable process assets in this zip

- `specs/_DRAFT_SPEC.md` — the full blog authoring spec (structure, schema, References, keyword/AEO/GEO rules, hard rules).
- `specs/_VALIDATION_SPEC.md` — the 6-dimension validation rubric an agent follows to produce findings JSON.
- `specs/_VISUALS_SPEC_recent6.md` — per-post visual spec + generation prompts for screenshots/hero art.
- `skills/content-validator/scripts/excel_helpers.py` — the workbook styling helpers (assign returned style objects; light-shade colors must be defined locally).
- `learned-rules/` — the two durable gotcha notes (CMS concurrency bug, internal-link liveness + `/contact-us`).

## To reproduce the skills on another account

- **content-validator, docx, xlsx, pdf, artifact-design** are Anthropic/plugin skills — enable them from the target account's skill/plugin settings (they're standard). Their behavior is captured in the spec files here so nothing is lost if a version differs.
- **devcommx-brand** is a custom skill — copy `skills/devcommx-brand/` into `~/.claude/skills/devcommx-brand/` on the target machine (it reads `~/devcommx-brand-book-logo-first.pdf` for the deep reference, but the SKILL.md carries the tokens needed for figures).
- **devcommx-keyword-governance** is custom — recreate from the 3-question rule + exclusion list if needed.
