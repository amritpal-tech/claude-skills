# Logo — full reference

Brand Book v3.1, Section 01. One wordmark, three surfaces.

## Anatomy

Two parts, always locked together:
- The **charcoal "DevCommX" wordmark**, set in Inter.
- The **"D" symbol** — a navy counter with diagonal hatching that resolves into a
  red curve. That hatch echoes across the whole brand as our signature texture.

Tagline lockup: `EMPOWERING IDEAS. ENGINEERING SOLUTIONS.` sits beneath the
wordmark, all caps, tracked wide.

**Mark colours are fixed and sit outside the UI palette:**
`#213065` navy · `#D22B27` red. They are never used for interface colour.

## Variants

| Variant | When |
|---|---|
| **Colour · on light** | The default. White or Mist backgrounds only. |
| **White · on dark** | Ink, blue, red, green, or photographic surfaces. |
| **Black · one-colour** | Single-ink print, fax, engraving, stamps. |

## Clear space & minimum size

The measurement unit is the cap height of the "D" — call it **X**.

- Keep at least **1X of empty space on every side**, clear of type, edges, and
  other marks. More is always fine; less is never.
- Never let text, imagery, or a page edge enter the clear zone.
- The full lockup holds down to **120px wide, or 28mm in print**.
- Below that, drop to the "D" symbol — favicons, avatars, app tiles.

## The D symbol

Same navy and red, same hatch, square footprint.

| Use | Spec |
|---|---|
| App icon | Rounded square, ~24% corner radius. Colour D on white; white D on Electric Blue or Ink. |
| Favicon | Ships at 16 / 32 / 64 px (and 180px for touch). At the smallest size the hatch simplifies — legibility beats detail. |
| Social avatar | White D on Electric Blue, centred in a circle. The default profile picture across platforms. |

**Use the full lockup when:** the brand is being introduced for the first time;
there is room for the wordmark at 28mm or wider; on covers, decks, letterhead,
headers, and email signatures.

**Use the D symbol when:** space is square or tight; the full lockup would fall
below its minimum size; the audience already knows the brand and needs a shorthand.

## Misuse — the six we see most

1. **Don't recolour the wordmark.** It is charcoal. Full stop.
2. **Don't stretch or distort.** Scale proportionally, never one axis.
3. **Don't sit it on busy colour or texture.** On mid-tones or texture, use the
   white lockup.
4. **Don't add shadow or outline.** No drop shadows, glows, or strokes.
5. **Don't rotate or tilt.** The mark always sits level and horizontal.
6. **Don't rebuild the D by hand.** Never redraw or re-typeset. Use the file.

One rule underneath all six: **use the supplied logo files, unaltered.**

## Files

```
~/devcommx-brand-assets/logos/dcx-logo-color.png
~/devcommx-brand-assets/logos/dcx-logo-white.png
~/devcommx-brand-assets/logos/dcx-logo-black.png
~/devcommx-brand-assets/derived/dcx-symbol-transparent.png
~/devcommx-brand-assets/derived/dcx-symbol-white.png
~/devcommx-brand-assets/derived/dcx-symbol-square.png
~/devcommx-brand-assets/book/book.css          ← design tokens, book source
```

## File naming

```
dcx-[asset]-[variant].[ext]

dcx-carousel-aeo-01.png
dcx-banner-company-ink.png
dcx-ad-square-18score.png
dcx-deck-title-ink.png
```

Lowercase, hyphenated, prefixed `dcx-`. Variant last.
