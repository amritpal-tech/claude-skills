# Schema dates and the two schema locations

Audited 2026-09-03 across all 221 items in the Blog collection.

## The two locations (this is real, not a mistake)

Every blog can carry its JSON-LD **twice**:

1. **The `schema-markup` CMS field** (PlainText). Rendered by a hidden `HtmlEmbed`
   in the Blogs Template (`689c92652a4b35f0e9a14fd5`, the element styled `hide`).
   The page-level JSON-LD setting is `null`, so this field is the template's source.
2. **A `<script type="application/ld+json">` block inside `post-body`**, wrapped in a
   `data-rt-embed-type` embed. This is the "You can't see this custom code while
   you're in the Editor" block visible in the CMS editor.

They drift. Counts at audit time: 186 items had both, 35 had only the field, and
**20 held two different versions of the schema**.

Store **bare JSON** in the field (214 of 221 items do). The 6 items that store it
wrapped in `<script>` tags do not parse and are very likely double-wrapped at render.
The body embed always needs its own `<script>` wrapper, so when copying the field
into the body, **unwrap first** or you nest script tags.

## The date defect

All 53 blogs this program produced were authored from a spec that hardcoded
`2026-07-01`, so `datePublished`, `dateModified` and the `last-updated` field were
identical across the whole batch and disagreed with the real publish date in the
CMS `date` field.

At audit: **70 items hardcoded to `2026-07-01`**, **67 whose schema date disagreed
with the CMS `date` field**, **64 with `last-updated` stuck at `2026-07-01`**.

## The correction rule

| Value | Source |
|---|---|
| `datePublished` | the item's CMS `date` field, the real publish date |
| `dateModified` | the item's real last modification: `max(lastPublished, lastUpdated)`. Where that equals the publish date, meaning the post was never edited after publishing, use today, so the two dates differ and both stay truthful. |
| `last-updated` field | set equal to `dateModified`, so the on-page "Last updated" cannot contradict the schema |

Never set `dateModified` to today across the board. A schema repair is not a content
edit, and claiming 67 posts changed today when they did not is a freshness signal
you cannot support.

## Doing the fix

`scripts/fix_schema_dates.py` computes and verifies the payloads; it patches only the
two date **values** and never regenerates the schema, so FAQ text and every other node
stay byte-identical. Its verifier proves: only the three intended fields differ, the
schema differs only in date values, both locations agree afterwards, body prose outside
the embed is untouched, no dash regression, and parse status never worsens.

```bash
python3 scripts/fix_schema_dates.py --items items.json --today YYYY-MM-DD --verify
```

`scripts/apply_schema_date_fix.py` runs the same logic straight against the Webflow
API: fetch, verify, back up, patch sequentially, read back each write, publish.

```bash
export WEBFLOW_TOKEN=...
python3 scripts/apply_schema_date_fix.py --dry-run
python3 scripts/apply_schema_date_fix.py --apply
```

**Why a script rather than the MCP tool:** the MCP connector needs every field value
retyped as a literal tool argument. For this fix that is ~1.8MB of blog HTML, which is
slow and risks silently corrupting a live post on a single mistyped character. The MCP
tool is right for a handful of items; a token-authenticated script is right for a
whole-collection sweep. Note `update_collection_items` **merges** (verified on a draft),
so only changed fields need sending.

## Other schema defects found, not yet fixed

Reported and deliberately left alone in the date pass:

- **12 items whose `schema-markup` does not parse at all** (6 wrapped in stray `<script>`
  tags, the rest malformed). Google sees no structured data on those pages. Bigger loss
  than the wrong dates.
- **73 legacy items with FAQ-only schema**, no `BlogPosting` node, so no author,
  headline or date signals at all.
- **7 items with an empty CMS `date` field**, 5 of which carry a schema date. No source
  of truth to correct against.
- `agentic-gtm-ai-agents-gtm-engineering` has an `@id` of `...-2026#article` that does
  not match its slug.
