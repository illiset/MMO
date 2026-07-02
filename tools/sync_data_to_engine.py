"""Copy canonical design data (data/) into the UE project's Content/Data
folder, where the game's TRGameDataSubsystem loads it at startup.

Usage: python tools/sync_data_to_engine.py
Run after every extract_from_xlsx.py + validate.py cycle.
"""
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TARGETS = [
    Path(r"C:\dev\ThreeRealms\Content\Data"),      # legacy 5.8 project
    Path(r"C:\dev\MMOKitEval\Content\Data"),       # MMO Kit project (primary)
]

src = REPO / "data"
for target in TARGETS:
    target.mkdir(parents=True, exist_ok=True)
    copied = 0
    for f in src.rglob("*.json"):
        dest = target / f.relative_to(src)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
        copied += 1
    print(f"synced {copied} json files -> {target}")
