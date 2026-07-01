"""Convert MMOStats.xlsx into canonical JSON design data under data/.

Usage: python tools/extract_from_xlsx.py [path-to-xlsx]
Defaults to design/MMOStats-source-snapshot.xlsx. Re-run whenever the
spreadsheet changes; data/ is generated output and should not be hand-edited.
"""
import json
import re
import sys
from pathlib import Path

import openpyxl

REPO = Path(__file__).resolve().parent.parent
DEFAULT_XLSX = REPO / "design" / "MMOStats-source-snapshot.xlsx"

FACTIONS = [
    ("Great North", "great-north", "GN"),
    ("Mystic Lands", "mystic-lands", "ML"),
    ("Honorguard", "honorguard", "HG"),
]
ARCHETYPE_NAMES = {"Frontline", "Healers", "Support", "DPS"}
STAT_CATEGORIES = ["Fitness", "Intelligence", "Skill", "Ancestral"]
# Spelling fixes for shared mechanical identifiers (stat names must match
# across factions). Creative names (classes, races) are kept as authored.
STAT_NAME_FIXES = {"Widsom": "Wisdom"}


def slug(name: str) -> str:
    s = name.strip().lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def cell_str(v):
    return str(v).strip() if v is not None else ""


def is_mark(v):
    return cell_str(v).lower() == "x"


def parse_sheet(ws):
    grid = {}
    for row in ws.iter_rows(min_row=1, max_row=60, max_col=40):
        for c in row:
            if c.value is not None and cell_str(c.value) != "":
                grid[(c.row, c.column)] = c.value

    # Row 1: archetype headers and class names, left to right.
    archetypes = []  # [{name, col, classes: [{name, col}]}]
    current = None
    for col in range(6, 41):
        name = cell_str(grid.get((1, col)))
        if not name:
            continue
        if name in ARCHETYPE_NAMES:
            current = {"name": name, "col": col, "classes": []}
            archetypes.append(current)
        elif current is not None:
            current["classes"].append({"name": name, "col": col})

    class_cols = {c["col"]: c["name"] for a in archetypes for c in a["classes"]}

    # Find where the stats section starts ("Stats" marker in column D).
    stats_row = next(r for r in range(1, 61) if cell_str(grid.get((r, 4))) == "Stats")

    # Race section: rows 2..stats_row-1. Column E holds either a culture-group
    # header (no marks in class columns) or a race (marks present).
    groups = []
    for r in range(2, stats_row):
        name = cell_str(grid.get((r, 5)))
        if not name:
            continue
        marks = [class_cols[c] for c in sorted(class_cols) if is_mark(grid.get((r, c)))]
        if marks:
            if not groups:
                groups.append({"name": "Ungrouped", "races": []})
            groups[-1]["races"].append({"name": name, "allowed": marks})
        else:
            groups.append({"name": name, "races": []})

    # Stats section: category header rows (no values) and stat rows (numeric
    # minimum under each archetype column; numbers or x-marks under classes).
    categories = []
    budget = None
    for r in range(stats_row, 61):
        name = cell_str(grid.get((r, 5)))
        arch_cols = [a["col"] for a in archetypes]
        if not name:
            v = grid.get((r, arch_cols[0]))
            if isinstance(v, (int, float)) and not budget:
                budget = int(v)
            continue
        if name in STAT_CATEGORIES:
            categories.append({"name": name, "stats": []})
            continue
        name = STAT_NAME_FIXES.get(name, name)
        stat = {"name": name, "archetypeMin": {}, "classMin": {}, "classKey": []}
        for a in archetypes:
            v = grid.get((r, a["col"]))
            if isinstance(v, (int, float)):
                stat["archetypeMin"][a["name"]] = int(v)
        for col, cls in class_cols.items():
            v = grid.get((r, col))
            if isinstance(v, (int, float)):
                stat["classMin"][cls] = int(v)
            elif is_mark(v):
                stat["classKey"].append(cls)
        if categories:
            categories[-1]["stats"].append(stat)

    return archetypes, groups, categories, budget


def build_faction_json(name, fid, abbr, archetypes, groups, categories):
    out = {"id": fid, "name": name, "abbreviation": abbr, "archetypes": [], "cultureGroups": []}
    for a in archetypes:
        arch = {
            "id": slug(a["name"]),
            "name": a["name"],
            "statMinimums": {},
            "classes": [],
        }
        for cat in categories:
            for s in cat["stats"]:
                if a["name"] in s["archetypeMin"]:
                    arch["statMinimums"][slug(s["name"])] = s["archetypeMin"][a["name"]]
        for c in a["classes"]:
            cls = {"id": slug(c["name"]), "name": c["name"], "statMinimums": {}, "keyStats": []}
            for cat in categories:
                for s in cat["stats"]:
                    if c["name"] in s["classMin"]:
                        cls["statMinimums"][slug(s["name"])] = s["classMin"][c["name"]]
                    if c["name"] in s["classKey"]:
                        cls["keyStats"].append(slug(s["name"]))
            arch["classes"].append(cls)
        out["archetypes"].append(arch)
    for g in groups:
        if not g["races"]:
            continue
        out["cultureGroups"].append({
            "id": slug(g["name"]),
            "name": g["name"],
            "races": [
                {"id": slug(r["name"]), "name": r["name"],
                 "allowedClasses": [slug(c) for c in r["allowed"]]}
                for r in g["races"]
            ],
        })
    return out


def main():
    xlsx = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_XLSX
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    data_dir = REPO / "data"
    (data_dir / "factions").mkdir(parents=True, exist_ok=True)

    stats_json = None
    for sheet, fid, abbr in FACTIONS:
        archetypes, groups, categories, budget = parse_sheet(wb[sheet])
        faction = build_faction_json(sheet, fid, abbr, archetypes, groups, categories)
        path = data_dir / "factions" / f"{fid}.json"
        path.write_text(json.dumps(faction, indent=2) + "\n", encoding="utf-8")
        n_races = sum(len(g["races"]) for g in faction["cultureGroups"])
        n_classes = sum(len(a["classes"]) for a in faction["archetypes"])
        print(f"{fid}: {n_classes} classes, {n_races} races, budget {budget}")
        if stats_json is None:
            stats_json = {
                "budgetPerArchetype": budget,
                "categories": [
                    {"id": slug(c["name"]), "name": c["name"],
                     "stats": [slug(s["name"]) for s in c["stats"]]}
                    for c in categories
                ],
            }
    (data_dir / "stats.json").write_text(
        json.dumps(stats_json, indent=2) + "\n", encoding="utf-8")
    print("wrote data/stats.json")


if __name__ == "__main__":
    main()
