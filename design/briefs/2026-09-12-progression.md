# Brief: leveling and progression refinement (for an Opus design session)

**Owner:** Daniel. **Session model:** Opus. **Writes to:** this design repo only
(`design/progression-v1.md`). No game-repo changes tonight.

## What exists
- Engine today: XP per kill from `Content/Data/mob-rewards.json` (Training Dummy 5, Rimethrall
  Stalker 12 … Halvard 90), curve `XpPerLevelBase (100) × level` with carry-over, level-up
  verified live; XP bar = 20 bubbles. No death penalty (player death is lane M6). No quest XP yet.
- Creation: realm → class type → race → name; levels 1–9 on the archetype tree; class quest at 10
  (`data/quests.json`). Stat minimums per archetype/class in `data/factions/great-north.json`
  (from MMOStats). Race × class matrix gates which true classes a race can reach.
- Business model (pillars): F2P trial up to a content gate (FFXIV-style), $15/mo sub, zero
  microtransactions, zero XP boosts. Players start in plain clothes and build up gear.
- Roadmap: first dungeon is the thesis (Phase 3); "systems-driven depth, not content volume".

## Questions to settle (decisions, with numbers as proposals for the sheet)
1. Level cap for launch and the XP curve shape to it; target hours to 10 / 20 / cap for a
   normal player.
2. XP sources and their ratio: kills, quests, exploration/discovery, dungeon completion, group
   bonus. Rested XP or not.
3. Stat growth per level and where the creation stat minimums bite (class quest at 10).
4. Death penalty and recovery (feeds lane M6).
5. Gear progression: clothes → leather/cloth tiers → dungeon sets; drops vs crafted; what a
   level-10 character wears.
6. The free-trial content gate: which level / zone boundary, and what the sub unlocks.
7. Post-cap progression that is PvE-first (dungeon tiers, raid-lite, titles, a PvE "renown"
   track) — the battle-royale event is parked at Phase 6 and must not become the gear path.

## Rules
- Pillars in `CLAUDE.md` are non-negotiable; MMOStats.xlsx stays the numbers' home.
