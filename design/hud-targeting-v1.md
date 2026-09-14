# HUD targeting v1 — the con ring (Daniel, 2026-09-14 11:50)

When something is selected (animal, NPC, enemy, player) a **see-through coloured circle** sits on the ground under it.
The colour is the target's level relative to mine (the "con"):

| Colour | Target level vs mine | Meaning |
|--------|----------------------|---------|
| Grey   | 3 or more below      | too low for XP |
| Green  | 2 below              | easy |
| Blue   | 1 below              | comfortable |
| Yellow | same, or 1 above     | even |
| Orange | 2 above              | possible, but highly unlikely to beat |
| Red    | 3 above              | you should almost never beat it |
| Purple | 4 or more above      | you can almost never defeat it |

Rules
- The ring is translucent (about 35% alpha), 1.2x the target's capsule radius, flat on the ground, always visible through
  grass; it fades with distance but never hides; friendly NPCs use the same colours (their con tells you their level).
- Daniel 2026-09-14: "auto-attacking should mean a level 1 dies — you must use skills to live against a yellow, or even a
  blue unless extremely geared." Auto-attack alone loses to an even con; skills win it at ~1/3 HP cost.
- Combat tuning must MATCH the table: an even-level fight is 15–25 s and costs ~1/3 HP; orange should be a coin-flip at
  best; red a loss almost every time; purple a loss. Mob stats per level are tuned to make these outcomes true, not the
  colours to match the stats.
- XP multiplier by con lives in Content/Data/progression.json `con.bands` (updated to these offsets the same day). Purple
  pays 0 XP by the anti-towing rule (a level 5 towed through a level 40 zone earns nothing); Daniel may revisit.
- Same colours on the target frame's name text and level number.
