---
name: feedback_webflow_cms_concurrency_bug
description: "Webflow data_cms_tool races under parallel calls — create CMS items sequentially, never in a fan-out"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 39dac381-37df-48e7-a02c-d1fa1ec212f4
---

The Webflow `data_cms_tool` (create/update collection items) is NOT concurrency-safe. When multiple create calls hit it in parallel (e.g. a Workflow fan-out with one agent per blog), it **double-creates items** (the second copy gets a random `-xxxxx` slug suffix because the clean slug is already taken) and **cross-wires responses** (an agent's create returns an unrelated item's slug/id). In one batch of 13 parallel creates, the first 7 all duplicated.

**Why:** server-side response-routing / queue mismatch under concurrent load. This is distinct from the known slug-filter bug (list/filter returning the wrong item).

**How to apply:** Create/update CMS items **sequentially** — one call at a time, or a single call with all items in the `fieldData` array — never a parallel fan-out. Drafting can still be parallel (agents just write JSON to disk); only the Webflow write step must be serial. After any batch write, **re-enumerate the collection** (paginate list, match by slug prefix) to detect duplicates/suffixed slugs, and dedupe. Deleting CMS items is permanent (no Webflow trash) — get explicit user approval before deleting, then delete in one sequential call. See [[project_devcommx_seo_blog_state]].
