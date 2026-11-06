# Daily brief template

One file per day: `devcommx/linkedin-daily/YYYY-MM-DD.md` (IST date). The same content is
what goes to the delivery target (Notion page, Google Doc, or email). Keep the
`<!-- post:... -->` and `<!-- comment:... -->` markers in the repo file: `check_post.py`
reads them. Strip the markers when pasting into Notion or a doc.

Attribute values for the post marker:
- `format:` text | listicle | carousel | single-image | reference-map | document | video
- `ask:` save-this | repost-if | sharp-question | comment-gate
- `type:` news | curation | evergreen | receipts

````markdown
# LinkedIn daily desk · {Weekday} {D Mon YYYY}

Run at {HH:MM} IST · research window: last {48|72}h · DST: US {on|off}, Europe {on|off}

| Profile | Slot | Story | Pillar | Format | Ask | Gate |
|---|---|---|---|---|---|---|
| Amrit Pal Singh | {on slot 14:00 IST / next: Thu 14:00} | {one line} | {pillar} | {format} | {ask} | {PASS / PASS w/ warnings / FAIL} |
| Sumit Nautiyal | ... |
| Pankaj Kumar | ... |

Publish only after a human review. Every [NEEDS:] flag and every "verify" line below must
be cleared first.

---

## Research scan

### Marketing / SEO / AEO lane
| # | Update | Source · date | Score | Used? |
|---|---|---|---|---|
| 1 | ... | [publisher](url) · Nov 3 | 15 | ✅ Amritpal |
| 2 | ... | ... | 11 | held: {why} |

### GTM lane (Sumit + Pankaj)
| ... |

{One line on anything the scan could not verify, or a lane that came up thin.}

---

## Amrit Pal Singh · Marketing / AEO

**Slot:** {Thu 5 Nov · 14:00 IST · lands CET 09:30} · **Pillar:** {pillar} ·
**Archetype:** {newsjack / system-as-content / curation} · **Rung:** {1-6}

### Research brief
- **What happened:** {2-4 facts, verbatim where it matters}
- **Source:** [{publisher, title}]({url}), published {date}. {Primary / secondary, and the primary link if secondary.}
- **Why it matters to his reader:** {2 lines}
- **What the source does not say:** {rollout, pricing, regions; so the post doesn't either}
- **Angle:** {the one take only this profile would write}

### Strategy
- **Format:** {format} because {one line}
- **Hook options:** 1) ... 2) ... 3) ... → **picked {n}**: {why}
- **Ask:** {ask}

### Post
<!-- post:amritpal format:{format} ask:{ask} type:{type} -->
{final post copy, blank line between lines}
<!-- /post -->

### Creative ({format})
{full slide-by-slide or card copy, per devcommx-brand. Omit for text posts or write
"text only; optional hook card: ..."}

### First comment
<!-- comment:amritpal -->
{source line with URL, extra detail, optional checker line}
<!-- /comment -->

### Tags to consider (verify each company page before posting)
{vendor pages named in the post, or "none"}

### Before publish
- {[NEEDS:] flags, verify items, anything inferred}
- First hour: author online 60 min, 3 teammates comment by minute 60.

### Gate
{paste the check_post.py line for this profile}

---

## Sumit Nautiyal · GTM leader
{same blocks, marker post:sumit}

---

## Pankaj Kumar · GTM engineer
{same blocks, marker post:pankaj}

---

## Reviewer checklist
- [ ] Every fact traces to the linked source, dated inside the window
- [ ] No invented first-person experience or DevCommX number
- [ ] Voice matches the profile (casing, cadence, tics)
- [ ] One ask per post, link only in first comment, zero hashtags
- [ ] Creative copy complete for visual posts
````
