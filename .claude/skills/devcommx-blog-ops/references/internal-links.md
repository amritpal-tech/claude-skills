# Internal links

## The rule

**Curl-verify every internal target returns 200 before it goes in a draft.** The CMS slug
inventory includes unpublished drafts, and linking to one produces a live 404. See
gotchas.md #2.

```bash
bash .claude/skills/devcommx-blog-ops/scripts/check_links.sh agentic-gtm-ai-agents-gtm-engineering gtm-engineering-stack
# or check the whole inventory
bash .claude/skills/devcommx-blog-ops/scripts/check_links.sh --file devcommx/data/_existing_slugs.txt
```

**If the session cannot reach the domain, the check is not valid.** A Claude Code web
or remote session usually sits behind an egress proxy that blocks `devcommx.com`
outright (curl gets `CONNECT tunnel failed, response 403`; WebFetch returns
`EGRESS_BLOCKED`). Every target then reports DEAD, which is a false negative. Run the
check from a local machine or an environment whose network policy allows the domain,
and never remove or "fix" a link on the strength of a blocked run. If liveness cannot
be verified in the current session, say so and hold the link decision rather than
guessing.

Build a verified-live menu at the start of each batch and hand **only that menu** to the
drafting agents.

## Non-blog pages

| URL | Status | Use |
|---|---|---|
| `https://www.devcommx.com/contact-us` | 200 | the CTA on every post |
| `https://www.devcommx.com/ai-sdr` | 200 | AI SDR vendor-selection posts |
| `https://www.devcommx.com/revenue-operations` | 200 | RevOps posts |
| `https://www.devcommx.com/gtm-engineering` | 200 | GTM engineering posts |
| `https://www.devcommx.com/book` | 301 → `/contact-us` | avoid, link the target |
| `https://www.devcommx.com/contact` | **404** | never |

## The working menu from the handoff session

Verified live at that time. **Re-verify before reuse.**

```
agentic-gtm-ai-agents-gtm-engineering
gtm-engineering-stack
best-gtm-engineering-agencies
definitive-guide-to-ai-sdrs
ai-sdr-system-cost
ai-sdr-pricing
human-in-the-loop-ai-sdr-orchestration
hybrid-ai-sdr-model-account-split
b2b-buying-signals-guide-signal-based-prospecting
abm-campaign-strategy-signal-based-targeting
clay-data-enrichment-fields-integrations-guide
clay-hubspot-integration-guide
clay-pricing-breakdown
clay-alternatives-data-enrichment-tools
b2b-email-deliverability-guide-2026
cold-email-domain-setup-checklist
best-email-warmup-tools-deliverability
email-deliverability-rules-2026-spf-dkim-dmarc-compliance
b2b-outbound-automation-guide
b2b-outbound-tool-stack
how-to-get-cited-by-chatgpt
how-to-optimize-content-for-llms-llmo-playbook
how-to-measure-llmo-ai-visibility-tracking
how-clay-uses-clay-seo-aeo-strategy
mcp-for-sales-model-context-protocol-revenue-stack
company-news-sales-outreach-event-based-outbound
contextual-outreach-playbook-buying-signals-meetings
```

Three of these (`b2b-buying-signals-guide-signal-based-prospecting`,
`email-deliverability-rules-2026-spf-dkim-dmarc-compliance`,
`hybrid-ai-sdr-model-account-split`) were the exact slugs that turned out to be
unpublished drafts. They are on the list because they were later fixed, not because they
are permanently safe. Re-verify.

## Protected URLs

From `devcommx-keyword-governance`, never change or fragment:

- `/blogs/best-gtm-engineering-agencies` — position 2.9, 10.67% CTR, the highest on the
  site. Never change that URL.
- the `claude sdr` cluster — position 3.8, 5.56% CTR. Expand it, do not fragment it.

## Full inventory

`devcommx/data/_existing_slugs.txt` — 149 slugs as of the handoff. Regenerate by
enumerating the collection (offsets 0, 100, 200).
