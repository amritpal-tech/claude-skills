# Schema date fix — runbook and current state

**Status: 1 of 67 items fixed and live. 66 remaining.**

## What was wrong

Audit of all 221 items in the Blog collection (`689c92652a4b35f0e9a14fc2`) on 2026-09-03:

| Defect | Items |
|---|---|
| Schema `datePublished` disagrees with the CMS `date` field | **67** |
| Hardcoded to `2026-07-01` by the original draft spec | 70 |
| `last-updated` field stuck at `2026-07-01` | 64 |
| Schema present in **two** locations that disagree | 20 |
| No JSON-LD embed in `post-body` at all | 36 |
| `schema-markup` does not parse (invalid structured data) | 12 |
| Legacy FAQ-only schema, no `BlogPosting` node | 73 |
| CMS `date` field empty, no source of truth | 7 |

The last three are **out of scope for this pass** by your decision (dates only), and are
recorded in `.claude/skills/devcommx-blog-ops/references/schema-dates.md`.

## The correction rule

- `datePublished` = the item's CMS `date` field (the real publish date)
- `dateModified` = the item's real last modification, `max(lastPublished, lastUpdated)`;
  where that equals the publish date (17 posts never edited since publishing) today is
  used, so the two dates differ and both stay truthful
- `last-updated` field = set equal to `dateModified`, so the on-page "Last updated"
  cannot contradict the schema
- Both schema locations get the same corrected values

## Done

`ai-agents-revops-revenue-operations-automation` (the item in the screenshot):
`2026-07-01` → `datePublished 2026-08-21`, `dateModified 2026-09-03`, in **both** the
`schema-markup` field and the `post-body` embed. Patched and published.

## Finishing the remaining 66

```bash
export WEBFLOW_TOKEN=...      # Webflow > Site settings > Apps & integrations > API access
                              # needs CMS read + write

python3 .claude/skills/devcommx-blog-ops/scripts/apply_schema_date_fix.py --dry-run
python3 .claude/skills/devcommx-blog-ops/scripts/apply_schema_date_fix.py --apply
```

The script is **idempotent** — it recomputes from live state and skips anything already
correct, so the item already fixed is left alone and a re-run is safe. It backs up all
221 items to a dated JSON file before writing, writes sequentially (the CMS is not
concurrency safe), reads each item back to prove the bytes landed, and publishes only
the items that verified.

Run `--dry-run` first: it prints every item with its old date, its new dates, and what
happens to its body embed, and writes nothing.

Use `--limit 5` for a cautious first batch, and `--no-publish` to stage without going live.

## Why this is not being done through the chat connector

The Webflow MCP connector requires every field value to be retyped as a literal tool
argument. `post-body` averages 27KB per blog, so the 67 items are ~1.8MB of live blog
HTML to hand-copy, and each round trip echoes the whole item back. The one item above
cost roughly 50,000 tokens end to end; the remaining 66 would be several million and
well over a hundred round trips, with a real chance of silently corrupting a published
page on any single mistyped character.

`api.webflow.com` is blocked by this session's network egress proxy, so the script
cannot be run from here either. It has to run somewhere with plain internet access:
a laptop, or any environment whose network policy allows the domain.
