#!/usr/bin/env python3
"""Builds devcommx/blogs/batch4/cold-email-hackers-alternatives.json"""
import json, os, re, html

SLUG = "cold-email-hackers-alternatives"
URL = f"https://www.devcommx.com/blogs/{SLUG}"
OG = "https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"
OUT = "/home/user/claude-skills/devcommx/blogs/batch4/cold-email-hackers-alternatives.json"

TH = 'style="border:1px solid #ddd; padding:12px; text-align:left; background:#f5f5f5; color:#1f2937;"'
TD = 'style="border:1px solid #ddd; padding:12px;"'
NPS = "Not publicly stated"

headers = ["Agency", "Stated service scope", "Pricing model", "Contract minimum",
           "Channel coverage", "Publicly stated ICP"]

rows = [
    ["Belkins",
     "B2B appointment setting and lead generation",
     NPS + ", quote on consultation",
     NPS,
     "Email and LinkedIn into booked appointments",
     NPS],
    ["CIENCE",
     "Outsourced SDR and outbound lead generation",
     "Pricing page published; figures " + NPS.lower() + " in checkable sources",
     "Month to month terms stated",
     "Email, phone and LinkedIn, plus research",
     NPS],
    ["Cleverly",
     "LinkedIn outreach, cold email and cold calling",
     "Published tiers: LinkedIn $397, $697, $997 a month; cold email from $1,995",
     "Three months on LinkedIn plans; cold email month to month",
     "LinkedIn, email, calling, LinkedIn ads, content",
     NPS],
    ["Martal Group",
     "Three tiers, lead generation to account management",
     "Flat monthly fee quoted on inquiry; commission on some tiers",
     "Three month pilot, then a monthly subscription",
     "Outbound built around fractional SDR capacity",
     NPS],
    ["SalesHive",
     "SDR team, strategist, platform, data and tools, one package",
     "One flat monthly fee, no setup fee; dollar figures " + NPS.lower(),
     "No long term contract stated; month to month",
     "Cold calling, email and LinkedIn",
     NPS],
    ["DevCommX",
     "AI SDR systems, revenue operations, GTM engineering, on client owned assets",
     NPS,
     NPS,
     "Email and LinkedIn, on client owned domains and inboxes",
     "B2B teams that want to own the system, not rent a campaign"],
]

table = ["<div data-rt-embed-type='true'><div style=\"overflow-x:auto;\">",
         '<table style="width:100%; border-collapse:collapse; font-family:Arial, sans-serif; font-size:14px; line-height:1.7;">',
         "<thead><tr>"]
for h in headers:
    table.append(f"<th {TH}>{h}</th>")
table.append("</tr></thead><tbody>")
for r in rows:
    table.append("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>")
table.append("</tbody></table></div></div>")
TABLE = "".join(table)

FAQ = [
 ("What are the best Cold Email Hackers alternatives?",
  "This comparison does not rank agencies, because no public dataset supports a quality ranking. The five firms with enough checkable public information to compare here are Belkins, CIENCE, Cleverly, Martal Group and SalesHive, plus DevCommX, which competes in the category. Shortlist on published pricing model, contract minimum and channels, then judge fit through references and a paid pilot."),
 ("What are the best cold email agencies?",
  "There is no objective answer, because the outcome data that would settle it is private to each vendor and client. A defensible shortlist comes from criteria you can check: does the firm publish a price, does it publish a contract minimum, does it name its channels, and will it name an ICP it declines."),
 ("How much does a cold email agency cost?",
  "Only some firms publish a figure. Cleverly publishes LinkedIn tiers at $397, $697 and $997 a month and cold email from $1,995 a month. SalesHive publishes a flat monthly fee with no setup fee. Belkins and Martal Group quote after a consultation. Where a firm does not publish, treat third party ranges as hearsay until you hold a written quote."),
 ("Should you outsource cold email?",
  "Outsource when your offer converts, your ICP is broad enough for list building, and your closers have open capacity. Keep it in house when the first conversation needs deep product knowledge, when the ICP is unproven, or when the sending infrastructure and data must stay yours. The condition matters more than the vendor."),
 ("What contract minimum should a B2B outbound agency state?",
  "Ask for it in writing before the pilot. Martal Group publishes a three month pilot followed by a monthly subscription. Cleverly states a three month minimum on LinkedIn plans and month to month on cold email. SalesHive states no long term contract. Where a minimum is unpublished, expect three to six months and negotiate the exit terms."),
]

def p(s): return "<p>" + s + "</p>"

body = []
body.append(p("The <strong>Cold Email Hackers alternatives</strong> with enough public information to compare are Belkins, CIENCE, Cleverly, Martal Group and SalesHive, alongside DevCommX. This <strong>cold email agency comparison</strong> ranks nothing and rates nothing. It records only what each firm publishes: service scope, pricing model, contract minimum, channel coverage and stated ICP, so you can score six vendors against your own requirements."))

body.append(p('Most "best cold email agencies 2026" lists are affiliate pages wearing a comparison table, asserting reply rates nobody can audit. This piece is deliberately less satisfying: published facts, attributed, with an empty cell wherever the vendor has not said. We build outbound systems for B2B teams, and the fix for a bad vendor decision is usually a better checklist, not a better shortlist. For the economics underneath, start with <a href="https://www.devcommx.com/blogs/true-cost-of-outbound-ai-vs-agency-vs-in-house">the true cost of outbound across AI, agency and in house</a>.'))

body.append("<h2>Methodology: how these Cold Email Hackers alternatives were compared</h2>")
body.append(p("Research was carried out in September 2026. Five comparison firms were selected on one criterion: enough public, checkable information to fill most of a row. Selection was not a quality screen and implies nothing about any firm absent from it. Five published attributes were recorded for each: service scope, pricing model, contract minimum, channel coverage and stated ideal customer profile."))
body.append(p('<strong>Where the facts come from.</strong> Every entry traces to something a vendor published on its own site, or to a dated third party write up quoting that page. Where a vendor publishes no figure, the cell reads "Not publicly stated" rather than a range borrowed from a competitor. Several cells read that way, which is the accurate outcome, not a research gap.'))
body.append(p("<strong>What could not be verified directly.</strong> Most vendor domains, including saleshive.com, cleverly.co, cience.com and clutch.co, were unreachable from the research environment used here, and every direct fetch returned a blocked response. Those pages were read through published summaries and search result text quoting them, not through a direct review of the live page. Each URL is in References so you can open it yourself, and the pricing column is preparation for a procurement call, not a quote."))
body.append(p("<strong>What was not assessed.</strong> Nothing here claims anything about any firm's quality, deliverability, results or client outcomes. That includes Cold Email Hackers, whose published positioning is a managed B2B cold email service covering ICP definition, list building, infrastructure and copy, per its agency directory listing. No ranking, no scoring, no verdict."))

body.append("<h2>Disclosure: DevCommX competes in this category and is in the table</h2>")
body.append(p("DevCommX sells B2B outbound services and appears in the comparison below. Read everything with that conflict in mind. Two rules follow. DevCommX is held to the same evidence standard as every other row, so where it publishes no number its cells read \"Not publicly stated\" like the others. And the only performance figure asserted anywhere in this post is one DevCommX result, 40+ qualified demos in ~6 weeks, because no comparable figure for another named firm was published in a checkable form."));
body.append(p('That is why a vendor written comparison should never be your only input. Use this one for the checklist below, then run the same questions at us: our own <a href="https://www.devcommx.com/ai-sdr">AI SDR systems clients own outright</a> positioning is a claim too, not evidence.'))

body.append("<h2>The comparison table: scope, pricing model, contract minimum, channels and ICP</h2>")
body.append(p("Six firms, five attributes, one rule: if it was not published, it is not in the cell. Read the empty cells as information. Publishing a price and a contract minimum makes a firm easy to compare, which is a procurement fact, not praise."))
body.append(TABLE)
body.append(p('The ICP column is almost entirely empty, and that is the most useful pattern here. Five of the six publish their channels and the shape of their pricing, but not the buyer they are built for or the buyer they decline. Outsourced cold email pricing is easier to discover in 2026 than outsourced cold email fit, which is backwards. Our note on <a href="https://www.devcommx.com/blogs/ai-sdr-pricing">how AI SDR pricing models are structured</a> covers the same gap on the software side.'))

body.append("<h2>Six agency profiles, published facts only</h2>")
body.append("<h3>Belkins</h3>")
body.append(p("Belkins publishes B2B appointment setting and lead generation as its scope, and publishes explainer content on appointment setting pricing models, including retainer and pay per appointment structures. It does not publish its own rates, and published reviews note that a quote requires a consultation. Contract minimum: not publicly stated. Third party ranges circulate; none is a Belkins figure."))
body.append("<h3>CIENCE</h3>")
body.append(p("CIENCE publishes a pricing page for outsourced SDR and outbound lead generation and states month to month terms rather than a lock in. Stated scope covers trained SDRs, research, outreach and appointment setting. Tier figures appear in third party write ups but could not be verified against the page, so they are recorded as not publicly stated."))
body.append("<h3>Cleverly</h3>")
body.append(p("Cleverly publishes per tier figures: LinkedIn outreach at $397, $697 and $997 a month, cold email from $1,995 a month, cold calling from $3,995 a month, with Sales Navigator required and billed separately. Published reviews state a three month minimum on the LinkedIn plans and month to month terms on cold email. Channels span LinkedIn, email, calling, ads and content."))
body.append("<h3>Martal Group</h3>")
body.append(p("Martal Group publishes three service tiers, from lead generation through onboarding to account management, and publishes its pricing structure without a price: a three month pilot, then a monthly subscription at a flat fee quoted on inquiry, with commission on some tiers. Delivery is fractional SDR capacity, covered in our <a href=\"https://www.devcommx.com/blogs/best-fractional-sdr-services\">guide to fractional SDR services</a>."))
body.append("<h3>SalesHive</h3>")
body.append(p("SalesHive publishes a pricing page stating the model: one flat monthly fee covering the SDR team, a strategist, the platform, data and tools, with no setup fee and no long term contract. Published channels are cold calling, email and LinkedIn. Per tier dollar figures in third party reviews varied between sources and could not be checked, so they are not asserted."))
body.append("<h3>DevCommX</h3>")
body.append(p("DevCommX publishes its scope as AI SDR systems, revenue operations and GTM engineering, delivered on domains, inboxes and CRM records the client owns, with email and LinkedIn as channels. It publishes no rate card and no contract minimum, so both cells read not publicly stated. The one published result referenced here is 40+ qualified demos in ~6 weeks."))

body.append("<h2>How to choose between Cold Email Hackers alternatives: five questions</h2>")
body.append(p("<strong>1. What is the exit state?</strong> Ask which assets you keep the day after cancellation: domains, warmed inboxes, sequences, the enriched list, the CRM records. A campaign run on the vendor's infrastructure leaves you a list of meetings that already happened. That is a legitimate product, but price it as rental, not as a channel."))
body.append(p("<strong>2. Who writes the copy, and who approves it?</strong> Ask for two live sequences written for a client in your segment, and who signs off before anything sends from a domain tied to your brand. That workflow decides how your brand reads in an inbox for six months."))
body.append(p("<strong>3. What is the qualification bar, in writing?</strong> A meeting is not a unit until the definition is written down: title seniority, company size, stated problem, showed up. Without it you will argue about invoices in month three. Our <a href=\"https://www.devcommx.com/blogs/outbound-sales-kpis-metrics-2026\">outbound sales KPIs worth tracking</a> has the definitions to bring."))
body.append(p("<strong>4. Which ICP would you decline?</strong> Any B2B outbound agency that has run enough programs knows which buyers its motion fails against. A firm that serves everyone has either not noticed the pattern or will not say. That answer tells you more than the case study deck."))
body.append(p("<strong>5. What happens in weeks one to four?</strong> Domain purchase, DNS authentication, inbox provisioning and warmup take calendar time before volume is safe. Ask for that sequence and the date volume ramps, then compare it against the same build done in house using <a href=\"https://www.devcommx.com/blogs/cold-email-marketing-services-vs-diy-what-works-best-for-b2b-sales\">cold email services versus doing it yourself</a>."))

body.append("<h2>Category wide red flags, not firm specific ones</h2>")
body.append(p("<strong>Guaranteed meeting counts.</strong> A guarantee prices your risk into the retainer and shifts the incentive toward booking whoever will accept an invite. It is a commercial structure, not evidence of confidence, and the qualification definition in the contract decides whether the number means anything."))
body.append(p("<strong>Pricing that only appears on a call.</strong> Quoting on inquiry is normal here and is not a fault, but it changes your procurement job. Ask every shortlisted firm for the same scope, channel mix and contract length, then compare written quotes, not pitches."))
body.append(p("<strong>No named ICP and no declined ICP.</strong> As the table shows, this is the category norm rather than a vendor specific problem. Treat it as a question to ask, not a disqualifier."))

body.append("<h2>Build your own selection checklist</h2>")
body.append(p("The shortlist matters less than the checklist you score it with. Take the five questions above, add the exit state and the qualification bar, and run every vendor through the same grid, us included. If you want that grid as a working document, <a href=\"https://www.devcommx.com/contact-us\">send us the shortlist you are already considering</a> and we will send the checklist back filled in for your scope."))

body.append("<h3>Further Reading</h3><ul>"
  '<li><a href="https://www.cleverly.co/pricing" target="_blank" rel="noopener noreferrer">Cleverly, published pricing page</a></li>'
  '<li><a href="https://saleshive.com/pricing" target="_blank" rel="noopener noreferrer">SalesHive, published pricing page</a></li>'
  '<li><a href="https://www.cience.com/pricing/" target="_blank" rel="noopener noreferrer">CIENCE, published pricing page</a></li>'
  "</ul>")

body.append("<h3>References</h3><ul>"
  '<li><a href="https://www.cleverly.co/pricing" target="_blank" rel="noopener noreferrer">Cleverly, pricing page</a>, source for the LinkedIn tiers at $397, $697 and $997 a month, cold email from $1,995 and cold calling from $3,995, read through summaries.</li>'
  '<li><a href="https://www.salesforge.ai/blog/cleverly-review" target="_blank" rel="noopener noreferrer">Salesforge, Cleverly agency review, 2026</a>, source for the Sales Navigator requirement and the three month minimum on LinkedIn plans.</li>'
  '<li><a href="https://saleshive.com/pricing" target="_blank" rel="noopener noreferrer">SalesHive, pricing page</a>, source for the flat monthly fee covering team, strategist, platform, data and tools, no setup fee, no long term contract.</li>'
  '<li><a href="https://www.cience.com/pricing/" target="_blank" rel="noopener noreferrer">CIENCE, pricing page</a>, source for the month to month terms on outsourced SDR capacity.</li>'
  '<li><a href="https://belkins.io/blog/appointment-setting-costs-pricing-models" target="_blank" rel="noopener noreferrer">Belkins, B2B appointment setting costs and pricing models</a>, source for the stated scope and the pricing structures published in place of rates.</li>'
  '<li><a href="https://clutch.co/profile/martal-group" target="_blank" rel="noopener noreferrer">Clutch, Martal Group profile</a> and <a href="https://www.g2.com/products/martal-group/pricing" target="_blank" rel="noopener noreferrer">G2, Martal Group pricing</a>, sources for the three tiers and the flat fee quoted on inquiry.</li>'
  '<li><a href="https://www.salesforge.ai/directory/agencies/cold-email-hackers" target="_blank" rel="noopener noreferrer">Salesforge agency directory, Cold Email Hackers listing</a>, source for the published positioning as a managed B2B cold email service covering ICP definition, list building, infrastructure and copy.</li>'
  "</ul>")

body.append("<h3>FAQ</h3>")
for q, a in FAQ:
    body.append(f"<h4>{q}</h4>" + p(a))

BODY_NO_SCHEMA = "".join(body)

schema = {
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "BlogPosting",
     "@id": f"{URL}#article",
     "headline": "Cold Email Hackers Alternatives: 6 B2B Outbound Agencies Compared (2026)",
     "description": "A published facts comparison of six B2B outbound agencies: stated service scope, pricing model, contract minimum, channel coverage and stated ICP, with no quality ranking.",
     "url": URL,
     "datePublished": "2026-09-15",
     "dateModified": "2026-09-15",
     "keywords": "Cold Email Hackers alternatives, cold email agency comparison, best cold email agencies 2026, outsourced cold email pricing, B2B outbound agency",
     "image": {"@type": "ImageObject", "url": OG, "width": 1200, "height": 630},
     "author": {"@type": "Person", "name": "Sumit Nautiyal",
                "jobTitle": "VP of Revenue Operations & GTM Engineering, DevCommX",
                "url": "https://www.linkedin.com/company/devcommx"},
     "publisher": {"@type": "Organization", "name": "DevCommX", "url": "https://www.devcommx.com",
                   "logo": {"@type": "ImageObject", "url": OG}},
     "mainEntityOfPage": {"@type": "WebPage", "@id": URL}},
    {"@type": "ItemList",
     "@id": f"{URL}#agencies",
     "name": "Six B2B outbound agencies compared on published positioning",
     "description": "Agencies compared on published service scope, pricing model, contract minimum, channel coverage and stated ICP. The order is alphabetical and is not a ranking.",
     "itemListOrder": "https://schema.org/ItemListUnordered",
     "numberOfItems": 6,
     "itemListElement": [
       {"@type": "ListItem", "position": i + 1,
        "item": {"@type": "Organization", "name": n, "url": u}}
       for i, (n, u) in enumerate([
         ("Belkins", "https://belkins.io"),
         ("CIENCE", "https://www.cience.com"),
         ("Cleverly", "https://www.cleverly.co"),
         ("DevCommX", "https://www.devcommx.com"),
         ("Martal Group", "https://martal.ca"),
         ("SalesHive", "https://saleshive.com"),
       ])]},
    {"@type": "FAQPage",
     "@id": f"{URL}#faq",
     "mainEntity": [
       {"@type": "Question", "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
  ],
}
SCHEMA_STR = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
assert SCHEMA_STR.endswith("]}]}"), SCHEMA_STR[-20:]

BODY = BODY_NO_SCHEMA + "<div data-rt-embed-type='true'><script type=\"application/ld+json\">" + SCHEMA_STR + "</script></div>"

words = len(re.sub(r"<[^>]+>", " ", html.unescape(
    re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", BODY, flags=re.S | re.I))).split())

item = {
  "collection_id": "689c92652a4b35f0e9a14fc2",
  "isDraft": True,
  "isArchived": False,
  "fieldData": {
    "name": "Cold Email Hackers Alternatives: 6 B2B Outbound Agencies Compared (2026)",
    "slug": SLUG,
    "meta-title": "Cold Email Hackers Alternatives: 6 Agencies Compared",
    "meta-description": "A cold email agency comparison of six B2B outbound agencies on published scope, pricing model, contract minimum, channels and stated ICP. No rankings, no verdicts.",
    "post-summary": "Six B2B outbound agencies compared on published facts only: stated service scope, pricing model, contract minimum, channel coverage and publicly stated ICP, with a methodology note on what could not be verified, a visible competitor disclosure, five questions to ask any agency before signing, and category wide red flags. No quality ranking of any named firm.",
    "post-body": BODY,
    "schema-markup": SCHEMA_STR,
    "date": "2026-09-15T00:00:00.000Z",
    "last-updated": "2026-09-15T00:00:00.000Z",
    "author-name": "Sumit Nautiyal",
    "author-title": "VP of Revenue Operations & GTM Engineering, DevCommX",
    "add-blog-reading-time": str(round(words / 220)),
    "blog-list": URL,
    "og-image": {"fileId": "69ce06f820d4562027a83191", "url": OG},
    "author": "677194290c472080e6cd6c06",
    "authors-collection": "69d8f4fd2475affd96f68115",
    "category": ["689c9183e68cf0a3029741d1"],
  },
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(item, f, ensure_ascii=False, indent=2)
print("words:", words, "reading time:", round(words / 220))
print("wrote", OUT)
