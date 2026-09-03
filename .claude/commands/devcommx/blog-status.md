---
description: Enumerate the Webflow blog collection and reconcile it against the local corpus.
argument-hint: "[optional: slug or batch to focus on]"
---
# /devcommx:blog-status

Report the current state of the DevCommX blog program. Focus: **$ARGUMENTS**

Load `devcommx-blog-ops` and read `references/state.md` for the last known snapshot.
**Re-enumerate rather than trusting it** — the SEO team keeps publishing drafts, so
publish state drifts.

## Steps

1. **Enumerate the collection** `689c92652a4b35f0e9a14fc2` with `list_collection_items`,
   paginating offsets 0, 100, 200. It was 221 items at last count.
2. **Detect duplicates** — any slug carrying a random `-xxxxx` suffix is a concurrency-bug
   artifact. List them; do not delete without explicit approval (deletion is permanent).
3. **Reconcile** the live collection against `devcommx/blogs/` (53 drafts on disk) and
   `devcommx/data/_existing_slugs.txt`. Report:
   - on disk but not in the CMS (never pushed)
   - in the CMS but not on disk (drafted elsewhere)
   - in both, and whether draft or published
4. **Refresh the slug inventory** — write the enumerated slugs back to
   `devcommx/data/_existing_slugs.txt`.
5. **Validation coverage** — which blogs have findings in `devcommx/validation/`, and
   the current scores:
   ```bash
   python3 .claude/skills/devcommx-blog-ops/scripts/score_findings.py devcommx/validation/*.json
   ```

## Output

Counts, the draft-vs-published split, duplicates found, reconciliation gaps in both
directions, and the open items from `references/state.md` that are still open.
