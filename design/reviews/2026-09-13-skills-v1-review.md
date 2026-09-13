# Review: Skills System v1 + 1–9 ladders + Dál Riata class kits (2026-09-13)

Reviewer: Opus subagent commissioned by the Fable session, against Daniel's decisions (nothing shared after
level 10; ladder 1–9 shared per archetype), the pillars, and the engine as it ships (12-slot bar; slot 1
auto-attack Bastard Sword 18 dmg @ 2.4 s A/B; slot 2 Frontline Strike `frontline-t-strike` 23/3 s; slot 3
Shield Bash `frontline-t-shield-bash` 38/6 s; no resource costs yet; master program stamina 100, 7/12 regen).

**Verdict: satisfied with fixes.** Safe to stand overnight (touches no data/ or engine). Fix 1–3 before
authoring against it.

1. **"Nothing shared after 10" is already broken.** §1 promises it; §10 re-homes the orphan skills to several
   classes ("Rending Cut | Reaver, Zealot") and the kits ship duplicates: Rending Cut I/II in Zealot AND Reaver,
   Crushing Blow in Knight AND Zealot, Exsanguinate in Knave AND Reaver, Rebuke in Squire AND Zealot (different
   effects, same name). §10's table also disagrees with the kits (Guard Stance, Battle Shout assigned to
   Zealot/Reaver but in neither tree). FIX: each orphan becomes either a ≤10 ladder skill or a per-class
   unique with its own name and effect.
2. **The doc sets disagree about level 9.** gn-ladders claims "seven actives plus auto-attack by level 9, in
   every archetype"; its own rhythm table says auto + 1 signature at L1 while all three ladders grant two;
   the Frontline ladder grants six actives; its L9 table credits the tank with Guard Stance, which §10 deleted.
   FIX: one L9 census table across the four archetypes.
3. **Rework of what ships.** "Shield Bash stays out of the ladder" retires shipped slot 3; slot 2 renamed to
   Northern Strike; damage anchors clash (ladders: auto 15 @ 2.0 s; §11: 100% @ 2.4 s; engine: 18 @ 2.4 s —
   same DPS, per-hit modifiers drift 20%); §3 assumes a second bar page at 20. FIX: keep the shipped ids and
   the 18 @ 2.4 anchor; renames are display names only; no second bar page in v1.
4. **Scope.** §9 says slice-four is "the only authoring lane that is open" (144 nodes), yet 504 nodes were
   authored across 14 classes (ten from prefix clones) and the "focused hour per class" excludes the invented
   systems: Rattled/Wound/Hollowing stacks, oath tracking, shapeshifting ("the most expensive thing
   proposed"), body-swap, Recant (rewinds 8 s of damage). FIX: mark those systems PROPOSED until engineering
   costs them; ship the slice lane first.
5. **Its own caps break.** "no class exceeds 2 Reactive skills or 2 Cornerstone cooldowns" — Zealot, Squire,
   Truthspeaker, Provacateur carry three; Frontiersman (240 s) and Volva (300 s) exceed the 60–180 s band;
   pets "capped at one active pet" vs "four thralls"; CC "mez, sleep and mass root live here, nowhere else" vs
   "only the Draoi brings mass roots". Undecided: do ladder skills count against caps? FIX: a validator pass.

**Lock (got right):** the topology (3 branches × 12 nodes, 4/4/4 grades, costs 1/2/4/6, gates 3/10/20 — all
13 trees conform); three response classes with interrupts off-GCD; "a passive is never a grant", validator-
enforced.

**Open items:** Daniel-only except these need engineering cost first: Truthspeaker oath tracking, Rattled
stacks, Wear It, Draoi shapeshifting, Pickpocket. Joint: the Concentration clash between docs, and the route
into MMOStats (CLAUDE.md: never hand-edit data/; §10 lists schema additions "not started").

**Progression v1:** not produced yet (no design/progression-v1.md as of 2026-09-13 01:00).
