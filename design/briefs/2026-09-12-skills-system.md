# Brief: the skills system conversation (for an Opus design session)

**Owner:** Daniel. **Session model:** Opus. **Writes to:** this design repo only
(`design/skills-system-v1.md`); no changes to `data/` (generated from MMOStats) and none to the
game repo tonight.

## What exists (read these first)
- `design/GN-Frontline-Starter-1-9-v1.md` in the GAME repo (`C:\dev\MMOKitEval\docs\design\`) —
  the master program: normalized weapon damage model (Bastard Sword 100% / 2.4 s, stamina pool
  100 with 7/12 regen), threat system, 13 icon states, the Frontline 1–9 ladder (Auto Attack, Kick
  + Interrupts, Threat + Shout, Charge, Sweeping Slash …). Local copy: `design/frontline-gn-1-9.md`.
- `design/skill-requirements.md` — proposed two-layer `requires` schema (equipment at use time,
  class-at-level-10 grant filter). Waiting on Daniel's gear matrix and equipment vocabulary.
- `data/skills/great-north/archetypes/*.json` and `classes/*.json` — the 532 skills already
  extracted from MMOStats; `data/quests.json` rule: class TYPE is chosen at creation, levels 1–9
  are on the archetype tree, the true class is earned at level 10 via a class quest.
- In the engine today: slot 1 auto-attack, slot 2 Frontline Strike, slot 3 Shield Bash, data-driven
  from JSON, server-validated, independent cooldowns; 12-slot action bar; no resource costs
  enforced yet.

## Questions to settle (the doc should answer each with a decision, not options)
1. Acquisition: trainers, auto-grant on level, skill books, or spec points (DAoC-style lines)?
   PvE-first: what makes group roles matter?
2. Resource model: stamina / mana / focus per archetype; regen in and out of combat.
3. Cooldown philosophy and the global cooldown; how many actives per class by level 10 / 20 / 50.
4. What "Support" actually does moment to moment (songs, wards, debuffs) vs Healer.
5. Specialization after level 10: lines, respec cost, hybrid rules.
6. Ranged and pet classes: how they fit the auto-attack cadence model.
7. Equipment gating vocabulary (the thing `skill-requirements.md` is waiting on).

## Rules
- Never contradict the pillars in `CLAUDE.md` (PvE-first, no microtransactions).
- Numbers stay in MMOStats.xlsx; the doc proposes, Daniel edits the sheet.
