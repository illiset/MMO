# Skills System v1 — Great North

**Status:** DECIDED with Daniel, 2026-09-12 (Opus design session, brief
`design/briefs/2026-09-12-skills-system.md`).
**Scope of this doc:** design repo only. No `data/` edits (generated), no game-repo
changes, no engine work. Numbers below are **proposals for MMOStats.xlsx** — Daniel
edits the sheet, the sheet stays the source of truth.
**Faction scope: Great North only** (Daniel, 2026-09-12). Mystic Lands and Honorguard
have 25 classes each on the spreadsheet and **zero skills authored** — no
`data/skills/` directory exists for either. The system below is written to apply to all
three realms, but nothing gets authored for ML or HG until GN's first dungeon proves the
system is fun. See §9 for what actually ships.
**Companion docs:** `frontline-gn-1-9.md` (the 1–9 ladder), `skill-requirements.md`
(superseded in part — see §7), `progression-v1.md` (owns level cap, XP, death).

---

## 0. Premise correction — what actually exists today

The brief says "the 532 skills already extracted from MMOStats." That is not what is
in `data/`. The real inventory:

| | count | source |
|---|---|---|
| Authored archetype templates | 4 × 8 = **32** | hand-written in `tools/generate_skills.py` |
| Authored class kits (Knight, Squire, Bard, Ranger) | 4 × 20 = **80** | hand-written in the same tool |
| Generated prefix clones (21 classes) | **420** | `generate_skills.py`, `status: "draft"` |
| **Total** | 532 | **none of it comes from MMOStats.xlsx** |

Zealot, Wizard and Reaver are the *same twenty skills* with "Fervent / Arcane / Grim"
pasted in front. So there are **8 real kits of design and 21 placeholders**, and the
skills pipeline is currently the one part of `data/` that is *not* spreadsheet-derived.

Two consequences this doc is built on:

1. A skills system that assumes 25 distinct kits would be fiction. §9 defines the
   production method that makes 25 real kits authorable by one person.
2. `tools/generate_skills.py` is scaffolding, not design. It should emit **tree
   skeletons** to be filled, not finished skills that look authored.

---

## 1. Acquisition — the class tree (Q1)

**Decision: levels 1–9 are a fixed shared ladder; level 10 opens a per-class node tree
bought with points. No trainers-as-gatekeepers, no skill drops.**

- **Levels 1–9: no choices.** The archetype ladder Daniel authored (Auto-attack,
  Northern Strike, Focus, Kick, Shout, Charge, Sweeping Slash, Northern Strike II)
  arrives on schedule. New players learn a kit, they don't build one.
- **Level 10: the class quest opens your class tree.** Three branches, 36 nodes, yours
  alone — nothing shared with other classes after 10 (Daniel, 2026-09-12).
- **Points: 1 per level from 10 to cap.** At cap 50 that is **41 points** against a
  **90-point tree**, so a character owns roughly 45% of their own tree. Choosing is the
  game; owning everything is not on the menu.
- **Spending is free-form and instant, out of combat, anywhere.** No trainer trip to
  spend. (Trainers still exist for respec — §5 — and for the class quest itself.)
- **Skill books and drops grant no combat power, ever.** They are the delivery mechanism
  for *secondary* skills only: fishing, crafting, tradeskills, languages. This protects
  the pillar promise — nothing that decides your combat strength sits behind RNG or a
  wallet.

### The anti-PoE law

Daniel's steer: *"a skill tree similar to PoE but not as cancerous, non weapon dependent
— a lot of customization but not overwhelming."* That becomes one hard rule governing
every node ever authored:

> **Every node changes a verb. If a node cannot be written as one sentence that changes
> how you play, it does not exist.**

No `+2% damage`. No `+7 Strength`. No filler travel nodes. A 36-node tree where every
node is a real decision beats a 1300-node tree where 1200 are arithmetic — and it is
readable without a build guide, which is the actual difference between "deep" and
"cancerous."

### Three node grades

| grade | what it does | share of tree |
|---|---|---|
| **Grant** | Gives a new **active** skill — a new button on the bar | 12 of 36 (4 per branch) |
| **Rank** | Upgrades a skill you already own (the "II" convention: Northern Strike → II → III) | 12 of 36 |
| **Modifier** | Changes how an owned skill behaves — *"Sweeping Slash also applies your bleed"*, *"Shout reaches two more enemies"*, *"your HoT ticks twice as fast at half strength"* | 12 of 36 |

Modifiers are where the customization lives, and they cost no action-bar space — which
is how a tree adds 40 levels of depth without adding 40 buttons (§3).

Two rules keep the grant column honest, and both are validator-enforced (§9):

> **A passive is never a grant.** A passive doesn't add a button, it changes how your
> existing skills behave — so it is a modifier node by definition. (Daniel,
> 2026-09-12.)

> **If a skill is a variation of something you already press, fold it in — unless you'd
> want both behaviors available in the same fight.** By default it becomes a rank or
> modifier on the skill it varies, not a thirteenth button. Shield Charge is not a new
> skill; it is what Charge does once you've specced for it. (Daniel, 2026-09-12: "yes
> unless it makes sense to.")

**The exception test.** A fold is wrong when it *takes something away*. After folding,
ask: can the player still do the original thing? If "Charge now knocks down" means you
can never charge *without* a knockdown — and a knockdown sometimes hurts you, because it
breaks your Support's mez on the adds — then the fold removed a choice, and the two
belong on separate buttons. Fold when the upgrade is strictly better; split when the
player needs to pick which version to use, and when.

The second rule has a side benefit worth stating outright: folds like Shield Charge →
Charge and Sundering Slam → Shield Slam keep the **level 1–9 ladder load-bearing at
level 40**, instead of a starting kit that turns into dead weight the moment the tree
opens.

### Tree topology (identical shape for all 25 classes, content never shared)

```
Branch (×3 per class)      nodes   cost each   branch cost
  Tier 1                     4         1            4
  Tier 2                     4         2            8
  Tier 3                     3         4           12
  Capstone                   1         6            6
                            ---                    ---
                            12                      30      ×3 = 90 points
```

Depth gates, per branch: **Tier 2** needs 3 points spent in that branch, **Tier 3**
needs 10, **Capstone** needs 20.

What 41 points buys — all three are legitimate builds:

- **Specialist:** one branch complete (30) + 11 points broad in a second. Capstone plus
  a real secondary.
- **Duelist:** 26 in one (capstone) + 15 in another (through Tier 3).
- **Generalist:** Tiers 1–2 across all three + a few Tier 3s. No capstone, most tools.

---

## 2. Resources (Q2)

**Decision: two pools, both on every character. No third bar.**

| | pool | in-combat regen | out-of-combat | notes |
|---|---|---|---|---|
| **Stamina** | 100 base, scales with Fitness stats | **7/s** | **12/s** | martial kits; also fuels sprint |
| **Mana** | 100 base, scales with Intelligence/Ancestral stats | **2/s** | **10/s** | casting kits |

- **Everyone has both.** Archetypes differ in which pool their kit *taxes*, not in which
  bars they have. This is already true in the data — the Knight's Holy Edge costs mana,
  the Bard's Refrain restores stamina — and making it universal removes a whole class of
  special cases.
- **Sitting doubles out-of-combat regen** (24/s stamina, 20/s mana). Combat ends 5 s
  after the last damage dealt or taken. Sitting is the oldest, cheapest verb in the genre
  for making downtime feel like a place rather than a loading screen.
- **In-combat mana regen is deliberately punishing (2/s).** A caster cannot brute-force a
  long fight alone. That single number is what makes a Support's mana refrain worth a
  group slot in PvE — the interdependence is designed in, not hoped for.
- **Concentration is not a third pool.** It is a *capacity*: how many sustained songs or
  wards a character can keep running at once. It does not regenerate; it frees up when
  you drop an effect. See §4.

---

## 3. Action economy — GCD, cooldowns, button budget (Q3)

Daniel's steer: *"some instant, some cds, some gcds."* So response type is a property of
the skill, not one global rule.

### Three response classes

| class | rule | who gets it |
|---|---|---|
| **Reactive** | Instant, **off the GCD**, own cooldown only | Interrupts (Kick), Intercept, panic buttons (Last Stand, Unbreakable). **Max 2 per class.** |
| **Standard** | Instant, **on the 1.5 s GCD**, own cooldown | Most actives: strikes, taunts, direct damage, quick heals, shouts |
| **Committed** | Wind-up or cast time, **interruptible**, own cooldown | Big casts, channels, heavy strikes (Crushing Blow), rez |

The reactive class exists for one reason: an interrupt that can be eaten by a global
cooldown is not an interrupt, it is a lottery ticket. Capping it at two per class stops
"off-GCD" from becoming the answer to everything.

**Damage still reads off the normalized weapon model.** A strike's `power` is a
multiplier on normalized weapon damage (Bastard Sword = 100% @ 2.4 s), so weapon choice
keeps mattering to your numbers even though it never gates your skills (§7).

**Casting is interruptible, and that is the PvE glue.** Ordinary damage causes 0.5 s of
pushback; a dedicated interrupt (Kick) fully cancels the cast and locks that skill for
5 s. This is precisely why a group needs a tank holding threat off the caster and a
Support interrupting the enemy caster — the roles are load-bearing because casting is
fragile.

### Cooldown bands

| band | range | purpose | budget |
|---|---|---|---|
| **Rotational** | 2–6 s | the things you press constantly | 3–4 per class |
| **Tactical** | 10–30 s | situational answers | 5–7 per class |
| **Cornerstone** | 60–180 s | the fight-defining button | **max 2 per class** |

Two cornerstones is a ceiling, not a target. A class with five 90-second buttons plays as
a slot machine of cooldown alignment rather than a character.

### Button budget

| level | owned actives | in-fight bar |
|---|---|---|
| 9 | 7 + auto-attack | 8 slots |
| 10 (class quest) | 10 + auto | 11 slots |
| 20 | ~13 | 12 slots — at the ceiling |
| cap (50) | ~15 | ≤12 in any one fight |

**The 12-slot bar is the design ceiling for a fight.** Growth past level 20 comes from
rank and modifier nodes (which change buttons you already have) rather than from new
buttons. A **second bar page unlocks at 20** for out-of-combat and situational skills
(rez, travel buffs, gathering, camouflage) so utility never competes for a rotation slot.
If a class needs a 13th combat button, the class is over-authored.

---

## 4. Support vs Healer (Q4)

Daniel: *"some of those support classes should be able to dps or just support or heal
depending on the one."*

**Decision: Support is the flexible archetype, and the class tree is how it flexes.**
Every Support class shares one thing — a Concentration spine — and its other two branches
point somewhere different per class.

### The Concentration spine (all six Support classes)

- Sustained songs and wards are **auras** with a 10 m radius, costing **1–2
  Concentration** each. The Support must stay with the group; positioning is the cost.
- **Concentration cap: 2 at level 10, 3 at 16, 4 at 22, 5 at cap.** Capacity, not a
  regenerating bar — dropping a song frees its cost immediately.
- Moment to moment: set songs before the pull → in the fight, **mez/root the adds,
  interrupt the enemy caster, debuff the boss, feed the party stamina and mana**.

### Per-class leanings (proposal — Daniel edits)

| class | branch 1 (spine) | branch 2 | branch 3 | plays as |
|---|---|---|---|---|
| **Bard** | Songs | Mending (HoTs, group regen) | Verse (direct damage) | support-healer |
| **Dracomancer** | Songs | The Drake (permanent pet) | Cacophony (AoE damage) | support-DPS |
| **Muse** | Songs | Inspiration (party offense) | Warding (party defense) | pure support |
| **Provacateur** | Songs | Derision (debuff stacking) | Control (mez, root, pull) | debuff-control |
| **Syndicate** | Songs | Shadow (utility, stealth, escape) | Sabotage (armor/resist strip) | utility-control |
| **Philosopher** | Songs | Economy (mana, stamina, cleanse) | Discourse (wards, absorbs) | sustain support |

### The guardrails that keep the other archetypes necessary

1. **Support healing is throughput-only** — HoTs and regen, never burst. A Support healer
   holds a 5-man through trash and dies to a boss pull. **Only Healers get emergency
   heals, and only Healers rez.**
2. **Support DPS caps at ~70–75% of a DPS class's sustained damage.** Enough that the
   damage branch is a real choice; never enough to make the DPS slot optional.
3. **Only Support crowd-controls.** Mez, sleep and mass root live here, nowhere else.

So a 5-man wants 1 Frontline / 1 Healer / 1 Support / 2 DPS — and each of those four
Support-flavored ways to fill the third slot changes how the group plays without any of
them being the wrong answer.

---

## 5. Specialization, respec, hybrids (Q5)

- **Specialization *is* the tree** (§1). There is no separate spec system.
- **Respec is free, unlimited, at any class trainer, out of combat.** PoE's respec pain is
  a large part of what Daniel called "cancerous," and in a PvE-first game you *want*
  players re-cutting their build to fill a group's missing role. Free, but frictioned by a
  trip to town.
- **Your build locks on entering an instance.** No re-specing mid-dungeon between bosses;
  encounters are designed against a committed build.
- **No multiclassing, no cross-class trees.** Your class is the tree, per Daniel's
  "nothing shared after 10." Hybridization happens *inside* the class, across its three
  branches.
- **Level 1–9 characters cannot respec because they have nothing to respec** — the ladder
  is fixed. The class quest at 10 is the first irreversible choice, and it stays
  irreversible: changing class means a new character.

---

## 6. Ranged and pets (Q6)

### Ranged

- **Bow cadence: 3.0 s draw, 130% normalized weapon damage per shot.** Slower and
  harder-hitting than the 2.4 s melee baseline.
- **You must be stationary to fire.** Movement cancels the draw. That is the whole trade:
  range for mobility, and it gives melee something to do about an archer.
- Ranged strike skills are **Standard** (on the GCD) and consume the draw.
- No ammunition counting. It is bookkeeping, not decision-making.

### Pets

Two grades, both capped at **one active pet**:

| grade | example | cost | behavior |
|---|---|---|---|
| **Temporary summon** | Ranger's Wolfpack | cooldown only (90 s), no upkeep | fights for a duration, expires |
| **Permanent companion** | Dracomancer's Drake | **1 Concentration** (Support) or **mana upkeep** (others); re-summon after death via a Committed cast | persists, follows, three commands |

- Commands: **attack / follow / passive**. Three, not a pet action bar.
- **Pets scale at 60% of their owner's damage** and hold their own threat.
- **Pets cannot taunt.** A pet class solos comfortably; it never replaces a Frontline in
  group content. That single restriction is what keeps the tank slot real.

---

## 7. Equipment gating and vocabulary (Q7)

Daniel, 2026-09-12: gating is **physically literal only**. This *partially supersedes*
`skill-requirements.md`.

### What survives

**Layer 1 (`requires.equipment`) survives, narrowed to the literal cases.** A skill is
gear-gated only when the gear *is* the skill. The canonical gate vocabulary is exactly
five values:

```json
"requires": { "equipment": ["shield"] }
```

| gate value | meaning | example skills |
|---|---|---|
| `shield` | a shield is equipped | Shield Bash, Shield Slam, Shield Charge, Phalanx |
| `bow` | a bow is equipped | Longshot, Rain of Arrows, Heartseeker |
| `staff` | a staff is equipped | staff-channel skills |
| `two-hand` | a two-handed weapon is equipped | overhead and cleave finishers |
| `dagger` | a dagger is equipped | backstab-family openers |

Enforced server-side at use time, same refusal path as range and cooldown ("Requires a
shield"). The action bar **greys** an unsatisfiable skill rather than hiding it — a hidden
button teaches nothing.

### What is deleted

- **Weapon *family* never gates a skill.** Sword, axe, mace and spear are interchangeable
  for every skill in the game; picking one is look, feel and damage profile, not a build
  tax. This is the direct meaning of "non weapon dependent," and it is the one place this
  design deliberately departs from DAoC.
- **Layer 2 (`requires.classes`) is deleted entirely.** It existed to stop a Wizard from
  keeping a Knight's shared skill. With per-class trees and nothing shared after 10,
  identity gating is *structural* — the skill simply is not in your tree. One fewer system
  to build.
- **The class × equipment matrix `skill-requirements.md` was waiting on is no longer
  needed** for skills. Armor and weapon proficiency still need per-class answers, but as
  gear progression (progression-v1), not as a skill prerequisite.

### Canonical vocabulary (for the schema)

- **Weapon families (8):** `sword`, `axe`, `mace`, `spear`, `dagger`, `bow`, `staff`,
  `shield`
- **Grip tags (2):** `one-hand`, `two-hand`
- **Armor classes (4):** `cloth`, `leather`, `mail`, `plate` — plus the `cloak` slot
- **Items sit inside families:** Bastard Sword and Arming Sword are both `sword`. The 1–9
  ladder's item unlocks (bastard-sword @1, arming-sword @9) are *proficiency* unlocks, not
  gates.

---

## 8. Worked example — the Knight tree

Built from the Knight's 20 authored skills plus re-homed orphans (§10) and proposed
rank/modifier nodes. **Auto-granted at the class quest (level 10, no points):** Shield
Slam, Crusader's Oath, Zealous Taunt.

### Branch A — Aegis *(protection; the main-tank build)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Guard Stance** | grant | trade damage for defense *(re-homed orphan)* |
| 1 | Shield Slam II | rank | +40% damage |
| 1 | Braced | modifier | blocking refunds 5 stamina |
| 1 | Retribution | modifier | blocked attacks are answered in kind *(was a passive)* |
| 2 | Aegis of the North | grant | plant your shield: party damage shield |
| 2 | Guard Stance II | rank | **Phalanx** — immovable: heavier defense, slower steps |
| 2 | Vigilant Guard | modifier | **Intercept** — in Guard Stance you take the blows aimed at your nearest ally |
| 2 | Guardian's Bond | modifier | your guarded ally takes 15% less damage *(was a passive)* |
| 3 | Unbreakable | grant | big mitigation cooldown *(Reactive)* |
| 3 | Aegis of the North II | rank | +50% shield, also absorbs magic |
| 3 | Shield Slam III | rank | **Sundering Slam** — ignores armor |
| **C** | **Bastion** | grant | become the wall: absorb for the whole party |

### Branch B — Crusade *(holy offense)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | Holy Edge | grant | blade wreathed in consecrated light |
| 1 | Northern Strike III | rank | ×1.4 over NS II |
| 1 | Zealous Fervor | modifier | Zealous Taunt also deals weapon damage |
| 1 | Consecrated Steel | modifier | Holy Edge refunds mana on kill |
| 2 | Consecrate | grant | sanctify the ground against foes |
| 2 | Sweeping Slash II | rank | +40% damage, +1 m radius |
| 2 | Holy Edge II | rank | +50% damage, burns undead |
| 2 | Righteous Momentum | modifier | Charge resets Holy Edge |
| 3 | Judgment of Steel | grant | a verdict delivered edge-first |
| 3 | Consecrate II | rank | larger ground, longer duration |
| 3 | Executioner's Verdict | modifier | Judgment +50% below 30% HP |
| **C** | **Deliverance** | grant | the blow that ends the battle |

### Branch C — The Line *(threat and party leadership)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Battle Shout** | grant | rally nearby allies' strength *(re-homed orphan)* |
| 1 | Shout II | rank | +50% threat |
| 1 | Hilt Work | modifier | **Pommel Strike** — Shield Slam also dazes |
| 1 | Shield Charge | modifier | **Charge** knocks down enemies you pass through — *but only while in Guard Stance*, so you choose when |
| 2 | Banner of Valor | grant | plant a banner: allies fight harder |
| 2 | **Crushing Blow** | grant | a heavy, slow strike *(re-homed orphan, Committed)* |
| 2 | Charge II | rank | 15 m range, shorter cooldown |
| 2 | Crusade | modifier | Banner also grants the party's offense surge |
| 3 | Banner of Valor II | rank | larger radius, adds stamina regen |
| 3 | Crushing Blow II | rank | +40% damage, staggers |
| 3 | Paragon of the Realm | modifier | your Banner and Shout linger as an aura *(was a passive)* |
| **C** | **Rally the Line** | grant | mass heal-over-time and courage |

**The Shield Charge node is the exception test in action.** A knockdown is not strictly
better — it breaks your Support's mez on the adds — so folding it into Charge outright
would take a choice away. Gating it behind Guard Stance gives the player both behaviors
off one button: charge in stance to knock down, out of stance to just close the gap.

**Tally:** all 20 of the Knight's authored skills and all 4 re-homed orphans appear
above — **12 as buttons, 12 as ranks or modifiers**. Nothing was cut, and the bar stays
inside budget.

Three readable Knights fall out of this: **Aegis capstone** (the immovable main tank),
**Crusade capstone** (the damage-dealing off-tank), **The Line capstone** (the group
buffer who holds the pull together). None is a trap; none is strictly best.

---

## 9. Production method and what actually ships

Daniel chose one full tree per class with nothing shared. Great North alone is
25 × 36 = **900 nodes**; all three realms would be **2,700**. It is tractable only if the
*shape* is fixed and only the *content* is authored:

1. **Topology is law** (§1): 3 branches × (4/4/3/1) nodes, per-branch cost 30, depth gates
   3/10/20. Never varies by class. One UI, one balance frame, one validator.
2. **Per-class authoring is a fill-in:** name 3 branches, then per branch place 4 grants,
   4 ranks and 4 modifiers. Start from the class's existing authored skills — the actives
   that deserve their own button become the grants, the passives become modifiers, and the
   variations fold into the skill they vary (§1). Roughly a focused hour per class.
3. **Order of work:** slice-four first (Knight, Squire, Bard, Ranger — the only classes
   with real kits), then the remaining Frontline three, then whichever archetype the first
   dungeon needs.
4. **The 420 prefix clones are scaffolding, not drafts.** Deleting "Fervent Shield Bash"
   costs nothing; the honest state is *21 classes unauthored*, and the data should say so.
   `generate_skills.py` should emit **empty tree skeletons** with `status: "skeleton"`
   rather than fake skills with `status: "draft"`.
5. **Validator additions** (`tools/validate.py`): branch costs sum to 30; every node is one
   of the three grades; every rank and modifier names a skill the tree can actually grant;
   **no node of grade `grant` has `kind: "passive"`**; no class exceeds 2 Reactive skills
   or 2 Cornerstone cooldowns; exactly 12 grants per tree. The button budget gets enforced
   by tooling, not by memory.

### What ships in the slice

Pillar 3 says ship like Project Gorgon, not like DAoC launch. At ~1 hour per class, all
75 classes is roughly two working weeks of *pure design* before a single icon, animation
or balance pass — which is exactly the DAoC-launch mistake in miniature. So:

| stage | scope | nodes | status |
|---|---|---|---|
| **Slice** | GN: Knight, Squire, Bard, Ranger | 4 × 36 = **144** | the only authoring lane that is open |
| **Next** | GN: remaining 21 classes | 756 | after the first dungeon proves the system |
| **Paper** | Mystic Lands + Honorguard, 50 classes | 1,800 | spreadsheet only; not authored, not scheduled |

The slice four are deliberately one per archetype — Knight (Frontline), Squire (Healer),
Bard (Support), Ranger (DPS). That is a complete 5-man composition, which means the first
dungeon can be designed, played and tuned against a real group without any of the other
21 classes existing yet. They are also the only four with authored kits today, so the
slice costs no new skill invention — just tree placement.

**Levels 1–9 have their own gap:** only the GN Frontline ladder is written. Healer,
Support and DPS ladders (3 × ~8 skills) are unwritten and block the slice just as hard as
the trees do — Squire, Bard and Ranger cannot be played from level 1 without them.

---

## 10. Consequences for existing docs and data

**Resolves `frontline-gn-1-9.md` open item #1 — the orphaned five.** With nothing shared
after 10 they cannot live in a trunk, so they are re-homed into class trees as proposals:

| orphan | goes to |
|---|---|
| Guard Stance | Knight (Aegis T2), Zealot, Reaver |
| Intercept | Knight (Aegis T2), Squire |
| Rending Cut | Reaver, Zealot |
| Battle Shout | Knight (Line T1), Zealot |
| Crushing Blow | Knight (Line T2), Reaver, Zealot |

None remains in the 1–9 ladder. Shield Bash stays out of the ladder (rule B: no shields
before 10) and reappears as a `requires.equipment: ["shield"]` node in the trees of shield
classes.

**Answers open item #2:** Focus = 15 s duration, 45 s cooldown, 20 stamina, with the
stamina model now fixed at 100 pool / 7 per second in combat / 12 out.

**Schema additions needed** (data lane, not started): tree node objects (`grade`,
`branch`, `tier`, `cost`, `requires.pointsInBranch`, `modifies`), `response`
(`reactive` | `standard` | `committed`) on every skill, `band`
(`rotational` | `tactical` | `cornerstone`), and `concentration` cost on sustained Support
effects.

**`skill-requirements.md` should be marked partially superseded:** Layer 1 narrowed to
five literal gates, Layer 2 deleted, gear matrix no longer blocking.

---

## 11. Numbers for MMOStats (proposal)

| knob | proposed value |
|---|---|
| GCD | 1.5 s |
| Reactive skills per class | max 2 |
| Cornerstone cooldowns per class | max 2 |
| Stamina pool / regen | 100 / 7 per s combat / 12 per s out / ×2 sitting |
| Mana pool / regen | 100 / 2 per s combat / 10 per s out / ×2 sitting |
| Combat-exit delay | 5 s |
| Tree points | 1 per level from 10 (41 at cap 50) |
| Tree cost | 90 (3 branches × 30) |
| Node costs | T1 = 1, T2 = 2, T3 = 4, capstone = 6 |
| Depth gates | T2 at 3 in branch, T3 at 10, capstone at 20 |
| Concentration cap | 2 at L10, 3 at L16, 4 at L22, 5 at cap |
| Action bar | 12 slots; second page at L20 |
| Melee baseline | Bastard Sword 100% @ 2.4 s |
| Bow baseline | 130% @ 3.0 s, stationary |
| Pet damage | 60% of owner; cannot taunt |
| Support damage ceiling | 70–75% of a DPS class sustained |
| Respec | free, at trainers, locked on instance entry |

---

## Open items for Daniel

1. **Support leanings table (§4)** — six classes, my read of each name. Bard as the
   healer-ish one and Philosopher as the mana-economy one are guesses about your intent.
2. **Level cap 50** is assumed here for the point math; `progression-v1.md` owns the real
   answer. If the cap moves, points = cap − 9 and the 90-point tree may need to move with
   it.
3. **The Knight tree (§8)** is the pattern for the other 24. If the branch naming
   convention or the 4/4/4 grant/rank/modifier mix is wrong, it is much cheaper to fix
   now.
4. **The three missing 1–9 ladders** (Healer, Support, DPS) block the slice as hard as
   the trees do — Squire, Bard and Ranger have no levels 1–9 to play. These want the same
   treatment the Frontline ladder got: your design, skill by skill, with me running the
   balance math.
5. **Deleting the 420 prefix clones** (§9.4) — say the word and it becomes a tools lane
   task, not something I do unasked.
6. **GN's "Wizard" is a Frontline class.** Its clone kit is a plate-and-taunt tank wearing
   a caster's name. Before its tree is authored: battle-mage, or a naming artifact from the
   sheet?
