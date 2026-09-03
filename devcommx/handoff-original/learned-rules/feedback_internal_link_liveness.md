---
name: feedback_internal_link_liveness
description: "Blog internal-link targets must be checked LIVE (200), not just present in the Webflow CMS"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 39dac381-37df-48e7-a02c-d1fa1ec212f4
  modified: 2026-08-11T08:24:01.160Z
---

When drafting DevCommX blogs, internal links must point to slugs that are **published and return 200**, not merely slugs that exist in the CMS. The `_existing_slugs.txt` inventory is built from a CMS item list, and that list **includes unpublished drafts**. Linking to those produces live 404s.

This actually shipped: 3 dead targets (`b2b-buying-signals-guide-signal-based-prospecting`, `email-deliverability-rules-2026-spf-dkim-dmarc-compliance`, `hybrid-ai-sdr-model-account-split`) created 11 broken links across 9 posts, 5 of which were already public.

**How to apply:** Before drafting, curl each candidate internal-link slug (`https://www.devcommx.com/blogs/<slug>`) and keep only the 200s as the approved link menu. After drafting, re-audit every `href` in every post. Note that a `curl` 403 on an EXTERNAL link is usually anti-bot (Gartner, Apollo KB, SEC.gov, DOL.gov, Perplexity all 403 to curl but load fine in a browser) — verify in a real browser before "fixing" a link that is not broken.

**The contact CTA URL is `/contact-us`, NOT `/contact`.** `https://www.devcommx.com/contact` is a hard 404; the real page is `https://www.devcommx.com/contact-us` (and `/book` 301s to it). DevCommX's own team-written blogs use `/contact-us`. The old `_DRAFT_SPEC.md` used `/contact`, so 31 drafts created in this project have a **broken CTA** and need `/contact` → `/contact-us` (URL-only find/replace, then re-push + republish the live ones). Live service/hub pages that vendor-selection posts should link: `/ai-sdr`, `/revenue-operations`, `/gtm-engineering` (all 200).

**Fixing live posts:** update with the COMPLETE fieldData (partial payloads risk dropping fields), pin `isDraft` to the item's current value so publish state is never flipped, and remember a Webflow update only *stages* the change: an already-live item needs `publish_collection_items` before the fix is public. See [[feedback_webflow_cms_concurrency_bug]].
