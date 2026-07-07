# Mythic Earth — Claude Code Rules (repo dir keeps old working title "three-realms")

A PvE-first MMORPG in the spirit of Dark Age of Camelot. Solo dev (Daniel) +
Claude as full coding/systems/tooling partner. This file carries the
load-bearing decisions — treat them as authoritative direction, not a starting
point to second-guess.

## Non-Negotiable Design Pillars

1. **PvE-FIRST.** DAoC died because Mythic over-prioritized RvR/PvP at the
   expense of PvE. Every modern "successor" chases the same PvP mistake. This
   project exists to fill the empty PvE niche: group dungeons, raid content,
   world soul. Never pivot suggestions toward PvP "because that's what MMOs do."
2. **Monetization is locked:** F2P download on Steam (free trial up to a
   content gate, FFXIV-style), $15/month subscription for full content, billed
   outside Steam (Stripe/Paddle via account portal) to avoid the 30% cut.
   **Zero microtransactions. Zero paid cosmetics. Zero XP boosts.** Players
   earn everything in-game. This is part of the brand promise — when revenue
   gets soft someday, the answer is never "add a $5 mount."
3. **Scope: ship like Project Gorgon, not like DAoC launch.** A vertical slice
   deep enough to land the first 100 devoted players, then grow outward over
   years.

## Tech Decisions

- **Engine: Unreal Engine 5.8** (final UE5.x release; mesh terrain suits
  dungeon-heavy PvE). Free until $1M/yr revenue; Quixel + MetaHumans + Iris
  replication earn their keep for a 2-person team.
- **Engine project: `C:\dev\ThreeRealms`** (own git repo) — deliberately
  outside OneDrive; sync fights engine binaries and derived-data caches.
  This design repo is fine in OneDrive. Build via VS 2022 toolchain;
  UE's bundled .NET 10 (use `Build.bat`, not UnrealBuildTool.exe directly).
- Dedicated-server builds will eventually need the source-built engine from
  Epic's GitHub (launcher builds can't compile Server targets).

## Data Flow — Single Source of Truth

- Daniel authors game design in **MMOStats.xlsx** (lives in
  `C:\Users\delli\Downloads\`; a snapshot is committed at
  `design/MMOStats-source-snapshot.xlsx`).
- `python tools/extract_from_xlsx.py` converts it to canonical JSON in
  `data/`. **Never hand-edit `data/`** — fix the spreadsheet (or the
  extractor) and re-run. Copy the fresh xlsx over the snapshot when it changes.
- `python tools/validate.py` checks referential integrity and design gaps.
  Run it after every extraction. It must pass with 0 errors before committing.

## Structure

- Three factions: **Great North** (GN), **Mystic Lands** (ML), **Honorguard**
  (HG). Per faction: 25 classes in 4 archetypes (Frontline 4 / Healers 4 /
  Support 6 / DPS 11), 16 races in 3–4 culture groups, race×class gating.
- 16 stats in 4 categories (Fitness / Intelligence / Skill / Ancestral),
  100-point budget per archetype. See `data/README.md` for the schema and
  known data quirks.

## Working Rules

- Pre-commit: `python tools/validate.py` must pass.
- Design questions get settled by Daniel, recorded in `design/`, then encoded
  in data — in that order.
