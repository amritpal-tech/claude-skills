# claude-skills

Account skill library for Claude Code — the personal skills and namespaced
commands installed on the Claude account, kept in version control so they can be
restored on any machine.

Imported from the `claude-skills-2026-09-03` export.

## Contents

| Path | Installs to | Count |
|---|---|---|
| `skills/` | `~/.claude/skills/` | 151 skills |
| `commands/` | `~/.claude/commands/` | 27 commands in 8 namespaces |
| `plugins/` | *(reference only — install as plugins)* | 3 plugins, 19 skills |

`INVENTORY.md` has the full list with descriptions.

## Install

```bash
git clone https://github.com/amritpal-tech/claude-skills.git
cd claude-skills
./install.sh
```

Then restart Claude Code. Skills load from `~/.claude/skills/<name>/SKILL.md`;
commands are invoked as `/<namespace>:<command>`.

To install somewhere other than `~/.claude`:

```bash
CLAUDE_DIR=/some/path ./install.sh
```

## Command namespaces

`design-ops`, `design-research`, `design-systems`, `designer-toolkit`,
`interaction-design`, `prototyping-testing`, `ui-design`, `ux-strategy`

## Plugin skills

`plugins/` holds reference copies of three plugin bundles. Do not copy them into
`~/.claude/skills/` — they are managed by the plugin system and several of their
skills (`docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`) would collide with skills
Claude already syncs to the account. Install them as plugins instead:

- **marketing** — from the `knowledge-work-plugins` marketplace
- **cowork-plugin-management** — from the `knowledge-work-plugins` marketplace
- **anthropic-skills** — ships with Claude; arrives via account skill sync

## Notes

- **`skills/design` shadows the built-in `design` skill.** Claude Code ships a
  `design` skill (the Claude Design canvas editor). The personal `design` skill
  here uses the same name and takes precedence once installed. Rename the
  directory and its frontmatter `name:` if you want the built-in back.
- **Duplicate-looking pairs are intentional.** Several skills exist in both a
  short and a long form (`ads`/`paid-ads`, `emails`/`email-sequence`,
  `cro`/`page-cro`, `competitors`/`competitor-alternatives`, and others). Both
  were installed on the source account and both are kept here.
- **Built-in skills are not included.** `artifact-design`, `code-review`,
  `dataviz`, `simplify`, `loop`, and friends ship inside the Claude Code binary
  and reappear on their own.
- `~/.claude/skills/synced/` is the account sync directory. `install.sh` writes
  alongside it and never modifies it.
