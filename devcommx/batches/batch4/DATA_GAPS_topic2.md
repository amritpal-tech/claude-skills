# Data gaps: Batch 4, Topic 2

Slug: `ai-sdr-for-ecommerce-fit-criteria`
Drafted: 2026-09-15

Everything below is something the draft either could not source to a primary page,
or deliberately left out rather than invent.

## 1. Primary pages could not be fetched (network egress blocked)

Two WebFetch calls returned `EGRESS_BLOCKED` from the agent proxy:

- `https://www.forrester.com/press-newsroom/forrester-us-b2b-e-commerce-will-reach-an-estimated-3-trillion-by-2027`
- `https://saleshive.com/blog/pay-per-meeting-models-best-practices-deals`

The figures attributed to both in the post come from search-result summaries, not
from a read of the source page. Someone should open both URLs and confirm before
publish:

- Forrester: US B2B e-commerce reaching about $3 trillion by 2027, and roughly
  24 percent of total US B2B sales. Both numbers are used inline in H2 #1.
- SalesHive: the post only says pricing "scales with qualification depth" and
  quotes no dollar figure from it, so the exposure here is low.

## 2. Bridge Group meeting quota stated as a range, not a number

Search summaries conflicted: one reported an average SDR quota of "21 meetings set
per month", another "12 to 20 qualified meetings depending on motion". The report
itself is gated. The draft therefore says "average monthly meeting quotas in the
high teens to low twenties per rep" rather than picking a number. If someone has
the report, tighten this to the published figure.

## 3. Gartner buying-group size deliberately omitted

Search results gave three different figures for average B2B buying group size
(6 to 10 stakeholders, 11, and 13 internal plus 9 external). None could be tied to
a single Gartner page, so no buying-group number appears in the post. Only the
17 percent of purchase time spent with suppliers is cited, which was consistent
across sources.

## 4. No DevCommX cost-per-meeting figure exists to publish

Per the batch brief, the break-even section is built entirely from reader inputs.
The worked examples use inputs labelled illustrative at every mention:

- $400 cost per booked meeting (B2B example and DTC example)
- 15 percent meeting to closed won, 75 percent gross margin (B2B)
- 8 percent conversation to purchase, $90 order, $240 LTV, 55 percent margin (DTC)

None of these are presented as DevCommX data or as a benchmark. If DevCommX ever
publishes a real blended cost per booked meeting, this section should be revisited
so the anchor is sourced rather than illustrative.

## 5. No e-commerce landing page or city page exists

The sheet's conversion path `/ai-sdr/{city}/ecommerce` is a template placeholder.
Per the brief, the draft links `https://www.devcommx.com/ai-sdr` instead and
invents neither a city page nor an e-commerce landing page.

## 6. No published AI SDR vendor pricing specific to e-commerce ICPs

Searched for it; nothing vendor-published segments AI SDR pricing by e-commerce
buyer type. The post therefore keeps the break-even generic rather than quoting a
segment-specific price.

## 7. Primary keyword is not verbatim in the H1

The brief mandates the title verbatim as `name`
("Does AI SDR Work for E-commerce? The ACV and Buyer Criteria That Decide It
(B2B vs DTC)"), which does not contain the exact string "AI SDR for ecommerce".
That string is present in the meta-title, the slug, the first sentence, two H2s,
one FAQ question and the schema keywords. Flagging only because the generic spec
also asks for it in the H1 and the brief's instruction takes precedence.

## 8. Regulatory claim kept deliberately vague

The DTC section says cold emailing consumers "raises consent and deliverability
problems". An earlier draft asserted that consumer cold email "sits in a different
regulatory position from business to business outreach in most markets". That is
broadly true (GDPR, PECR, CASL, CAN-SPAM all treat it differently) but no single
citation covers "most markets", so the claim was cut rather than sourced loosely.
