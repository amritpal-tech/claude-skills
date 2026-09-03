#!/usr/bin/env bash
# Build one .zip per skill for upload to claude.ai
# (Settings -> Capabilities -> Skills -> Upload skill).
#
# Account-uploaded skills sync to every chat on every device, which is the only
# way to get these skills outside this repo. Output lands in dist/ (gitignored).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="${1:-$REPO/dist}"

rm -rf "$OUT"; mkdir -p "$OUT"

cd "$REPO/.claude/skills"
for d in */; do
  name="${d%/}"
  zip -qr "$OUT/$name.zip" "$name"
done

echo "Wrote $(ls "$OUT" | wc -l | tr -d ' ') skill zips to $OUT"
