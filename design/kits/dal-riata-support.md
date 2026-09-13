# Dál Riata class kits — Support (Bard, Provacateur)

**Status:** PROPOSED by Claude, 2026-09-12. Daniel approves or edits.
**Governed by:** `skills-system-v1.md` §4. **Shared before this:** the Support ladder
1–9 (`gn-ladders-1-9-v1.md`) — Chant of Swiftness, Discord, Lullaby, Cut Short, Chant
of Vigor, Mock, Dissonance, Lullaby II, plus Concentration 1 at L1 and 2 at L5.
**Scope:** Celtic allows 2 of the 6 GN Supports. Dracomancer, Muse, Syndicate and
Philosopher are not playable in Dál Riata and are not authored here.

### A note on the Concentration spine

The system doc says every Support shares a "Songs" spine. That is the *mechanic* —
sustained 10 m auras held against a Concentration cap — not the fiction. Each class
renames it:

| class | spine is called | and it works by |
|---|---|---|
| **Bard** | Songs | melodies that strengthen the party |
| **Provacateur** | Jeers | mockery that weakens the enemy |

Same rules, opposite direction: the Bard's auras buff allies, the Provacateur's debuff
enemies. Two Supports in one group stack cleanly without overlapping, which is the
point of the rename.

---

## Bard — the Northern Voice

The flexible one. A Bard can hold a group together as a second healer, push real damage,
or do neither and just make everyone else 20% better. Its ceiling is never the highest
in any single column — the guardrails in §4 see to that — but it is the only class in
Dál Riata that can change what it is between two pulls.

**Core (auto-granted at the class quest):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Song of Steel** | standard, **1 concentration** | 15 mana | 10 s | aura: party deals +12% weapon damage |
| **Biting Verse** | standard | 10 mana | 3 s | 20 damage; the filler that keeps a Bard busy |
| **Traveler's March** | standard, **1 concentration** | 12 mana | 8 s | aura: +20% out-of-combat speed, +10% in |

### Branch A — Songs *(the aura economy)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Chord of Stamina** | grant | aura, 1 conc: party regains +5 stamina and +3 mana per second |
| 1 | Song of Steel II | rank | +18% weapon damage |
| 1 | Encore | modifier | your auras persist 6 s after you stop singing *(was a passive)* |
| 1 | Crowd Favorite | modifier | your auras reach 14 m instead of 10 *(was a passive)* |
| 2 | **Battle Ballad** | grant | aura, 1 conc: party attack speed +15% |
| 2 | Chord of Stamina II | rank | +8 stamina, +5 mana per second |
| 2 | Battle Ballad II | rank | +22% attack speed |
| 2 | Virtuoso | modifier | your Concentration cap rises by 1 *(was a passive)* |
| 3 | **The North Remembers** | grant | aura, 2 conc: all party stats +10% |
| 3 | The North Remembers II | rank | +15%, and it cannot be dispelled |
| 3 | Silver Tongue | modifier | vendors, quest-givers and crowds favour you; your auras also affect nearby allied NPCs *(was a passive)* |
| **C** | **Song of Sanctuary** | grant | aura, 2 conc: the party takes 25% less damage while you keep singing |

### Branch B — Mending *(the second healer)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Song of Mending** | grant | aura, 1 conc: party heals 7 per second — throughput only, never burst |
| 1 | Biting Verse II | rank | 28 damage |
| 1 | Long Phrase | modifier | Song of Mending also ticks on allies up to 20 m for half |
| 1 | Breath Control | modifier | your auras cost 1 less mana per second each |
| 2 | **Refrain of Vigor** | grant | instant: restores 40 stamina and 25 mana to the party; 20 s cd |
| 2 | Song of Mending II | rank | 11 healing per second |
| 2 | Refrain of Vigor II | rank | 60 stamina, 40 mana |
| 2 | Answering Verse | modifier | Refrain of Vigor also heals 40 |
| 3 | **Threnody** | grant | 15 s: the most wounded party member heals 20 per second |
| 3 | Threnody II | rank | the two most wounded |
| 3 | Carried in Song | modifier | allies below 25% health take 20% less damage while any of your songs play |
| **C** | **The Hearth Song** | grant | 10 s: the party heals 25 per second and cannot fall below 10% health *(cornerstone, 180 s)* |

### Branch C — Verse *(damage and control)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Heckle** | grant | the target attacks recklessly: +20% damage taken, −20% dealt, 12 s; 12 s cd |
| 1 | Biting Verse III | rank | **Ballad of the Fallen** — Biting Verse also leaves 24 grief damage over 12 s |
| 1 | Sour Note | modifier | Heckle and Mock *(ladder)* also reduce enemy armour 15% |
| 1 | Cutting | modifier | Discord *(ladder)* and Biting Verse ignore 25% of magic resistance |
| 2 | **Sleep Song** | grant | mez up to 3 enemies in a cone, 12 s, breaks on damage; 25 s cd |
| 2 | Sleep Song II | rank | 5 enemies, 18 s |
| 2 | Biting Verse IV | rank | **Requiem** — the grief damage doubles and spreads on death |
| 2 | Careful Ear | modifier | your mez breaks cleanly: the enemy does not aggro the breaker |
| 3 | **Discordant Blast** | grant | 55 damage in an 8 m cone, interrupts every cast it touches; 18 s cd |
| 3 | Discordant Blast II | rank | 80 damage, 10 m |
| 3 | Shattering | modifier | Discordant Blast strips one beneficial effect from each enemy hit |
| **C** | **The Final Verse** | grant | consume every song you hold: 60 damage per song to all enemies in 12 m, and the party heals the same *(cornerstone, 120 s)* |

---

## Provacateur — the Goad

The Provacateur does not make the party stronger. It makes the enemy worse — and then
worse again, and then stupid. Where the Bard's auras are gifts, the Provacateur's are
insults hung on whatever is trying to kill you. Its control branch is the reason a group
brings it to a pull it cannot survive honestly.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Jeer of Weakness** | standard, **1 concentration** | 15 mana | 10 s | aura: enemies within 10 m deal 12% less damage |
| **Barb** | standard | 10 mana | 3 s | 20 damage and one stack of **Rattled** (see Derision) |
| **Bait** | standard | 12 mana | 10 s | the target chases you for 4 s, taking 20% more damage while it does |

### Branch A — Jeers *(auras that subtract)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Jeer of Sloth** | grant | aura, 1 conc: enemies within 10 m attack 15% slower |
| 1 | Jeer of Weakness II | rank | 18% less enemy damage |
| 1 | Carrying | modifier | your jeers reach 14 m *(mirrors the Bard's Crowd Favorite)* |
| 1 | They Heard That | modifier | enemies entering a jeer's radius are immediately affected, no ramp |
| 2 | **Jeer of Doubt** | grant | aura, 1 conc: enemy casts take 25% longer and fail 10% of the time |
| 2 | Jeer of Sloth II | rank | 22% slower |
| 2 | Jeer of Doubt II | rank | 35% longer, 15% failure |
| 2 | Practiced Contempt | modifier | your Concentration cap rises by 1 |
| 3 | **Jeer of Ruin** | grant | aura, 2 conc: enemies take 15% more damage from all sources |
| 3 | Jeer of Ruin II | rank | 22% |
| 3 | Nowhere to Stand | modifier | enemies fleeing your jeers stay affected 5 s after leaving |
| **C** | **The Whole Field Laughing** | grant | aura, 2 conc: every jeer you hold applies to every enemy in 20 m, not 10 |

### Branch B — Derision *(stacking contempt)*

**Rattled** is the class's stack: up to 5 on a target, each −4% to everything it does.

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Needle** | grant | 15 damage, 2 stacks of Rattled; 5 s cd |
| 1 | Barb II | rank | 28 damage |
| 1 | Thin Skin | modifier | Rattled stacks last 20 s instead of 12 |
| 1 | Under the Ribs | modifier | Mock *(ladder)* applies 2 stacks of Rattled |
| 2 | **Public Humiliation** | grant | spread every Rattled stack on the target to all enemies in 8 m; 20 s cd |
| 2 | Needle II | rank | 3 stacks |
| 2 | Rattled Cap | rank | Rattled stacks to 8 instead of 5 |
| 2 | Compounding | modifier | at 5+ stacks, Rattled also prevents the enemy from healing |
| 3 | **Unmanned** | grant | consume all Rattled: 20 damage per stack and a 2 s stun; 30 s cd |
| 3 | Unmanned II | rank | 32 damage per stack, 3 s stun |
| 3 | It Never Stops | modifier | Rattled stacks no longer expire while your jeers are audible |
| **C** | **Nothing It Does Will Work** | grant | 12 s: the target is at maximum Rattled and cannot lose stacks *(cornerstone, 120 s)* |

### Branch C — Misdirection *(control and chaos)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Wrong Target** | grant | the enemy attacks its nearest ally for 6 s; 20 s cd |
| 1 | Bait II | rank | 6 s chase, +30% damage taken |
| 1 | Slippery | modifier | Bait also grants you 40% move speed while the enemy chases |
| 1 | Second Thoughts | modifier | Lullaby *(ladder)* no longer breaks on damage below 30 |
| 2 | **Pratfall** | grant | knock the target down 3 s; 25 s cd |
| 2 | Wrong Target II | rank | 10 s, and the victim takes 25% more from its own ally |
| 2 | Pratfall II | rank | 4 s, and the target rises Rattled ×3 |
| 2 | Crowd Work | modifier | Pratfall hits every enemy within 4 m of the target |
| 3 | **The Whole Brawl** | grant | 10 s: enemies in 8 m attack each other instead of the party *(cornerstone, 90 s)* |
| 3 | The Whole Brawl II | rank | 15 s, 12 m |
| 3 | Laughing Stock | modifier | enemies that hit each other under your control take double damage doing it |
| **C** | **Exit, Pursued** | grant | 8 s: every enemy in 15 m chases you and cannot attack anyone else — you take 70% less damage for the duration *(cornerstone, 150 s)* |

---

## Balance check — do they step on each other?

Bard and Provacateur in the same 5-man, both holding two auras:

- **No overlap.** Song of Steel (+12% party damage) and Jeer of Ruin (+15% damage taken)
  multiply rather than compete; Chord of Stamina feeds resources, Jeer of Sloth takes
  them away from the other side.
- **Both bring mez** (Sleep Song, the ladder's Lullaby) and **both bring an interrupt**
  (Discordant Blast, the ladder's Cut Short) — which is correct: crowd control is the
  Support archetype's exclusive verb, so having two Supports should mean *more* control,
  not redundant control.
- **Healing does not double up.** The Bard's Song of Mending is 7–11 HPS of throughput;
  the Provacateur has none. A group running both Supports still needs a Healer for any
  fight with burst damage, which is the §4 guardrail doing its job.

Concentration is the real limiter: 2 slots at level 10 rising to 5 at cap, so even a
capstone Bard holds four songs, not nine.

---

## Open items for Daniel

1. **`Exit, Pursued`** (the Provacateur pulls every enemy onto itself and survives) is a
   Support doing a tank's job for 8 seconds. It is the most fun node in this file and the
   most likely to break a dungeon. Approve, nerf, or cut.
2. **The jeers-versus-songs split** is my invention to stop two Supports being redundant.
   If you would rather every Support sing, the Provacateur's branch A gets rewritten.
3. **Rattled** adds a stack-tracking system the engine does not have. It is the only new
   mechanic in this file — everything else rides existing buff/debuff plumbing.
4. **Four of the six GN Supports are not Celtic-allowed** (Dracomancer, Muse, Syndicate,
   Philosopher), so Dál Riata offers the thinnest archetype roster of the four. Worth
   checking against the race×class matrix if Support is meant to feel like a real choice
   in the first zone.
