#!/usr/bin/env bash
# Install this repo's skills and commands into the local Claude account.
#
# You do NOT need this for Claude Code sessions started on this repo — skills in
# .claude/skills/ and commands in .claude/commands/ are discovered automatically.
#
# Use this to make the skills available OUTSIDE this repo, on a machine where
# ~/.claude persists (a local install, not an ephemeral web container):
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

cp -R "$REPO/.claude/skills/." "$CLAUDE_DIR/skills/"
cp -R "$REPO/.claude/commands/." "$CLAUDE_DIR/commands/"

echo "Installed into $CLAUDE_DIR"
echo "  skills:   $(find "$REPO/.claude/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
echo "  commands: $(find "$REPO/.claude/commands" -name '*.md' | wc -l | tr -d ' ')"
echo
echo "Restart Claude Code to pick up the new skills."
