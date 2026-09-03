# claude-skills

Account skill library for Claude Code — 151 skills and 27 namespaced commands,
kept in version control so they load in every session on this repo and can be
restored anywhere else.

Imported from the `claude-skills-2026-09-03` export.

## Layout

| Path | Purpose |
|---|---|
| `.claude/skills/` | 152 skills — **auto-loaded** in any Claude Code session on this repo |
| `.claude/commands/` | 35 commands in 9 namespaces — auto-loaded, invoked as `/namespace:command` |
| `devcommx/` | working corpus for the DevCommX blog operation (53 drafts, validation findings, workbooks) |
| `plugins/` | reference copies of 3 plugin bundles (install via the plugin system) |
| `install.sh` | copy skills into `~/.claude` for use outside this repo |
| `package-for-upload.sh` | build per-skill zips for uploading to your claude.ai account |
| `INVENTORY.md` | full list with descriptions |

## Where skills load from, and what survives a new chat

Claude Code reads skills from three places. They differ in what persists:

| Location | Scope | Survives a new chat? |
|---|---|---|
| `.claude/skills/` in a repo | sessions on that repo | **Yes** — it's committed |
| `~/.claude/skills/` | all sessions on that machine | Only if `~/.claude` persists. On Claude Code **web**, the container is ephemeral, so **no** |
| `~/.claude/skills/synced/` | every chat, every device | **Yes** — synced from your claude.ai account |

This repo keeps skills in `.claude/skills/` for that reason. A web session gets a
fresh container each time and a fresh clone of the repo — anything written to
`~/.claude` is gone, but anything committed here comes back.

### Using these skills in new chats

- **Sessions on this repo** — nothing to do. They load automatically.
- **Sessions on another repo** — copy `.claude/skills/` into that repo, or add
  this repo as a second source for the session.
- **Every chat, everywhere (including claude.ai)** — upload to your account:
  ```bash
  ./package-for-upload.sh          # writes dist/<skill>.zip x151
  ```
  Then claude.ai → Settings → Capabilities → Skills → Upload skill. Account
  skills sync down to `~/.claude/skills/synced/` on every device.
- **A local (non-web) machine** — `./install.sh` writes into `~/.claude`, which
  persists there.

## Command namespaces

`design-ops`, `design-research`, `design-systems`, `designer-toolkit`,
`devcommx`, `interaction-design`, `prototyping-testing`, `ui-design`, `ux-strategy`

## DevCommX blog operations

The account's live blog program has a full knowledgebase in this repo:

- **`.claude/skills/devcommx-blog-ops/`** — the operating manual. Webflow collection IDs
  and field schema, the draft spec, the 6-dimension validation rubric, the batch
  pipeline, the internal-link liveness protocol, and the gotchas that already cost
  rework once. Plus working scripts: a hard-rules draft gate, the weighted scorer, the
  workbook builder, and a link checker.
- **`.claude/commands/devcommx/`** — `/devcommx:blog-batch`, `blog-draft`,
  `blog-validate`, `blog-push`, `blog-audit`, `blog-status`, `blog-figures`,
  `blog-review-doc`.
- **`devcommx/`** — the corpus: 53 drafts, 53 validation findings, 4 workbooks, the slug
  inventory, and the original session handoff verbatim.

Companion skills already in the library: `devcommx-brand` (visual system) and
`devcommx-keyword-governance` (the keyword filter that runs before any brief).

The blog program needs the **Webflow MCP connector authorized on the account** —
nothing in the push, audit or status flow works without it.

## Plugin skills

`plugins/` holds reference copies of three plugin bundles. Do not copy them into
a skills directory — they are managed by the plugin system, and several of their
skills (`docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`) would collide with skills
Claude already syncs to the account. Install them as plugins instead:

- **marketing** — from the `knowledge-work-plugins` marketplace
- **cowork-plugin-management** — from the `knowledge-work-plugins` marketplace
- **anthropic-skills** — ships with Claude; arrives via account skill sync

## Notes

- **`design` shadows a built-in.** Claude Code ships a `design` skill (the Claude
  Design canvas editor). The personal `design` skill here uses the same name and
  takes precedence. Rename the directory and its frontmatter `name:` to get the
  built-in back.
- **Duplicate-looking pairs are intentional.** Several skills exist in both short
  and long form (`ads`/`paid-ads`, `emails`/`email-sequence`, `cro`/`page-cro`,
  `competitors`/`competitor-alternatives`). Both were on the source account.
- **Built-in skills are not included.** `artifact-design`, `code-review`,
  `dataviz`, `simplify`, `loop` and friends ship inside the Claude Code binary.
