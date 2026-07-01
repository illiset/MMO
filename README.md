# Three Realms (working title)

A PvE-first MMORPG in the spirit of Dark Age of Camelot — three factions, deep
group PvE, no microtransactions ever.

## What's here

| Path | What it is |
|---|---|
| `data/` | Canonical game-design data as JSON (generated — do not hand-edit) |
| `design/` | Vision doc, source spreadsheet snapshot, design notes |
| `tools/extract_from_xlsx.py` | Converts MMOStats.xlsx → `data/` |
| `tools/validate.py` | Consistency checks over `data/` |

## The three factions

| Faction | Culture groups |
|---|---|
| **Great North** | Crusaders, Elves, Hillback Empire, Dew Hollow |
| **Mystic Lands** | Persian Empires, The Fallen, Alkebulan, Nomads |
| **Honorguard** | The Builders, The Shrouded, Peacefuls |

Each faction fields 25 classes across four archetypes (Frontline, Healers,
Support, DPS) and 16 playable races, with a race×class permission matrix.

## Workflow

1. Edit the design in `MMOStats.xlsx` (Downloads), copy it over
   `design/MMOStats-source-snapshot.xlsx`
2. `python tools/extract_from_xlsx.py`
3. `python tools/validate.py` — must pass with 0 errors
4. Commit

See [CLAUDE.md](CLAUDE.md) for the load-bearing project decisions,
[design/vision.md](design/vision.md) for the full design philosophy, and
[design/roadmap.md](design/roadmap.md) for the phase-by-phase roadmap.
