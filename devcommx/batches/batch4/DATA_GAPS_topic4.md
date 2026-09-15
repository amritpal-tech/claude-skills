# Data gaps: batch 4, topic 4 (cold-email-hackers-alternatives)

Recorded 2026-09-15. This is the highest-risk post in the batch because it names real
companies. Everything below is something the draft deliberately does NOT assert.

**This ships as a Draft and requires a human factual-accuracy review before publish.**

## 0. Research method and its limits

Research was carried out in September 2026 using 8 WebSearch calls and 5 WebFetch calls
(the hard caps for the task). **Every one of the 5 WebFetch attempts returned
`EGRESS_BLOCKED`**: saleshive.com, www.cleverly.co, www.cience.com, www.revenueflow.com
and clutch.co are all unreachable from this environment. **No vendor page was read
directly.** Every vendor claim in the post comes from published summaries and search
result text that quote those pages. The methodology H2 in the post states this plainly,
names the blocked domains, and gives the month and year of the research.

## 1. Cells deliberately left as "Not publicly stated", and why

| Row | Column | Why |
|---|---|---|
| Belkins | Pricing model | Belkins does not publish rates; every source says a quote requires a sales consultation. Third-party ranges ($2,000 to $25,000+/month, $300 to $800 per appointment) circulate widely and none is a Belkins-published figure, so none is used. |
| Belkins | Contract minimum | Third-party reviews report 3 to 6 months and a $10,000+ minimum project size on Clutch. Clutch was egress-blocked and Belkins does not publish it, so the cell is empty. |
| Belkins | Publicly stated ICP | No named ICP or declined ICP found in any published Belkins statement. |
| CIENCE | Pricing model (figures) | CIENCE publishes a pricing page, which is stated. The specific figures reported in third-party write-ups ($2,400/month platform-only, $6,000/month shared capacity, $10,000 to $15,000 dedicated SDR, $5,000 setup) appeared in a single search summary and could not be checked against cience.com/pricing, which is blocked. Figures omitted. |
| CIENCE | Publicly stated ICP | Not published. A third-party blog says CIENCE will develop an ICP with the client; that is not a stated ICP and is not used. |
| Cleverly | Publicly stated ICP | Cleverly publishes pricing in detail but no named ICP or declined ICP was found. |
| Martal Group | Pricing model (price) | Martal publishes the pricing structure (three-month pilot, then a monthly subscription at a flat fee, commission on some tiers) but not a price. Third-party ranges of $4,100 to $10,500/month are not used. |
| Martal Group | Publicly stated ICP | Not published in any source reviewed. |
| SalesHive | Pricing model (figures) | SalesHive publishes a pricing page stating a flat monthly fee, no setup fee and no long-term contract, all of which is used. Per-tier dollar figures differed between third-party reviews (a "Crush" plan at $12,000/month US or ~$7,000/month Philippines vs. general $3,000 to $15,000 ranges), so no dollar figure is asserted. |
| SalesHive | Publicly stated ICP | Not published in any source reviewed. |
| DevCommX | Pricing model | DevCommX does not publish a rate card. Held to the same standard as every other row and left empty on purpose; this is stated in the disclosure H2. |
| DevCommX | Contract minimum | Not published. Same reason. |

A table with eleven "Not publicly stated" cells is the correct outcome here. Every one
of them is a fact the vendor has not published, not a fact the research missed.

## 2. Nothing is asserted about Cold Email Hackers beyond published positioning

The post names Cold Email Hackers only once in the body, to state its published
positioning (a managed B2B cold email service covering ICP definition, list building,
deliverability infrastructure and copy), sourced to the Salesforge agency directory
listing. **No claim about its pricing, quality, results, deliverability, client
outcomes, reviews or ratings appears anywhere.** Its own domain and its Clutch profile
were not reachable, so neither its published pricing (if any) nor its profile data
(minimum project size, headcount, founding year) is stated.

## 3. No quality judgement about any named firm

There is no ranking, no scoring, no "best", no verdict and no comparative quality
language about any of the six firms. The two FAQ questions that contain the word "best"
are the PAA target phrasings from the brief; both answers explicitly refuse to rank and
redirect the reader to checkable criteria. The ItemList schema carries
`itemListOrder: ItemListUnordered` and the post states that the order is alphabetical
and is not a ranking.

## 4. No invented statistics

No reply rate, meeting rate, cost per meeting, deliverability figure or client outcome
is stated for any firm, including DevCommX. The only performance claim in the post is
the permitted one, "40+ qualified demos in ~6 weeks", attributed to DevCommX, used
twice (once in the disclosure, once in the DevCommX profile) and flagged in the
disclosure as the reason a vendor-written comparison should not be a reader's only input.

## 5. Unused third-party figures (recorded so a reviewer can check them if wanted)

These surfaced in search but are NOT in the post:
- Belkins: $3,000 to $15,000/month; $300 to $800 per appointment; $10,000+ minimum
  project size; 3 to 6 month minimum.
- CIENCE: $2,400/month platform-only; $6,000/month shared; $10,000 to $15,000/month
  dedicated; $5,000 one-time GTM setup sprint.
- Martal Group: $4,100 to $10,500/month; $5,000 to $9,000/month typical.
- SalesHive: "Crush" plan at $12,000/month (US SDRs) or ~$7,000/month (Philippines
  SDRs); 2 SDRs; 500+ touches per day.
- Category: $2,500 to $12,000/month typical retainer, $500 to $2,500 setup fee.

## 6. Action before publish

A human should open the five pricing pages linked in References and confirm, at minimum:
Cleverly's $397 / $697 / $997 LinkedIn tiers, the $1,995 cold email floor and the
$3,995 cold calling floor; SalesHive's "no setup fee, no long-term contract" wording;
CIENCE's month-to-month terms; Martal's three-month pilot; and that Belkins still
publishes no rates. If any figure has changed, correct the table cell and the matching
FAQ answer (FAQ answers 3 and 5 repeat the published figures and must stay in sync with
the schema, which mirrors them word for word).
