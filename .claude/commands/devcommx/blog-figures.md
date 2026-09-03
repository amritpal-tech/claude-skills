---
description: Generate and embed on-brand SVG figures into DevCommX blog drafts.
argument-hint: "[slug or batch]"
---
# /devcommx:blog-figures

Add figures to: **$ARGUMENTS**

Load `devcommx-blog-ops` (read `references/visuals.md`) and `devcommx-brand`.

## Why

Visual Elements scores **~2/5 across every batch** — it is the library's standing
weakness, and the drafts carry no in-body images at all. An embedded SVG lifts it off
the floor without any asset upload.

## How

- Inline SVG **renders inside a Webflow HTML embed**, same mechanism as the tables.
  Wrap it: `<div data-rt-embed-type='true'>...</div>`.
- **Keep each figure under ~9KB.** The embed block caps around 10,000 characters.
- Brand rules, non-negotiable: Electric Blue `#2F5BFF` as the only accent, Ink `#0C0F1A`
  text, Mist `#EEF1F8` panels, Signal Red `#FF3B1F` for the risk, Signal Green `#1F8F3A`
  for the win. Flat fills only, no gradients, no shadows, no 3D. 0.5px hairlines.
  Inter for type, JetBrains Mono for every number and label.
- Patterns that worked: two-card comparisons, numbered checklists with a red walk-away
  panel, build/buy/hybrid decision boxes, workstream tile grids, two-column spec tables.
- Every figure needs alt text and a caption naming the source of any number in it.

## What you must not do

**Do not fabricate product screenshots or dashboards.** Where a post needs one, write
the spec instead — dimensions, alt text, placement, what to redact — for the client to
capture. Follow the format in
`devcommx/handoff-original/specs/_VISUALS_SPEC_recent6.md`.

## Then

Re-run `scripts/check_draft.py` (the embed-size check will flag an oversized figure),
push the updated items sequentially, and republish anything already live.

## Output

The figures added per post, a contact sheet for review, and the visual specs handed
back to the client for anything requiring a real screenshot.
