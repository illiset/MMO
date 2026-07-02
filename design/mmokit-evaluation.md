# MMO Kit evaluation — 2026-07-01

**Verdict: ADOPT as the engine-side foundation.** Daniel owns CodeSpartan's
MMO Kit (+ MMO Kit Code plugin). Eval project at `C:\dev\MMOKitEval` (UE 5.7
— kit supports 5.1–5.7, NOT 5.8).

## Architecture (verified from installed files + docs/search)

- **UE dedicated server, authoritative** — gameplay in Blueprints (~950
  assets) over a thin C++ plugin (38 files: WebSockets, HTTP, buffs/ability
  subsystems, base GameInstance/PlayerController/PlayerState).
- **C# Persistence Server** (open source, github.com/CodeSpartan/
  MMOKitPersistenceServer, license requires kit ownership — we qualify):
  login/auth, character persistence, chat relay, guilds. **MySQL or SQLite**
  preconfigured (SQLite = zero-setup local testing).
- **OnlineSubsystemSteam wired in** — matches our Steam distribution plan.
- **Data-asset driven**: Equipment / BasicItem / Ability / Buff /
  CreatureAppearance primary asset types — our xlsx→JSON pipeline can
  GENERATE these, keeping the spreadsheet as the design cockpit.

## What it ships that we'd otherwise build for months

Login + character creation, grid inventory with drag-drop, equipment, loot,
chat, party, GUILDS, buffs/debuffs, mob AI (behavior trees), nameplates,
resurrection, GM tools (spawn mob / create item in-game), persistence,
maps (StartMap login flow, BasicMap, LargeMap), retargeting folder for
characters.

## Honest costs

1. **UE 5.7, not 5.8** — we lose mesh terrain until the kit updates.
   Acceptable; nothing shipped depends on 5.8.
2. **Blueprint-heavy gameplay** — Claude works fastest in text (C++/C#/data).
   Mitigation: extend via C++ subclasses + generated data assets;
   Blueprint wiring via editor when needed (computer-use verified working).
   Persistence server is C# — fully text-editable.
3. **Their patterns, not ours** — combat feel (classic controls, swing
   timers), PoE UI skin, and design-data must be ported INTO kit idioms.
   Est. days, not weeks; the kit's own grid inventory is already PoE-like.
4. Single-maintainer product — mitigated by open persistence server and
   full Blueprint source; worst case we own the code we bought.

## Migration plan (next sessions)

1. Build + run kit demo locally (SQLite): see login → char create → world.
2. Port design pipeline: generator that emits kit data assets (abilities,
   items) from `data/*.json`.
3. Port classic-MMO controls + camera onto BP_PlayerCharacter.
4. Recreate Knight + Shield Slam in kit ability system.
5. ThreeRealms 5.8 repo becomes reference/archive; MMOKitEval graduates to
   the real project repo once validated.

## Assets note

Kit demo characters serve as _DevPlaceholder content; Free Fantasy Weapon
Sample (owned) supplies real sword meshes. No purchases needed now.
