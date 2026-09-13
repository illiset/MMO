# Progression v1 — leveling, XP, death, gear, the gate

**Status:** DECIDED with Daniel, 2026-09-13 (Opus design session, brief
`design/briefs/2026-09-12-progression.md`).
**Scope of this doc:** design repo only. No `data/` edits (generated), no game-repo
changes, no engine work. Numbers below are **proposals for MMOStats.xlsx** — Daniel
edits the sheet, the sheet stays the source of truth.
**Companion docs:** `skills-system-v1.md` (owns the class tree, resources, action
economy), `gn-ladders-1-9-v1.md` and `frontline-gn-1-9.md` (own levels 1–9),
`names/great-north-places.md` (owns Dál Riata's geography), `roadmap.md` (owns phases).

---

## 0. Premise corrections — what changed under this brief

The brief was written before `skills-system-v1.md` landed. Three of its assumptions
are now stale, and one of its facts was never true.

1. **There is no level-22 content ceiling.** The brief's world had 532 authored skills
   topping out at level 22. `skills-system-v1.md` §0 established that 420 of those are
   prefix clones — scaffolding, not design — and replaced the model with a **36-node
   per-class tree, 90 points, bought at 1 point per level from 10 to cap**. Content now
   *scales with the cap* instead of ending at 22.
2. **The cap is no longer a free choice.** The tree's depth gates (capstone needs 20
   points in one branch) mean a cap below 29 makes capstones mathematically unreachable
   and the build game imaginary. See §1.
3. **Levels 1–9 gear is already decided**, identically across all four archetypes
   (cloth@1, leather@3, cloak@7, weapon rank-up@9). This doc owns only what happens
   *after* 10 — which is where `mail` and `plate` have to be placed. See §5.
4. **"No quest XP yet" is an engine statement, not a design one.** Dál Riata already
   has an authored quest arc (`names/great-north-places.md`): four archetype starts at
   1–9, a raider camp at 8–10, a 5-man Dungeon at 9–15, and Portcorr as the boat out.
   The XP model below assumes that arc exists.

---

## 1. Level cap and the XP curve (Q1)

**Decision: Early Access caps at 30. The destination cap is 50. The curve is authored
for 50 now, so raising the cap never requires a re-tune.** (Daniel, 2026-09-13.)

### Why 30, and why not lower

Tree points = `cap − 9`, against a 90-point tree:

| cap | points | % of tree | capstone? | what a character can actually build |
|---|---|---|---|---|
| 20 | 11 | 12% | **never** | Tier 1 nodes only — the tree barely opens |
| 22 | 13 | 14% | **never** | Tier 3 in one branch at best |
| **30** | **21** | **23%** | **yes** | **exactly one capstone — a real endpoint** |
| 40 | 31 | 34% | yes | capstone + 11 points elsewhere |
| 50 | 41 | 46% | yes | the full design: specialist / duelist / generalist |

Level 30 is the lowest cap at which the class tree is a game rather than a preview: 21
points buys exactly one capstone (20 in a branch) with one to spare. "Reach your
capstone" is a clean, nameable Early Access goal. Everything above 30 is then a real
content beat rather than a patch note.

**This resolves `skills-system-v1.md` open item #2.** Its point math assumed 50 and
stands unchanged — 41 points at cap, 90-point tree, no resize needed.

### The curve

Replace the engine's `XpToLevel = XpPerLevelBase × level` (a straight line, which makes
every level cost the same ~12 kills). The shipped curve reaches level 50 in **4.2
hours**; the target is **150**.

```
kills(L)      = 6.29 × L^1.3        even-con normal kills to clear level L
baseMobXp(L)  = 2 + 8L              XP from an even-con normal mob of level L
XpToLevel(L)  = kills(L) × baseMobXp(L)      rounded to legible numbers
```

`baseMobXp` is the authored Rimethrall progression extended, not a new invention:
Frost Raider 10, Huntress 18, Warden 26 are exactly `2 + 8L` at levels 1, 2, 3.

| level | XP to next | even-con kills | cumulative hours | milestone |
|---|---|---|---|---|
| 1 | 60 | 6 | 0.0 | plain clothes, first signature skill |
| 2 | 280 | 15 | 0.0 | |
| 3 | 680 | 26 | 0.2 | **leather** |
| 7 | 4,600 | 79 | 1.4 | **cloak** |
| 9 | 8,100 | 109 | 2.6 | weapon rank-up; **Dungeon opens (9–15)** |
| 10 | 10,500 | 125 | **3.4** | **class quest — tree opens — TRIAL ENDS** |
| 15 | 26,000 | 213 | 8.9 | top of the first Dungeon's band |
| 16 | 30,000 | 231 | 10.4 | Concentration 3 |
| 20 | 50,000 | 309 | **17.6** | **plate** (Frontline) / **mail** (Support) |
| 22 | 62,500 | 350 | 22.0 | Concentration 4 |
| 29 | 117,000 | 501 | 42.1 | first capstone possible |
| 30 | 127,000 | 523 | **45.6** | **EARLY ACCESS CAP** |
| 40 | 245,000 | 761 | 89.3 | |
| 49 | 390,000 | 991 | 143.1 | |
| 50 | — | — | **150.0** | **DESTINATION CAP**, Concentration 5 |

**Total XP 1→50: 6,005,620.**

**Brief's target question, answered:** level 10 at **3.4 h**, level 20 at **17.6 h**,
Early Access cap at **45.6 h**, destination cap at **150 h**.

### Three properties worth stating

- **The hours are mixed-source, not kill-only.** The kill column is the *yardstick* used
  to set absolute XP values; it assumes quests, discovery and dungeons deliver roughly
  comparable XP per hour (a quest chain costs travel and turn-in time too). A player who
  refuses to quest takes longer, and should.
- **Early levels stay fast on purpose.** Level 2 in six kills, leather by 0.2 h, the
  whole 1–9 ladder in 2.6 h. The trial has to hook inside one sitting.
- **Carry-over survives.** The engine already carries surplus XP across a ding; keep it.

### Curve lives in data, not in a C++ constant

`XpPerLevelBase = 100` in `TRCombatComponent.h` becomes a per-level **table** shipped in
`Content/Data/`, sourced from MMOStats like everything else. A 50-row table is cheaper
than a formula the designer cannot edit, and it lets the curve be re-shaped without a
build. (Implementation lane, not started.)

---

## 2. XP sources, con, grouping, rested (Q2)

### The mix, over a full 1→50 run

| source | share | notes |
|---|---|---|
| **Kills** | 55% | the floor activity; always available, never the fastest |
| **Quests** | 25% | the directed path; carries the story and the zone tour |
| **Dungeon completion** | 12% | boss kills plus a **completion bonus** worth ~1 full clear again |
| **Exploration / discovery** | 8% | one-time, per named location |

Discovery XP is the cheapest possible reason to look at a world someone hand-built, and
Dál Riata now has named coves, fords, mills and a strait to find. One-time awards,
scaled to the location's level band, no repeat farming.

### Con table (XP by level difference)

`diff = mobLevel − yourLevel`

| diff | con | XP |
|---|---|---|
| ≤ −9 | grey | **0%** |
| −8 … −6 | green | 40% |
| −5 … −3 | blue | 70% |
| −2 … +2 | yellow (even) | **100%** |
| +3 … +5 | orange | 130% |
| +6 … +8 | red | 170% |
| ≥ +9 | purple | **0%** |

Grey at 0% is what stops a level 30 from farming the starter camp; purple at 0% is what
stops a level 5 from being towed through a level 40 zone. **Every group member's XP is
computed against their own level**, which makes power-levelling structurally impossible
without banning anything.

### Grouping — the PvE-first rule

**Kill XP is not divided.** Every member of a group receives the *full* XP value of
anything the group kills, plus **+5% per additional member, capping at +20% at five**.

This is the single most important number in the document for Pillar 1. A split-XP model
makes grouping a sacrifice, and every "PvE-first" game that splits XP quietly teaches its
players to solo. Undivided XP means a five-man kills faster, pulls bigger, dies less, and
earns more — so the group is simply the better way to play, which is the thing the whole
project exists to prove. The 150 h target is measured **solo**; a committed group should
see roughly 1.5–2.5×.

The cap at five is shaped to the 5-man Dungeon composition (`skills-system-v1.md` §4:
1 Frontline / 1 Healer / 1 Support / 2 DPS), and it is graduated rather than flat because
at a hundred players the duo and the trio are far more common than the full group — a bonus
that only pays the fifth player pays almost nobody.

### Rested XP — yes, with a caveat flagged

**Rested XP accrues while logged out inside a settlement** (Dunadd, the four starts, any
inn), grants **1.5× kill XP** until the pool drains, and caps at **one full XP bar** — a
single level's worth, no more. (Daniel, 2026-09-13: *"yes but only for a full bar's worth."*)

> **Pillar check, stated openly.** Pillar 2 says "zero XP boosts." That clause is about
> *monetization* — nothing that affects XP may ever be purchasable. Rested XP is earned by
> logging off in a bed, and its whole purpose is to let a player with a job keep pace with
> a player without one. It brushes the letter of the pillar while serving its spirit, so it
> is called out here rather than buried. **Daniel took it, 2026-09-13: in, one bar.**

---

## 3. Stat growth, and the level-10 trap (Q3)

### The problem, measured

Two facts in the data collide:

1. Each archetype's stat minimums sum to **exactly 100** — the entire creation budget.
   Races carry only `allowedClasses`, no stat modifiers. **Every Great North Frontline
   therefore begins statistically identical, and race is mechanically inert.**
2. Every class needs **+10 points over its archetype baseline** to meet its own minimums —
   **Volva needs +13, Hundr +12** — concentrated in five specific stats.

So as authored, the level-10 class quest is a **gate a player can fail by accident**,
nine levels after the choice that doomed them, with no warning and no fix.

### Decision

**Growth: +2 stat points per level, levels 2–50 (+98 by cap, +18 by level 10).**

| stream | per level | who allocates | why |
|---|---|---|---|
| **Automatic growth** | +1 | the system, by **archetype profile × race rate** (§3a) | your archetype keeps you viable; your race makes you *someone* |
| **Discretionary** | +1 | the player | the only stat choice in the game; free respec at a trainer, matching `skills-system-v1.md` §5 |

**The class quest grants its minimums; it does not check them.** Completing the class
quest raises any stat below the class minimum up to it. Class stat minimums become *a
description of what the class makes you*, not a filter you can fail.

This is the load-bearing call in this section, and it follows directly from Daniel's own
framing of the gate: *"Nobody loses a character."* The race × class matrix already does
the gating, at creation, where the player can see it. A second hidden gate nine levels
later gates nothing except goodwill.

---

## 3a. Races: different bases, and different growth rates

**Decision: every race carries both a starting stat profile and a per-stat growth rate.**
(Daniel, 2026-09-13: *"races should have stat base difs and gain them at dif speeds."*)

This is what gives creation consequences, and it fixes the deeper problem at the same
time — race is currently pure gating with no mechanical existence.

> **No stat allocation at character creation.** (Daniel, 2026-09-13: *"no modding stats at
> char creation."*) There is no point-buy screen and no slider. Creation stays exactly the
> flow that already ships — class type → race → name — and your starting stats fall out of
> those two picks. The variance below is carried entirely by *which race you chose*, not by
> numbers the player types in. The one stat decision in the game is the +1 discretionary
> point per level (§3), and it is reversible at any trainer.

### The two halves

**1. Base profile.** A signed modifier applied at creation, on top of the archetype
minimums. Each race's profile **sums to zero**, so the 100-point budget is untouched and
no race starts stronger — only differently shaped. Range −2 to +3 on any one stat.

**2. Growth rate.** Each race marks **3 Swift** stats and **3 Slow** stats; the other ten
are Even. The automatic +1 per level is allocated by:

```
weight(stat) = archetypeMinimum(stat) × raceRate(stat)
raceRate:  Swift 1.75  ·  Even 1.00  ·  Slow 0.50
```

normalized so the stream delivers exactly one point per level. Fractions accumulate and
pay out as whole points — deterministic, no RNG.

**Every race gains exactly the same 49 automatic points from level 2 to 50.** Races differ
in *where* those points land, never in how many they get. That is the whole balance
argument: identity without power creep.

### What it actually feels like

Points gained in a stat across levels 2–50, Frontline:

| stat | no race tilt | Germanic | Hillback | Fae | Romance |
|---|---|---|---|---|---|
| strength | 3.4 | **5.6** | **5.7** | 1.7 | 1.6 |
| constitution | 2.5 | 2.3 | **4.1** | 1.2 | 2.3 |
| elements | 2.5 | 1.1 | 1.2 | **4.2** | 2.3 |
| logic | 3.4 | 3.2 | 3.3 | 3.3 | **5.6** |

A Germanic Knight and a Fae Knight end level 50 about **four points apart in strength** on
a stat that grows from roughly 7 to 12 over the run — a third of its total growth. Clearly
felt in play, never enough to make a race the "wrong" pick for a class it is allowed.

Two guardrails make that safe:

- **Affinities are authored to match the race × class matrix.** A race that cannot play a
  martial class is never Swift in Strength. Validator rule: every Swift stat must be a key
  stat of at least one class the race is allowed to take.
- **Nothing can brick a build**, because the class quest grants its minimums rather than
  checking them (§3). A Slow stat can never lock you out of your own class quest. The two
  decisions were designed to compose.

### The 16 Great North races

| race | base profile | Swift | Slow |
|---|---|---|---|
| **Celtic** | spirit +1, survival +1, impulse +1, detail −1, calmness −1, logic −1 | spirit, survival, impulse | detail, calmness, logic |
| **Germanic** | strength +2, conditioning +1, finesse −1, elements −1, calmness −1 | strength, conditioning, discipline | elements, finesse, calmness |
| **Romance** | knowledge +2, logic +1, strength −1, survival −1, impulse −1 | knowledge, logic, detail | strength, survival, impulse |
| **Hellenic** | athleticism +2, logic +1, spirit −1, constitution −1, wisdom −1 | athleticism, logic, calmness | spirit, constitution, wisdom |
| **Slavic** | constitution +2, conditioning +1, finesse −1, logic −1, elements −1 | constitution, conditioning, survival | finesse, logic, elements |
| **Baltic** | awareness +2, survival +1, strength −1, knowledge −1, discipline −1 | awareness, survival, finesse | strength, knowledge, discipline |
| **Armenian** | spirit +2, discipline +1, athleticism −1, impulse −1, awareness −1 | spirit, discipline, wisdom | athleticism, impulse, awareness |
| **Severus** | detail +2, calmness +1, strength −1, conditioning −1, spirit −1 | detail, calmness, knowledge | strength, conditioning, spirit |
| **Mythic** | elements +3, wisdom +1, strength −1, conditioning −1, constitution −2 | elements, wisdom, logic | strength, conditioning, constitution |
| **Sidhe** | finesse +2, awareness +2, strength −1, conditioning −1, constitution −2 | finesse, awareness, impulse | strength, conditioning, constitution |
| **Alfar** | survival +2, impulse +1, spirit +1, knowledge −1, calmness −1, conditioning −2 | survival, impulse, spirit | knowledge, calmness, conditioning |
| **Hillback Dwarves** | constitution +2, strength +2, athleticism −1, elements −1, impulse −2 | constitution, strength, detail | athleticism, elements, impulse |
| **Woodling** | finesse +2, survival +1, awareness +1, strength −1, conditioning −1, discipline −2 | survival, finesse, knowledge | strength, conditioning, discipline |
| **Gobbledrift** | impulse +2, athleticism +1, detail +1, wisdom −1, discipline −1, strength −2 | impulse, detail, athleticism | strength, wisdom, discipline |
| **Fae** | elements +3, spirit +2, strength −1, athleticism −1, conditioning −1, constitution −2 | elements, spirit, calmness | strength, conditioning, constitution |
| **Centaur** | athleticism +2, conditioning +2, finesse −1, detail −1, elements −2 | athleticism, conditioning, strength | finesse, detail, elements |

All sixteen validate: every base sums to zero, every race has exactly 3 Swift and 3 Slow
with no overlap, and **every one of the 16 stats is Swift for at least one race** — so no
stat is orphaned.

**Celtic is deliberately the flattest profile.** It is the first zone's race and the one a
new player meets first; the starter race should not be the one that teaches you stat
extremes.

This is an **MMOStats.xlsx + extractor change** — 16 rows, Great North only. Mystic Lands
and Honorguard stay unauthored until GN's loop proves out, per the scope pillar.

### Data gap to fix in the sheet

**Seven of eleven Great North DPS classes have no class stat minimums authored** —
Whisper, Veil Tamer, Relic Master, Ranger, Pankrator, Frontiersman, Draoi. They compute
as `+0` against the archetype baseline, which is why DPS looks cheaper than every other
archetype. `tools/validate.py` should treat a class with no `statMinimums` as an **error**,
not a silent pass.

---

## 4. Death and recovery (Q4)

**Decision: XP debt. No de-levelling, ever.** (Daniel, 2026-09-13.)

| rule | value |
|---|---|
| Debt incurred on death | **10% of your current level's XP requirement** |
| Level loss | **never** — debt cannot drop you below your current level's threshold |
| Paying it off | **50% of XP earned** clears debt, 50% still advances you |
| Healer resurrection | clears **75%** of outstanding debt, restores you where you fell |
| Self-release | rally point at the nearest settlement, full debt stands |
| **Below level 10** | **no debt at all** — the trial never punishes |
| Durability / repair costs | **none.** One death cost, not three |

Worked example at level 30: debt is 12,700 XP, about 52 even-con kills at the half rate —
roughly 22 minutes. Take a Healer's rez and it is about 5 minutes.

**Why this shape.** Death costs *time*, never *progress* — the player is always moving
forward, just slower, so no session ends net-negative. And the rez number is doing real
design work: resurrection is Healer-exclusive (`skills-system-v1.md` §4), so a group with
a Healer recovers from a wipe four times faster than one without. That is the
interdependence pillar paying rent, without a single punitive mechanic.

The DAoC alternative — real XP loss and con loss — is the most-criticised thing about the
game this project succeeds. Feels weighty for ten minutes, then teaches players not to
attempt anything hard. Explicitly rejected.

**Feeds lane M6 (player death).** M6 needs: a death state, a rally point per settlement,
the debt field on the character record, and the Healer rez interaction.

---

## 5. Gear progression (Q5)

### The armor ladder

Levels 1–9 are already fixed and identical for all four archetypes
(`gn-ladders-1-9-v1.md`). This doc places **mail** and **plate**, which were left
unassigned in the `cloth / leather / mail / plate` vocabulary:

| archetype | 1 | 3 | 7 | 10 (class quest) | 20 | ceiling |
|---|---|---|---|---|---|---|
| **Frontline** | cloth | leather | cloak | **mail** | **plate** | plate |
| **Healer** | cloth | leather | cloak | **mail** | — | mail |
| **Support** | cloth | leather | cloak | — | **mail** | mail |
| **DPS** | cloth | leather | cloak | — | — | **leather** |

DPS stays in leather for life, on purpose: their 1–9 ladder already established that
dodge is how they survive (*"you have no armor; this is how you live"*). Their power comes
from tier within leather, not from a heavier class.

Level 20 carries the armor step for two archetypes because it has nothing else left: the
`2026-09-13-skills-v1-review.md` fix list removed the second action-bar page from v1, so
20 was an empty level until this table gave it plate and mail.

### What a level-10 character actually wears

Full leather, a cloak, their level-9 weapon rank-up (Arming Sword / Yew Staff / Ash Spear
/ bow-or-sword), and **the first mail or class piece handed over by the class quest**. The
class quest is the first time a character looks like their class rather than like their
archetype — which is exactly the beat Daniel asked the trial to end on (§6).

### Drops vs crafted

| path | role |
|---|---|
| **Drops** | the aspirational path. Dungeon set pieces and boss uniques. Bind on pickup. |
| **Crafted** | the reliable path. Best-available gear *between* dungeon tiers, fills the slots drops refuse to, freely tradeable. |

Crafting is the small-population glue: with 100 players, a market where crafters matter is
worth more than another loot table. Crafted gear is never best-in-slot at a tier's top, and
never worse than the tier below's drops.

**Recipes and secondary skills come from books** — the one place `skills-system-v1.md` §1
allows books to exist, because they grant no combat power.

### Tiers across the run

| band | levels | source |
|---|---|---|
| T0 | 1 | plain clothes — the pillar's starting image |
| T1 | 3–9 | quest rewards, vendor leather, first crafted pieces |
| T2 | 10–15 | class quest kit + the first Dungeon's set |
| T3 | 16–30 | zone drops, crafted, Dungeon tier 2 |
| T4 | 31–50 | later zones, Dungeon tier 3 |
| T5 | cap | Raid (20-man) and tiered Dungeon sets — see §7 |

---

## 6. The free-trial gate (Q6)

**Decision, Daniel verbatim, 2026-09-13:**

> "Trial = any class type, the 1 to 9 ladder, the travel and the level-10 class quest to
> choose your true class; everything after that is subscription. Make the class quest
> itself the climax. It should end with the class granted and the first node of the new
> tree shown or handed over, so the paywall arrives one beat after the best moment of the
> trial, not instead of it. Say what a locked character can still do: log in, stand in
> Dunadd, chat, but no XP, no tree points, no boat. Nobody loses a character for not
> subscribing, they just can't move forward."

### What the trial contains

Character creation in any of the four class types · all four archetype starts (Lissban,
Rinnbeg, Tobarglas, Dromcairn) · the full 1–9 ladder · the raider camp at 8–10 · **the
5-man Dungeon at its 9–10 band** · the journey to Dunadd · **the level-10 class quest,
completed** · the class granted · **the first tree node handed over**.

That is roughly **3.4 hours** of critical path (§1), plus quests and the Dungeon — call it
a **5–7 hour trial** that ends on the best moment the game has.

### The gate is a boat

`names/great-north-places.md` already built it: **Portcorr is the boat out of Dál Riata.**
The subscription gate needs no invented fiction and no invisible wall — the trial is an
island, and the boat is the sub. A locked player standing on the quay at Portcorr
understands the offer without a single line of UI copy.

### What a locked character can do

| can | cannot |
|---|---|
| log in, forever | earn XP |
| stand in Dunadd, walk Dál Riata | earn or spend tree points |
| chat on every channel | board the boat at Portcorr |
| keep every character, forever | progress past level 10 |

**No character is ever deleted for not subscribing.** A lapsed subscriber becomes a locked
character, not a lost one.

### The Dungeon is inside the trial

**Decided, Daniel 2026-09-13.** The level-9 ladder step includes the quest into the first
5-man, so the Dungeon sits inside the trial at its **9–10 band**, and remains a gear run up
to 15 for subscribers. The 5-man *is* the thesis — Phase 3 is "the whole point of the
project" in the roadmap's own words — so the trial has to let a player *do* group PvE, not
read about it.

**Tuning consequence:** the Dungeon's first clear must be achievable by a level 9–10 group.
Its 9–15 band is a content band, not a difficulty ramp that locks the boss behind level 13.
This needs the world/encounter lane to agree.

---

## 7. Post-cap progression (Q7)

PvE-first, and none of it may become a second gear treadmill that makes The Hunt or any
future PvP the path to power.

### What a level 50 does

1. **Dungeon tiers — the main answer.** The same dungeon at T1 / T2 / T3, where each tier
   *adds mechanics* rather than adding health. The boss that had one mechanic at T1 has
   three at T3, and the pulls-with-personality change behaviour. This is "systems-driven
   depth, not content volume" (roadmap standing risk #2) applied literally: a solo dev
   cannot out-produce player appetite for *new* dungeons, but can absolutely out-design it
   on *the same* dungeon.
2. **Raid (20-man)** as the apex, per the established nomenclature.
3. **PvE Renown** — a track earned from dungeon tiers, raid progress, and world events.
   Renown buys **titles, earned cosmetics, mounts, and account conveniences**. It **never
   buys raw power.** This is the cosmetic economy that Pillar 2 forbids selling — so it is
   given away for playing instead, which is a better version of the same feature.
4. **Respec as replay.** At 50 a character owns 41 of 90 tree points. The other 49 are the
   endgame's variety: a free respec turns the Aegis tank into the Crusade off-tank without
   rerolling. This is the reason the tree is deliberately larger than any character can buy.
5. **Secondary skills** — fishing, crafting, languages — horizontal, book-taught,
   uncapped by level.

### Explicitly rejected

- **Post-cap tree points.** Any trickle of points past 50 eventually completes the 90-point
  tree, at which point every character of a class is identical and the build game — the
  entire content of `skills-system-v1.md` — evaporates. **41 of 90 is the design.**
- **A post-cap stat/AA grind** (DAoC's Realm Ranks, ToA-style). Vertical power creep with
  no ceiling; the reason ToA is remembered the way it is.
- **Gear from The Hunt.** Restating the roadmap guardrail: the battle royale's rewards are
  catch-up, consumable, cosmetic or a parallel currency — **never best-in-slot**, ever.
- **Anything purchasable.** Unchanged, forever.

---

## 8. Numbers for MMOStats (proposal)

| knob | proposed value |
|---|---|
| Early Access level cap | **30** |
| Destination level cap | **50** |
| XP curve | `kills(L) = 6.29 × L^1.3`, `baseMobXp(L) = 2 + 8L`, table-driven |
| Total XP 1→50 | 6,005,620 |
| Hours to L10 / L20 / L30 / L50 (solo) | 3.4 / 17.6 / 45.6 / 150 |
| XP source mix | kills 55% / quests 25% / dungeon 12% / discovery 8% |
| Con multipliers | grey 0, green 40%, blue 70%, even 100%, orange 130%, red 170%, purple 0 |
| Grey / purple thresholds | −9 and below / +9 and above |
| Group kill XP | **undivided**, full value per member; **+5% per extra member, cap +20% at five** |
| Rested XP | 1.5× kill XP, caps at **one full bar**, accrues logged-out in a settlement |
| Stat points per level | **+2** (1 automatic = archetype × race rate, 1 discretionary) |
| Stat allocation at creation | **none** — race and archetype fully determine starting stats |
| Race base profile | signed, sums to zero, range −2..+3 (16 GN races, §3a) |
| Race growth rates | 3 Swift (×1.75) / 3 Slow (×0.5) / 10 Even; equal 49-point totals |
| Concentration (Support) | 1 @ L1 · 2 @ L5 · 3 @ L16 · 4 @ L22 · 5 @ cap |
| Stat respec | free, at a trainer, out of combat |
| Class minimums at the quest | **granted, not checked** |
| Death debt | 10% of current level's requirement |
| Debt repayment rate | 50% of XP earned |
| Healer rez | clears 75% of debt |
| Death penalty below L10 | none |
| Armor ceilings | Frontline plate@20 · Healer mail@10 · Support mail@20 · DPS leather |
| Trial ends | end of the level-10 class quest, at Dunadd |
| Trial length | ~5–7 h including quests and the Dungeon |

---

## 9. Consequences for other docs, data and the engine

**Resolves `skills-system-v1.md` open item #2** — cap 50 confirmed as the destination, so
its 41-point / 90-point math stands unchanged. Early Access at 30 gives 21 points and one
capstone; the doc's three build archetypes are 50-cap shapes and should be labelled as such.

**Checked against `reviews/2026-09-13-skills-v1-review.md`.** The cap math here rests
entirely on that review's **locked** topology (3 branches × 12 nodes, costs 1/2/4/6, depth
gates 3/10/20 = 90 points), so nothing in §1 moves if its five fixes are applied. One fix
did land on this doc: the review removed the second action-bar page from v1, so level 20's
milestone is the armor step (§5), not a bar page. This doc takes no position on the
contested damage anchors — the curve is built from kill-cycle time and mob XP, not from
per-hit damage, so 15 @ 2.0 s versus 18 @ 2.4 s does not change a single number in §1.

**Engine changes (implementation lane, not started):**
- `TRCombatComponent`: replace `XpPerLevelBase × level` with a per-level table from
  `Content/Data/`; add con-based XP scaling; add undivided group XP; add the XP-debt field
  and its 50% repayment path.
- `mob-rewards.json` gains a `level` per entry so con can be computed; the existing values
  already fit `2 + 8L`, so no authored number changes.
- Rested XP needs a logout timestamp and location on the character record.
- Lane M6 (player death) gains: rally points per settlement, the debt field, Healer rez.

**Data / MMOStats changes for Daniel:**
- The 50-row XP table.
- Race stat modifiers (§3, option A) — or the budget raise (option B).
- The seven missing DPS class stat-minimum rows (§3).
- `tools/validate.py`: error on a class with no `statMinimums`.

**`items.json` holds exactly one item** (`worn-longsword`). The tier table in §5 is a
skeleton with nothing in it yet; itemization is the largest unstarted data lane in the
project and it now has a shape to fill.

---

## Open items — all six closed by Daniel, 2026-09-13

| # | item | resolution |
|---|---|---|
| 1 | Rested XP vs Pillar 2 | **In**, 1.5×, capped at **one full bar** — not 1.5 levels |
| 2 | Creation stat freedom | **Race carries it.** Base profiles + per-race growth rates (§3a); **no player stat allocation at creation** |
| 3 | Dungeon inside the trial | **Yes**, first clear at the 9–10 band (§6) |
| 4 | Concentration clash | **1 @ L1 · 2 @ L5 · 3 @ L16 · 4 @ L22 · 5 @ cap** — see below |
| 5 | Group bonus | **+5% per extra member, cap +20% at five** (§2) |
| 6 | Cap-raise scheduling | **Roadmap line**, Phase 6: cap 30 → 50 |

### On #4, the one item that needed another session's agreement

The clash was between `gn-ladders-1-9-v1.md` (Support gets 1 Concentration at L1, 2 at L5)
and `skills-system-v1.md` §4 (2 at L10). **The trial decision settles it.** The trial *is*
levels 1–9, so anything gated at level 10 does not exist for a free player — gate
Concentration at 10 and every trial Support spends the entire trial without the resource
that defines the archetype, which is exactly the failure the ladders doc warned about
("nine levels thinking they rolled a bad damage class").

The ladders version wins on the early rungs; the system doc's later rungs are untouched:

> **1 @ L1 · 2 @ L5 · 3 @ L16 · 4 @ L22 · 5 @ cap**

**Action:** `skills-system-v1.md` §4 needs its Concentration line updated to match. That
doc belongs to the Skills System v1 session, so this is a note to that session, not an edit
made here.

---

## Still genuinely open (not Daniel's, not settled tonight)

1. **Dungeon tuning (§6).** A level 9–10 group must be able to clear the first 5-man. Its
   9–15 band has to be a content band, not a difficulty ramp — the world/encounter lane
   has to agree before the trial's shape is real.
2. **The seven missing DPS stat-minimum rows (§3)** and the **16 race rows (§3a)** are
   MMOStats work. Nothing here is buildable until they exist in the sheet.
3. **The engine changes in §9 are unstarted** — the XP table, con scaling, undivided group
   XP, the debt field, and rested accrual are five separate implementation lanes.
