# Batch 4: independent verification log

Every draft is checked in the main thread after the agent reports, because the
pipeline's rule is not to trust agent self-reports. This file records what was
actually re-verified at source, as opposed to what an agent claimed.

## Record correction

Commit `61bc9ee` is labelled "Draft batch 4 topics 1 and 2" but also contains
topic 6's draft. Topic 6's agent wrote its file early, as instructed, and a
`git add -A` swept it in before that agent had finished. The content is the
agent's final version and it is correct; only the commit label is imprecise.

## Structural checks run on every draft

Gate at the batch-specific word band, plus, independently in the main thread:
schema byte-identical across the `schema-markup` field and the post-body embed,
FAQ schema mirroring the visible H4/P block word for word, no em or en dashes,
no HTML comments, no bare-URL anchor text, no `/contact` (as against
`/contact-us`), table headers carrying `color:#1f2937`, and the permitted
DevCommX performance claim used at most once.

One false positive worth noting: a naive `<th` substring count also matches
`<thead>`, which made topic 1's table look mis-styled. All four real `<th>`
elements were correctly styled.

## Claims re-verified at source

| Claim | Post | Result |
|---|---|---|
| Forrester, US B2B e-commerce $3T by 2027, 24% of US B2B sales | topic 2 | Confirmed; cited URL is the real press page |
| Gartner, AI agents outnumber sellers 10 to 1 by 2028, under 40% report improved productivity | topic 6 | Confirmed verbatim; cited URL exact |
| Gartner, 67% of B2B buyers prefer a rep-free experience | topic 6 | Confirmed: 9 March 2026, 646 buyers, fielded Aug to Sep 2025. Draft correctly uses the current 67% rather than the superseded 61% |

## Open items a human must close before publish

1. **Topic 1, LinkedIn terms.** `linkedin.com` is egress-blocked from this
   session, so the User Agreement and Prohibited Software policy could not be
   read directly. The draft paraphrases rather than quotes, asserts no section
   number or effective date, and claims no invitation limit, appeal SLA or
   detection mechanism as fact. Someone with access must confirm the
   prohibited-conduct clause still says what the post implies.
2. **Topic 2, e-commerce conversion path.** The sheet specifies
   `/ai-sdr/{city}/ecommerce`, a template placeholder with no resolvable URL.
   The draft links the verified `/ai-sdr` service page instead. Swap in the real
   landing page before publish.
3. **Topic 4, named competitors.** Requires the factual-accuracy review the
   source sheet mandates. Ships as a Draft only.
4. **Bridge Group figures** in topics 2 and 6 come from public summary pages
   rather than the gated primary report.
5. **Internal links** were verified against the Webflow CMS, not by fetching
   live URLs, because `devcommx.com` is egress-blocked here.
