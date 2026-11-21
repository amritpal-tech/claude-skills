#!/usr/bin/env python3
"""
Print today's run context for the DevCommX daily LinkedIn desk.

Usage:
    python3 daily_context.py            # human-readable
    python3 daily_context.py --json     # machine-readable
    python3 daily_context.py --date 2026-11-05   # pretend it is another IST day

What it answers, so the agent never does timezone math in its head:
  - today's date and weekday in IST
  - each profile's posting slot in IST for this date (DST-aware: every slot is
    pinned to a market-local time, so the IST time moves when DST starts/ends)
  - whether today is one of that profile's posting days, and the next slot if not
  - the research freshness window (48h, or 72h on Monday so the weekend counts)

Slots come from Notion "Posting Schedule v2" (standing from Week 9). If that page
changes, change PROFILES below; nothing else depends on it.
"""
import argparse
import datetime as dt
import json
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

# market_tz + market_time is what the slot is designed to hit; days are IST weekdays
PROFILES = {
    "amritpal": {
        "name": "Amrit Pal Singh",
        "lane": "Marketing / SEO / AEO",
        "market": "Europe (CET 09:30, UK 08:30)",
        "market_tz": "Europe/Paris",
        "market_time": (9, 30),
        "days": ["Tue", "Thu", "Fri"],
    },
    "sumit": {
        "name": "Sumit Nautiyal",
        "lane": "GTM leader",
        "market": "US East (ET 09:00, peak)",
        "market_tz": "America/New_York",
        "market_time": (9, 0),
        "days": ["Mon", "Tue", "Wed", "Thu"],
    },
    "pankaj": {
        "name": "Pankaj Kumar",
        "lane": "GTM engineer / RevOps",
        "market": "US West (PT 09:00, ET 12:00)",
        "market_tz": "America/Los_Angeles",
        "market_time": (9, 0),
        "days": ["Mon", "Tue", "Wed", "Thu"],
    },
}

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def slot_ist(day: dt.date, market_tz: str, hm) -> dt.datetime:
    """The IST datetime of the market-local slot on the market's same calendar day.

    The slot is anchored to the IST posting day: build the market-local time on the
    IST date, convert to IST. For the US slots this lands the same evening in IST.
    """
    local = dt.datetime(day.year, day.month, day.day, hm[0], hm[1], tzinfo=ZoneInfo(market_tz))
    return local.astimezone(IST)


def next_slot(day: dt.date, p: dict):
    for i in range(0, 8):
        d = day + dt.timedelta(days=i)
        if WEEKDAYS[d.weekday()] in p["days"]:
            return d, slot_ist(d, p["market_tz"], p["market_time"])
    return None, None


def build(day: dt.date, now_ist: dt.datetime):
    weekday = WEEKDAYS[day.weekday()]
    window_h = 72 if weekday == "Mon" else 48
    out = {
        "date_ist": day.isoformat(),
        "weekday": weekday,
        "now_ist": now_ist.strftime("%Y-%m-%d %H:%M"),
        "us_dst_in_force": bool(dt.datetime(day.year, day.month, day.day, 12, tzinfo=ZoneInfo("America/New_York")).dst()),
        "eu_dst_in_force": bool(dt.datetime(day.year, day.month, day.day, 12, tzinfo=ZoneInfo("Europe/Paris")).dst()),
        "research_window_hours": window_h,
        "research_window_start_ist": (now_ist - dt.timedelta(hours=window_h)).strftime("%Y-%m-%d %H:%M"),
        "fallback_window_days": 7,
        "profiles": {},
    }
    for key, p in PROFILES.items():
        on = weekday in p["days"]
        nd, ns = next_slot(day, p)
        out["profiles"][key] = {
            "name": p["name"],
            "lane": p["lane"],
            "posting_days": p["days"],
            "on_slot_today": on,
            "slot_today_ist": slot_ist(day, p["market_tz"], p["market_time"]).strftime("%H:%M") if on else None,
            "next_slot": f"{WEEKDAYS[nd.weekday()]} {nd.isoformat()} {ns.strftime('%H:%M')} IST" if nd else None,
            "lands_at": p["market"],
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--date", help="IST date to compute for, YYYY-MM-DD")
    a = ap.parse_args()

    now = dt.datetime.now(IST)
    day = dt.date.fromisoformat(a.date) if a.date else now.date()
    ctx = build(day, now)

    if a.json:
        print(json.dumps(ctx, indent=2))
        return

    print(f"IST date: {ctx['weekday']} {ctx['date_ist']}  (now {ctx['now_ist']} IST)")
    print(f"DST: US {'on' if ctx['us_dst_in_force'] else 'off'} · Europe {'on' if ctx['eu_dst_in_force'] else 'off'}")
    print(f"Research window: last {ctx['research_window_hours']}h (since {ctx['research_window_start_ist']} IST); fallback up to {ctx['fallback_window_days']} days, labelled")
    print()
    for key, p in ctx["profiles"].items():
        status = f"ON SLOT today {p['slot_today_ist']} IST" if p["on_slot_today"] else f"off today, next slot {p['next_slot']}"
        print(f"- {p['name']} ({p['lane']}): {status} · lands {p['lands_at']}")


if __name__ == "__main__":
    main()
