# Post formats, pillars, hooks and asks

House rules come from the 360Brew Playbook (Notion, approved by Amritpal), the content
engine registry, and `dcx-humanizer`. `scripts/check_post.py` enforces the mechanical ones.

## The hard rules (a breach is an automatic fail)

1. **No em dashes or en dashes.** Anywhere: post, slides, first comment.
2. **No "not X, it's Y" / "not just X, but Y".** Say the plain thing in one clause.
3. **No AI/corporate verbs**: leverage, unlock, elevate, delve, empower, supercharge,
   seamless, robust, game-changer, tapestry, testament, underscore, foster, harness.
4. **Hook = first line, under ~10 words**, a number, a paradox, or the change itself. It
   must be cashable by real facts in the body.
5. **Blank line between lines.** One idea per line. No paragraph over ~3 lines.
6. **Links go in the first comment**, never the body (body links cost 40-60% reach).
7. **Zero hashtags** on standard posts. Reference Maps are the one exception.
8. **Exactly one explicit ask** at the end (see Asks). Never "thoughts?", never "like if".
9. **No emoji-led lines.** No engagement bait.
10. **1,200-1,900 characters** for the body (2.9x reach vs short posts).
11. **Sentence case for all three.** A capital at the start of every line and every
    sentence, proper nouns capitalised. Amritpal and Sumit switched from lowercase on
    2026-11-04 (Amritpal's call); Pankaj already wrote this way.

## Format menu

Aim for **~70% visual across each profile's week** (carousel, single image, document).
Visual specs follow the **`devcommx-brand`** skill (Brand Book v3.1: Ink #0C0F1A, Electric
Blue #2F5BFF, Mist #EEF1F8, Signal Red #FF3B1F, Signal Green; Inter + JetBrains Mono; flat
fills; sentence-case headlines; eyebrow kicker in caps). The old #000814 / #4d9fff palette
in early drafts is retired. Load `devcommx-brand` before writing any creative spec.

### A · News-to-playbook (the daily default) · `format:text` or `carousel`

The newsjack that teaches. Built so the reader can act this week.

```
hook: the change, or its sharpest number, in under 10 words

what changed (2-4 lines, facts only, attributed: "google says", "per the changelog")

why it matters to <this reader> (2-3 lines, the mechanism)

what i'd do this week:
1. ...
2. ...
3. ...
(3-5 steps, each concrete: a field, a query, a page, a test)

the honest limit / what we don't know yet (1-2 lines)

one-line verdict

the ask
```

### B · Listicle / stack curation · `format:listicle` or `carousel`

The reach unlock (vendors amplify, readers save).

```
hook with an odd number + the job ("7 AI tools that ___. one limit each.")

one line on how the list was chosen

1. Tool. what job it owns. ↳ the honest limit.
2. ...
(5-7 items; each item three short beats)

the pattern across the list (one line)

save-this ask
```

Every tool named must be real and verified to exist today. No affiliate tone. The limit
is mandatory on every item.

### C · Realist take / contrarian with evidence · `format:text` or `single-image`

```
hook: the claim everyone is repeating, or the uncomfortable number
the evidence (the source, the numbers)
what is theater vs what is real (two short lists, or two lines)
the rule you'd apply
one honest disqualifier ("if you ___, ignore this")
sharp question
```

### D · Carousel spec · `format:carousel`

The brand book's fixed frame (`devcommx-brand` → references/applications.md): 8 slides,
1080x1350, screenshot-worthy reference material, not a narrated story.

- **01 · Cover, Ink `#0C0F1A`:** white logo top-left, mono kicker, the hook as a
  sentence-case headline, one sub-line. No slide number; footer `NAME · LANE · 01 / 08`.
- **02-07 · Interior, Surface `#181B25`:** eyebrow top-left, **one number per tile**
  (large, JetBrains Mono / Inter 800), ghost slide number top-right, swipe cue lower-left,
  one or two lines of copy. Nothing competes with the number.
- **08 · Close, Signal Red `#FF3B1F`:** white logo, the post's closing rule, and the one
  brand offer (the free GTM Audit) as a ghost CTA pill. The caption still carries the
  post's single ask.
Slide copy is sentence case too. Write every slide's copy in full
in the brief. The designer should not have to invent text.

### E · Single image (stat or quote card) · `format:single-image`

One line front and centre, legible at a third of the size. Eyebrow kicker, headline,
one support line, footer. Use when the story is one number or one rule.

### F · Reference Map · `format:reference-map` (weekly anchor, not daily)

A single-image table: six rows, three columns (the thing / what it answers / the tool or
source). Carries vendor tags and up to 10 hashtags. Requires 24h commenter triage
(ICP / peer / vendor) by the owner. The daily desk only drafts one when the brief says
the week's map slot is open.

## Pillars and how they map to formats

| Profile | Pillar | Default format | Default ask |
|---|---|---|---|
| Amritpal | AI search & LLM visibility updates | A (carousel when there are 5+ steps) | save-this |
| Amritpal | Google & SEO updates | A (text) | sharp-question |
| Amritpal | AI tools for marketers | B (carousel) | save-this |
| Amritpal | Marketing platform shifts | A or C | sharp-question |
| Sumit | Release-week takes | A or C (text) | sharp-question |
| Sumit | The realist take | C (text or single image) | repost-if |
| Sumit | GTM market moves & buyer research | C (single image stat card) | sharp-question |
| Sumit | AI tools for GTM leaders | B (carousel) | save-this |
| Pankaj | Changelog reads | A (text, steps as trigger → path → write) | sharp-question |
| Pankaj | Stack curation | B (carousel) | save-this |
| Pankaj | Data truth & RevOps mechanics | C or A (single image checklist) | save-this |
| Pankaj | Agentic GTM builds | A (text) | repost-if |

## Hooks

Mechanics that work for this fleet: **curiosity gap**, **contrarian with evidence**,
**the specific number**, **the change stated flat**. Odd numbers and stakes beat round ones.

Formulas, filled from the lane:
- the change, flat: "Google just split AI Mode out of Search Console."
- the number: "61% of buyers ask a model before they ask you."
- the paradox: "More AI agents. Fewer replies."
- the myth: "\"Qualified\" is the biggest lie your reps tell your forecast."
- the stakes: "Your CRM history is not history."
- the receipt (only with a cleared number): "we scored our own site 18/100."

Banned: soft wind-ups ("In today's world", "Big news!", "I'm excited to share"), emoji-led
lines, questions as hooks unless they are sharp, "it's not X, it's Y".

Write **three hook options** in the brief, pick one, and say why in one line.

### Using the Scripe hook bank

The hook bank is engagement evidence from other creators in the same niches. It tells us
which *shapes* of first line are stopping the scroll this fortnight. It is never a source
of words, facts or numbers.

1. **Read by niche.** In the sheet: `SEO / AEO` informs Amritpal, `GTM` informs Sumit,
   `RevOps` informs Pankaj (GTM hooks about Clay, Claude Code or the stack inform Pankaj
   too). Fresh hooks (posted within 14 days of the pull) are this fortnight's trend; the
   rest are proven patterns.
2. **Pick the pattern, not the hook.** Start from the niche's pattern scoreboard. Comments
   outrank reactions, so weigh the comment ratio: a pattern that starts arguments beats one
   that collects likes. Name it as the sheet does (Shift statement, Myth-bust, Expectation
   vs reality, Number + gap, Contrarian truth, Then vs now, Dialogue, 90/10 split...).
3. **Rebuild it from today's story** in the profile's voice. The shape travels; the words,
   claims and numbers come only from our research and cleared DevCommX facts.
4. **Filter what the house bans** even when it trends (see the table below).
5. **Log it** in the brief's Strategy block: "pattern: <name> (sheet #<n>, <engagement>
   eng., <fresh or proven>)". This builds a record of which patterns win for us.

**House filters for the sheet's patterns:**

| Pattern in the sheet | How we may use it |
|---|---|
| Expectation vs reality, Then vs now, Number + gap, Contrarian truth, Bold one-liner, Common mistake, Reframe, Gap statement, Comparison | Free to use. Fill with our facts. |
| Myth-bust "[A], [B] and [C] are NOT the same thing" | Fine, in sentence case: no ALL CAPS "NOT" in a post (carousel slides only). |
| Shift statement "[X] is no longer just [old]. The focus will be on [new]" | Too close to the banned "not just X, but Y". State the change flat: "AI answers now decide which brands get named." |
| 90/10 split, Shock stat, Data study, Data claim | Only with a number from today's sourced research. Never "90% of brands" without a source; write "most brands" instead. |
| Experience / Authority (years in the job, big-name clients, "my biggest win"), Proof + framework, Counter-intuitive result, Before / after with AI, Insider room, Story + proof | Need a real first-person fact recorded in the brief or a cleared DevCommX number (18/100, ~$380K). Otherwise a `[NEEDS:]` flag, never an invented year, client, dinner or result. |
| Dialogue (CEO / Me) | Only as a labelled composite ("The question I hear most from CEOs:"), or a real conversation the brief records. Never a quoted exchange presented as real. |
| Lead magnet (comment-to-get), Steal this SOP, Resource / roadmap | Only as `comment-gate` with a finished, existing asset (the AI visibility checker counts: "comment your domain"), 1-2 per profile per week, DM owner named. No "Free access 👇". |
| Breaking news "🚨" | Keep the urgency, drop the emoji: no emoji-led lines. |

The gate enforces step 3: `check_post.py --bank` fails any post that shares a six-word run
with any hook or formula in the bank (sheet `.txt` files plus the Doc's batches).

## Asks (exactly one per post)

| Ask | Use on | Close with |
|---|---|---|
| `save-this` | reference posts, listicles, carousels, checklists | "save this before your next ___." |
| `repost-if` | frameworks and realist takes | "repost if your team ___." |
| `sharp-question` | news reads, receipts, stories | one specific question the reader can answer from their own work. Never "thoughts?" |
| `comment-gate` | only with a **finished, existing** asset (template, skill, checker run). Capped 1-2 per profile per week. Prefer rich gates ("comment your domain") | "comment ___ and i'll DM it within 24h." Needs the DM fulfilment owner named in the brief. |

The daily desk does **not** invent gated assets. It proposes a gate only when the brief
names an asset that already exists (e.g. a run of the AI visibility checker on the
commenter's domain).

## First comment

Every post has one. It holds, in this order:
1. the source line(s) with URL for any news post ("source: Google Search Central, Nov 3: <url>")
2. an extra detail that did not fit (a setup note, the seventh row)
3. at most one line pointing to https://ai.devcommx.com/ when the post is about AI
   visibility, described as the free checker that runs on Claude with live web search.

## First-hour protocol (put it in the brief, the humans run it)

Publish at the slot → Slack ping → author online 60 minutes replying to every comment →
3 teammates comment substantively, staggered across minutes 15-60.
