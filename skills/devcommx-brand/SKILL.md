---
name: devcommx-brand
version: 1.0.0
description: |
  Apply the DevCommX Brand Book v3.1 (logo-first) to anything being produced for
  DevCommX — creatives, carousels, single-image posts, banners, avatars, ads,
  decks, PDFs, documents, letterheads, email signatures, web pages, landing pages,
  UI, charts, and video. Use whenever the output carries the DevCommX name or will
  be seen by a DevCommX prospect, and whenever the user says "brand it", "use our
  branding", "on-brand", "brand book", "brand guidelines", "DevCommX style", or
  names DevCommX while asking for a design, document, deck, or page.
  Loads the canonical colors, type scale, logo rules, layout system, voice, and the
  pre-publish checklist. This overrides any earlier or remembered DevCommX palette.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# DevCommX brand system

Source of truth: `~/devcommx-brand-book-logo-first.pdf` (Brand Book **v3.1 · 2026**).
Source files: `~/devcommx-brand-assets/`. Tokens: `assets/dcx-tokens.css` in this skill.
Owner: amritpal@devcommx.com.

**If any other document, memory, or older file states different DevCommX hex values,
this skill wins.** The pre-v3 palette (`#000814`, `#4d9fff`) is dead.

---

## The one-paragraph brief

DevCommX is the go-to-market firm that runs all nine motions — agentic, and made
simple. Everything we ship is **proof over polish**, written for the most senior
person in the room, and built on a high-contrast system where **every colour means
something**. Blue is the answer. Red is the myth or the risk. Green is the win. Ink
is the depth. White is the room to think. One hero colour per surface, one idea per
block, one action at the end.

---

## Non-negotiables (apply to every output)

1. **One hero background colour per surface.** A page, section, or slide gets one
   dominant colour. Never stack two heroes side by side.
2. **Colour ratio ~70 / 20 / 10** — 70% neutral (white / mist / ink), 20% Electric
   Blue, 10% signal (red / green).
3. **Body text is never blue.** Blue marks the key idea and the action only.
   Reading copy is ink on light, white on dark.
4. **Flat fills only.** No gradients, no 3D, no drop shadows, no glows. Hairlines
   are 0.5px. Radius is 9px for controls, 8–12px for cards.
5. **Headlines in sentence case.** Capitalise the first word only. Eyebrows in ALL
   CAPS, tracked +14%, weight 600, electric blue.
6. **Highlight with colour, not underline.** Underline is reserved for links.
7. **Inter for everything typographic; JetBrains Mono for every number, label, and
   piece of meta.** Numbers are always mono and tabular.
8. **Every claim carries a real number.** Round it, source it, and label anything
   illustrative as illustrative. No stat without a source.
9. **Ends with one usable action.** One decision per asset. Two decisions = two assets.
10. **Never redraw the logo.** Use the supplied files, unaltered, with 1X clear space.

---

## Colour — memorise these

| Role | Name | Hex | Use |
|---|---|---|---|
| Primary | Electric Blue | `#2F5BFF` | Key idea, action, CTA |
| Primary | Ink | `#0C0F1A` | Dark surface, body text |
| Primary | White | `#FFFFFF` | Base, clarity, space |
| Primary | Mist | `#EEF1F8` | Panels, quiet fills |
| Signal | Signal Red | `#FF3B1F` | Old rule, myth, risk, CTA background |
| Signal | Signal Green | `#1F8F3A` | The win, proof, positive |
| Signal | Mint | `#7EE692` | Positive metric **on dark** |
| Signal | Sky Tint | `#8CB0FF` | Soft highlight, accent |
| Support | Surface | `#181B25` | Raised dark panels |
| Support | Charcoal | `#333333` | Wordmark, deep neutral text |
| Support | Muted | `#5A6173` | Meta, secondary text |
| Support | Hairline | `#E2E6F0` | 0.5px rules, card borders |

**Logo-only colours — never used for UI:** navy `#213065`, red `#D22B27`. These
belong to the mark alone and sit outside the UI palette.

Contrast pairs that ship: ink/white 18.1:1 · white/ink 18.1:1 · white/blue 4.9:1 ·
ink/mist 16.4:1. **White on Signal Red is 3.4:1 — large text and fills only, never
body copy.**

Full tint/shade ramps (50→900 per hue): `references/color.md`.

---

## Typography — the scale

| Role | Font | Spec |
|---|---|---|
| Display | Inter 800 | 46–70px, tracking −2.5%, sentence case |
| Section (H2) | Inter 800 | 24px, tracking −2.0%, sentence case |
| Eyebrow | Inter 600 | 10px, +14% tracking, ALL CAPS, electric blue |
| Body | Inter 400–500 | 11–13px, 0% tracking, sentence case |
| Label / data | JetBrains Mono 500 | 8.5–11px, +6%, caps or as-set |
| Footer | JetBrains Mono 400 | 9px, +4%, muted ink |

Fallback stack: `Inter → Helvetica Neue → Arial → sans-serif`.
Bold is surgical — one idea per block gets weight. Never Title Case a headline,
never underline for emphasis, never bold three phrases in one line.

Details and worked examples: `references/typography.md`.

---

## The six graphic devices

Every DevCommX surface is built from these six and nothing else:

1. **Ghost numeral** — oversized, faint section number, top-right.
2. **Eyebrow kicker** — ALL CAPS wide-tracked label, top-left, electric blue.
3. **Diagonal hatch** — the 45° texture from the logo D. An accent only, never a
   full background. Fades in from one corner.
4. **Hairline & footer** — a 0.5px rule structures the page and caps the footer.
5. **Semantic colour** — blue = answer, red = myth/old rule, green = win/proof.
6. **Card system** — plain, tint, or blue-accent cards. 8–12px radius, hairline
   border, no shadow.

Layout: 12-column grid, 6px gutters, 15mm margins (A4). Spacing on a 4/8pt base
(4·8·12·16·24·32·48·64). Anchor content low; leave the top band as air. Aim for a
60–80% fill — whitespace is a device.

Icons: one monoline set, 24×24 grid, 1.5px stroke, round joins, 2px corner radius.
No fills, no duotone, no mixed weights.

Details: `references/layout-and-devices.md`.

---

## Voice — how we sound

Written for the most senior person in the room. Calm, credible, specific.
Founder to founder, to the person accountable for the number.

1. **Lead with the problem they feel** — name the pipeline pain in the first line.
2. **Say it like the most senior person** — no junior filler, no walls of text.
3. **Make the complex simple** — nine motions, one plan.
4. **Concrete over abstract** — trade adjectives for numbers (14.9k → 97.2k, not "grew a lot").
5. **One decision per page.**
6. **End with the next step, not a slogan.**

**Banned words — never ship:** unlock, leverage, elevate, seamless, supercharge,
game-changer, cutting-edge, holistic, synergy, delve, robust, revolutionary, "in
today's landscape". Also strip "AI-powered" filler — name the product (agentic AI
SDR, AI SEO) or say "agentic". Watch em-dash overuse, rule-of-three padding, and
the "it's not X, it's Y" reflex.

Test: *if a line could have been written about any vendor, rewrite it until it
could only be ours.*

Brand promise, the three pillars, the fixed names of the nine motions, and the
conversion flow: `references/voice-and-messaging.md`. **Motion names are fixed —
copy them exactly.**

---

## Logo rules

- One wordmark, three variants: **colour on light** (white/mist only), **white on
  dark** (ink, blue, red, green, photo), **black one-colour** (single-ink print).
- Clear space = 1X, where X is the cap height of the "D", on all four sides.
- Minimum size for the full lockup: **120px wide / 28mm**. Below that, use the
  standalone D symbol.
- The D symbol is the avatar, favicon, and app icon: white D on Electric Blue or
  Ink, colour D on white. Never squeeze the full lockup into a circle.
- Six misuses, all forbidden: recolouring the wordmark, stretching, sitting on busy
  colour or texture, shadows/outlines, rotation/tilt, hand-rebuilding the D.

Files: `~/devcommx-brand-assets/logos/dcx-logo-{color,white,black}.png`,
`~/devcommx-brand-assets/derived/dcx-symbol-{transparent,white}.png`.
Details: `references/logo.md`.

---

## Per-format rules

Load `references/applications.md` when producing any of these — it carries the
exact specs:

| Format | Key rule |
|---|---|
| LinkedIn carousel | 8 slides: ink cover (no number), 6 interiors (one number each), red close with the free GTM Audit CTA |
| Single-image post | 1080×1080, ink, one line front and centre, legible at 1/3 size |
| Company banner | 1128×191, ink or blue, white logo left-aligned, one line |
| Avatar / favicon | D symbol only — white on blue or ink, colour on white |
| Business card | 3.5×2in, 3mm radius, 400gsm uncoated, ink front / white back, one tagline, no QR |
| Email & letterhead | Blue rule + mark, one link: the free GTM Strategy |
| Deck | 3 slide types, eyebrow top-left, mark bottom-left, page number bottom-right, one hero colour per slide |
| Web page | Light is default; dark for campaign/account pages. Never two competing CTAs |
| Ads | One hero colour, one buyer, real numbers, one capture path |
| Charts / data | Flat fills, one accent + neutral, mono numbers, round figures, label illustrative |
| Video | Extension of the system — see `references/applications.md` |

---

## Ready-to-use assets in this skill

- `assets/dcx-tokens.css` — every token as a CSS custom property, plus the base
  classes for eyebrow, ghost numeral, hatch, cards, buttons, and stat tiles.
- `assets/dcx-page-template.html` — a working A4/slide scaffold with the six
  devices wired up. Start here for any HTML → PDF deliverable.

For an HTML deliverable, link or inline `dcx-tokens.css` and use the variables —
never hardcode a hex that isn't in the table above.

---

## Before you publish — run this checklist

- [ ] One hero background colour per surface
- [ ] Electric Blue marks the one key idea (and nothing else)
- [ ] Red / green used for meaning, not decoration
- [ ] Headline sentence case; eyebrow ALL CAPS
- [ ] Body copy is ink or white — never blue
- [ ] Flat fills, no gradients, no shadows, 0.5px hairlines
- [ ] Inter for type, JetBrains Mono for every number and label
- [ ] A real number in every claim; anything illustrative is labelled
- [ ] No banned words / AI-tells
- [ ] Ends with one usable action
- [ ] Correct logo variant for the background, 1X clear space, above minimum size
- [ ] File named `dcx-[asset]-[variant].[ext]` — lowercase, hyphenated, variant last

If a deliverable fails a box, fix it before handing it over — don't ship and note it.
