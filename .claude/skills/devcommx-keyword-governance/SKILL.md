---
name: devcommx-keyword-governance
version: 1.0.0
description: |
  The DevCommX keyword filter. Apply BEFORE writing any DevCommX content brief,
  blog post, service page, landing page or pSEO template, and whenever a keyword,
  topic or "we should rank for X" idea is proposed for DevCommX.
  Classifies every keyword with the 3-question rule (service page / supporting blog /
  do not build), and holds the standing exclusion list of terms DevCommX has
  deliberately walked away from, each with its recorded reason.
  Use when the user says "keyword", "should we target", "content brief", "what should
  we rank for", "SEO topic", "new page for", "keyword research", or proposes any term
  for the DevCommX site. Also use to answer a request to target an excluded term —
  reply with the recorded reason rather than re-arguing it.
license: MIT
---

# DevCommX Keyword Governance

Source: **DevCommX Keyword Strategy v1.0, 3 August 2026** — sections 4 (The Operating
Rule) and 9–10 (The Exclusion List).

This is the filter every content brief has to pass **before a single word is written**.

---

## The 3-question rule

Ask these in order. The first "yes" decides the format.

| # | Question | If yes → build | Never |
|---|---|---|---|
| 1 | **Would this searcher hire someone this month?** | **Service page.** Top-level URL, in the navigation, form on the page itself. | Never a blog post. |
| 2 | **Are they learning or comparing before they hire?** | **Blog post** whose only job is to pass authority and traffic into the matching service page. | Never a standalone post with no money-page link. |
| 3 | **Would an AI answer end their search?** | **Do not build it at all.** | The impression lands, the click does not. |

**The failure mode this exists to stop:** almost everything DevCommX has was built as
answer 2 — 144 blog posts and one generic contact form. New work must skew to answer 1.

### Which query shapes survive the click

| Query shape | Example | Click survives? |
|---|---|---|
| Vendor selection | `gtm agency`, `saas lead generation agency` | **Yes** — a summary cannot pick a supplier |
| Cost and pricing | `ai sdr pricing`, `gtm services cost` | **Yes** — no engine can quote our price |
| Agency comparison | `belkins alternatives`, `belkins vs martal` | **Yes** — the buyer is mid-purchase |
| Definitions | `what is gtm engineering` | No — answered in the results page |
| Statistics / how-to | `ai sdr statistics`, `how to become a gtm engineer` | No — extracted and summarised |
| Tool comparison | `clay vs apollo` | No — and the buyer wants software anyway |

---

## The exclusion list

Full term-by-term list with reasons: **[references/exclusion-list.md](references/exclusion-list.md)**

Cut by category:

| Category | Count | The reason, once |
|---|---|---|
| Job seekers | 3 | `gtm engineer` (1,600/mo) is the biggest term and a trap — 1,723 impressions produced **9 clicks**. Candidates, not buyers. |
| Tool queries | 19 | DevCommX sells a service. `clay vs apollo` produced **27 clicks from 25,824 impressions**. |
| Wrong buyer / ICP | 7 | `salesforce crm tool` carries 27,100 searches and DevCommX does not sell a CRM. Volume without relevance is a cost. |
| Informational | 10 | Answered inside the results page by AI Overviews. |
| Junk intent | 3 | `ai agents for sale` — people buying and selling agents, not hiring a GTM firm. |
| Generic SEO | 3 | Difficulty 48–66 and the wrong business. DevCommX sells AI search, not SEO retainers. |
| Head terms | 3 | `generative engine optimization` at difficulty 75, informational. Take the `agency` and `services` variants instead. |
| Wrong service | 3 clusters | Google Ads (~11,000), publicity stunts (~9,000), AI chat (9,900). Services DevCommX does not sell. |
| Bulk noise | 2 blocks | 157 `[tool] pricing` keywords (ColdIQ earns ~96 visits/mo from all of them combined); ~600 zero-volume GEO/AEO long-tails. |

### The trade being made, stated plainly

The six largest excluded terms carry **42,880 searches a month** — roughly 36× the entire
Tier A list. DevCommX is choosing **1,170 searches over 42,880** because the smaller
number is made of buyers.

> **Traffic is not the product. Booked meetings are.**

### The most tempting mistake

`ai agents for sale` has a difficulty score of **2** — the lowest number in the entire
dataset. It is still a cut. The intent is people buying and selling AI agents, not
companies hiring a go-to-market firm.

> **A low difficulty score is not a reason to build.**

### Leave alone, do not extend

`gtm engineer salary` and `how to become a gtm engineer` carry 12,436 impressions and
produce no pipeline. Leave the existing pages as they are. Build no more like them.

---

## Protected terms — never retarget these

| Term | Owned by | Why it is protected |
|---|---|---|
| `gtm engineering agency` | `/blogs/best-gtm-engineering-agencies` | Position 2.9, **10.67% CTR — the highest on the site.** Never change that URL. New and edited pages take adjacent terms only. |
| `claude sdr` | existing cluster | Position 3.8, **5.56% CTR.** A niche DevCommX already owns — expand it, do not fragment it. |

---

## How to answer a request to target an excluded term

Do **not** re-argue it. Reply with the recorded reason:

> "`<term>` is on the standing exclusion list, cut as **<category>** because
> **<reason>**. It was excluded on a named reason, not on volume. If the reason has
> changed — for example the domain rating has passed 40 for `b2b marketing company` —
> say so explicitly and we can revisit that one term."

The only legitimate way back onto the list is a **changed reason**, stated explicitly.

---

## Applying this to a content brief

Every DevCommX content brief must open with a classification block:

```
KEYWORD:        <term>
VOLUME / KD:    <n>/mo · KD <n>
3-QUESTION:     Q1 hire-now / Q2 learning / Q3 AI-answered
FORMAT:         service page | supporting blog | DO NOT BUILD
MONEY PAGE:     <the page this must link into>   ← required for supporting blogs
EXCLUSION CHK:  clear | EXCLUDED (<category>: <reason>)
PROTECTED CHK:  clear | conflicts with <protected term>
```

A brief without this block is not ready to write.
