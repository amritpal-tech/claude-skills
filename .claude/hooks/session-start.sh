#!/bin/bash
# SessionStart hook for amritpal-tech/claude-skills
#
# Mirrors this repo's skill library into the session's Claude config dir so the
# skills and commands are available even where project-level .claude/skills
# discovery does not reach the session (Claude Code on the web).
#
# Runs synchronously and on purpose: skills are enumerated at session start, so
# this must finish before the agent loop reads them.
#
# Idempotent, quiet, and never fails session startup.

set -uo pipefail

# Web sessions only. On a local machine ~/.claude persists and is the user's own;
# use ./install.sh there instead of overwriting it on every session start.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REPO="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"

[ -d "$REPO/.claude/skills" ] || exit 0

mkdir -p "$DEST/skills" "$DEST/commands" 2>/dev/null || exit 0

cp -R "$REPO/.claude/skills/." "$DEST/skills/" 2>/dev/null
cp -R "$REPO/.claude/commands/." "$DEST/commands/" 2>/dev/null

skills=$(find "$DEST/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
cmds=$(find "$DEST/commands" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
echo "Skill library installed: ${skills} skills, ${cmds} commands available."

exit 0
