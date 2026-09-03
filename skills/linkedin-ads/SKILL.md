---
name: linkedin-ads
description: Plan and create LinkedIn lead generation ads by analysing your ICP, researching competitor ads in the LinkedIn Ad Library, and producing ad copy, campaign strategy, and creative briefs. Use when the user wants to create LinkedIn ads, research what competitors are running on LinkedIn, plan a LinkedIn campaign, or improve LinkedIn advertising performance.
---

# LinkedIn Ads Planner

## Quick start

Invoke this skill, then provide:
1. Your ICP file path (first time only — stored in memory as `linkedin_ads_icp_path` for future runs)
2. Competitor company names or LinkedIn page URLs
3. The offer or product being advertised this session

---

## Phase 1 — Load ICP & context

- [ ] Check memory for `linkedin_ads_icp_path`; if not found, ask user to share the file path
- [ ] Read the ICP file and extract:
  - Target job titles & seniority levels
  - Target industries & company sizes
  - Key pain points (top 3)
  - Desired outcomes / transformation
  - Objections to overcome
- [ ] Confirm the offer being promoted (product, service, lead magnet, demo, etc.)

---

## Phase 2 — Competitor research

For each competitor provided:
- [ ] Search LinkedIn Ad Library: `site:linkedin.com/ad-library "[company name]"`
- [ ] Web search: `"[company name]" LinkedIn ads examples 2024 2025`
- [ ] Note for each: hook style, pain points addressed, offer structure, CTA used, ad format (image/carousel/video), tone (formal/casual/urgent)
- [ ] Identify 3–5 cross-competitor patterns ("what's working in this space")
- [ ] Identify whitespace angles competitors are NOT covering

---

## Phase 3 — Strategy

Based on ICP + competitive intel, define:

| Field | Recommendation |
|---|---|
| Objective | Lead Generation |
| Ad formats | Single Image + one Carousel variant |
| Audience targeting | Job titles, seniority, industries, company size |
| Audience size target | 50k–300k (sweet spot for LinkedIn CPL) |
| Daily budget | Recommend range based on audience size |
| Campaign duration | Minimum 2 weeks per test |
| Bid strategy | Maximum Delivery for first 2 weeks |

Messaging angles: propose 3 differentiated angles, ranked by gap vs. competitors.

---

## Phase 4 — Deliverables

Produce all three for each messaging angle:

### Ad Copy
```
Headline: (≤150 chars — hook first, outcome-focused)
Intro text: (2–3 lines — pain → credibility → CTA)
CTA button: [Book a Demo / Download / Get Started / Learn More]
```

### Creative Brief (per angle)
- Visual direction: tone, imagery style, colour mood
- Key message to show on the creative
- What to avoid (angles already saturated by competitors)

### Campaign Setup Checklist
- [ ] Create Lead Gen Form with 3 fields max (Name, Email, Company)
- [ ] Set up conversion tracking via LinkedIn Insight Tag
- [ ] Build 2 audiences: primary ICP + lookalike from existing leads
- [ ] Schedule A/B test: run 2 angles simultaneously, pause lower CTR after 7 days

---

## Notes

- Always lead with the pain point, not the product feature — B2B LinkedIn converts on outcomes
- LinkedIn Ad Library URL pattern: `linkedin.com/ad-library/detail/[ad-id]`
- If the ICP file path changes, ask the user for the new path and update memory
