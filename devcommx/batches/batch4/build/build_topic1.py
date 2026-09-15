#!/usr/bin/env python3
"""Build the batch4 topic-1 DevCommX blog draft JSON."""
import json, os, re, html

SLUG = "ai-sdr-linkedin-account-safety"
URL = f"https://www.devcommx.com/blogs/{SLUG}"
OG = "https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png"
NAME = ("Can an AI SDR Run LinkedIn Without Getting Your Account Restricted? "
        "Limits, Risk and What Stays Human (2026)")
DESC = ("What an AI SDR can and cannot safely do on LinkedIn in 2026: the action by action "
        "automate, assist or keep human table, what triggers a restriction, and recovery steps.")

# --- external sources -------------------------------------------------------
UA = "https://www.linkedin.com/legal/user-agreement"
PSE = "https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions"
PCP = "https://www.linkedin.com/legal/professional-community-policies"
RESTRICT = "https://www.linkedin.com/help/linkedin/answer/a1340522"
ENFORCE = "https://www.linkedin.com/help/linkedin/answer/a1342754"
HIQ = "https://law.justia.com/cases/federal/appellate-courts/ca9/17-16783/17-16783-2022-04-18.html"
PW = "https://www.privacyworld.blog/2022/12/linkedins-data-scraping-battle-with-hiq-labs-ends-with-proposed-judgment/"

EXT = ' target="_blank" rel="noopener noreferrer"'


def a(href, text, external=False):
    return f'<a href="{href}"{EXT if external else ""}>{text}</a>'


TH = ('<th style="border:1px solid #ddd; padding:12px; text-align:left; '
      'background:#f5f5f5; color:#1f2937;">')
TD = '<td style="border:1px solid #ddd; padding:12px;">'

ROWS = [
    ("Account and company research", "Automate",
     "Reading public pages at human pace touches nobody.",
     "Agent builds the brief, the trigger and the talking points."),
    ("List building and enrichment", "Automate",
     "Data should come from a licensed provider, not your session.",
     "Buy the data. Never point an extension at search results."),
    ("ICP scoring and prioritisation", "Automate",
     "Ranking happens in your systems, not on LinkedIn.",
     "Score and route the queue daily, unsupervised."),
    ("Drafting the connection note", "Automate",
     "Writing is not an action on the platform.",
     "Generate the note, the evidence line and two alternates."),
    ("Sending the connection request", "Keep human",
     "The most scored, most rate limited, most reportable action.",
     "Queue it. The account owner clicks send."),
    ("Profile views", "Assist",
     "Hundreds of views an hour is a velocity pattern.",
     "Cap it, spread it, tie each view to a queued action."),
    ("First message after acceptance", "Assist",
     "The recipient consented, but it is still a write action.",
     "AI drafts, a human approves and sends."),
    ("Follow ups in an open thread", "Assist",
     "The lowest risk surface, and where replies come from.",
     "AI drafts the batch, a rep approves it in one sitting."),
    ("Likes, comments and reactions", "Keep human",
     "Generated engagement reads as inauthentic to the buyer.",
     "Give the rep a daily shortlist. They write it."),
    ("Replying to an objection", "Keep human",
     "Where the deal is won, and a wrong answer is unrecoverable.",
     "AI suggests in the CRM. The rep sends it."),
    ("Exporting profiles to your CRM", "Keep human",
     "Bulk copying profile data is the conduct the terms name.",
     "Sync only records from a licensed source."),
]


def table():
    head = "".join(TH + h + "</th>" for h in
                   ("LinkedIn action", "Verdict", "Why it sits there",
                    "What the software may do"))
    body = ""
    for r in ROWS:
        body += "<tr>" + "".join(TD + c + "</td>" for c in r) + "</tr>"
    return ("<div data-rt-embed-type='true'><div style=\"overflow-x:auto;\">"
            '<table style="width:100%; border-collapse:collapse; font-family:Arial, sans-serif; '
            'font-size:14px; line-height:1.7;">'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div></div>")


FAQ = [
 ("Is LinkedIn automation against the terms of service?",
  "Yes, on a plain reading. LinkedIn's User Agreement tells members not to use software, scripts, "
  "robots, crawlers, plug-ins or add-ons to scrape the service or copy profile data, and not to use "
  "bots or automated methods to access it, add contacts or send messages. A separate prohibited "
  "software policy repeats the point for browser extensions."),
 ("Can you get banned for using LinkedIn automation?",
  "Yes. LinkedIn applies temporary or permanent restrictions depending on the severity and repetition "
  "of the activity, and says members who break these rules risk having accounts restricted or shut "
  "down. A first action is usually a feature limit or an identity check, but repeat patterns on one "
  "profile escalate."),
 ("Can AI SDRs use LinkedIn?",
  "They can support LinkedIn work without touching the account. An AI SDR can research accounts, "
  "detect triggers, score the queue and draft the connection note and the follow up, all outside the "
  "platform. What it should not do is log in and click for you. The safe division of labour is AI up "
  "to the draft, a human from the send onward."),
 ("What is the safest AI SDR LinkedIn setup in 2026?",
  "One human owned profile per rep, no shared logins, no headless browsers, no proxy tricks, and "
  "every write action performed by the account owner. The agent runs research, targeting and drafting "
  "on your own infrastructure, then hands a reviewed queue to the rep. Volume stays inside the "
  "platform limits rather than probing them."),
 ("How long does a restricted LinkedIn account take to recover?",
  "It depends on the tier. An identity verification prompt is the fastest path back because it "
  "resolves once your documents pass review. A contested restriction goes through the Help Center "
  "appeal queue and takes days rather than hours. LinkedIn publishes no service level for appeals, so "
  "plan for a week or more off the channel."),
 ("Does LinkedIn detect AI written messages?",
  "The risk is not that text was generated. It is that a hundred messages share one skeleton. Near "
  "duplicate copy sent at machine cadence is a pattern any platform can cluster. Text genuinely "
  "different per recipient, sent at human pace from a real profile, looks like a person writing, "
  "because in every measurable respect it is."),
]

SCHEMA = {
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "BlogPosting", "@id": f"{URL}#article",
     "headline": NAME,
     "description": DESC,
     "url": URL,
     "datePublished": "2026-09-15", "dateModified": "2026-09-15",
     "keywords": ("AI SDR LinkedIn, LinkedIn automation ban risk, safe LinkedIn automation 2026, "
                  "AI SDR account safety, LinkedIn automation ToS"),
     "image": {"@type": "ImageObject", "url": OG, "width": 1200, "height": 630},
     "author": {"@type": "Person", "name": "Sumit Nautiyal",
                "jobTitle": "VP of Revenue Operations & GTM Engineering, DevCommX",
                "url": "https://www.linkedin.com/company/devcommx"},
     "publisher": {"@type": "Organization", "name": "DevCommX",
                   "url": "https://www.devcommx.com",
                   "logo": {"@type": "ImageObject", "url": OG}},
     "mainEntityOfPage": {"@type": "WebPage", "@id": URL}},
    {"@type": "FAQPage", "@id": f"{URL}#faq",
     "mainEntity": [{"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": ans}}
                    for q, ans in FAQ]}
  ]
}
SCHEMA_STR = json.dumps(SCHEMA, ensure_ascii=False, separators=(",", ":"))

B = []
P = B.append

# 1. extractable answer
P("<p>An <strong>AI SDR LinkedIn</strong> workflow is safe only when the software stops at the draft "
  "and a person performs the action. LinkedIn's terms prohibit third party tools that automate "
  "activity on the site, so the defensible pattern is <strong>AI for research, targeting and "
  "drafting</strong>, with a <strong>human sending connection requests and first touches</strong> "
  "from their own logged in session.</p>")

# 2. intro, exactly one internal link
P("<p>That costs money, which is why it gets argued with. Most LinkedIn tooling is sold on the idea "
  "that clicking is the expensive part. In the systems we build, clicking is cheap and the profile is "
  "the asset: an account carries years of network and warm threads no tool rebuilds. The limits "
  "themselves are covered in our guide to "
  + a("https://www.devcommx.com/blogs/linkedin-connection-request-limits-2026-safe-outreach",
      "LinkedIn connection request limits and safe outreach") +
  ". This piece answers what happens when software works inside them.</p>")

# H2 1
P("<h2>The Short Answer: What an AI SDR LinkedIn Workflow Can and Cannot Safely Do</h2>")
P("<p><strong>Start with the contract.</strong> LinkedIn's "
  + a(UA, "User Agreement", True) +
  " tells members not to develop, support or use software, devices, scripts, robots or other means, "
  "including crawlers, browser plug-ins and add-ons, to scrape the services or copy profile data, and "
  "not to use bots or other automated methods to access the services, add contacts or send messages. "
  "The separate "
  + a(PSE, "prohibited software and extensions policy", True) +
  " repeats it for anything that scrapes, modifies or automates activity on the site. There is no "
  "carve out for low volume.</p>")
P("<p>So the answer is not a number of messages per day. It is a line through the workflow. "
  "Everything upstream of the click is yours: research, trigger detection, scoring, drafting, reply "
  "suggestion, CRM logging. Everything that writes to the platform belongs to the person named on the "
  "profile. That split keeps nearly all the leverage and removes your LinkedIn automation ToS "
  "exposure, because no third party software acts in your session.</p>")
P("<p><strong>The real trade.</strong> A rep sending their own invitations from a pre researched "
  "queue spends fifteen minutes a day on LinkedIn. That is AI SDR account safety in practice, and the "
  "wider architecture sits in our "
  + a("https://www.devcommx.com/blogs/definitive-guide-to-ai-sdrs", "definitive guide to AI SDRs") +
  ".</p>")

# H2 2
P("<h2>What Actually Triggers a LinkedIn Restriction, and What People Wrongly Believe Does</h2>")
P("<p><strong>Four patterns cause most enforcement.</strong> Velocity: more actions per hour than a "
  "hand could produce, or an even cadence with no gaps for lunch or sleep. Sameness: many messages "
  "sharing one skeleton with a swapped first name. Negative recipient signal: invitations marked "
  "unwanted or messages reported as spam. Session anomalies: a login from a new country, a headless "
  "browser or a rotating IP while an extension drives the page.</p>")
P("<p>Identity sits underneath all four. LinkedIn's "
  + a(PCP, "Professional Community Policies", True) +
  " require members to use their true identity and share information that is real and authentic, and "
  "LinkedIn will restrict a profile it believes is fraudulent. Burner profiles and shared logins are "
  "therefore the worst foundation for outbound: they fail the authenticity test before volume is "
  "discussed, and they concentrate LinkedIn automation ban risk on an account with no history.</p>")
P("<p><strong>What does not trigger one.</strong> Using AI to write a message is not a violation. Nor "
  "is a CRM, a Sales Navigator seat, or a playbook telling a rep who to contact. Hitting a weekly cap "
  "is a limit, not an offence. The line the "
  + a(ENFORCE, "enforcement policy", True) +
  " draws is between a human performing informed actions and software performing them for a "
  "human.</p>")

# H2 3 + table
P("<h2>The Action by Action Table: Automate, Assist or Keep Human</h2>")
P("<p>Put this in front of whoever is buying the tool. <strong>Automate</strong> means software runs "
  "it end to end. <strong>Assist</strong> means software prepares it and a human confirms before "
  "anything leaves. <strong>Keep human</strong> means a person performs the action in their own "
  "browser session, with no exception for a busy quarter.</p>")
P(table())
P("<p>Read the third column before the verdict. Risk tracks who receives the action, not how hard it "
  "is to automate. Anything reaching a stranger, or copying their data, is high risk. Anything "
  "reaching someone who accepted you is low risk. Anything that never leaves your infrastructure is "
  "not a LinkedIn question. That is safe LinkedIn automation 2026 in one rule.</p>")

# H2 4
P("<h2>Why Connection Requests Are the Highest Risk Action and Messaging Is Not</h2>")
P("<p><strong>An invitation is an unconsented touch with a report button attached.</strong> The "
  "recipient can decline it, ignore it, or tell LinkedIn they do not know you, and that last option "
  "feeds a signal the platform acts on. It is why invitations are the most heavily rate limited "
  "action on the site, and why a queue of unanswered pending requests is itself a quality signal.</p>")
P("<p>A message to an accepted connection is a different object: the recipient opted in, the thread "
  "is private, and the platform has less reason to police it. Most teams have this inverted. Ration "
  "invitations hard, target them precisely, then be generous with follow up inside threads already "
  "open, which is how our "
  + a("https://www.devcommx.com/blogs/linkedin-outreach-templates-2026", "2026 LinkedIn outreach templates")
  + " are structured. High acceptance is self protecting: accepted invitations generate none of the "
  "signal restrictions are built on.</p>")
# H2 5
P("<h2>The Human in the Loop Model: Where a Person Has to Stay in an AI SDR LinkedIn Sequence</h2>")
P("<p><strong>Four checkpoints, in order.</strong> ICP approval, where a human signs off on the "
  "account list and trigger definitions. Message approval, where a rep reads every draft for the "
  "first few weeks, then samples once quality is proven. The send, performed by the account owner. "
  "Reply handling, where a person owns the thread the moment a prospect answers.</p>")
P("<p>The objection is that this does not scale. It scales further than expected, because the human "
  "minutes sit where outcomes are decided and the ceiling becomes the platform limit rather than the "
  "rep's attention. On a recent engagement this structure produced <strong>40+ qualified demos in ~6 "
  "weeks</strong> with no automated write action against any LinkedIn profile.</p>")
P("<p><strong>Build it so the agent cannot click.</strong> Give the system no LinkedIn credentials "
  "and no extension, and safety becomes structural rather than a policy someone overrides in month "
  "four. That is how we architect "
  + a("https://www.devcommx.com/ai-sdr", "the AI SDR systems we build") + ".</p>")

# H2 6
P("<h2>If an Account Gets Restricted: What Recovery Looks Like and How Long It Takes</h2>")
P("<p><strong>Restrictions come in tiers.</strong> Mildest is a feature limit, where invitations or "
  "search stop working while the account otherwise functions. Then an identity verification prompt, "
  "then a full account restriction, and at the top permanent removal. LinkedIn's "
  + a(RESTRICT, "account restrictions help page", True) +
  " describes the ladder and states that restrictions are temporary or permanent depending on the "
  "severity or repetition of the activity.</p>")
P("<p>Recovery steps are the same at every tier. Remove every extension from the browser immediately, "
  "including ones you think are unrelated, because a second detection during review makes the appeal "
  "unwinnable. Log in from the usual device. Complete any verification request. Appeal through the "
  "Help Center, say plainly what changed, then stop touching the account. LinkedIn publishes no "
  "appeal service level, so plan for a week or more off the channel.</p>")
P("<p><strong>Assume it may not come back.</strong> Terms of this kind hold up. The hiQ Labs "
  + a(HIQ, "Ninth Circuit scraping case", True) + " ended in a "
  + a(PW, "consent judgment against hiQ", True) +
  ", including a 500,000 dollar judgment and a permanent injunction, after the court found that "
  "scraping and the use of false profiles breached the User Agreement. The lesson for a revenue team: "
  "do not build a channel that depends on rules not being enforced.</p>")

# H2 7
P("<h2>How This Changes the Economics: A Burned Profile Versus the Saved Hours</h2>")
P("<p><strong>Price the downside first.</strong> A restricted profile does not cost you a seat "
  "licence. It costs the connections, the conversation history, the credibility of a real posting "
  "record, and every thread that was mid deal that day. None of it transfers. Against that, "
  "automating the click saves fifteen minutes of a rep's day.</p>")
P("<p>What moves the number is how much surrounding work disappears: research, list building, trigger "
  "monitoring, drafting, logging, scheduling. That is where an AI SDR earns its cost. The cost side "
  "is in our "
  + a("https://www.devcommx.com/blogs/ai-sdr-pricing", "AI SDR pricing breakdown") +
  " and the output side in our analysis of "
  + a("https://www.devcommx.com/blogs/ai-sdr-reply-rates-roi", "AI SDR reply rates and ROI") +
  ". Keep a one page channel policy naming which actions are automated, assisted and human. Most "
  "account losses are a trial nobody switched off.</p>")

# CTA
P("<h2>Build This With DevCommX</h2>")
P("<p>DevCommX builds autonomous, signal based AI SDR systems that your team owns, with research, "
  "scoring and drafting handled by the agent and every platform action left with the account owner. "
  "If you want a LinkedIn motion that produces pipeline without putting your reps' accounts at risk, "
  + a("https://www.devcommx.com/contact-us", "book a GTM strategy call") +
  " and we will map the automate, assist and human split to your team.</p>")

# Further reading
P("<h3>Further Reading</h3><ul>"
  f"<li>{a(UA, 'LinkedIn User Agreement, the section governing automated access', True)}</li>"
  f"<li>{a(PSE, 'LinkedIn Help, Prohibited software and extensions', True)}</li>"
  f"<li>{a(PCP, 'LinkedIn Professional Community Policies', True)}</li>"
  "</ul>")

# References
P("<h3>References</h3><ul>"
  f"<li>{a(UA, 'LinkedIn User Agreement, source for the ban on scripts, robots, crawlers and plug-ins used to scrape or send messages', True)}</li>"
  f"<li>{a(PSE, 'LinkedIn Help, Prohibited software and extensions, source for the ban on tools that automate activity on the site', True)}</li>"
  f"<li>{a(PCP, 'LinkedIn Professional Community Policies, source for the true identity requirement', True)}</li>"
  f"<li>{a(RESTRICT, 'LinkedIn Help, Account restrictions, source for the restriction tiers and enforcement', True)}</li>"
  f"<li>{a(ENFORCE, 'LinkedIn Help, How we enforce our Professional Community Policies, source for the enforcement approach', True)}</li>"
  f"<li>{a(HIQ, 'hiQ Labs, Inc. v. LinkedIn Corporation, Ninth Circuit 2022, the scraping litigation', True)}</li>"
  f"<li>{a(PW, 'Privacy World, LinkedIn and hiQ consent judgment, source for the 500,000 dollar judgment and injunction', True)}</li>"
  "</ul>")

# FAQ
P("<h3>FAQ</h3>")
for q, ans in FAQ:
    P(f"<h4>{q}</h4><p>{ans}</p>")

P("<div data-rt-embed-type='true'><script type=\"application/ld+json\">"
  + SCHEMA_STR + "</script></div>")

BODY = "".join(B)

words = len(html.unescape(re.sub(r"<[^>]+>", " ",
             re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", BODY, flags=re.S | re.I))).split())

item = {
  "collection_id": "689c92652a4b35f0e9a14fc2",
  "isDraft": True,
  "isArchived": False,
  "fieldData": {
    "name": NAME,
    "slug": SLUG,
    "meta-title": "AI SDR LinkedIn Safety: Limits, Risk and What Stays Human",
    "meta-description": DESC,
    "post-summary": ("A risk guide for running an AI SDR on LinkedIn in 2026: what LinkedIn's own "
                     "User Agreement and prohibited software policy actually say, the four patterns "
                     "that trigger a restriction, an action by action table of what to automate, "
                     "what to assist and what to keep human, why connection requests carry the risk "
                     "that messaging does not, and what recovery looks like if a profile is limited."),
    "post-body": BODY,
    "schema-markup": SCHEMA_STR,
    "date": "2026-09-15T00:00:00.000Z",
    "last-updated": "2026-09-15T00:00:00.000Z",
    "author-name": "Sumit Nautiyal",
    "author-title": "VP of Revenue Operations & GTM Engineering, DevCommX",
    "add-blog-reading-time": str(round(words / 220)),
    "blog-list": URL,
    "og-image": {
      "fileId": "69ce06f820d4562027a83191",
      "url": OG
    },
    "author": "677194290c472080e6cd6c06",
    "authors-collection": "69d8f4fd2475affd96f68115",
    "category": ["689c9183e68cf0a3029741d1"]
  }
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{SLUG}.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(item, f, ensure_ascii=False, indent=2)
print("words:", words, "->", out)
