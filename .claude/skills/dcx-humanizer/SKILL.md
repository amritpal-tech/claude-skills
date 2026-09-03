---
name: dcx-humanizer
version: 1.0.0
description: |
  Rewrite any DevCommX draft (LinkedIn post, carousel, DM, bio, email) so it reads
  like a real operator wrote it: strips AI-tells AND enforces the DevCommX house
  style + honesty gate in one pass. Use when a draft "sounds like AI" or "sounds like
  a brand", before it goes to the dcx-content-auditor, or to clean anything a
  generative tool produced. Triggers: "humanize this", "make this sound human / less
  AI", "clean this up to house style", "de-slop", "this reads like ChatGPT".
  Layers on top of the generic `humanizer` skill (Wikipedia Signs-of-AI catalog).
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# DevCommX Humanizer

Turn AI-sounding or brand-sounding DevCommX drafts into copy a real operator would post. This is the **rewrite** counterpart to `dcx-content-auditor` (which only detects). It does two jobs at once: remove AI-tells, and force the draft into DevCommX house style without flattening the profile's voice.

## Source of truth (read first when available)

1. `/Users/amrit/.claude/devcommx-content-os/CONTEXT.md` — house rules, honesty rules, AI-tells.
2. `/Users/amrit/devcommx-content-engine/engine/voice-profiles.md` — the locked per-profile voices (Pankaj = contrarian provocateur, Shrey = build-in-public field-log, Yuvraj = front-line reporter, Sumit = lowercase stat-verdict, Ananthan = witnessed-moment, etc.). Draft-from-bible is authoritative.
3. The generic `humanizer` skill — the exhaustive Wikipedia "Signs of AI writing" pattern catalog. This skill assumes those 29 patterns and adds the DevCommX layer below. If you have not internalized them, read that skill too.

If a profile is named, humanize INTO that profile's voice. If not, ask which profile, or default to the DevCommX operator register (specific, first-person, no marketer gloss).

## The DevCommX hard rules (non-negotiable — an AI-tell here is an automatic fail)

1. **No em dashes or en dashes. Ever.** Rewrite with a period, comma, or parentheses. This is the single most common tell in our drafts.
2. **No "not X, it's Y" / "not just X, but Y" symmetrical negation.** This is banned even when it sounds punchy. Rewrite as one plain clause.
3. **No corporate/AI verbs:** leverage, unlock, elevate, delve, empower, supercharge, seamless, robust, game-changer, tapestry, testament, underscore, foster, harness. Say the plain thing.
4. **Hook = first 1–2 lines, under 10 words**, a number or a paradox. If the hook is a soft wind-up, cut to the sharp line.
5. **High whitespace: one blank line between every line.** No walls of text.
6. **CTA goes in the FIRST COMMENT, never the post body.** If a draft ends in a pitch or a link, move it to `firstComment` with `[TOOL_LINK]`.
7. **Close on a genuine discussion question. Zero hashtags. No engagement bait** ("comment X for the resource" is forbidden).
8. **Lowercase-voice profiles stay lowercase** (e.g. Sumit, Amritpal). Do not "correct" their casing into title-case brand voice.

## The honesty gate (humanizing must never break this)

- **Do not invent, round differently, or upgrade any number.** If a stat is illustrative it must stay illustrative. Preserve every `[NEEDS:]` / `confirm-numbers-before-post` flag exactly.
- **Only two numbers are real/safe** unless told otherwise: the **18/100** own-site score and the **~$380K** found in our own HubSpot. Everything else stays flagged.
- **The tool is Claude-powered with live web search.** Never let a rewrite imply "we tested ChatGPT/Gemini/every engine."
- **No client names or exact client amounts.** Rounded and anonymized only.
- **Vignesh firewall:** Vignesh stays on the GTM-founder track; do not drift his copy to govt.

If humanizing a line would require touching a flagged number, leave the number and flag intact and only fix the prose around it.

## Highest-frequency DevCommX tells (fix these first)

**1. Em/en dash**
- Before: `The buyer already decided, before you ever spoke.`  *(if it were an em dash version)* → keep as a period. `The buyer already decided. Before you ever spoke.`

**2. Symmetrical negation ("not X, it's Y")**
- Before: `It is not the copy. It is the lack of a human gate.`
- After: `The copy is fine. What is missing is a human gate before send.`

**3. Corporate abstraction / copula avoidance**
- Before: `Our platform empowers teams to unlock seamless pipeline velocity.`
- After: `We help teams close faster by pointing outreach at real buying signals.`

**4. Rule of three**
- Before: `We build faster, cleaner, and smarter revenue engines.`
- After: `We build revenue engines that close, not ones that just look busy.`

**5. Marketer gloss instead of operator specificity**
- Before: `Leverage cutting-edge AI to elevate your outbound strategy.`
- After: `We pointed a Claude agent at our own HubSpot and it surfaced ~$380K in closed-lost we had written off.`

**6. Announcement / signposting**
- Before: `Let's dive into why your pipeline isn't closing. Here's what you need to know.`
- After: `Your pipeline looks busy and refuses to close. Here is the part everyone skips.`

**7. Generic upbeat close instead of a real question**
- Before: `The future of GTM is bright. Exciting times ahead.`
- After: `What is the last GTM role you saw quietly disappear?`

## Preserve the soul (do not sand it into clean-but-dead)

Clean is not the goal; *human operator* is. Keep:
- First person and a real moment ("a prospect told me last week...").
- One honest disqualifier or a named loss where the voice calls for it (Sumit, Spencer, Vignesh).
- Varied rhythm: short punchy lines next to one longer one.
- The profile's verbal tics from the voice bible.

A draft that passes every rule above but has no pulse still fails. Add the operator back in.

## Process

1. Identify the profile (ask if unknown) and read its voice from the bible.
2. First pass: strip the 8 hard-rule tells + the universal Signs-of-AI patterns.
3. Second pass: voice-match to the profile (casing, cadence, vocabulary, the honest-disqualifier move).
4. Honesty pass: confirm no number changed, every flag intact, tool described as Claude-powered, no client data, Vignesh firewall held.
5. Final anti-AI pass: ask "what still makes this read as AI or as a brand?" list the remaining tells briefly, then revise once more.

## Output format

1. **Humanized draft** — the rewritten copy, in house format (blank line between every line; CTA pulled out).
2. **First comment** — the CTA with `[TOOL_LINK]` (if the original had an in-body CTA).
3. **What still read as AI/brand** — brief bullets from the final pass.
4. **Flags preserved** — list any `[NEEDS:]` / illustrative numbers left untouched, so the auditor and reps know they still need confirming.
5. **Handoff note** — "ready for dcx-content-auditor" or "needs a real number before it can pass honesty."

Never emit a version that silently resolves a `[NEEDS:]` flag or invents a metric. Humanizing changes the prose, not the facts.
