# Daily research playbook

The job: find, for each profile, **one fresh, verifiable, educational update** that its
reader would want explained today, and the angle only that profile would take on it.

## The freshness ladder

Work down the ladder only when the rung above produces nothing that scores 10+ (scoring
below). Write the rung used into the brief.

1. **Fresh primary-source update**: published inside the research window
   (`daily_context.py`: 48h, 72h on Monday). Official blog, changelog, docs, release notes.
2. **Fresh secondary report** of a real change, inside the window, where the primary
   source exists and you have opened it.
3. **Recent update not yet covered by us**, up to 14 days old, primary source opened.
   Label its age honestly ("last week", "two weeks ago").
4. **New data or study**, up to 14 days old (a benchmark, a citation study, a survey).
5. **AI tool of the week**: a tool launch or major feature in the lane, curated with the
   honest limit.
6. **Evergreen educational post** anchored on the most recent relevant item. Label it
   `type:evergreen` in the brief. Never pass an old story off as news.

## Verification protocol (non-negotiable)

For every candidate you might use:

1. **Open the page** (WebFetch). A search snippet is not a source.
2. **Confirm the date** on the page itself. If there is no date, find one elsewhere or
   drop the candidate.
3. **Find the primary source.** Trade press reporting a Google change → open Google's own
   post or docs. If no primary exists, write "reported by X" in the post.
4. **Extract facts verbatim**: what changed, for whom, when, numbers, regions, plans.
   Note anything the source does *not* say (rollout timing, pricing) so the post does not
   say it either.
5. **Record**: title, publisher, URL, publish date, the 2-4 facts the post will use.

If the search tools return thin or stale results, say so in the brief. A short brief with
one real story beats three stories half-verified.

## Search tactics that work (learned on the first run, 2026-11-04)

- **Standard WebSearch lags on news under a week old.** Queries like "Google search update
  November 2026" returned only 2025 coverage. Use `mode: "extended"` for the lane sweep
  ("SEO and AI search news this week: ..."), then a targeted extended search per lead.
- **Go to primary sources directly.** GitHub release pages
  (`github.com/<org>/<repo>/releases`, `/releases/tag/<tag>`, `BREAKING-CHANGES.md`) and
  vendor newsrooms (`anthropic.com/news`) list exact dates and verbatim feature lines.
- **The cloud environment's network policy may block WebFetch for some hosts**
  (seen: seroundtable.com, searchengineland.com, status.search.google.com,
  developers.hubspot.com). WebSearch still reaches them server-side. When a host is
  blocked: stop trying more hosts that fail the same way, take the facts from an extended
  search summary of that exact article, and add a "Verify: open <url> and confirm <fact>"
  line to the post's before-publish list. Note the blocked hosts in the brief header.
- **Two sources disagreeing on a number** (e.g. AI Overview coverage 43% vs 80%+) means
  neither goes in the post without the method next to it. Prefer the one with a dated
  method from a named research team.

## Lane source maps

Search the named sources first, then the query bank. Swap `{month} {year}` for today's.

### Amrit Pal Singh · marketing / SEO / AEO

**Primary sources**
- Google Search Central blog: developers.google.com/search/blog
- Google Search Status Dashboard (core, spam, other ranking updates): status.search.google.com
- Google product blog, Search section (AI Mode, AI Overviews): blog.google/products/search
- Google Ads & Commerce blog / Ads product updates (AI Max, PMax, Demand Gen)
- OpenAI news and ChatGPT release notes (search, shopping, ads, memory, apps): openai.com/news, help.openai.com release notes
- Perplexity blog and changelog
- Anthropic news (Claude web search, citations): anthropic.com/news
- Microsoft Bing / Copilot search blog: blogs.bing.com
- LinkedIn: LinkedIn Engineering blog, LinkedIn Marketing Solutions blog, LinkedIn Pressroom
- Schema.org releases, llms.txt / robots.txt and AI-crawler policy changes

**Trusted secondary**: Search Engine Land, Search Engine Roundtable, Search Engine Journal,
Glenn Gabe, Lily Ray, Aleyda Solis (SEOFOMO), Marie Haynes, Ahrefs and Semrush research,
AI-visibility trackers' studies (Profound, Peec AI, Otterly, Scrunch), Marketing AI Institute.

**Query bank**
- `Google search update {month} {year}`, `Google core update {month} {year}`
- `AI Mode update`, `AI Overviews change {month} {year}`, `Search Console new feature`
- `ChatGPT search update`, `ChatGPT shopping ads`, `Perplexity new feature`, `Claude web search citations`
- `AI search citations study {year}`, `LLM visibility study`, `share of voice AI answers`
- `AI crawler robots.txt {year}`, `llms.txt adoption`
- `LinkedIn algorithm change {month} {year}`, `LinkedIn ads new feature`
- `AI marketing tool launch {month} {year}`, `AI content tool for marketers new`

### Sumit Nautiyal · GTM leader

**Primary sources**
- Anthropic news (Claude models, Claude Code, agents, enterprise features)
- OpenAI news (agents, enterprise, ChatGPT for business)
- Google Cloud / Gemini enterprise announcements
- Salesforce newsroom (Agentforce), HubSpot newsroom and product blog (Breeze, AI agents)
- LinkedIn Sales Solutions blog (Sales Navigator), Microsoft Dynamics/Copilot for Sales
- Gartner and Forrester press releases on sales/GTM, Bridge Group, Pavilion research
- Gmail / Yahoo / Microsoft sender-requirement announcements (they change budgets)

**Trusted secondary**: TechCrunch (funding, M&A), The Information, SaaStr, Pavilion,
GTMnow, Kyle Poyar's Growth Unhinged, Clari/Gong labs research, Crunchbase News.

**Query bank**
- `AI SDR {month} {year}`, `agentic sales news`, `AI agents sales team {month} {year}`
- `Claude new release`, `Anthropic announces`, `OpenAI agents enterprise {month} {year}`
- `Agentforce update`, `HubSpot Breeze agent new`, `Sales Navigator new feature`
- `sales tech funding {month} {year}`, `GTM acquisition {month} {year}`, `SDR layoffs AI`
- `B2B buyer research study {year}`, `Gartner sales survey {year}`, `B2B buying AI assistant study`

### Pankaj Kumar · GTM engineer / RevOps

**Primary sources (changelogs first)**
- Clay changelog and university updates
- n8n release notes (GitHub n8n-io/n8n releases) and n8n blog
- HubSpot developer changelog (developers.hubspot.com/changelog) and HubSpot product updates
- Salesforce release notes, Attio changelog, Apollo changelog
- Smartlead, Instantly, lemlist, HeyReach product updates
- Claude Code / Agent SDK / MCP releases (Anthropic docs and GitHub), OpenAI API changelog
- New or updated MCP servers from GTM vendors (HubSpot, Salesforce, Clay, Apollo)
- Signal tools: Common Room, UserGems, RB2B, Warmly, Koala product updates
- Data plumbing: dbt, Segment, Census / Hightouch (reverse ETL), Fivetran release notes
- Deliverability and platform limits: Google/Yahoo/Microsoft bulk-sender rules, LinkedIn
  automation and API limits

**Trusted secondary**: Clay community and GTM-engineering newsletters, RevOps Co-op,
Wizard of Ops, Hacker News (for dev tooling), The Pipeline.

**Query bank**
- `Clay new feature {month} {year}`, `Clay changelog`
- `n8n release {month} {year}`, `n8n AI agent node new`
- `HubSpot developer changelog {month} {year}`, `HubSpot API change`, `HubSpot MCP server`
- `Salesforce release notes Agentforce API`, `Attio new feature`, `Apollo API update`
- `MCP server CRM launch`, `Claude Code new feature`, `Agent SDK release`
- `cold email deliverability change {year}`, `Microsoft Outlook bulk sender requirements`
- `RevOps tool launch {month} {year}`, `GTM engineering tool new`

## Scoring a candidate (0-3 each)

| Criterion | 3 | 0 |
|---|---|---|
| **Freshness** | inside the window, primary source | older than 14 days |
| **Reader relevance** | changes what this profile's reader does this quarter | interesting, but not their job |
| **Teachability** | a mechanism plus steps can be written | only "X announced Y" |
| **Angle fit** | the profile's voice has a strong, honest take | any profile could write it |
| **Specificity** | concrete facts: names, numbers, dates, limits | vague or rumour |
| **Novelty** | not covered by us in the last 10 days | same story or same angle recently (score -3) |

Pick the top scorer at **10+**. Ties go to the one with the stronger *what to do this week*.
Below 10 everywhere: drop a rung on the ladder.

## Avoiding repeats

Before scoring, read the last 10 daily briefs (Notion Daily Post Desk, or
`devcommx/linkedin-daily/*.md` in the repo, whichever the run has). List the stories,
formats and asks already used per profile. Then:
- never the same story for the same profile within 10 days unless a material follow-up happened
- rotate format so a profile's week lands near 70% visual (carousel / single image / document)
- do not repeat the same ask three days running
