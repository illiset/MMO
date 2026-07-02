"""Copy canonical design data (data/) into the UE project's Content/Data
folder, where the game's TRGameDataSubsystem loads it at startup.

Usage: python tools/sync_data_to_engine.py
Run after every extract_from_xlsx.py + validate.py cycle.
"""
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENGINE_DATA = Path(r"C:\dev\ThreeRealms\Content\Data")

src = REPO / "data"
ENGINE_DATA.mkdir(parents=True, exist_ok=True)
copied = 0
for f in src.rglob("*.json"):
    dest = ENGINE_DATA / f.relative_to(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(f, dest)
    copied += 1
print(f"synced {copied} json files -> {ENGINE_DATA}")
