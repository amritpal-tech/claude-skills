# Typography — full reference

Brand Book v3.1, Section 03. One display face, one mono face.

- **Inter (variable)** carries every headline and body line.
- **JetBrains Mono** carries every label, number, and score.

Weights in use: 400 / 500 / 600 / 800.
Fallback stack: `Inter → Helvetica Neue → Arial → sans-serif`.

## The scale

| Role | Font / weight | Size | Tracking | Case | Used for |
|---|---|---|---|---|---|
| Display | Inter 800 | 46–70px | −2.5% | Sentence | Page and hero headlines |
| Section | Inter 800 | 24px | −2.0% | Sentence | Section titles, H2 |
| Eyebrow | Inter 600 | 10px | +14% | ALL CAPS | Kickers, section tags |
| Body | Inter 400–500 | 11–13px | 0% | Sentence | Running copy, leads |
| Label / data | JetBrains Mono 500 | 8.5–11px | +6% | Caps or as-set | Meta, code, figures |
| Footer | JetBrains Mono 400 | 9px | +4% | As-set | Footers, fine print |

Scale proportionally for screen and slide formats — the *relationships* (weight,
tracking, case, the mono/sans split) are what must hold, not the absolute px.

## The four typographic rules

1. **Headlines in sentence case.** Capitalise the first word only. Never Title Case
   a headline.
2. **Eyebrows in all caps, tracked wide.** +14% letter-spacing, weight 600,
   electric blue.
3. **Highlight with colour, not underline.** Electric blue marks the key idea;
   underline is reserved for links.
4. **Bold is surgical.** One idea per block gets weight. Bold everything and
   nothing reads.

## Do / don't

**Do**
- Sentence case headlines
- Blue to mark one key phrase
- Mono for every number and label

**Don't**
- Title Case Every Word
- Underline text for emphasis
- Bold three phrases in one line

## Numerals

JetBrains Mono, **tabular figures**, so columns of numbers align. Every figure in
a stat tile, chart axis, scorecard, or inline proof point is mono.

Colour a figure only when it carries meaning: blue for the key number, green/mint
for the win, red for the risk or the zero that hurts.

## Link style

Electric blue with a hairline underline. Underline belongs to links and nothing else.

## Worked example — hierarchy in a real block

```
PROOF OVER POLISH                          ← eyebrow, Inter 600, ALL CAPS, +14%, blue

We scored our own site 18 out of 100       ← display, Inter 800, sentence case, −2.5%

We ran DevCommX through the same free GTM Strategy audit we hand to
prospects, before we hand anyone else's. The verdict was blunt, and we
published it instead of hiding it. Proof over polish, for the people who
sign off.                                  ← body, Inter 400–500, ink on light

  Most growth problems are signal          ← pull quote, Inter 700, blue left rule
  problems, not volume problems.
  PULL QUOTE · INTER 700                   ← mono label under the quote

Then we fixed the signal. Blog impressions moved from 14.9k to 97.2k
month over month.                          ← mono numerals inline, blue for the key figure
```

Specimen setting for a headline that turns: line one in ink, line two in electric
blue — the colour shift *is* the emphasis. Never underline it.
