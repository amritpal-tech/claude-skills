---
description: Create or update DevCommX blog drafts in Webflow CMS, sequentially.
argument-hint: "[batch name, slug, or glob]"
---
# /devcommx:blog-push

Push to Webflow: **$ARGUMENTS**

Load `devcommx-blog-ops` and read `references/webflow-cms.md` and `references/gotchas.md`.

## Non-negotiable

**`data_cms_tool` is not concurrency-safe.** Parallel creates double-create items and
cross-wire responses. **One call at a time. Never fan out the write step.**

## Steps

1. **Gate** — `scripts/check_draft.py` on everything being pushed. Do not push a file
   with an ERROR.
2. **Enumerate first** — paginate the collection (offsets 0, 100, 200) and confirm none
   of these slugs already exist. A push on top of an existing slug creates a duplicate.
3. **Create sequentially** — `create_collection_items`, `isDraft: true`, one call each.
   After every call, **check the returned slug for a random `-xxxxx` suffix**. A suffix
   means a duplicate was created; stop and resolve it before continuing.
4. **On a dropped connection** — do NOT retry blindly. Enumerate to see whether it landed.
5. **Re-enumerate** — match by slug prefix, confirm clean singletons.

## For updates to existing items

- Send the **complete fieldData**. Partial payloads risk dropping fields.
- **Pin `isDraft` to the item's current value** so publish state never flips by accident.
- A Webflow update only *stages* a change. A live item needs `publish_collection_items`
  before the fix is public.

## Publishing

**Draft-only unless the user explicitly says publish.** If publishing a linked hub set,
publish the whole set together or the inter-hub links 404.

Deleting is permanent, there is no Webflow trash. Get explicit approval, then delete
sequentially.

## Output

Per item: slug, item ID, draft/live state, and whether the returned slug was clean.
