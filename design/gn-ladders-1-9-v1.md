# Great North — the three missing 1–9 ladders (Healer, Support, DPS)

**Status:** PROPOSED by Claude, 2026-09-12. Daniel approves or edits.
**Why this exists:** only the Frontline ladder was authored
(`frontline-gn-1-9.md`). Dál Riata has all four archetype starts — Lissban
(Frontline), Rinnbeg (Damage), Tobarglas and Dromcairn (Healer, Support) — so
three archetypes currently have no levels 1–9 to play at all.
**Governed by:** `skills-system-v1.md` (response classes, resources, GCD).
Numbers are proposals for MMOStats.xlsx.

---

## The shared rhythm

All four ladders use the rhythm Daniel set for Frontline, so every new character
learns the same shape regardless of archetype:

| level | what arrives |
|---|---|
| 1 | auto-attack + 1 signature skill |
| 2 | 1 skill |
| **3** | **no skill — armor unlock (leather)** |
| 4 | 1 skill — *the archetype's interrupt* |
| 5 | 1 skill |
| 6 | 1 skill |
| **7** | **no skill — cloak unlock** |
| 8 | 1 skill — *the archetype's AoE* |
| **9** | weapon unlock + **rank-up (II)** of the level 1 signature, then the class quest at 10 |

**Seven actives plus auto-attack by level 9**, in every archetype. Two quiet
levels that pay in gear rather than buttons. Everyone gets an interrupt at 4,
because interrupts are what make group PvE a conversation (`skills-system-v1.md`
§3) — a party where only the tank can interrupt has three players watching.

Anchors, from the Frontline doc: auto 15 damage per swing, player 200 HP, mobs
120–150 HP, mob DPS ~2.2. Stamina and mana pools 100 (§2 of the system doc).

---

## 1. Healer ladder — "the Hearth-Tender"

**Starting gear:** Rowan Staff (85% weapon damage @ 2.8 s — healers are not meant
to melee), cloth armor. **Unlocks:** leather @3, cloak @7, **Yew Staff @9**.

| L | skill | response | cost | cd | value | notes |
|---|---|---|---|---|---|---|
| 1 | **Mend** | committed (2.0 s cast) | 12 mana | 2 s | heals 45 | the spine; everything else is built around its cast time |
| 1 | **Smite** | committed (1.5 s cast) | 10 mana | 3 s | 16 dmg | a healer with nothing to do between heals is a bored healer |
| 2 | **Renew** | standard | 15 mana | 4 s | 60 over 12 s | pre-cast on the tank before a pull |
| 3 | — | — | — | — | — | **leather armor** |
| 4 | **Purify** | **reactive** (off-GCD) | 15 mana | 8 s | — | removes poison/disease; the healer's interrupt-slot equivalent |
| 5 | **Ward** | standard | 20 mana | 15 s | absorbs 50 | preventive, not reactive — rewards reading the fight |
| 6 | **Greater Mend** | committed (3.0 s cast) | 25 mana | 5 s | heals 90 | the big one; slow enough to be interrupted |
| 7 | — | — | — | — | — | **cloaks** |
| 8 | **Circle of Healing** | committed (3.0 s cast) | 35 mana | 12 s | 40 to party | the AoE beat; shines at 3+ wounded |
| 9 | **Mend II** | committed (2.0 s cast) | 14 mana | 2 s | heals 63 | ×1.4 rank step + **Yew Staff** |

**Mana math:** 100 pool, 2/s in combat. Mend at 12 mana ≈ 8 casts before empty,
about 45 s of steady healing. That is deliberately not enough for a long fight —
it is what makes a Support's mana chant worth a group slot, and what makes sitting
between pulls a real part of the loop.

**Healing math:** Mend 45 per 2 s cast = 22 HPS against a raider mob's 2.2 DPS.
One healer can hold roughly 5 characters under steady chip damage, or one tank
under a serious beating, not both — which is the tension a 5-man should have.

---

## 2. Support ladder — "the Voice"

**Starting gear:** Short Sword (90% @ 2.2 s) and a carved horn. The horn is
cosmetic — songs never require an instrument item (the non-weapon-dependent rule,
system doc §7). **Unlocks:** leather @3, cloak @7, **Ash Spear @9**.

**Concentration arrives on the ladder:** 1 slot at level 1, 2 at level 5. This is
the archetype's defining resource and it should be in the player's hands from the
first minute, not held back until the class quest.

| L | skill | response | cost | cd | value | notes |
|---|---|---|---|---|---|---|
| 1 | **Chant of Swiftness** | standard, **1 concentration** | 15 mana | 10 s | +15% party move speed | sustained aura, 10 m; **Concentration cap 1** |
| 1 | **Discord** | standard | 10 mana | 3 s | 16 dmg | the filler |
| 2 | **Lullaby** | committed (2.0 s cast) | 15 mana | 15 s | sleeps 1 | single-target mez — the Support's identity button, and it lands in the first ten minutes |
| 3 | — | — | — | — | — | **leather armor** |
| 4 | **Cut Short** | **reactive** (off-GCD) | 10 mana | 15 s | — | interrupt; cancels a cast and locks that school 5 s |
| 5 | **Chant of Vigor** | standard, **1 concentration** | 15 mana | 10 s | +4/s party stamina, +2/s mana | **Concentration cap 2** — the first real choice: which two songs? |
| 6 | **Mock** | standard | 12 mana | 10 s | −20% enemy damage, 15 s | the debuff beat |
| 7 | — | — | — | — | — | **cloaks** |
| 8 | **Dissonance** | standard | 20 mana | 10 s | 12/tick, 5 ticks, 8 m | the AoE beat, as a damage-over-time field |
| 9 | **Lullaby II** | committed (2.0 s cast) | 18 mana | 15 s | sleeps 1, longer, breaks cleaner | ×1.4 rank step + **Ash Spear** |

**Why mez at level 2:** crowd control is the Support's whole reason to exist in a
group (system doc §4), and a player who does not have it until level 10 spends nine
levels thinking they rolled a bad damage class. Lullaby breaking on damage teaches
target discipline early, which is exactly the lesson the first dungeon needs them to
have already learned.

---

## 3. DPS ladder — "the Edge"

**Starting gear:** two Hunting Knives (one-handed, 95% @ 1.8 s each — fast and
light), cloth. **Unlocks:** leather @3, cloak @7, **choice of Hunting Bow or
Arming Sword @9**.

This ladder must serve a future Ranger, a Knave and a Draoi alike, so every skill
here is **weapon-agnostic** — they read off whatever you hold (system doc §7). The
level 9 weapon choice is the first hint of where your class quest is heading, and
it is not binding.

| L | skill | response | cost | cd | value | notes |
|---|---|---|---|---|---|---|
| 1 | **Quick Strike** | standard | 8 stam | 2 s | 18 dmg | cheap, spammable, the rhythm |
| 1 | **Aimed Attack** | standard | 12 stam | 5 s | 28 dmg | the harder hit on a real cooldown |
| 2 | **Evasion** | standard | 0 | 20 s | +30% dodge, 8 s | you have no armor; this is how you live |
| 3 | — | — | — | — | — | **leather armor** |
| 4 | **Throw Stone** | **reactive** (off-GCD) | 8 stam | 15 s | 5 dmg, interrupt | a *ranged* interrupt — also the DPS's only pull tool, which teaches pulling |
| 5 | **Ambush** | standard | 20 stam | 12 s | 28, ×2.0 from behind | positional identity: get behind it |
| 6 | **Serrated Edge** | standard | 15 stam | 10 s | 28 over 10 s | the bleed; stacks with Ambush openers |
| 7 | — | — | — | — | — | **cloaks** |
| 8 | **Whirl** | standard | 20 stam | 10 s | 20/target, 4 m | the AoE beat |
| 9 | **Quick Strike II** | standard | 10 stam | 2 s | 25 dmg | ×1.4 rank step + **bow or sword** |

**DPS math:** at level 9, Quick Strike II on cooldown plus autos ≈ 21 sustained
DPS against the Frontline's ~18. The gap is deliberately small — a DPS that doubles
the tank's damage makes tanking feel like a chore — but the DPS gets there without
Guard Stance's survivability, and dies to two mobs where the Frontline survives four.

**TTK sanity:** DPS opener (Ambush from behind 56 + Serrated Edge + Quick Strike II
chain) kills a 120 HP mob in ~7 s versus the Frontline's 8–9. Faster, and much more
punishing when the pull goes wrong.

---

## Cross-archetype check at level 9

| | actives | sustained DPS | survivability | group verb |
|---|---|---|---|---|
| **Frontline** | 7 + auto | ~18 | highest (Guard Stance, 200 HP, leather) | holds threat |
| **DPS** | 7 + auto | ~21 | lowest (dodge only) | kills things |
| **Healer** | 7 + auto | ~6 | low, but ranged | keeps people alive |
| **Support** | 7 + auto | ~8 | low, but controls | mez, interrupt, economy |

Four characters who cannot do each other's jobs, by level 9, before a single class
quest has fired. That is the bar the first dungeon is designed against.

---

## Open items for Daniel

1. **Names.** Mend / Smite / Renew / Purify / Ward are placeholders in the plain
   register. The Frontline ladder got Great North flavour ("Northern Strike",
   "Shout") — these deserve the same pass, and Dál Riata is Gaelic, so there may be
   an argument for a Celtic register on the Healer and Support ladders specifically.
2. **Healer starting weapon:** staff, or a mace-and-shield Squire-flavoured option?
   Staff is assumed here because it keeps healers out of melee range by default.
3. **The level 9 weapon choice on the DPS ladder** (bow or sword) is the only place
   any ladder branches. It is flavour, not a gate — but say the word if you would
   rather it be a straight unlock like the other three.
4. **Concentration on the Support ladder** (1 at L1, 2 at L5) moves the resource
   earlier than `skills-system-v1.md` §4 assumed (2 at L10). The system doc should be
   amended to match whichever you prefer.
