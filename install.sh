#!/usr/bin/env bash
# Install this repo's skills and commands into the local Claude account.
#
#   ./install.sh            # install into ~/.claude
#   CLAUDE_DIR=/path ./install.sh
#
# Existing skills/commands with the same name are overwritten.
# ~/.claude/skills/synced/ (account-synced skills) is never touched.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${CLAUDE_DIR:-$HOME/.claude}"

mkdir -p "$CLAUDE_DIR/skills" "$CLAUDE_DIR/commands"

cp -R "$REPO/skills/." "$CLAUDE_DIR/skills/"
cp -R "$REPO/commands/." "$CLAUDE_DIR/commands/"

echo "Installed into $CLAUDE_DIR"
echo "  skills:   $(find "$REPO/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
echo "  commands: $(find "$REPO/commands" -name '*.md' | wc -l | tr -d ' ') in $(find "$REPO/commands" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') namespaces"
echo
echo "Plugin skills under plugins/ are reference copies. Install them as plugins instead:"
echo "  marketing, cowork-plugin-management  ->  from the knowledge-work-plugins marketplace"
echo "  anthropic-skills                     ->  ships with Claude / account skill sync"
echo
echo "Restart Claude Code to pick up the new skills."
