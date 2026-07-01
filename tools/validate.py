"""Validate the canonical design data in data/ for internal consistency.

Usage: python tools/validate.py
Exits non-zero on hard errors (broken references, malformed data).
Warnings flag design gaps worth a look, not data corruption.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FACTION_IDS = ["great-north", "mystic-lands", "honorguard"]

errors, warnings = [], []


def check(cond, msg, hard=True):
    if not cond:
        (errors if hard else warnings).append(msg)


def main():
    stats = json.loads((REPO / "data" / "stats.json").read_text(encoding="utf-8"))
    stat_ids = {s for c in stats["categories"] for s in c["stats"]}
    check(len(stat_ids) == 16, f"expected 16 unique stats, got {len(stat_ids)}")

    factions = {}
    for fid in FACTION_IDS:
        factions[fid] = json.loads(
            (REPO / "data" / "factions" / f"{fid}.json").read_text(encoding="utf-8"))

    arch_mins_by_faction = {}
    for fid, f in factions.items():
        class_ids = set()
        for arch in f["archetypes"]:
            for cls in arch["classes"]:
                check(cls["id"] not in class_ids, f"{fid}: duplicate class id {cls['id']}")
                class_ids.add(cls["id"])
                for s in list(cls["statMinimums"]) + cls["keyStats"]:
                    check(s in stat_ids, f"{fid}/{cls['id']}: unknown stat {s}")
            for s in arch["statMinimums"]:
                check(s in stat_ids, f"{fid}/{arch['id']}: unknown stat {s}")
        arch_mins_by_faction[fid] = {
            a["id"]: a["statMinimums"] for a in f["archetypes"]}

        playable = set()
        for g in f["cultureGroups"]:
            for race in g["races"]:
                check(len(race["allowedClasses"]) > 0,
                      f"{fid}/{race['id']}: race has no allowed classes", hard=False)
                for c in race["allowedClasses"]:
                    check(c in class_ids, f"{fid}/{race['id']}: unknown class {c}")
                    playable.add(c)
        for c in sorted(class_ids - playable):
            warnings.append(f"{fid}: class '{c}' is allowed by no race")

    base = arch_mins_by_faction[FACTION_IDS[0]]
    for fid in FACTION_IDS[1:]:
        check(arch_mins_by_faction[fid] == base,
              f"archetype stat minimums differ between {FACTION_IDS[0]} and {fid}",
              hard=False)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
