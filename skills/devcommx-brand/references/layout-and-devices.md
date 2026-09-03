# Design system — devices, grid, icons, data

Brand Book v3.1, Sections 04 and 05.

## The six graphic devices

Six devices carry the brand across every page. They repeat, so the reader learns
the system fast — and every one earns its place. **A reader who sees the ghost
numeral, the eyebrow, and the hatch on page one already knows the system by page
three. Nothing new is invented per page.**

| # | Device | Spec |
|---|---|---|
| 01 | **Ghost numeral** | The section number, oversized and faint, top-right. Orients the reader without shouting. Typically Inter 800 at ~120–180px in a 6–10% tint of the surface's contrast colour. |
| 02 | **Eyebrow kicker** | All-caps, wide-tracked label, top-left. Electric blue. Names the section in one glance. |
| 03 | **Diagonal hatch** | The 45° texture drawn from the logo D. `var(--dcx-hatch-navy)`. An accent only — never a full background. Fades in from one corner. |
| 04 | **Hairline & footer** | A 0.5px rule structures the page and caps the footer. Thin lines, generous air. Footer = mark bottom-left, page number bottom-right, mono. |
| 05 | **Semantic colour** | Colour carries meaning, not decoration. Blue = answer/key idea. Red = myth/old rule. Green = win/proof. One hero hue per page, used to a rule. |
| 06 | **Card system** | Plain, tint, and blue-accent cards — 8–12px radius, hairline border, **no shadow**. |

## Grid & spacing

| Property | Value |
|---|---|
| Columns | 12 |
| Gutter | 6px |
| Margin | 15mm |
| Print format | A4 |

Spacing base: **4 / 8pt** → 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64.

Structure stays invisible; the reader only feels the calm.

## Layout principles

- **Anchor content low.** Headline and body settle toward the lower two-thirds.
  The page reads with weight.
- **Top as negative space.** Leave the upper band open. Only the eyebrow and the
  ghost numeral live there.
- **One hero colour.** A single accent per page carries meaning. Everything else
  stays ink and white.
- **Generous whitespace.** Space is a device. Aim for a confident 60–80% fill,
  never a crammed page.

## Iconography

One monoline set, built on a 24px grid to match Inter. Geometric, clarity, never
ornament.

| Property | Value |
|---|---|
| Grid | 24 × 24px |
| Stroke | 1.5px |
| Joins & caps | Round |
| Style | Monoline |
| Corner | 2px radius |

**Do:** keep one consistent 1.5px stroke across the whole set; align every shape to
the 24px grid and its keylines; round all joins and caps.

**Don't:** no filled or duotone shapes; don't mix stroke weights or add drop
shadows; don't skew, stretch, or place icons off the grid.

Core set in use: signal · search/ai · chart-up · target · mail · flywheel · check ·
document.

---

## Data & charts — proof, shown simply

Numbers a CRO can read in a glance. We chart pipeline outcomes, round the numbers,
and **label anything illustrative** so real proof stays honest.

Rules, verbatim from the book:
- Flat fills
- One accent + neutral
- Mono numbers
- No 3D · no gradients
- Round figures
- Label illustrative

Chart patterns in the system:
- **Score ring** — coverage/progress. Green stroke on a neutral track, mono figure
  in the centre.
- **Bar chart** — before/after. Mint = before, blue = after. Nothing else on the
  canvas. Value labels sit above the bars in mono.
- **Stacked bar / breakdown** — one blue bar carries the leading segment, the rest
  in neutral. Percentages right-aligned in mono.
- **Scorecard** — 2×2 tiles, one number per tile, mono, with a one-line caption
  underneath naming what it is and whether it is real proof or illustrative.

Colour a figure only when it means something: blue = the key number, green/mint =
the win, red = the risk or the zero that hurts.

---

## Interface kit

Consistent radii, half-pixel hairlines, blue for the action, red only when it warns.
Plain labels — the button says what the visitor gets.

| Element | Spec |
|---|---|
| Radius | 9px on every control |
| Hairline | 0.5px |
| Primary button | Blue fill, white label — the action |
| Destructive button | Red fill, white label — destructive only |
| Secondary button | Mist fill, ink label |
| Ghost button | Outline, ink label |
| Shadows | None (except a faint lift on device mockups) |

**Badges & pills:** one label per pill. Blue tags the offer, green marks the
flagship state, mono carries a term. No overlap, generous gap.

**Forms:** one field per line, labels above. Placeholder in muted, typed value in
ink. Focus state = 1.5px blue border. The submit button carries the value —
"Get my free GTM strategy", never a vague "Submit".

**Nav:** white logo on ink, one blue CTA, links tracked tight.

Every control shares the same corner and the same line weight.
