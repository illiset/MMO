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

    # Abilities (hand-authored, not xlsx-generated) must reference real
    # factions/classes and carry sane numbers.
    abilities_path = REPO / "data" / "abilities.json"
    if abilities_path.exists():
        abilities = json.loads(abilities_path.read_text(encoding="utf-8"))["abilities"]
        seen_ids = set()
        for ab in abilities:
            aid = ab.get("id", "<missing-id>")
            check(aid not in seen_ids, f"abilities: duplicate id {aid}")
            seen_ids.add(aid)
            faction = factions.get(ab.get("factionId"))
            check(faction is not None, f"abilities/{aid}: unknown faction {ab.get('factionId')}")
            if faction:
                class_ids = {c["id"] for a in faction["archetypes"] for c in a["classes"]}
                check(ab.get("classId") in class_ids,
                      f"abilities/{aid}: unknown class {ab.get('classId')}")
            check(ab.get("costType") in ("stamina", "mana", "none"),
                  f"abilities/{aid}: bad costType {ab.get('costType')}")
            check(ab.get("cost", 0) >= 0, f"abilities/{aid}: negative cost")
            check(ab.get("cooldown", 0) >= 0, f"abilities/{aid}: negative cooldown")
            check(ab.get("range", 0) > 0, f"abilities/{aid}: range must be positive")
            dmg = ab.get("damage", {})
            check(0 < dmg.get("min", 0) <= dmg.get("max", 0),
                  f"abilities/{aid}: bad damage range")

    # Items (hand-authored like abilities).
    items_path = REPO / "data" / "items.json"
    if items_path.exists():
        items = json.loads(items_path.read_text(encoding="utf-8"))["items"]
        seen_items = set()
        for item in items:
            iid = item.get("id", "<missing-id>")
            check(iid not in seen_items, f"items: duplicate id {iid}")
            seen_items.add(iid)
            check(item.get("type") in ("weapon", "armor", "misc"),
                  f"items/{iid}: bad type {item.get('type')}")
            if item.get("type") == "weapon":
                dmg = item.get("damage", {})
                check(0 < dmg.get("min", 0) <= dmg.get("max", 0),
                      f"items/{iid}: bad damage range")
                check(item.get("delay", 0) > 0, f"items/{iid}: delay must be positive")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
