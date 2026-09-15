# Data gaps: batch 4, topic 1 (ai-sdr-linkedin-account-safety)

Recorded 2026-09-15. Everything below is something the draft deliberately does NOT
assert, because it could not be sourced from a primary document in this environment.

## 1. LinkedIn's own pages could not be fetched directly
`www.linkedin.com` and `learn.microsoft.com` are both blocked by the network egress
proxy in this session. Three WebFetch attempts returned `EGRESS_BLOCKED`.

The User Agreement and Prohibited Software and Extensions wording quoted in the post
comes from search result text that quotes those pages, not from a direct read of them.
The URLs themselves are cited inline and in References and are the correct canonical
locations:

- https://www.linkedin.com/legal/user-agreement
- https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions
- https://www.linkedin.com/legal/professional-community-policies
- https://www.linkedin.com/help/linkedin/answer/a1340522 (Account restrictions)
- https://www.linkedin.com/help/linkedin/answer/a1342754 (How we enforce our policies)

**Action before publish:** a human should open the User Agreement and confirm the
prohibited conduct clause is still numbered 8.2 and still reads as paraphrased. The
draft deliberately paraphrases rather than presenting a verbatim block quote, and it
never claims a section number or an effective date.

## 2. No numeric weekly invitation limit is stated
Search results conflict badly: one set says 100 invitations per week across all tiers,
another says 100 free / 150 Premium / 250 Sales Navigator, another says the cap varies
by account age and SSI. LinkedIn does not publish a figure on a page that could be
verified here. The draft therefore treats invitation volume as "the platform limit"
without a number and links to
`linkedin-connection-request-limits-2026-safe-outreach`, per the brief.

## 3. No appeal or recovery SLA is claimed
Third-party sources give 24 to 48 hours for identity verification and 24 hours to two
weeks for an appeal. None of these trace to a LinkedIn-published service level. The
draft states only that LinkedIn publishes no appeal service level and advises planning
for a week or more off the channel, which is a planning recommendation and not a claim
about LinkedIn's queue.

## 4. No detection-mechanism claims
Secondary sources describe browser fingerprinting, velocity monitoring, message
similarity clustering and IP anomaly detection as LinkedIn's detection stack. LinkedIn
does not publish this. The draft describes the four patterns as observable risk
patterns from practitioner experience, not as LinkedIn's confirmed detection methods.

## 5. No restriction-rate or ban-rate statistic
No defensible figure exists for what share of LinkedIn restrictions are caused by
automation tooling, or what percentage of automation users are restricted. Nothing of
that shape appears in the draft.

## 6. DevCommX performance claim
Only the permitted claim is used: "40+ qualified demos in ~6 weeks", once, in the
human-in-the-loop section. No other client result, conversion rate or cost figure is
asserted.

## 7. hiQ figures
The 500,000 dollar judgment and permanent injunction are sourced to the Privacy World
write-up of the December 2022 consent judgment, cited inline. The Ninth Circuit opinion
is linked via Justia. Neither was fetched directly; both came back consistently across
search results.
