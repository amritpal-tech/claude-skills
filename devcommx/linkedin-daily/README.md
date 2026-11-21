# LinkedIn daily desk: briefs

One file per IST day, written by the `dcx-daily-linkedin` skill
(`.claude/skills/dcx-daily-linkedin/`). Each brief holds the day's research scan and a
complete post package for Amrit Pal Singh (marketing / AEO), Sumit Nautiyal (GTM leader)
and Pankaj Kumar (GTM engineer): research brief with sources, strategy, hook options, the
post, creative spec, first comment, before-publish flags and the gate result.

Nothing here is published automatically. A human reviews each post, clears its flags, and
posts at the profile's slot.

Re-check any brief:

```bash
python3 .claude/skills/dcx-daily-linkedin/scripts/check_post.py devcommx/linkedin-daily/2026-11-04.md
```

See today's slots:

```bash
python3 .claude/skills/dcx-daily-linkedin/scripts/daily_context.py
```
