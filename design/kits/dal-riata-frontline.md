# Dál Riata class kits — Frontline (Knight, Zealot, Wizard, Reaver)

**Status:** PROPOSED by Claude, 2026-09-12. Daniel approves or edits.
**Governed by:** `skills-system-v1.md` — 3 branches × 12 nodes, **4 grants / 4 ranks /
4 modifiers per branch** (per-tier mix is free, the totals are law), tier costs
1 / 2 / 4 / 6, depth gates 3 / 10 / 20. Passives are never grants; variations fold
into the skill they vary unless the player needs both behaviours in a fight.
**Scope:** Celtic-allowed classes, which is all four GN Frontlines.
**Shared before this:** the Frontline ladder 1–9 (`frontline-gn-1-9.md`) — Northern
Strike, Focus, Kick, Shout, Charge, Sweeping Slash, Northern Strike II.

Every tree below is built to answer one question: **what kind of tank is this?**
Four frontlines that mitigate the same incoming damage in four incompatible ways.

| class | tanks by | weapon | armor |
|---|---|---|---|
| **Knight** | mitigation — shield, plate, guarding others | one-hand + shield | plate |
| **Zealot** | fury — being too dangerous and too terrifying to ignore | two-hand | mail |
| **Wizard** | wards — mana spent as effective health, enemies bound in place | one-hand + focus | mail |
| **Reaver** | drain — taking the enemy's strength for itself | one-hand, paired | leather |

---

## Knight — the Accolade

Full tree in `skills-system-v1.md` §8; repeated here in summary so all four
frontlines read side by side.

**Core (auto-granted at the class quest):** Shield Slam, Crusader's Oath, Zealous Taunt.
**Gear:** `shield` gate on Shield Slam family; plate at 10.

| branch | fantasy | capstone |
|---|---|---|
| **Aegis** | the immovable wall; guards allies, absorbs for the party | **Bastion** |
| **Crusade** | consecrated offense; the damage-dealing off-tank | **Deliverance** |
| **The Line** | banners, shouts, holding a pull together | **Rally the Line** |

---

## Zealot — the Fervent

The Zealot does not mitigate. It converts. Damage taken is fuel, and the enemy is
held not by a taunt but by the entirely correct belief that the Zealot is the most
dangerous thing on the field. Two-handed, no shield, and the lowest survivability
floor of the four — with a ceiling nothing else touches once it is hurt.

**Core (auto-granted at 10):** *(all three are `two-hand` gated)*

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Fervent Strike** | standard | 14 stam | 3 s | 30 damage; a committed overhead |
| **Zeal** | standard | 20 stam | 45 s | 20 s: damage taken is converted — you deal +1% damage per 2% health missing |
| **Rebuke** | standard | 10 stam | 8 s | forced attention, 3 s; threat scales with your missing health |

### Branch A — Fervor *(the wound economy)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Flagellant** | grant | strike yourself for 15: gain 30 stamina and +15% damage for 10 s *(reactive, off-GCD)* |
| 1 | Fervent Strike II | rank | +40% damage |
| 1 | Bloodheat | modifier | Zeal also grants +15% attack speed |
| 1 | Pain Is Proof | modifier | damage taken below 50% health generates threat |
| 2 | **Wrathful Blow** | grant | 35 damage, +100% if you are below half health; 12 s cd |
| 2 | Zeal II | rank | 30 s duration, conversion rate ×1.5 |
| 2 | Flagellant II | rank | no self-damage; same benefit |
| 2 | Second Breath | modifier | Focus (ladder) also heals you 20 when it ends |
| 3 | **Martyr's Fury** | grant | for 10 s, 40% of damage taken is dealt back to your attacker *(cornerstone, 90 s)* |
| 3 | Wrathful Blow II | rank | +40% damage, refunds 15 stamina on kill |
| 3 | The Wound Is the Door | modifier | Wrathful Blow's bonus applies at 65% health, not 50% |
| **C** | **Apotheosis** | grant | 12 s: you cannot drop below 1 health, and your damage doubles as you fall *(cornerstone, 180 s)* |

### Branch B — Terror *(threat through dread)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Dread Howl** | grant | 8 m: enemies take −25% damage for 8 s and fixate on you; 20 s cd |
| 1 | Rebuke II | rank | +50% threat, 2 targets |
| 1 | Carrying Voice | modifier | Shout (ladder) and Rebuke gain +50% radius |
| 1 | No Quarter | modifier | enemies fleeing you take 25% more damage |
| 2 | **Bone-Chill** | grant | the target's casts take 50% longer for 10 s; 25 s cd |
| 2 | Dread Howl II | rank | 12 m, −35% enemy damage |
| 2 | Shout III | rank | Shout also reduces enemy accuracy 15% |
| 2 | Unignorable | modifier | Zeal makes your threat unloseable while it lasts |
| 3 | **The Reaping Look** | grant | mass fixate, 15 m, 6 s — the emergency "everything on me" *(cornerstone, 120 s)* |
| 3 | Bone-Chill II | rank | also applies −20% attack speed |
| 3 | Terror Has a Name | modifier | enemies below 25% health flee from you, taking No Quarter damage |
| **C** | **The Fear of the North** | grant | aura, 12 m: all enemies deal −20% damage and cannot flee your presence |

### Branch C — Scourge *(the two-handed arc)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Cleave** | grant | 25 damage to 3 enemies in a 120° arc; 8 s cd |
| 1 | Sweeping Slash II | rank | +40% damage, +1 m radius |
| 1 | Wide Arc | modifier | Cleave and Sweeping Slash gain +1 target |
| 1 | Momentum | modifier | each enemy hit by an AoE refunds 4 stamina |
| 2 | **Rending Cut** | grant | 28 bleed over 12 s *(re-homed orphan)*; 10 s cd |
| 2 | Cleave II | rank | +40% damage, 4 enemies |
| 2 | Charge II | rank | Charge (ladder) hits everything you pass through |
| 2 | Blood in the Furrow | modifier | Rending Cut spreads to a second enemy on the target's death |
| 3 | **Crushing Blow** | grant | 73 damage, slow wind-up *(re-homed orphan, committed, 12 s cd)* |
| 3 | Rending Cut II | rank | 40 over 12 s, stacks twice |
| 3 | Harvest | modifier | Crushing Blow's cooldown drops 3 s per enemy bleeding nearby |
| **C** | **The Red Field** | grant | 6 s channel: every enemy within 5 m takes Rending Cut and 20 damage per second |

---

## Wizard — the Arcane Frontline

Yes, a Frontline. The GN Wizard is a **battle-mage who tanks with mana** — wards
standing in for plate, bindings standing in for a shield wall. It holds a pull by
literally fixing enemies in place, and its effective health is the sum of its
hit points and everything its mana can absorb. Mail, one-hand, a focus in the
off-hand. *(If this reading is wrong, it is the cheapest thing in the repo to change
— see open items.)*

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Runeblade** | standard | 15 mana | 3 s | 28 damage; your weapon carries bound force |
| **Mantle** | standard | 25 mana | 20 s | absorbs 60 damage for 20 s; refreshes on re-cast |
| **Compel** | standard | 12 mana | 8 s | forced attention, 3 s, plus a 30% slow |

### Branch A — Wards *(mana as armour)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Sap Ward** | grant | 15 s: 30% of damage you take is drawn from mana instead of health |
| 1 | Mantle II | rank | absorbs 90 |
| 1 | Threadbare | modifier | Mantle's remaining absorb explodes for that value when it breaks |
| 1 | Stillness | modifier | standing still 3 s doubles your in-combat mana regen |
| 2 | **Aegis Minor** | grant | ward an ally for 45; 15 s cd |
| 2 | Sap Ward II | rank | 50% conversion |
| 2 | Aegis Minor II | rank | wards two allies |
| 2 | Spent Force | modifier | every 100 mana spent grants a 20-point ward automatically |
| 3 | **Reflection** | grant | 8 s: spells cast at you are returned to their caster *(reactive, 60 s)* |
| 3 | Reflection II | rank | also reflects the next melee blow |
| 3 | The Cost of Being Struck | modifier | attackers who break your wards lose 20 mana |
| **C** | **Unbroken Circle** | grant | 10 s: you and every ally within 8 m take no damage that a ward can pay for *(cornerstone, 180 s)* |

### Branch B — Runeblade *(bound force)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Frost Brand** | grant | your weapon deals +8 cold damage and slows 20% for 20 s |
| 1 | Runeblade II | rank | +40% damage |
| 1 | Etching | modifier | Northern Strike (ladder) carries your active brand |
| 1 | Kindling | modifier | brands last twice as long |
| 2 | **Flame Brand** | grant | your weapon deals +10 fire damage and burns for 12 over 6 s |
| 2 | Frost Brand II | rank | 35% slow, chills casters |
| 2 | Flame Brand II | rank | burn spreads to adjacent enemies |
| 2 | Two Runes | modifier | you may hold both brands at once |
| 3 | **Shatterstrike** | grant | 45 damage, doubled against a slowed or bound target; 15 s cd |
| 3 | Shatterstrike II | rank | +40% damage, refunds 20 mana on a bound target |
| 3 | Rune-Drunk | modifier | Runeblade hits restore 4 mana |
| **C** | **The Sword That Is a Spell** | grant | 20 s: every weapon hit casts your brand as a free spell at the target |

### Branch C — Binding *(holding the line, literally)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Root** | grant | the target cannot move for 8 s; breaks on damage above 40; 12 s cd |
| 1 | Compel II | rank | 5 s attention, 50% slow |
| 1 | Anchor | modifier | Root does not break until 80 damage |
| 1 | Drag | modifier | Compel pulls the target 3 m toward you |
| 2 | **Ward of Thorns** | grant | 6 m ring for 12 s: enemies crossing it are rooted 3 s |
| 2 | Root II | rank | 12 s, 2 targets |
| 2 | Ward of Thorns II | rank | also deals 10 damage per second inside |
| 2 | Held Fast | modifier | bound enemies take 20% more damage from everyone |
| 3 | **Gravebind** | grant | mass root, 8 m, 6 s *(cornerstone, 90 s)* |
| 3 | Gravebind II | rank | 10 m, 8 s |
| 3 | The Ground Remembers | modifier | enemies breaking a root of yours are slowed 50% for 5 s |
| **C** | **Nothing Moves** | grant | 8 s: every enemy within 10 m is rooted and cannot be freed by damage |

---

## Reaver — the Grim

The Reaver tanks by taking. Every bleed on the enemy is health coming back, and
a Reaver at full tilt in a pack of six is harder to kill than a Knight, while a
Reaver alone against one enemy is the most fragile frontline in the realm. Paired
one-handed weapons, leather — it cannot afford to stand still.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Grim Strike** | standard | 12 stam | 3 s | 26 damage, applies Wound (6 over 6 s) |
| **Leech** | standard | 15 stam | 10 s | 20 damage, heals you for every Wound on the target |
| **Grim Taunt** | standard | 10 stam | 8 s | forced attention, 3 s; +50% threat against Wounded enemies |

### Branch A — Bloodletting *(stack the wounds)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Rending Cut** | grant | 28 bleed over 12 s *(re-homed orphan)*; 10 s cd |
| 1 | Grim Strike II | rank | +40% damage, Wound 10 over 6 s |
| 1 | Salt | modifier | Wounds on a target you are facing tick 25% faster |
| 1 | Both Blades | modifier | Grim Strike applies Wound twice when you are dual-wielding |
| 2 | **Gash** | grant | 20 damage, +8 per Wound already on the target; 6 s cd |
| 2 | Rending Cut II | rank | 40 over 12 s, stacks twice |
| 2 | Gash II | rank | +40% damage |
| 2 | It Does Not Close | modifier | Wounds no longer expire while the target is below 50% health |
| 3 | **Open the Vein** | grant | consume all Wounds: 15 damage each, instantly; 20 s cd |
| 3 | Open the Vein II | rank | 22 damage per Wound |
| 3 | Six Ways to Bleed | modifier | your Wound cap rises from 3 to 6 |
| **C** | **Exsanguinate** | grant | 10 s: every Wound in 10 m ticks twice as fast and heals you for half *(cornerstone, 150 s)* |

### Branch B — The Grim Toll *(drain and sustain)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Drink Deep** | grant | 25 damage, heals you 60% of it; 8 s cd |
| 1 | Leech II | rank | +50% healing per Wound |
| 1 | Toll | modifier | killing a Wounded enemy heals you 25 |
| 1 | Cold Hands | modifier | you take 15% less damage from enemies you have Wounded |
| 2 | **Grave Hunger** | grant | 15 s: all your damage heals you for 20% |
| 2 | Drink Deep II | rank | heals 100% of damage dealt |
| 2 | Grave Hunger II | rank | 25 s, 30% |
| 2 | The Pack Feeds | modifier | Drink Deep also heals your nearest ally for half |
| 3 | **Final Draught** | grant | drain the target for 60 over 4 s; interrupted if you are stunned *(committed, 45 s)* |
| 3 | Final Draught II | rank | 90 over 4 s |
| 3 | Nothing Wasted | modifier | overhealing from drains becomes a ward, up to 60 |
| **C** | **The Long Toll** | grant | passive-aura capstone: while 3+ enemies are Wounded, you regain 3% health per second |

### Branch C — Dread *(take their strength)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Sunder** | grant | −25% enemy armor for 15 s; 12 s cd |
| 1 | Grim Taunt II | rank | 2 targets, +50% threat |
| 1 | Spreading Rot | modifier | Sunder spreads to enemies within 4 m on the target's death |
| 1 | Weak Hands | modifier | Wounded enemies deal 10% less damage |
| 2 | **Wither** | grant | −30% enemy damage and −20% healing received, 12 s; 20 s cd |
| 2 | Sunder II | rank | −40% armor |
| 2 | Wither II | rank | 20 s, also −20% attack speed |
| 2 | All of It | modifier | your debuffs last 50% longer on enemies you have Wounded |
| 3 | **Black Year** | grant | 10 m: enemies lose 20% of all stats for 15 s *(cornerstone, 120 s)* |
| 3 | Black Year II | rank | 25%, 20 s |
| 3 | The Grim Arithmetic | modifier | every debuff on an enemy adds 3% to your damage against it |
| **C** | **Nothing Left** | grant | the target's stats are halved for 10 s, and everything it loses, you gain |

---

## Balance check — four tanks, one pull

Against the standard test (4 mobs, 120 HP each, 2.2 DPS each, no healer):

| class | how it survives | fails when |
|---|---|---|
| **Knight** | flat mitigation + party absorbs; steady, predictable | the fight is long and nobody else brings damage |
| **Zealot** | gets stronger as it drops; Apotheosis is a real second life | burst damage kills it before the conversion pays |
| **Wizard** | mana is a second health bar; enemies never reach the healer | out of mana, it is a mail-wearing nobody |
| **Reaver** | drains 3+ Wounded enemies faster than they hurt it | single-target boss with no adds — the worst tank in the realm |

Every one of them is the best tank in some encounter and the worst in another,
which is what makes a group's frontline choice worth talking about.

---

## Open items for Daniel

1. **The Wizard reading.** Battle-mage-who-tanks-with-mana is my call, made because
   "Wizard" sits in the Frontline column on the sheet. If it is a naming artifact and
   you want a straight caster, this tree gets rewritten — say so before it is encoded.
2. **Reaver's weapon.** Paired one-handers is my assumption (it drives Both Blades and
   the Wound economy). Could as easily be a scythe/polearm fantasy.
3. **Zealot armor: mail, not plate**, to keep it distinct from Knight. Confirm.
4. **Cornerstone count:** Zealot carries three (Martyr's Fury, The Reaping Look,
   Apotheosis) against the system doc's cap of two per class. Deliberate — the Zealot's
   identity is big swings — but it breaks the rule and should either be approved as an
   exception or trimmed.
