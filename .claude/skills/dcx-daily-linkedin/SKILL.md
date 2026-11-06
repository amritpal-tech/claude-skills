---
name: dcx-daily-linkedin
version: 1.0.0
description: |
  The DevCommX daily LinkedIn desk. Every morning: research the last 48 hours of real,
  verifiable updates in each profile's lane, pick one educational story per profile,
  and produce a complete post package for three profiles in their locked voices:
  Amrit Pal Singh (marketing, SEO, AEO, AI search, AI tools for marketers), Sumit
  Nautiyal (GTM leader: agentic GTM, AI for GTM, market moves) and Pankaj Kumar (GTM
  engineer: RevOps, Clay/n8n/HubSpot changelogs, the stack). Each package carries the
  research brief with sources, pillar, archetype, format (text, listicle, carousel,
  single image), three hook options, the final copy, full creative spec, first comment,
  ask, posting slot and a hard-rules gate. Use for "today's LinkedIn posts", "daily
  post desk", "research a post for Sumit/Pankaj/Amritpal", "newsjack this for
  LinkedIn", or when a scheduled run invokes it.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebSearch
  - WebFetch
  - Skill
---

# DevCommX daily LinkedIn desk

One run produces one dated brief with three ready-to-review posts. Nothing publishes
itself: a human approves every post (the content engine's law: "human gate is absolute").

| Read | When |
|---|---|
| [references/profiles.md](references/profiles.md) | **Always**, before choosing stories. Lanes, voices, pillars, cleared numbers. |
| [references/research-playbook.md](references/research-playbook.md) | Before searching. Source maps, verification, scoring, the freshness ladder. |
| [references/post-formats.md](references/post-formats.md) | Before drafting. Hard rules, format skeletons, hooks, asks. |
| [references/output-template.md](references/output-template.md) | When writing the brief. |
| `devcommx-brand` skill | Before writing any carousel or image spec. |
| `dcx-humanizer` skill | On any draft that still reads like AI after the gate. |

## The run

### 1. Context
```bash
python3 .claude/skills/dcx-daily-linkedin/scripts/daily_context.py
```
It gives the IST date, each profile's slot (DST-aware), who is on slot today, and the
research window. Produce a post for **all three** profiles every run. A profile that is
off slot today gets its post marked for its next slot, so the bank never runs dry.

### 2. Memory
Read the last 10 daily briefs. They live in the Google Drive folder
**LinkedIn Daily Desk (DevCommX)** (`1WRfTiJfxCMJmQ339waVco2DEqva91j3q`): list it with
`search_files` (`parentId = '1WRfTiJfxCMJmQ339waVco2DEqva91j3q'`), read the newest ten with
`read_file_content`. Fall back to `devcommx/linkedin-daily/*.md` if Drive is unavailable.
List per profile: stories used, formats, asks. You will need it for novelty scoring and
format rotation.

### 3. Research (per lane)
Follow `research-playbook.md`. Two lanes: **marketing/SEO/AEO** (Amritpal) and **GTM**
(Sumit and Pankaj share it, then split). Run the lane's source checks and query bank
with WebSearch, open every candidate with WebFetch, confirm its date on the page, and
find the primary source. Collect 4-8 candidates per lane, score them, record them in the
brief's research scan table, including the ones you held and why.

Run the three lanes' searches in parallel where the tools allow. Do not stop at the first
plausible headline: the best story is the one that teaches the reader something they can
act on this week.

### 4. Pick
One story per profile, scoring 10+ on the rubric. Sumit and Pankaj get different stories
when possible; if one release is too big to skip, Sumit takes the decision and Pankaj the
wiring (`profiles.md`, "Keeping Sumit and Pankaj apart"). Choose pillar, format and ask
from the mapping table in `post-formats.md`, then check the last 10 days so the profile's
week trends toward ~70% visual and no ask runs three days in a row.

### 5. Draft
First read the **hook bank**: the Google Doc "Hook bank · Scripe trending (paste weekly)"
(`1uL_4WUNV8JLd6x1MRriknLWZzKewn3JM1Rt1v5lx-4Y`, same Drive folder). The team pastes trending
LinkedIn hooks from Scripe there each week. Use only batches from the last 14 days, split
by niche, and follow "Using the Scripe hook bank" in `post-formats.md`. Save the doc's text to
`$SCRATCH/hook-bank.txt` for the gate. If the bank is empty or stale, say so in the brief
and draft from the house hook formulas.

For each profile, in its voice from `profiles.md`, using the format skeleton:
- three hook options, at least one adapted from a trending mechanic in the bank when one
  fits; pick one, say why, and name the mechanic it borrows
- the body, 1,200-1,900 characters, blank line between lines
- facts attributed to the source; the honesty gate in `profiles.md` held
- creative spec in full for visual formats, per `devcommx-brand`
- first comment with the source URL first
- before-publish list: every `[NEEDS:]`, every "verify" (handles, tool claims)

### 6. Gate
Write the brief to `devcommx/linkedin-daily/YYYY-MM-DD.md` using the template, then:
```bash
python3 .claude/skills/dcx-daily-linkedin/scripts/check_post.py devcommx/linkedin-daily/YYYY-MM-DD.md --bank "$SCRATCH/hook-bank.txt"
```
(drop `--bank` only when the hook bank was empty). Fix every ERROR and re-run until it passes. Read every WARN and fix it unless the brief
says why it stays. Then do one human-eye pass per post: "what still reads like AI or like a
brand?" Fix it. If anything stubborn remains, run the `dcx-humanizer` skill on that post.
Paste the final gate lines into each profile's Gate block and the summary table.

### 7. Deliver
**Configured target: one Google Doc per day** (chosen by Amritpal, 2026-11-04).
```bash
python3 .claude/skills/dcx-daily-linkedin/scripts/to_doc.py devcommx/linkedin-daily/YYYY-MM-DD.md > "$SCRATCH/YYYY-MM-DD.doc.md"
```
Then Google Drive `create_file` with:
- `title`: `YYYY-MM-DD · {Ddd} · LinkedIn daily desk` (e.g. `2026-11-04 · Wed · LinkedIn daily desk`)
- `parentId`: `1WRfTiJfxCMJmQ339waVco2DEqva91j3q` (folder "LinkedIn Daily Desk (DevCommX)")
- `contentMimeType`: `text/markdown`, `textContent`: the file's full contents

Drive converts it to a Google Doc with working tables and links. Before creating, search
the folder for a doc with today's title; if one exists, do not create a duplicate, add
" (rerun)" to the new title instead. Confirm with `get_file_metadata` that `fileSize` is
well above 1 KB (conversion finished). Never edit or delete other files in Drive.

Other targets, only if a run's instructions say so: a Notion child page under
"DevCommX — LinkedIn HQ" (`37f2cf02-3ebe-818d-8d3f-cb3e408b12eb`), a Gmail draft, or the
repo file committed to a named branch.

End with a short summary: the three stories, slots, gate results, open flags, and the link
to the delivered page.

## Rules that do not bend

- **Nothing invented.** No fake first-person experience, no rounded or upgraded numbers,
  no tool or feature that the source does not show. Unknown → `[NEEDS: ...]`.
- **Only two cleared DevCommX numbers:** our own site's 18/100 AI-visibility score, and the
  ~$380K of written-off HubSpot pipeline a Claude agent resurfaced (Sumit's story).
- **The checker is Claude with live web search.** Never imply it tests ChatGPT or Gemini.
- **No client names, no exact client amounts.**
- **Old news is labelled.** If no fresh story clears the bar, use the ladder and say which
  rung, rather than dressing up a stale item.
- **Headless runs do not ask questions.** Make the call, write the reasoning in the brief,
  flag what a human must confirm.
