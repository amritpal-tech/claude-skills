#!/usr/bin/env bash
# Verify DevCommX internal link targets are LIVE (HTTP 200), not merely present in the CMS.
#
#   check_links.sh slug-a slug-b ...          check specific blog slugs
#   check_links.sh --file devcommx/data/_existing_slugs.txt
#   check_links.sh --urls https://... ...     check full URLs (e.g. external sources)
#   check_links.sh --drafts devcommx/blogs/traffic/*.json   extract + check every href
#
# The CMS slug inventory INCLUDES UNPUBLISHED DRAFTS. Linking to one produces a live
# 404. Only 200s go in the approved link menu.
#
# NETWORK: a Claude Code *web/remote* session usually cannot reach devcommx.com at all
# (the egress proxy returns 403 to CONNECT, and WebFetch returns EGRESS_BLOCKED). This
# script then reports everything DEAD, which is a false negative. Run it from a local
# machine, or from a session whose environment network policy allows the domain. Never
# "fix" links on the strength of a blocked run.
#
# On external URLs a 403 is usually anti-bot (Gartner, Apollo KB, SEC.gov, DOL.gov,
# Perplexity all 403 to curl and load fine in a browser). Verify in a real browser
# before "fixing" a link that is not broken.

set -uo pipefail
BASE="https://www.devcommx.com/blogs"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"

mode=slugs
case "${1:-}" in
  --file)   mode=file;   shift ;;
  --urls)   mode=urls;   shift ;;
  --drafts) mode=drafts; shift ;;
  "" ) echo "usage: check_links.sh [--file F | --urls U... | --drafts J...] slug..." >&2; exit 2 ;;
esac

targets=()
case $mode in
  slugs)  for s in "$@"; do targets+=("$BASE/$s"); done ;;
  file)   while read -r s; do
            s="${s%%#*}"; s="$(echo "$s" | tr -d '[:space:]')"
            [ -n "$s" ] && targets+=("$BASE/$s")
          done < "$1" ;;
  urls)   targets=("$@") ;;
  drafts) mapfile -t targets < <(grep -oh 'href="[^"]*"' "$@" \
            | sed 's/href="//; s/"$//' | grep '^http' | sort -u) ;;
esac

ok=0; bad=0; suspect=0
for url in "${targets[@]}"; do
  code=$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 20 -A "$UA" "$url" 2>/dev/null || echo 000)
  case "$code" in
    200)     printf '  %-4s OK       %s\n' "$code" "$url"; ok=$((ok+1)) ;;
    403|429) printf '  %-4s SUSPECT  %s  (likely anti-bot, verify in a browser)\n' "$code" "$url"
             suspect=$((suspect+1)) ;;
    *)       printf '  %-4s DEAD     %s\n' "$code" "$url"; bad=$((bad+1)) ;;
  esac
done

echo
echo "$ok live · $bad dead · $suspect suspect (of ${#targets[@]})"
[ "$bad" -eq 0 ]
