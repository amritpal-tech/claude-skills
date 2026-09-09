# Gotchas — failures that already shipped

Every item here cost real rework. Read this before any batch.

## 1. The Webflow CMS concurrency bug

`data_cms_tool` is **not concurrency-safe**. Parallel create calls:

- **double-create items** (the second copy gets a random `-xxxxx` slug suffix because
  the clean slug is already taken), and
- **cross-wire responses** (an agent's create returns an unrelated item's slug and id).

In one batch of 13 parallel creates, the first 7 all duplicated. This is distinct from
the known slug-filter bug where list/filter returns the wrong item.

**Apply:** create and update CMS items **sequentially** — one call at a time, or one
call carrying all items in a `fieldData` array. Never fan out the write step. Drafting
can still be parallel because agents only write JSON to disk. After any batch write,
**re-enumerate the collection** and match by slug prefix to detect suffixed duplicates,
then dedupe. Deleting is permanent, so get explicit approval before deleting.

**Connection drop mid-create:** do NOT blindly retry. Enumerate first to see whether it
landed.

## 2. Internal-link liveness

Internal links must point to slugs that are **published and return 200**, not merely
slugs that exist in the CMS. `_existing_slugs.txt` is built from a CMS item list, and
that list **includes unpublished drafts**. Linking to those produces live 404s.

This shipped: 3 dead targets (`b2b-buying-signals-guide-signal-based-prospecting`,
`email-deliverability-rules-2026-spf-dkim-dmarc-compliance`,
`hybrid-ai-sdr-model-account-split`) created 11 broken links across 9 posts, 5 of them
already public.

**Apply:** curl every candidate internal target before drafting, keep only the 200s as
the approved menu, and re-audit every `href` after drafting.
`scripts/check_links.sh` does the curl pass.

## 3. `/contact` is a 404

The contact CTA is **`https://www.devcommx.com/contact-us`**. `/contact` is a hard 404;
`/book` 301s to `/contact-us`. An earlier version of the draft spec said `/contact`, so
31 created blogs shipped with a broken CTA and needed a URL-only find and replace plus a
re-push and republish of the live ones.

## 4. External 403s are usually anti-bot, not broken links

Gartner, Apollo KB, SEC.gov, DOL.gov and Perplexity all return 403 to curl and load fine
in a browser. **Verify in a real browser before "fixing" a link that is not broken.**

## 5. The anchor-quote bug

Drafting agents sometimes emit `href=\"...\"` with a literal backslash, which breaks the
HTML. Assert no `\"` appears in `post-body` before creating. `check_draft.py` tests this.

## 6. Em and en dashes in the References list

The prose usually comes out clean and then a dash appears in "Source — what it supports."
Scan the **whole fieldData**, not just the body prose.

## 7. Webflow embed size limit

A `data-rt-embed-type` block caps around **10,000 characters**. Keep inline SVG figures
under ~9KB. Inline SVG **does** render inside a Webflow HTML embed, same mechanism as the
tables, so no asset upload is needed for diagrams.

## 8. Shell-quoting traps in validation

Validate with a **quoted heredoc** (`<<'PY'`) or a script file. Never an unquoted heredoc
or an inline `python3 -c` containing `\"` — the shell mangles it and produces false
positives and false negatives. This is why the checks live in `scripts/`.

## 9. Subagent runtime cap, and the session limit underneath it

A 31-agent workflow (~2M subagent tokens) tripped an org "Claude subscription access
disabled" cap mid-run.

**Agent count is not the real limit, total session tokens is.** A later batch of only
**12** agents, each doing WebSearch research plus a 2,500-word draft, hit a per-session
rate limit (HTTP 429, "You've hit your session limit") and **all 12 died at once, before
any of them wrote a file.** Twelve was inside the documented 13-agent cap and still blew
the budget, because long-form drafting agents are individually expensive.

**How to apply:** run long-form drafting in **waves of about 4**, not one big fan-out.
Cap each agent's research explicitly (for example, "at most 6 WebSearch calls"). Waves
also fail softer: a rate limit costs you one wave instead of the whole batch.

**Write the file before anything else can go wrong.** Every one of the 12 died mid-research
with nothing on disk. An agent that drafts first and polishes second leaves salvageable
work; one that researches exhaustively then writes leaves nothing.

## 10. Agents mislabel their own verdicts

Validation subagents write plausible findings and then attach the wrong verdict. **Always
recompute the weighted score in the main thread** from the raw criteria scores.
`scripts/score_findings.py` does this.

Related: subagents cannot run openpyxl reliably. Build the workbook in the main thread.

## 11. Do not trust drafting self-reports

Agents report "2,600 words, JSON parses" for files that are 1,900 words or fail a hard
rule. Re-validate every draft independently in the main thread.


## 12. Pushing a batch through the MCP connector does not scale

The connector needs every field value retyped as a literal tool argument. One blog is
about 30KB of HTML, and printing it to copy now exceeds the tool-output limit and gets
truncated to a file, so a single create costs several round trips.

Measured: one create through the connector was roughly 25,000 tokens end to end, counting
the print, the emission and the echoed response. Seven blogs is most of a session, and
every hand-copied character is a chance to silently corrupt a post.

**How to apply:** the connector is right for one or two items, or for reading. For a whole
batch use `scripts/push_drafts.py` with a Webflow site token. It is idempotent, so a
re-run after a partial push resumes rather than duplicating. Note that
`api.webflow.com` is blocked by the egress proxy in Claude Code web sessions, so the
script has to run somewhere with plain internet access.
