# Skill requirement rules (Daniel's directive, 2026-07-14)

"Not every frontline will have a shield — make rules so that at level 10
players don't have skills they shouldn't, depending on what they pick."

## The problem, precisely

Each archetype file grants 8 shared **classtype** skills (levels 1–9), and
those carry forward after the level-10 class quest. Shield Bash is a
frontline classtype skill, so today every eventual Knight, Zealot, Wizard,
and Reaver would keep it forever, shield or not.

## Two rule layers (proposal)

### Layer 1 — `requires.equipment` (gear-gated, use-time)
Optional per-skill field:
```json
"requires": { "equipment": ["shield"] }
```
Enforced SERVER-SIDE at use time: no shield equipped → refusal ("Requires
a shield"), same path as range/cooldown refusals. This is the DAoC model
(styles gated by weapon type) and it solves the frontline case cleanly on
its own — any frontline WITH a shield can Shield Bash at any level; a
two-hander build simply can't press it. No level-10 special-casing needed
for gear skills.

### Layer 2 — `requires.classes` (identity-gated, grant-time)
Optional per-skill field:
```json
"requires": { "classes": ["knight", "reaver"] }
```
Enforced at the LEVEL-10 GRANT FILTER: when the class quest fires, the
character's skill list is rebuilt = (classtype skills whose
requires.classes is absent or includes the new class) + (the class file's
own 20). For skills that should leave you at the crossroads regardless of
gear — thematic identity, not equipment.

Both fields absent = universal within its tree (current behavior).

## Worked example — GN frontline classtype 8

| id | proposal |
|----|----------|
| frontline-t-strike | universal (no requires) |
| frontline-t-taunt | universal |
| frontline-t-guard-stance | universal |
| frontline-t-shield-bash | `equipment: ["shield"]` |
| (other 4) | audit against the same lens |

Note: Shield Bash's authored description already hedges "Bash with shield
or pommel" — under Layer 1 the pommel reading dies and it becomes a true
shield skill. If Daniel wants a universal bash pre-10, alternative: rename
classtype skill to Pommel Strike (universal, weaker) and give shield
classes a proper Shield Bash in their class files.

## NEEDED FROM DANIEL — the frontline gear matrix

Layer 1 is only as good as the class↔equipment truth. Fill/correct
(placeholders are guesses, NOT design):

| GN frontline class | shield? | weapon families |
|--------------------|---------|-----------------|
| Knight   | ? (guess: yes) | ? |
| Zealot   | ? | ? |
| Wizard   | ? | ? |
| Reaver   | ? | ? |

Same matrix eventually per archetype and per faction (ML/HG frontlines
too). Equipment vocabulary also needs Daniel's list (shield, one-handed,
two-handed, staff, bow, …) so `requires.equipment` values are canonical.

## Engine enforcement (future lane, needs approval)

1. Data: add `requires` to the skill schema; author frontline first.
2. Server: ServerUseSkill validates requires.equipment against the kit
   equipment array (already replicated — e.g. "Equipment:Sword_01") with
   a player-facing refusal.
3. Level-10 class quest: grant-filter rebuild per Layer 2. (The class
   quest itself isn't built yet — this rule rides along when it is.)
4. UI: action bar only offers skills the character can currently satisfy
   (grayed or hidden — Daniel's call).

## Status
- Rule shape: PROPOSED (this doc) — awaiting Daniel's matrix + vocabulary.
- No data files edited yet; no engine work started (per lane discipline).
