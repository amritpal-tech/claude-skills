#!/usr/bin/env python3
"""
Compute the weighted score and verdict from validation findings JSONs.

Usage:
    python3 score_findings.py devcommx/validation/*.json
    python3 score_findings.py --json devcommx/validation/*.json

ALWAYS run this in the main thread. Validation agents write plausible findings and
then attach the wrong verdict, so the verdict is recomputed from the raw criteria.
"""
import sys, os, json, argparse

WEIGHTS = {
    "content_quality": 0.18,
    "seo":             0.18,
    "geo_aeo":         0.20,
    "brand":           0.15,
    "structure":       0.14,
    "schema":          0.15,
}
ORDER = list(WEIGHTS)
PUBLISH, REVISE = 3.9, 2.75


def verdict(score):
    return "PUBLISH" if score >= PUBLISH else ("REVISE" if score >= REVISE else "HOLD")


def score_file(path):
    d = json.load(open(path, encoding="utf-8"))
    dims, problems = [], []
    seen = set()

    for dim in d.get("dimensions", []):
        key = dim.get("key")
        crits = dim.get("criteria", [])
        seen.add(key)
        if key not in WEIGHTS:
            problems.append(f"unknown dimension key {key!r}")
            continue
        if len(crits) != 5:
            problems.append(f"{key} has {len(crits)} criteria, expected 5")
        w = WEIGHTS[key]
        if abs(float(dim.get("weight", w)) - w) > 1e-9:
            problems.append(f"{key} declares weight {dim.get('weight')}, canonical is {w}")
        scores = []
        for c in crits:
            s = c.get("score")
            if not isinstance(s, int) or not 0 <= s <= 5:
                problems.append(f"{key}/{c.get('criterion')} score {s!r} is not an int 0-5")
                s = 0
            scores.append(s)
        mean = sum(scores) / len(scores) if scores else 0.0
        dims.append({"key": key, "title": dim.get("title", key), "weight": w,
                     "mean": round(mean, 2), "verdict": verdict(mean),
                     "flag_type": dim.get("flag_type"), "flag": dim.get("flag", "")})

    for k in WEIGHTS:
        if k not in seen:
            problems.append(f"missing dimension {k}")

    overall = round(sum(x["mean"] * x["weight"] for x in dims), 3)
    return {
        "slug": d.get("slug") or os.path.basename(path).replace(".json", ""),
        "title": d.get("title", ""),
        "words": d.get("words", 0),
        "overall": overall,
        "verdict": verdict(overall),
        "dimensions": dims,
        "top_fixes": d.get("top_fixes", []),
        "problems": problems,
        "file": path,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true", help="print per-dimension detail")
    a = ap.parse_args()

    rows = [score_file(p) for p in a.files]
    rows.sort(key=lambda r: -r["overall"])

    if a.json:
        print(json.dumps(rows, indent=2))
        return

    print(f"{'SCORE':>6}  {'VERDICT':<8}  {'WORDS':>6}  SLUG")
    print("-" * 78)
    for r in rows:
        print(f"{r['overall']:>6.2f}  {r['verdict']:<8}  {r['words']:>6}  {r['slug']}")
        if a.full:
            for d in r["dimensions"]:
                print(f"          {d['mean']:>4.1f}  w{d['weight']:<5}  {d['title']}")
        for p in r["problems"]:
            print(f"          !! {p}")

    if rows:
        mean = sum(r["overall"] for r in rows) / len(rows)
        counts = {v: sum(1 for r in rows if r["verdict"] == v)
                  for v in ("PUBLISH", "REVISE", "HOLD")}
        print("-" * 78)
        print(f"{len(rows)} blogs · mean {mean:.2f} · "
              f"PUBLISH {counts['PUBLISH']} · REVISE {counts['REVISE']} · HOLD {counts['HOLD']}")

        # the standing cross-batch weakness: report the weakest criteria overall
        agg = {}
        for p in a.files:
            d = json.load(open(p, encoding="utf-8"))
            for dim in d.get("dimensions", []):
                for c in dim.get("criteria", []):
                    if isinstance(c.get("score"), int):
                        agg.setdefault(c.get("criterion", "?"), []).append(c["score"])
        weakest = sorted(((sum(v) / len(v), k, len(v)) for k, v in agg.items()))[:5]
        print("\nWeakest criteria across the set:")
        for m, k, n in weakest:
            print(f"  {m:.2f}/5  {k}  (n={n})")


if __name__ == "__main__":
    main()
