# Dál Riata class kits — DPS (Knave, Draoi, Frontiersman, Ranger, Veil Tamer)

**Status:** PROPOSED by Claude, 2026-09-12. Daniel approves or edits.
**Governed by:** `skills-system-v1.md`. **Shared before this:** the DPS ladder 1–9
(`gn-ladders-1-9-v1.md`) — Quick Strike, Aimed Attack, Evasion, Throw Stone, Ambush,
Serrated Edge, Whirl, Quick Strike II.
**Scope:** Celtic allows 5 of the 11 GN DPS classes. Jester, Hundr, Equal, Pankrator,
Relic Master and Whisper are not playable in Dál Riata and are not authored here.

Five ways to kill things, deliberately non-overlapping:

| class | range | damage shape | brings to a group |
|---|---|---|---|
| **Knave** | melee | burst from behind, best-in-realm single target | opens locks, steals, disappears when it goes wrong |
| **Draoi** | caster | area and over-time; the only DPS that scales with pack size | roots, weather, the pull that was too big |
| **Frontiersman** | melee/thrown | sustained, unglamorous, never stops | survival, tracking, terrain, off-tanks in a pinch |
| **Ranger** | ranged | steady from 30 m, spikes on a marked target | a pet, traps, scouting |
| **Veil Tamer** | melee | ramping drain damage that gets worse the longer it lives | short-lived spirit thralls, blink positioning |

---

## Knave — the Sly

Dál Riata's cutpurse. The Knave puts more damage on one target's back than anything else
in the realm, and folds instantly when something looks at it. Paired daggers, leather,
and an absolute refusal to fight fair.

**Core (auto-granted at the class quest):** *(Backstab family is `dagger` gated)*

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Shiv** | standard | 10 stam | 2 s | 22 damage, ×2.2 from behind |
| **Slip** | **reactive** | 15 stam | 25 s | vanish from combat for 4 s; enemies lose you |
| **Dirty Work** | standard | 12 stam | 12 s | blind the target 4 s: it cannot see who is hitting it |

### Branch A — Shiv *(single-target murder)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Kidney Stroke** | grant | 35 damage from behind, 3 s stun; 20 s cd |
| 1 | Shiv II | rank | 31 damage |
| 1 | Both Hands | modifier | Ambush *(ladder)* strikes twice at 60% each |
| 1 | Find the Gap | modifier | your damage from behind ignores 30% of armour |
| 2 | **Garrote** | grant | 60 over 12 s and silence 4 s, from behind only; 25 s cd |
| 2 | Kidney Stroke II | rank | 50 damage, 4 s stun |
| 2 | Garrote II | rank | 90 over 12 s |
| 2 | Opportunist | modifier | Slip's re-entry makes your next strike count as from behind |
| 3 | **Exsanguinate** | grant | 25 damage per bleed on the target, consuming them; 20 s cd |
| 3 | Shiv III | rank | 44 damage |
| 3 | Cold Efficiency | modifier | killing a target refunds Slip and 30 stamina |
| **C** | **Coup de Grâce** | grant | 150 damage to a target below 25% health; refunds fully if it kills *(cornerstone, 90 s)* |

### Branch B — Cutpurse *(theft and sabotage)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Pickpocket** | grant | steal coin and one consumable from any humanoid; 30 s cd |
| 1 | Dirty Work II | rank | 6 s blind, also −30% enemy accuracy |
| 1 | Light Fingers | modifier | Pickpocket does not break Slip or aggro |
| 1 | Deft | modifier | you open locked chests and doors without a key |
| 2 | **Cut the Strap** | grant | strip one buff from the enemy and gain it yourself for 10 s; 20 s cd |
| 2 | Pickpocket II | rank | also steals a beneficial effect |
| 2 | Cut the Strap II | rank | steals two |
| 2 | Sleight | modifier | stolen effects last twice as long on you |
| 3 | **Sabotage** | grant | the target's next 3 attacks deal 50% damage; 30 s cd |
| 3 | Sabotage II | rank | next 5 attacks |
| 3 | Professional | modifier | your thefts never fail and are never noticed |
| **C** | **Everything That Isn't Nailed Down** | grant | 15 s: every hit you land steals a buff, a debuff, or 3% of the target's health |

### Branch C — Luck *(the gambler)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Chance It** | grant | 15 s: +25% damage, but 15% of your attacks miss entirely |
| 1 | Slip II | rank | 6 s vanish, 18 s cd |
| 1 | Born Lucky | modifier | Evasion *(ladder)* has a 20% chance not to consume its cooldown |
| 1 | Cat-Footed | modifier | you take no falling damage and land silently |
| 2 | **Double or Nothing** | grant | your next strike deals triple damage or nothing, 50/50; 12 s cd |
| 2 | Chance It II | rank | +40% damage, same miss rate |
| 2 | Double or Nothing II | rank | 70/30 in your favour |
| 2 | House Edge | modifier | every miss you suffer adds 10% to your next hit, stacking |
| 3 | **The Long Odds** | grant | 10 s: critical hits refresh all your cooldowns; 60 s cd |
| 3 | The Long Odds II | rank | 15 s |
| 3 | Loaded Dice | modifier | your first attack on any enemy always crits |
| **C** | **Fortune Favours** | grant | 20 s: you cannot be hit by anything that is not a critical strike *(cornerstone, 180 s)* |

---

## Draoi — the Wild

The druid of Dál Riata, and the only DPS in the zone that *wants* the pull to be too
big. The Draoi's damage is area and over-time: slow to start, devastating by second
twelve, and nearly useless against one large target standing still. Cloth, staff, and
a great deal of weather.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Thornlash** | committed (1.5 s) | 12 mana | 3 s | 26 damage, applies Thorns (8 over 8 s) |
| **Rootbind** | standard | 15 mana | 12 s | root the target 8 s; breaks above 60 damage |
| **Green Sight** | standard | 0 | 20 s | 15 s: your over-time effects tick 20% faster |

### Branch A — Storm *(weather as artillery)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Stormcall** | grant | 40 damage to one target; 6 s cd |
| 1 | Thornlash II | rank | 36 damage |
| 1 | Gathering | modifier | each enemy hit by an area spell reduces your next cast by 0.2 s |
| 1 | Sky-Read | modifier | Green Sight also grants +15% spell damage |
| 2 | **Squall** | grant | 20 damage per second for 5 s in an 8 m circle; 15 s cd |
| 2 | Stormcall II | rank | 60 damage, chains to a second enemy |
| 2 | Squall II | rank | 30 per second, 10 m |
| 2 | Downpour | modifier | Squall also slows everything inside it by 40% |
| 3 | **Thunderhead** | grant | 12 s: lightning strikes a random enemy in 15 m every 2 s for 35 |
| 3 | Thunderhead II | rank | every 1.5 s for 50 |
| 3 | The Sky Answers | modifier | your roots and snares call a free Stormcall on whatever they catch |
| **C** | **The Long Winter** | grant | 20 s, 20 m: enemies are slowed 50%, take 25 per second, and cannot regenerate *(cornerstone, 180 s)* |

### Branch B — Thorn *(the creeping kill)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Chokevine** | grant | 45 over 15 s, spreads to one adjacent enemy on death; 8 s cd |
| 1 | Rootbind II | rank | 12 s root, breaks above 100 |
| 1 | Deep Root | modifier | Thorns on a rooted enemy tick twice as fast |
| 1 | Everything Grows | modifier | your over-time effects last 50% longer |
| 2 | **Briarfield** | grant | 10 m field, 15 s: enemies inside take 15 per second and are snared |
| 2 | Chokevine II | rank | 70 over 15 s |
| 2 | Briarfield II | rank | 25 per second, roots instead of snaring |
| 2 | Thorn Cap | modifier | Thorns stack to 5 instead of 3 |
| 3 | **Blight** | grant | every over-time effect on the target jumps to all enemies in 8 m; 25 s cd |
| 3 | Blight II | rank | also refreshes them to full duration |
| 3 | Rot | modifier | enemies with 3+ of your effects take 20% more damage from everyone |
| **C** | **The Wood Takes It Back** | grant | 15 s: every enemy with a Thorn is rooted, and Thorns tick three times as fast |

### Branch C — Beast-Shape *(when the spells run out)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Wolf-Shape** | grant | 30 s: melee form — 30 damage per 2 s auto, +40% speed, no casting |
| 1 | Green Sight II | rank | 25 s, +30% tick rate |
| 1 | Four-Legged | modifier | Wolf-Shape costs no mana and refunds 20 on exit |
| 1 | Hide | modifier | in any beast shape you take 20% less physical damage |
| 2 | **Bear-Shape** | grant | 30 s: +50% health, 45 damage per 3 s, taunts on hit |
| 2 | Wolf-Shape II | rank | 45 damage per 2 s |
| 2 | Bear-Shape II | rank | +80% health, also 20% damage reduction |
| 2 | Shift Freely | modifier | shapeshifting is off-GCD and clears snares and roots |
| 3 | **Stag-Shape** | grant | 30 s: charge 15 m, knocking down everything in the line |
| 3 | Stag-Shape II | rank | 25 m, and the charge deals 60 |
| 3 | Wild Blood | modifier | your over-time effects keep ticking and spreading while you are shifted |
| **C** | **The Old Shape** | grant | 25 s: all three forms at once — bear's health, wolf's speed, stag's charge, and you may still cast |

---

## Frontiersman — the Trailworn

No magic, no tricks, no stealth. The Frontiersman kills things with an axe, a knife and
an extremely good understanding of where it is standing. The most survivable DPS in the
zone and the one a group is happiest to see when the healer goes down. Mail, hand axe
and a belt of throwing knives.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Splitting Blow** | standard | 14 stam | 4 s | 32 damage; ignores 20% armour |
| **Throwing Knife** | standard | 8 stam | 3 s | 20 damage at 20 m; three in the air at once |
| **Set Footing** | standard | 0 | 20 s | 12 s: cannot be knocked down or moved; +15% damage |

### Branch A — The Axe *(honest violence)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Hamstring** | grant | 25 damage and 50% slow, 8 s; 10 s cd |
| 1 | Splitting Blow II | rank | 45 damage |
| 1 | Follow Through | modifier | Splitting Blow hits a second enemy behind the first for 60% |
| 1 | Weight Behind It | modifier | Set Footing raises the damage bonus to +25% |
| 2 | **Rend** | grant | 50 over 10 s, stacks 3 times; 6 s cd |
| 2 | Hamstring II | rank | 40 damage, 70% slow |
| 2 | Rend II | rank | 75 over 10 s |
| 2 | Butcher | modifier | your bleeds deal 50% more to enemies below half health |
| 3 | **Overhand** | grant | 90 damage, 2 s wind-up *(committed)*; 15 s cd |
| 3 | Overhand II | rank | 130 damage, knocks down |
| 3 | No Wasted Motion | modifier | every kill reduces all your cooldowns by 2 s |
| **C** | **The Work of the Day** | grant | 20 s: every strike applies Rend and your attack speed rises 5% per enemy struck |

### Branch B — Skirmish *(thrown steel, hit and run)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Fan of Knives** | grant | 18 damage to 4 enemies in a cone at 15 m; 8 s cd |
| 1 | Throwing Knife II | rank | 30 damage |
| 1 | Bandolier | modifier | five knives in the air instead of three |
| 1 | Read the Ground | modifier | you move 20% faster on any terrain the party has scouted |
| 2 | **Bolas** | grant | root the target 6 s at 20 m; 20 s cd |
| 2 | Fan of Knives II | rank | 28 damage, 6 enemies |
| 2 | Bolas II | rank | 10 s, and the target cannot use skills for 3 s |
| 2 | Coated | modifier | thrown weapons apply your active bleed |
| 3 | **Falling Back** | grant | leap 12 m backward, leaving a caltrop field that snares; 25 s cd |
| 3 | Falling Back II | rank | the field also deals 15 per second |
| 3 | Never Cornered | modifier | Falling Back refreshes when an enemy closes within 3 m of you |
| **C** | **A Knife for Everyone** | grant | 15 s: every throw hits every enemy within 20 m and costs nothing |

### Branch C — Woodcraft *(survival as a weapon)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Field Rations** | grant | out of combat: restore the party to full stamina and 50% mana; 120 s cd |
| 1 | Set Footing II | rank | 20 s, also 20% damage reduction |
| 1 | Hardy | modifier | you regain stamina in combat at out-of-combat rate |
| 1 | Trailcraft | modifier | the party moves at your speed, and you never get lost |
| 2 | **Bandage** | grant | heal yourself 80 over 6 s; 30 s cd |
| 2 | Field Rations II | rank | also grants +10% all stats for 10 minutes |
| 2 | Bandage II | rank | 140 over 6 s, may target an ally |
| 2 | Stubborn | modifier | effects that would kill you leave you at 1 health once per 3 minutes |
| 3 | **Hold the Gap** | grant | 15 s: you take 40% less damage and enemies cannot move past you |
| 3 | Hold the Gap II | rank | 25 s, and you taunt everything that tries |
| 3 | Someone Has To | modifier | while the party healer is dead, your damage and resistance rise 25% |
| **C** | **Still Standing** | grant | 30 s: you cannot be reduced below 20% health, and every blow you survive adds 3% damage *(cornerstone, 240 s)* |

---

## Ranger — the Warden of Paths

Authored kit, arranged into branches. The Ranger holds 30 m and makes one marked target
die faster than it should. Leather, Hunting Bow, and a wolf that is not a pet so much as
a colleague.

**Core (auto-granted at 10):** *(Longshot family is `bow` gated)*

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Longshot** | standard | 12 stam | 4 s | 34 damage at 35 m |
| **Hunter's Mark** | standard | 0 | 10 s | the target cannot stealth and takes +15% from you |
| **Swift Feet** | standard | 0 | 20 s | 12 s: move at full speed while drawing |

### Branch A — The Long Shot *(archery)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Barbed Arrow** | grant | 40 over 10 s; 8 s cd |
| 1 | Longshot II | rank | 48 damage |
| 1 | Keen Eye | modifier | your critical shots deal 50% more *(was a passive)* |
| 1 | Windrunner | modifier | attacking no longer slows your run *(was a passive)* |
| 2 | **Double Nock** | grant | two arrows, 26 each; 10 s cd |
| 2 | Barbed Arrow II | rank | 60 over 10 s |
| 2 | Double Nock II | rank | **Rain of Arrows** — three arrows, or one volley over 6 m |
| 2 | Steady | modifier | Longshot's damage rises 3% per metre beyond 20 m |
| 3 | **Piercing Gale** | grant | an arrow through every enemy in a 25 m line, 45 each; 25 s cd |
| 3 | Piercing Gale II | rank | 65 each, knocks back |
| 3 | Apex Predator | modifier | marked prey takes 10% more damage from everyone *(was a passive)* |
| **C** | **The Long Hunt** | grant | 120 damage to your marked target from any range, ignoring line of sight *(cornerstone, 90 s)* |

### Branch B — Trapcraft *(the ground does the work)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Snare Trap** | grant | armed trap: roots the first enemy 8 s; 20 s cd |
| 1 | Hunter's Mark II | rank | +25% damage from you, and the mark spreads on death |
| 1 | Master Trapper | modifier | traps arm instantly and bite 50% harder *(was a grant)* |
| 1 | Two Sprung | modifier | you may hold two traps armed at once |
| 2 | **Pinning Shot** | grant | nails the target in place 6 s; 18 s cd |
| 2 | Snare Trap II | rank | 12 s root, 6 m trigger radius |
| 2 | Pinning Shot II | rank | 10 s, and the target cannot turn |
| 2 | Baited | modifier | traps you set draw the nearest enemy toward them |
| 3 | **Camouflage** | grant | fade into terrain; your next shot from concealment deals triple; 30 s cd |
| 3 | Camouflage II | rank | may be entered in combat |
| 3 | Patient | modifier | every second spent concealed adds 10% to the shot that breaks it, to 200% |
| **C** | **Heartseeker** | grant | the shot they never hear: 200 damage from concealment, ignores armour *(cornerstone, 120 s)* |

### Branch C — The Wild *(the wolf and the wood)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Wolfpack** | grant | call a wolf of the North for 60 s: 60% of your damage, cannot taunt |
| 1 | Swift Feet II | rank | 20 s, +25% move speed |
| 1 | Warden of Paths | modifier | the party moves 20% faster off-road *(was a grant)* |
| 1 | Pack Sense | modifier | your wolf attacks your marked target automatically |
| 2 | **Crow Flight** | grant | a flock harries an 8 m area: 12 per second and −25% enemy accuracy, 10 s |
| 2 | Wolfpack II | rank | two wolves, or one at 100% of your damage |
| 2 | Crow Flight II | rank | 20 per second, 12 m |
| 2 | It Comes Back | modifier | your wolf resummons free 15 s after it dies |
| 3 | **Eagle's Descent** | grant | leap to high ground and shoot: 70 damage in a 6 m splash; 20 s cd |
| 3 | Eagle's Descent II | rank | 100 damage, stuns 2 s |
| 3 | Beast Speech | modifier | beasts in the world do not attack you unprovoked |
| **C** | **One with the Wild** | grant | 20 s: the wood fights beside you — wolves, crows and thorns strike everything you mark |

---

## Veil Tamer — the Veiled

Something follows the Veil Tamer, and it is not tame. This is a ramp class: weakest in
the first four seconds of any fight, strongest at second twenty, and the only DPS whose
damage *comes back to it* as survivability. Leather, a bound blade, and a thrall that
lasts thirty seconds at a time.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Hollow Strike** | standard | 12 stam | 3 s | 24 damage, applies Hollowing (stacks to 5, +4% damage taken each) |
| **Veilstep** | **reactive** | 15 stam | 20 s | blink 10 m through anything, including walls |
| **Bind Thrall** | standard | 25 mana | 45 s | a spirit serves 30 s: 50% of your damage, cannot taunt |

### Branch A — Hollowing *(the ramp)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Drain** | grant | 20 damage per Hollowing stack, healing you half; 10 s cd |
| 1 | Hollow Strike II | rank | 34 damage |
| 1 | Deepening | modifier | Hollowing stacks to 8 |
| 1 | Slow to Start | modifier | Hollowing stacks never fall off while the target lives |
| 2 | **Unmake** | grant | 45 damage, +15 per Hollowing stack; 8 s cd |
| 2 | Drain II | rank | 32 per stack |
| 2 | Unmake II | rank | +25 per stack |
| 2 | It Spreads | modifier | killing a Hollowed enemy passes its stacks to the nearest one |
| 3 | **The Long Hollow** | grant | 20 s: every hit applies two stacks instead of one |
| 3 | The Long Hollow II | rank | 30 s, three stacks |
| 3 | Nothing Left Inside | modifier | enemies at max Hollowing cannot be healed |
| **C** | **Unmade** | grant | consume all stacks on all enemies in 10 m: 40 damage per stack, healing you for a quarter *(cornerstone, 120 s)* |

### Branch B — Bindings *(the thralls)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Second Thrall** | grant | a second spirit serves at 35% of your damage |
| 1 | Bind Thrall II | rank | 60 s duration, 70% of your damage |
| 1 | Willing | modifier | thralls resummon free when they expire, once per fight |
| 1 | Quiet Servants | modifier | your thralls generate no threat at all |
| 2 | **Feed the Thrall** | grant | sacrifice 20% of your health: the thrall doubles in strength for 15 s |
| 2 | Second Thrall II | rank | 60% of your damage |
| 2 | Feed the Thrall II | rank | no health cost |
| 2 | Bound in Blood | modifier | damage your thralls deal heals you for 15% |
| 3 | **Wear It** | grant | 15 s: step inside your thrall — its body, your skills, immune to crowd control |
| 3 | Wear It II | rank | 25 s, and you take 40% less damage |
| 3 | The Veil Provides | modifier | when a thrall dies, the next is summoned instantly and enraged |
| **C** | **Everything on the Other Side** | grant | 20 s: four thralls at full strength *(cornerstone, 180 s)* |

### Branch C — Veilstep *(position as a weapon)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Fade** | grant | 8 s: 40% of attacks pass through you entirely |
| 1 | Veilstep II | rank | 15 m, 12 s cd |
| 1 | Arrive Badly | modifier | Veilstep deals 30 damage to everything you pass through |
| 1 | Between | modifier | you may Veilstep while stunned or rooted |
| 2 | **Pull Through** | grant | drag the target 10 m to you and stun it 2 s; 20 s cd |
| 2 | Fade II | rank | 12 s, 60% |
| 2 | Pull Through II | rank | drags every enemy in a 6 m radius |
| 2 | Both Sides | modifier | Veilstep leaves a copy behind that enemies attack for 3 s |
| 3 | **Elsewhere** | grant | 6 s: you cannot be targeted, damaged or found, and you may still attack |
| 3 | Elsewhere II | rank | 10 s |
| 3 | The Door Stays Open | modifier | Veilstep's cooldown resets on any kill |
| **C** | **Nothing Holds You** | grant | 20 s: Veilstep has no cooldown and every use applies three Hollowing stacks |

---

## Balance check — five DPS, one boss, one pack

**Single target, 60 s boss:** Knave 26 DPS → Veil Tamer 25 (ramped) → Ranger 23 →
Frontiersman 21 → Draoi 16.
**Six-mob pack, 30 s:** Draoi 48 effective DPS → Frontiersman 31 → Ranger 28 →
Veil Tamer 26 → Knave 24.

Nobody is top in both columns and nobody is bottom in both. The Draoi's spread is the
widest on purpose — it is the class that changes a group's answer to "that pull is too
big." Against the frontline baseline (~18 sustained), every DPS beats every tank on
damage while dying to anything the tank shrugs off.

**Group verbs, for the first dungeon's design:** only the Ranger and Frontiersman have
ranged pulls; only the Knave opens locks; only the Draoi brings mass roots; only the
Veil Tamer and Frontiersman can hold a second enemy for a few seconds when the tank is
overwhelmed.

---

## Open items for Daniel

1. **Draoi shapeshifting** is a whole feature — models, animation sets, a skill-bar swap.
   It is the most expensive thing proposed in any of these four kit files by a wide
   margin. If it is too much for the slice, branch C becomes a totem/spirit-animal branch
   instead and the class loses nothing structurally.
2. **Veil Tamer thralls versus Ranger's Wolfpack.** Both are pets under the §6 rules
   (cannot taunt, 60% owner damage). The Veil Tamer's are short-lived and stackable, the
   Ranger's is permanent-ish. Two pet classes in one zone is fine, but confirm the Veil
   Tamer is meant to be a pet class at all — the name suggests it, the clone kit does not.
3. **`Wear It`** (step inside your own thrall) is a body-swap mechanic with real engine
   cost. Flagged as the second-most-expensive node in these files.
4. **The Knave's `Pickpocket`** implies world NPCs carry loot tables and a theft system.
   Cheap fiction, real plumbing.
5. **Six of the eleven GN DPS classes are not Celtic-allowed.** Along with four of six
   Supports and one of four Healers, Dál Riata offers 14 of 25 GN classes. That is a
   design decision worth making on purpose — a first zone that shows a player only half
   the realm's classes may be correct, or may need the race×class matrix widened.
