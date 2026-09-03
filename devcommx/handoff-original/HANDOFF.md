# DevCommX Blog Operations — Complete Session Handoff

Purpose: hand this end-to-end DevCommX blog operation to a fresh Claude session (on any account) so it can continue without re-deriving anything. Read this first, then `SKILLS_USED.md`, then `BLOG_INVENTORY.md`.

---

## 1. What this operation is

Run DevCommX's SEO/AEO/GEO blog program in **Webflow CMS**: take keyword/topic sheets → draft long-form blogs to a strict spec → validate them (6-dimension rubric → Excel workbook) → create them in Webflow as drafts → fix/interlink → compile review docs.

**DevCommX** = B2B agency building autonomous, signal-based **AI SDR / GTM-engineering** systems (outbound, RevOps, Clay, cold email, LLMO/AEO). Clients **own the infrastructure**. Sanctioned proof framing: **"40+ qualified demos in ~6 weeks."** Author on every blog: **Sumit Nautiyal, VP of Revenue Operations & GTM Engineering.**

This session produced **53 blog drafts** (see `BLOG_INVENTORY.md`), 4 validation workbooks, ~15 review docs, 6 embedded brand SVG figures, and fixed a site-wide broken-CTA defect.

---

## 2. Webflow CMS — critical facts (memorize)

- **Collection ID:** `689c92652a4b35f0e9a14fc2` (the Blog collection).
- **Category ref:** `689c9183e68cf0a3029741d1` · **Author ref:** `677194290c472080e6cd6c06` · **Authors-collection ref:** `69d8f4fd2475affd96f68115`.
- **Default OG image** (also `image`/`og-image`): fileId `69ce06f820d4562027a83191`, url `https://cdn.prod.website-files.com/677194290c472080e6cd6ab0/69ce06f820d4562027a83191_imresizer-DevCommX-Blog-OG.png`.
- **URL pattern:** `https://www.devcommx.com/blogs/{slug}`.
- **CTA URL is `/contact-us`** — `https://www.devcommx.com/contact` is a **hard 404**. (`/book` 301s to `/contact-us`.)
- **Live service/hub pages** vendor-selection posts should link: `/ai-sdr`, `/revenue-operations`, `/gtm-engineering` (all 200).
- The Webflow MCP tool is `data_cms_tool` (server prefix `mcp__2b3254d1-c8d2-4f01-a504-59abe3eca6a6__`). Actions used: `list_collection_items`, `create_collection_items`, `update_collection_items`, `publish_collection_items`, `get_collection_details`. **On another account this MCP connector must be authorized first** (via claude.ai connector settings).
- The collection had **221 items** at end of session (3 pages of 100). Full enumeration needs offsets 0/100/200.

### The exact CMS item field schema (fieldData)
Every draft JSON on disk has this shape (see any file in `blogs/*/`):
```
collection_id, isDraft, isArchived, fieldData: {
  name, slug, meta-title, meta-description, post-summary, post-body (HTML),
  schema-markup (JSON string, @graph BlogPosting+FAQPage), date, last-updated,
  author-name:"Sumit Nautiyal", author-title, add-blog-reading-time, blog-list,
  og-image:{fileId,url}, author, authors-collection, category:[ref]
}
```

---

## 3. The blog spec (source of truth: `specs/_DRAFT_SPEC.md`)

Each blog: **2,300–2,800 words** (pillars 2,600–3,200). Required structure:
1. **Extractable answer paragraph** first (40–70 words, AEO) — directly answers the keyword.
2. Intro `<p>` with one internal link.
3. 5–8 `<h2>` sections.
4. **ONE comparison table** as a Webflow embed: `<div data-rt-embed-type='true'>…<table>…</table></div>` — every `<th>` MUST include `color:#1f2937` (fixes white-on-grey).
5. **CTA** to `/contact-us` (sales or AEO variant); vendor-selection posts also link a service page.
6. **Further Reading** — `<h3>` + 3 external links (`target="_blank" rel="noopener noreferrer"`).
7. **References** — `<h3>References</h3>` `<ul>` listing EVERY external source (added mid-session per client request; min 3–6).
8. **FAQ** — `<h3>FAQ</h3>` + 5–6 `<h4>` Q + `<p>` A, mirrored **exactly** into the FAQPage schema.

**Keyword + AEO + GEO (required):** primary keyword in H1/name, meta-title, first 100 words, ≥2 H2s, one FAQ question, and the slug; extractable answer; named/attributable sources inline (GEO); DevCommX stated as the entity for the topic.

**Hard rules:** valid JSON; **no em/en dashes anywhere** (use commas/colons/periods); FAQ body == FAQ schema; schema-markup must end `... ] } ] }`; author = Sumit Nautiyal in both `author-name` and schema `author`; dates `2026-07-01`; reading-time = round(words/220); **anchors use plain double quotes** (never `\"`).

---

## 4. The proven pipeline (repeat this per batch)

1. **Read the sheet** (Google Sheet via Drive MCP `read_file_content`). Apply the sheet's own tier/skip/consolidation verdicts — they are authoritative.
2. **Dedup** every candidate against existing slugs (`data/_existing_slugs.txt` + everything already built) AND against the live site. Never draft a duplicate; differentiate + cross-link overlaps.
3. **Curl-verify every internal-link target returns 200** before drafting (the CMS slug list includes unpublished drafts → live 404s). Build a verified-live link menu; only those go in the drafts.
4. **Draft in parallel** via the Workflow tool (fan-out, one agent per blog, general-purpose type). Each agent reads `_DRAFT_SPEC.md`, researches with WebSearch, writes `fieldData` JSON to disk, self-validates. Resilient pattern: **write file first**, create in Webflow later.
5. **Validate independently** in the main thread (don't trust agent self-reports) — parse JSON+schema, check word count, FAQ-mirror, table header color, References present, no dashes, no `\"`, ≥3 live internal links, `/contact-us` CTA.
6. **Create in Webflow STRICTLY SEQUENTIALLY** (one at a time) — see the concurrency bug below. Verify each returned slug has no random `-suffix`.
7. **Re-enumerate** the collection to confirm clean singletons (no dupes).
8. **Compile** a review doc (standalone HTML + `.docx` via pandoc) and, on request, a validation workbook.

Publishing is **draft-only** unless the user explicitly says publish. An update only *stages* a change on a live item — it needs `publish_collection_items` to go public.

---

## 5. Validation (source: `specs/_VALIDATION_SPEC.md`, skill: content-validator)

6 dimensions, 5 criteria each, scored 0–5, weighted: Content 18% · SEO 18% · GEO-AEO 20% · Brand 15% · Structure 14% · Schema 15%. Verdict ≥3.9 PUBLISH / ≥2.75 REVISE / else HOLD.

**Process:** agents write findings JSON to `validation/{slug}.json`; **the main thread computes the weighted score and builds the .xlsx** (subagents can't run openpyxl reliably; and the agents mislabel verdicts — always recompute from raw criteria). Workbook = Exec Summary + one tab per blog. `excel_helpers.py` returns style objects (assign them: `c.fill=fill(x)`). Note: the skill template imports light-shade colors (`C_LTGREEN` etc.) that DON'T exist in this helper lib — define them locally.

**Session validation results:** 25 long-tail (mean 3.73), 10 recent (4.29), 2 rest (4.06), 16 traffic (4.26). The one **cross-cutting gap in every batch: Visual Elements ≈ 2/5** (no in-body images — needs design assets). Second: inline stat attribution.

---

## 6. Known gotchas (learned the hard way — see `learned-rules/`)

- **CMS concurrency bug:** `data_cms_tool` is NOT concurrency-safe. Parallel `create` calls **double-create** (2nd copy gets a random `-xxxxx` slug) and **cross-wire responses**. → Always create/update **sequentially**, then re-enumerate + dedupe. (Full note: `learned-rules/feedback_webflow_cms_concurrency_bug.md`.)
- **Internal-link liveness:** the slug inventory includes unpublished drafts → curl-check every internal target for 200 before using. External `curl` 403s are usually anti-bot (Gartner, Apollo KB, SEC, DOL, Perplexity) — verify in a browser before "fixing" a working link. (`learned-rules/feedback_internal_link_liveness.md`.)
- **`/contact` is 404:** always `/contact-us`. (A mid-session fix corrected this across 31 already-created blogs.)
- **Anchor-quote bug:** agents sometimes emit `href=\"…\"` (literal backslash) → broken HTML. Assert no `\"` in post-body before creating.
- **Em/en dashes** slip into References lists ("Source — supports X"). Check the WHOLE fieldData, not just prose.
- **Webflow embed limit** ~10,000 chars per `data-rt-embed-type` block — keep inline SVG figures lean (<9KB). Inline SVG DOES render inside a Webflow HTML embed (same mechanism as the tables) — no asset upload needed.
- **Shell-quoting traps:** validate with a **quoted heredoc** (`<<'PY'`) or a script file, never an unquoted heredoc or inline `python3 -c` with `\"` — the shell mangles it and produces false positives/negatives.
- **Connection-drop on create:** if a create fails mid-response, DO NOT blindly retry — enumerate first to see if it landed (avoids duplicates).
- **Runtime cap:** a 31-agent workflow (~2M subagent tokens) tripped an org "Claude subscription access disabled" cap mid-run. Keep batches ≤~13 agents; a lighter re-run cleared it.

---

## 7. What was done this session (chronology)

1. Confirmed the Webflow connector, pushed queued Batch-9 blogs (earlier context).
2. **Batch 1 (13 long-tail)** + **Batch 2 (12 long-tail)** drafted, validated, created. Fixed 7 racing-bug duplicates.
3. **25-blog validation workbook.**
4. Fixed **11 dead internal links** across 9 live posts (unpublished-draft targets).
5. Fixed **3 Slack-flagged existing-blog issues** (cold-email cannibalization interlinks, `b2b-outbound-tool-stack` title/keyword alignment, deliverability-guide 2026 refresh).
6. **Batch 10 (4 pillars)** — Agentic GTM, AI Outbound stack, ABM+GTM Eng, Clay adaptation.
7. **Commercial (2)** — Closed-Lost re-engagement, PLG Outbound.
8. **Tier-1 vendor-selection (4)** — AI SDR Services, RevOps Agency vs In-House, Choose RevOps Firm, GTM Engineer vs Agency.
9. **Rest (2)** — RevOps Consulting pillar, AEO vs GEO.
10. **Discovered + fixed the `/contact` 404** on all 31 earlier blogs; republished the live ones.
11. Generated + embedded **6 on-brand SVG figures** into the recent 6 drafts (brand skill).
12. **Traffic sheet: 16 blogs** (Sales-Ops hub of 6 + 3 Tier-1 + 7 Tier-2) with the new References section requirement.
13. Validation workbooks for the 10, the 2, and the 16.

---

## 8. Open items / next steps

- **Visual Elements gap** (every batch ≈2/5): add in-body figures. I embedded SVGs into 6 posts; the pattern (`figures/` + `build_svgs.py` approach) can extend to the rest. Real screenshots (HubSpot/Clay/dashboards) must be captured by the client — see `specs/_VISUALS_SPEC_recent6.md`.
- **Publish decisions** are the user's. The 16 traffic + 2 rest are drafts; the Sales-Ops hub should be **published as a set** so its inter-hub links resolve.
- Inline stat attribution pass (move key stats from References to inline citations) would lift Content Quality across the board.
- Remaining un-drafted topics exist on earlier sheets (long-tail candidates in `data/_longtail_candidates.json`; master lists in the prior Google Docs/Sheets).
- **Blocked:** Ahrefs connector (plan-locked / needs auth) → volume/KD is directional; the SEO team keeps publishing drafts so publish-state drifts.

---

## 9. How to continue on another account

1. Authorize the **Webflow MCP connector** for that account (claude.ai connector settings) — nothing here works without it.
2. Load `SKILLS_USED.md` and install/enable the skills listed (the DevCommX brand skill is included in `skills/devcommx-brand/`; content-validator is a plugin skill — its rubric is captured in `specs/_VALIDATION_SPEC.md` and helper in `skills/content-validator/`).
3. Drop the blog JSONs in a working dir; they are ready to `create_collection_items` (isDraft:true) as-is.
4. Re-enumerate the collection (`689c92652a4b35f0e9a14fc2`) to get current slugs + publish state before drafting anything new (dedup).
5. Follow the pipeline in §4 and the gotchas in §6.

Everything referenced here is inside this zip.
