# Ad-hoc post · Sumit Nautiyal · Microsoft 365 outage · 13 Nov 2026

Requested by Amritpal: a post on today's Microsoft outage, for Sumit (continuing from his last request). Not part of the scheduled run.

**Slot:** newsjack, so post **today, Fri 13 Nov, 19:30 IST** (09:00 ET), as an exception to his Mon-Thu schedule. The story is under 30 hours old; by Monday it's stale. His Monday (HBR) and Tuesday (Morningscore) posts stay where they are.
**Pillar:** release-week takes / the realist take · **Archetype:** newsjacker, leader lens · **Rung:** 1 (live incident, Nov 12-13)

## Research brief
- **What happened:** connectivity problems with Microsoft 365 began shortly before 1 p.m. ET on Thursday, Nov 12, and carried into Friday. Outlook and Teams were hit, along with SharePoint and Copilot.
- **Scale:** nearly 150,000 reports of Outlook problems across the US and Canada (outage-tracker counts, via coverage). Banks, governments and courts in several countries, and hospitals across Canada, reported disruption.
- **Microsoft's explanation so far:** "a process on the affected servers responsible for establishing secure connections becomes overwhelmed"; "the increased load is not caused by a rise in traffic, but by a large number of servers being unexpectedly unavailable, which shifts the load to the rest of the infrastructure"; restored servers "can become unresponsive again once they begin receiving traffic". It is reverting "a recent network configuration change that correlates with the start of impact". Charles Lamanna, an EVP at Microsoft, said there's no indication of malicious activity.
- **Not known yet:** the confirmed root cause; Microsoft has said a post-incident report will follow. Status was improving but not fully fixed as of Friday morning.
- **Sources:** [CNN live](https://www.cnn.com/2026/11/12/business/live-news/microsoft-global-outage-intl-hnk) · [CNBC](https://www.cnbc.com/2026/11/12/microsoft-outage-outlook-aws-google.html) · [ABC7 live updates](https://abc7.com/live-updates/microsoft-outage-live-updates-what-know-outlook-365-other-apps-remain-down/20036817/) · [SecurityWeek](https://www.securityweek.com/microsoft-365-outage-disrupts-outlook-exchange-online-and-teams/) · [TechRadar live](https://www.techradar.com/news/live/outlook-outage-nov-2026) (via search summaries)
- **Why it matters to the reader:** for many revenue teams, email, meetings and documents run on one vendor. A day like Thursday tests whether live deals have a plan B.
- **Angle:** outages happen; what matters is hour one. Write the GTM outage plan now, and wait for the root cause before anyone pitches a migration.

## Strategy
- **Format:** text (a newsjack, out fast).
- **Hook options (from the Scripe sheet, pulled 10 Nov, GTM):** 1) "One vendor outage shouldn't stop your whole pipeline." · pattern: Bold one-liner (sheet #6, 3,010 eng.) 2) "Microsoft went down for hours. Did your pipeline?" · pattern: Case study question (#34), rejected: he uses that pattern on Tuesday 3) "Most sales teams don't have an outage plan." · pattern: Warning (#13), rejected: "most" is unsourced → **picked 1**: eight words, a leader's rule, and the body cashes it with the outage facts.
- **Pattern log:** Bold one-liner (sheet #6, 3,010 eng., proven).
- **Ask:** sharp-question

## Post
<!-- post:sumit format:text ask:sharp-question type:news -->
One vendor outage shouldn't stop your whole pipeline.

On Thursday, Microsoft 365 had a major outage. Outlook, Teams, SharePoint and Copilot ran into problems from shortly before 1 p.m. ET, and it carried into Friday.

Outage trackers logged nearly 150,000 Outlook problem reports across the US and Canada. Banks, governments, courts and hospitals reported disruption.

Microsoft's explanation so far: a large number of servers went unexpectedly unavailable, the load shifted to the rest, and the process that sets up secure connections got overwhelmed.

It's reverting a recent network configuration change that lines up with the start. Microsoft says there's no sign of malicious activity.

Here's the leader read.

For a lot of revenue teams, that's email, meetings and documents gone at once. Sequences stop sending. Demos lose their meeting room. Proposals sit in SharePoint.

Outages happen to every provider. What matters is what your team does in hour one.

Three things I'd write down this week:

1. A backup channel for live deals. Phone numbers and a second meeting link for every late-stage opportunity, stored outside the inbox.
2. One owner who pauses sequences until email is back, so nobody has to clean up afterwards.
3. A short note to every customer with a meeting that day, sent from whatever still works.

Here's the honest part: Microsoft hasn't published a final root cause yet. Read the post-incident report before anyone pitches you a migration.

Automate the typing. Never automate the judgment.

Resilience is a GTM decision, too.

What did your team do in the first hour?
<!-- /post -->

## Creative
**Image card (made 13 Nov, on request):** `creatives/2026-11-13-sumit-microsoft-outage.png` (1080x1350, for upload) and `...@2x.png` (2160x2700, sharper). Source: `...-microsoft-outage.html`.

- **Style:** the warm illustrated look chosen for Sumit's Fable 5.2 animation (cream, terracotta, teal panel), not the dark DevCommX surface.
- **What it shows:** headline "One vendor outage shouldn't stop your whole pipeline." A teal status board, "What went down": Outlook, Teams, SharePoint and Copilot marked Disrupted, "from ~1 PM ET Thu · into Fri", and "~150,000 Outlook problem reports across the US and Canada, per outage trackers", with a small scene of a rep on the phone next to an offline laptop. A cream card, "The hour-one plan", with the post's three steps. Footer: Sumit's initials (headshot to drop in), the pill "Resilience is a GTM decision, too." and the source line.
- **Claims on the card:** service names and the ~150,000 figure only, both from news coverage; no Microsoft logos or marks.

## First comment
<!-- comment:sumit -->
Coverage with Microsoft's status updates: https://abc7.com/live-updates/microsoft-outage-live-updates-what-know-outlook-365-other-apps-remain-down/20036817/

For the official record, the Microsoft 365 Service Health page in your admin centre has the incident and, later, the post-incident report.
<!-- /comment -->

## Before publish
- **Check right before posting:** whether service is fully restored. If it is, change "it carried into Friday" to give the end time, and keep the rest.
- **Verify:** the "nearly 150,000" Outlook reports figure and which tracker it came from, Microsoft's quoted explanation, the network configuration change, and Charles Lamanna's "no indication of malicious activity". All seen via search summaries of news coverage; the live pages weren't opened.
- **Check:** if Microsoft has published a root cause by posting time, replace the "honest part" line with what it says.
- **Note:** no first-person claim about DevCommX's own experience of the outage. If your team was hit, a line on what you did in hour one would make it stronger. That's a [NEEDS:] only if you want it.
- First hour: Sumit online 19:30-20:30 IST, 3 teammates comment by 20:30.

## Gate
`PASS · 1,599 chars · 0 errors · 0 warnings · no six-word overlap with the Scripe sheet`
