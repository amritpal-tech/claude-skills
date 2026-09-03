# The 360Brew Algorithm — Ground Truth for Profile Optimisation

Source: *DevCommX — The Master LinkedIn Strategy v1.0*. This file explains *why* the profile recommendations exist, so rewrites are reasoned, not cargo-culted.

## What 360Brew is

LinkedIn's decoder-only foundation model (~150B parameters, derived from the LLaMA-3 family) that replaced the old patchwork of metadata-driven ranking systems. **One model now powers 30+ tasks** — feed ranking, job and connection suggestions, ad targeting — by reading content and context **as language** rather than counting tags and clicks.

It feeds roughly **2–3 months of a user's activity** into the model as context and reasons, in plain language, about whether a given post is relevant to *that specific person*. Because it understands meaning, it can rank brand-new posts and cold-start profiles it has never seen — it does **not** need historical engagement to judge relevance.

**Consequence for profiles:** you can no longer game ranking with formatting tricks, hashtag stuffing, or keyword spam. The model reads the profile as prose and judges whether the person *credibly* knows what they post about. Reach is earned by being genuinely, legibly relevant.

## The three signals that decide reach

| Signal | What it measures | Profile implication |
|---|---|---|
| **Golden Hour** (first 60 min) | Quality of engagement while LinkedIn tests the post on 2–5% of the network | A strong profile lifts profile-visit→follow conversion during the test, compounding the post's audition. |
| **Dwell time** | How long people actually stop, read, and stay | The single strongest quality proxy in 2026. The About section and Featured must reward the click with depth, or the visit bounces. |
| **Authenticity / expertise match** | Whether the profile, post, and comments read as genuine, consistent expertise | **This is the profile's primary job.** 360Brew literally reads the profile and asks: *does this person credibly know this?* Mismatch = suppression. |

**The dwell number to remember:** posts with 0–3 seconds of dwell land around **1.2% engagement**; posts that hold readers **61+ seconds hit ~15.6% — a 13× difference.** Depth is the mechanism of reach, not a nice-to-have. The same logic applies to the profile: a profile that holds a visitor (clear pain → mechanism → proof) converts; one that doesn't, bounces.

## The engagement hierarchy (what actions are worth)

| Action | Relative weight |
|---|---|
| **Save** | Strongest signal — ~5× a like, ~2× a comment |
| **Share with thoughts** | Top endorsement signal |
| **Substantive comment (3+ sentences)** | ~2× a like; long comments far outweigh reactions |
| **Like / reaction** | Lowest-value signal — never optimise for it |
| **Poll vote** | Reach trap: ~1.78× reach but only ~0.37× engagement |

Profile relevance: the **Featured** section should host genuinely save-worthy assets (frameworks, checklists, case studies), because saves are the strongest reach signal and a save-worthy Featured item is what turns a profile visit into a durable follow.

## Why the profile is a ranking input AND a landing page

- **As a ranking input:** 360Brew reads the profile to score the *expertise match* signal. A headline, About, Experience, and Skills that are **keyword-consistent with what the person posts** tell the model "this person is the [X] authority for [ICP]." Incoherence (profile says one thing, posts say another) reads as a mismatch and **lowers trust**.
- **As a landing page:** every post drives profile visits. The profile is the conversion page. First 3 lines of About carry the click; the rest is behind "…see more." Banner is the above-the-fold pitch. Featured is proof + lead capture.

**The coherence rule:** a profile-to-content match is *itself* a ranking advantage. The headline becomes the template for every post hook, and that repetition is how the person becomes "the [X] person" in both the reader's mind and 360Brew's model of them.

## The profile-as-landing-page checklist

| Element | Job | Standard |
|---|---|---|
| Headline | Hook + positioning (humans + 360Brew) | Outcome + ICP + Mechanism; becomes the post-hook template |
| Profile photo | Trust in 0.5s | Clear, warm, high-res, recognisable face |
| Banner | Above-the-fold pitch | One line: who you help + the result + soft CTA |
| About | Conversion copy | Reader's pain → mechanism → proof → CTA; first 3 lines carry the click |
| Featured | Proof + lead capture | Best post, lead magnet, case study, booking link |
| Experience / Skills | Expertise signal | Keyword-consistent with post topics |

## The humanizer layer (why people stay and trust)

360Brew now actively rewards authentic, first-person voice and demotes sterile, AI-flavoured corporate content. The About section should read like the person talking, not a brochure:
- **First-person stakes** — what they tried, what failed, what it cost.
- **A point of view** — the thing they actually believe, even if spiky.
- **Plain, spoken language** — how they'd explain it to a founder over coffee.
- **A small, true detail** — the specific that proves a human lived it.

## The one-line thesis

> Win the first 60 minutes with relevant people, earn dwell time with depth, and let 360Brew read your profile-to-post match as a clean signal of expertise. The profile's role: be the coherent, high-dwell, conversion-ready landing page that makes that match obvious.
