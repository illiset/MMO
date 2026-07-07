# Roadmap

Milestone-gated, not date-gated: a solo dev + Claude ship when phases are
done, not when a calendar says so. Every phase ends with something you can
*run* — no phase is "infrastructure only." Phases are sequential; the
cross-cutting tracks at the bottom advance opportunistically inside them.

**Guiding scope rule (from vision.md):** ship like Project Gorgon. One
faction deep beats three factions shallow — Great North is the reference
faction and leads every content phase; ML/HG stay data-complete and join
when GN's loop is proven.

---

## Phase 0 — Foundation ✅ COMPLETE 2026-07-01

**Goal:** design data is canonical, tooling exists, engine is installed.

- [x] Extract MMOStats.xlsx → validated JSON pipeline (`data/`, `tools/`)
- [x] Repo on GitHub (illiset/MMO)
- [x] Stat-minimums proposal drafted (283 numbers, 57 classes)
- [x] Stat proposal accepted — every class fully numbered, as live formulas
- [x] DPS Logic floor resolved: stays 1 (checksum-load-bearing); caster DPS
      get Logic 9 via the Volva idiom
- [x] UE 5.8 installed, VS 2022 toolchain installed

> **2026-07-02 pivot:** project adopted CodeSpartan MMO Kit (see
> mmokit-evaluation.md). Primary engine project: `C:\dev\MMOKitEval`
> (UE 5.7). Phase 1's dedicated-server box and Phase 4's accounts/login
> are now DONE via the kit: persistence server (SQLite) + world server
> verified end-to-end (account, login, character "Aldric" in DB,
> 2026-07-02). Skills: 532 authored/drafted across GN (see data/skills).
> Class-type→class-at-10 design recorded in quests.json.

## PHASE 0A — CORE MMO CONTROLS (official standard, set 2026-07-07)

**Standing control/keybind specification** — authoritative detail lives in
`controls.md`; this is the roadmap-level contract. Spec only as of
2026-07-07: nothing below is implemented unless listed under "Preserve."

**Preserve (already works — do not rebuild):**
- WASD movement
- LMB hold look (look without moving)
- RMB + LMB move-forward
- RMB mouse-look
- Mouse wheel zoom
- Space jump

**Add / verify:**
- A/D turn left/right, **not strafe** by default
- Q/E strafe left/right
- F interact
- Num Lock auto-run toggle
- C toggle crouch (**C is NOT character**)
- X sit
- Tab targeting
- Clear-target behavior
- Auto-attack behavior
- Main action bar: **12 slots**, hotkeys 1–9, 0, -, = (old-school MMORPG)
- MMO panel hotkeys:
  - U progression/reputation
  - I/B inventory
  - O character stats (moved off C)
  - P party
  - J skills
  - K spec tree
  - L quest log
  - M map
  - N guild
  - Escape settings menu
- Chat slash channel-switching: `/p `, `/g `, `/1 `, `/w Name ` + Space →
  raw command disappears from the input, mode indicator + channel color
  change, message sends to that channel (full spec in controls.md)

## Phase 1 — Engine bring-up ← YOU ARE HERE

**Goal:** the project exists in UE 5.8 and your design data flows into it.

- [x] UE 5.8 C++ project at `C:\dev\ThreeRealms` (outside OneDrive), own git
      repo (engine content is too heavy for the design repo) — module builds
- [x] Third-person character walking around a gray-box zone — mannequin body,
      classic-MMO controls (120°/s keyboard turn), code-spawned test arena.
      Playtest verdict 2026-07-01: "beautiful controls and speed"
- [x] **Data bridge:** TRGameDataSubsystem loads `Content/Data/*.json`
      (synced from this repo) at startup — spreadsheet→JSON→engine is
      end-to-end. Verified 2026-07-01: 3 factions / 75 classes / 48 races
- [ ] Dedicated server target builds; two clients connect and see each other
      move (Iris replication from day one — retrofitting networking kills
      MMO projects)

**Done when:** you and one friend walk around the same gray-box zone from
two machines.

## Phase 2 — First Kill (core combat loop)

**Goal:** the moment it becomes a game.

- [ ] Vertical-slice picks: **one GN zone**, **4 classes** (one per
      archetype — proposal: Knight / Squire / Bard / Ranger)
- [ ] Character creation v1 from real data: race → class gating, stat
      minimums, 100-point budget
- [ ] Combat v1: targeting, auto-attack, 3–4 abilities per slice class,
      mob AI (aggro, leash), death/respawn
- [ ] XP and levels 1–5

**Done when:** you create a Celtic Knight, kill a mob, and ding level 2 —
on the dedicated server.

## Phase 3 — First Dungeon (the thesis proven)

**Goal:** group PvE that *feels like DAoC* — this phase is the whole point
of the project; everything before it is scaffolding.

- [ ] Party system; roles interdepend (tank threat, healer mana economy,
      support buffs that matter, DPS that dies if it pulls aggro)
- [ ] One real dungeon: 3 pulls-with-personality + 1 boss with a mechanic
- [ ] Loot v1: gear with stats, drop tables, rarity
- [ ] Server-side persistence (database: characters, inventory, progress)
- [ ] Levels 1–10 tuned for the slice

**Done when:** 4 people clear the dungeon, wipe at least once, and someone
argues over loot.

## Phase 4 — First 10 Players (friends & family alpha)

**Goal:** strangers-adjacent humans playing without you at the keyboard.

- [ ] Accounts + auth (simple), one cloud-hosted server
- [ ] A way to distribute builds and patch them (simple launcher; Steam
      comes later)
- [ ] Crash/telemetry basics, /bug command
- [ ] Second slice class per archetype (8 playable classes)

**Done when:** 10 people play for a weekend and come back Monday unprompted.

## Phase 5 — First 100 (the Project Gorgon moment)

**Goal:** a devoted community seed.

- [ ] Content breadth: 2–3 GN zones, second dungeon, first raid-lite
      (single hard boss for 2 groups)
- [ ] More of GN's 25 classes playable; crafting/economy v1 if pull exists
- [ ] Steam page + Steam Playtest program
- [ ] Discord + dev blog cadence

**Done when:** 100 concurrent-ish devoted players, and the feedback shifts
from "it crashed" to "nerf Volva."

## Phase 6 — Sustainability (Early Access → launch ramp)

**Goal:** the business model turns on, exactly as designed.

- [ ] Free-trial content gate (FFXIV-style)
- [ ] Account portal + Stripe/Paddle subscription ($15/mo, billed outside
      Steam) — **not built before Phase 5; nobody bills an empty server**
- [ ] Steam F2P launch
- [ ] Live-ops cadence; Mystic Lands then Honorguard content waves as the
      post-launch drumbeat

**Done when:** subscriptions cover server costs — the game pays its own rent.

---

## Cross-cutting tracks (advance inside every phase)

- **Design data:** ability/spell tables, itemization tables, mob/encounter
  data — same xlsx→JSON→UE pipeline as stats. The spreadsheet stays
  Daniel's design cockpit.
- **Tooling / Claude bridge:** whatever lets Claude drive UE5 directly
  (Python remote execution, commandlets, MCP bridge) — built when friction
  demands it, not speculatively.
- **Art:** gray-box → Quixel/Fab kitbash → bespoke. No custom art before
  Phase 4; the first 100 players come for the loop, not the graphics.
- **Names:** game title (repo working title `three-realms`), zone names,
  server name. Zero urgency until the Steam page (Phase 5).

## Standing risks to respect

1. **Networking debt** — every system built single-player-first gets
   rebuilt. Server-authoritative from Phase 1 onward.
2. **Content appetite** — MMO players eat content faster than any solo dev
   makes it. The counter is systems-driven depth (DAoC-style class matrix,
   replayable dungeons), not content volume.
3. **Scope creep toward three factions** — GN-first is the discipline.
   ML/HG stay alive in data only until the GN loop retains players.
