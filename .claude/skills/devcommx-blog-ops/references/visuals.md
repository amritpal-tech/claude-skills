# Visuals

The standing weakness of the whole library. Every validation batch scores **Visual
Elements ~2/5** because the drafts carry no in-body images, only an OG image.

## What can be produced here

**Inline SVG figures.** These render inside a Webflow HTML embed, the same mechanism as
the comparison tables, so **no asset upload is needed**. Wrap in
`<div data-rt-embed-type='true'>...</div>`. Keep each figure **under ~9KB** — the embed
block caps around 10,000 characters.

Six posts already carry embedded figures. A contact sheet of them is at
`devcommx/figures/contact_sheet.html`.

## Brand rules for every figure

From `devcommx-brand`. Load that skill for anything beyond this summary.

- **Electric Blue `#2F5BFF` is the only accent.** Ink `#0C0F1A` text. Mist `#EEF1F8`
  panels. Signal Red `#FF3B1F` for the risk or myth. Signal Green `#1F8F3A` for the win.
- Flat fills. **No gradients, no drop shadows, no glows, no 3D.**
- 0.5px hairlines. Generous whitespace.
- Inter for type, JetBrains Mono for every number and label.
- Numbers are mono **and sourced**.

Figure patterns that worked: two-card comparisons, numbered checklists with a red
walk-away panel, build/buy/hybrid decision boxes, workstream tile grids, two-column
spec comparisons.

## What cannot be produced here

**Product screenshots and dashboards must be captured from real tools by the client.**
Do not fabricate them. Where a post needs one, write the spec instead: dimensions, alt
text, placement, and what to redact.

Heroes and OG art can be generated. Every generation prompt should end with:

> Flat design, no gradients, no drop shadows, 0.5px hairlines, generous whitespace,
> Inter typeface, Electric Blue #2F5BFF as the only accent on an off-white #FFFFFF or
> Ink #0C0F1A ground. No stock-photo people, no 3D, no glow.

Export heroes at **1200×630** for OG, name `dcx-blog-{slug}-hero.png`, keep the DevCommX
D mark bottom-left with 1X clear space.

## Per-post specs

The worked example for six posts, with figure descriptions, hero prompts, alt text and
screenshot requests, is preserved at
`devcommx/handoff-original/specs/_VISUALS_SPEC_recent6.md`. Follow that format when
speccing visuals for a new batch.
