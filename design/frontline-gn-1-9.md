# Great North Frontline — Levels 1–9 (Daniel's design, 2026-07-16)

AUTHORITATIVE. Supersedes the old 8-skill classtype draft in
`data/skills/great-north/archetypes/frontline.json` (migration pending —
see "Data consequences"). Realm kits are DISTINCT: ML/HG frontlines will
be authored separately, no template crossover.

## Rules
- A. All GN Frontlines start with a **1-handed Bastard Sword**.
- B. **No shields or other weapons until the class pick at 10**
  (Knight / Zealot / Wizard / Reaver).
- C. Everyone is right-handed.
- D. Claude runs balancing math on all values (first pass below; Daniel
  approves).
- E. Everyone starts able to wear **cloth armor** (armor = helm, boots,
  legs, chest, gloves).

## Ladder (Daniel verbatim, condensed)
- **L1 — Auto-attack**: alternating 45° right-diagonal / left-diagonal
  slashes, swapping side every swing.
- **L1 — Northern Strike**: cd action skill, slight damage increase.
  Sword rises to near-vertical (slightly right), powerful down-left slash.
- **L2 — Focus**: self-buff — accuracy, speed, dodge, damage slightly up;
  sprinting costs no stamina while active; lasts X s; cd.
- **L3 — no skill**: unlock **leather armor**.
- **L4 — Kick**: interrupt — cancels enemy skill/spell if landed
  mid-animation, regardless of cast speed; cd.
- **L5 — Shout**: forced aggro/attention, establishes tank; landing an
  attack shortly after Shout boosts aggro by X; cd.
- **L6 — Charge**: 10 m gap-closer to selected enemy; aggro equal to
  Shout; damage equal to Northern Strike baseline; cd.
- **L7 — no skill**: unlock **cloaks**.
- **L8 — Sweeping Slash**: 360° AOE (step + pivot, horizontal slash);
  larger cd than Northern Strike; same baseline damage initially.
- **L9 — unlock Arming Sword** + **Northern Strike II** (damage rank-up).
  Quest: first 5-man instance (nomenclature: 5-man = "Dungeon", 20-man =
  "Raid"). Quest: learn fishing. After L9 quests complete AND level 10:
  quest to the race's local central castle to choose the Primary Class.
- Shields: possibly level 10+, class-dependent (not all Frontlines get
  one — consistent with skill-requirements.md gear gating).

## Balance math v1 (Claude, Rule D — Daniel approves/edits)
Anchors already live in-game: auto 15 dmg @ 2.0 s (7.5 DPS), player 200 HP,
mobs 120–150 HP, mob dps ~2.2 (raider). Stamina pool assumed 100,
regen ~5/s combat (system not yet built).

| Skill | Dmg | CD | Stam | Notes |
|-------|-----|----|------|-------|
| Auto | 15/swing @2.0s | — | 0 | 7.5 sustained DPS baseline |
| Northern Strike | 23 | 3s | 10 | +7.7 dps pressed on cd → ~15.2 rotation dps |
| Focus | — | 45s | 20 | +5% hit, +10% atk speed, +5% dodge, +5% dmg, 15s; sprint free |
| Kick | 0 | 15s | 10 | pure interrupt; no dmg keeps it a *decision*, not a rotation button |
| Shout | 0 | 8s | 8 | forced target 3s; attack within 4s = +bonus threat |
| Charge | 23 | 20s | 20 | 10m closer; threat = Shout; opener identity |
| Sweeping Slash | 23/target | 10s | 20 | 360°, ~4m radius; shines at 3+ targets |
| Northern Strike II | 32 | 3s | 12 | ×1.4 rank step; rotation dps → ~18.2 |

TTK sanity: L1 kit vs 120 HP mob ≈ 11 s; L9 kit (Charge opener + NS II +
Sweep + autos) ≈ 8–9 s single-target — leveling pace holds if mob HP
scales ~+8%/level. Solo threat: mob dps 2.2 vs player 200 = ~90 s of
tank-time; fine until mobs scale.

## Data consequences (for the implementation lane, NOT started)
- New skill kinds needed in schema: buff, interrupt, charge, aoe (strike/
  taunt/stance exist).
- Proficiency tables: armor (cloth@1, leather@3, cloak@7), weapon
  (bastard-sword@1, arming-sword@9) — per-level unlock data.
- Ranks: "II" convention; NS II replaces/upgrades NS at 9.
- OLD classtype 8: Strike→Northern Strike (rename+respec); Taunt→Shout
  (rework); **Shield Bash leaves classtype** (rule B — no shields pre-10;
  today's dev bar slot 3 must swap when this lands); Guard Stance,
  Intercept, Rending Cut, Battle Shout, Crushing Blow → Daniel to assign
  (class kits at 10+? cut?).
- Focus's sprint clause depends on: sprint feature (Shift — queued, not
  built) + stamina system (queued, not built).

## Open items for Daniel
1. Fate of the old five (Guard Stance / Intercept / Rending Cut / Battle
   Shout / Crushing Blow): class kits, later classtype levels, or cut?
2. Focus duration X and my proposed numbers — approve/edit.
3. Any additions for 1–9? (Claude's take: the ladder is already a FULL
   8-button bar by L9 — recommend adding at most ONE survival button,
   e.g. "Second Wind" self-heal at L7, or nothing at all.)
4. AAA slice target remains Northern Strike (was "Frontline Strike") —
   confirm the slice uses the NEW skill identity when Sol's prompt lands.
