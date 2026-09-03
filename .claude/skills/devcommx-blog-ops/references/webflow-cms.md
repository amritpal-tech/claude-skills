# Webflow CMS — the facts

## Identifiers (memorize)

| Thing | Value |
|---|---|
| Blog collection ID | `689c92652a4b35f0e9a14fc2` |
| Category ref | `689c9183e68cf0a3029741d1` |
| Author ref | `677194290c472080e6cd6c06` |
| Authors-collection ref | `69d8f4fd2475affd96f68115` |
| Default OG image fileId | `69ce06f820d4562027a83191` |
| Default OG image URL | `https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png` |
| Live blog URL pattern | `https://www.devcommx.com/blogs/{slug}` |

Collection size was **221 items** at the end of the handoff session. Full enumeration
needs three pages: offsets 0, 100, 200.

## The MCP connector

Tool: **`data_cms_tool`** on the Webflow MCP server. In this repo the server is
exposed as `mcp__Webflow__data_cms_tool` (in the handoff session it was
`mcp__2b3254d1-c8d2-4f01-a504-59abe3eca6a6__data_cms_tool` — the prefix is
account-specific, the tool name is not).

Call `webflow_guide_tool` once per session before the first CMS call.

Actions used in this operation:

| Action | Use |
|---|---|
| `list_collection_items` | enumerate (paginate by offset), dedup, read publish state |
| `get_collection_details` | confirm the field schema has not drifted |
| `create_collection_items` | create new drafts — **sequentially** |
| `update_collection_items` | fix existing items — **sequentially**, full fieldData |
| `publish_collection_items` | make a staged change public. Only on explicit instruction. |

**On a new account the connector must be authorized first** (claude.ai connector
settings). Nothing in this operation works without it.

## The item shape

```json
{
  "collection_id": "689c92652a4b35f0e9a14fc2",
  "isDraft": true,
  "isArchived": false,
  "fieldData": {
    "name": "<H1 / full post title>",
    "slug": "<slug>",
    "meta-title": "<=60 chars, keyword first>",
    "meta-description": "<150-160 chars>",
    "post-summary": "<40-60 words>",
    "post-body": "<HTML string>",
    "schema-markup": "<JSON string: @graph with BlogPosting + FAQPage>",
    "date": "2026-07-01T00:00:00.000Z",
    "last-updated": "2026-07-01T00:00:00.000Z",
    "author-name": "Sumit Nautiyal",
    "author-title": "VP of Revenue Operations & GTM Engineering, DevCommX",
    "add-blog-reading-time": "<round(words/220) as a string>",
    "blog-list": "https://www.devcommx.com/blogs/{slug}",
    "og-image": { "fileId": "...", "url": "..." },
    "author": "677194290c472080e6cd6c06",
    "authors-collection": "69d8f4fd2475affd96f68115",
    "category": ["689c9183e68cf0a3029741d1"]
  }
}
```

A ready-to-fill copy is at `assets/blog-item-template.json`.

## Writing rules

1. **Sequential only.** One create/update call at a time. See gotchas.md.
2. **Full fieldData on updates.** Partial payloads risk dropping fields.
3. **Pin `isDraft` to the item's current value** on an update so publish state never flips
   by accident.
4. **Verify the returned slug** has no random `-xxxxx` suffix. A suffix means the clean
   slug was already taken, which usually means a duplicate was created.
5. **After any batch write, re-enumerate** and match by slug prefix to catch duplicates.
6. **A failed create is not a signal to retry.** Enumerate first to see whether it landed.
7. **Deletion is permanent** (no Webflow trash). Get explicit user approval, then delete
   in one sequential pass.
8. **Draft-only by default.** Never publish without the user saying so.

## Live pages that are safe to link

`/contact-us` (the CTA), `/ai-sdr`, `/revenue-operations`, `/gtm-engineering`.
`/book` 301s to `/contact-us`. **`/contact` is a hard 404.**
