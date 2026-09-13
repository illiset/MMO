# Dál Riata class kits — Healers (Squire, Truthspeaker, Volva)

**Status:** PROPOSED by Claude, 2026-09-12. Daniel approves or edits.
**Governed by:** `skills-system-v1.md`. **Shared before this:** the Healer ladder
1–9 (`gn-ladders-1-9-v1.md`) — Mend, Smite, Renew, Purify, Ward, Greater Mend,
Circle of Healing, Mend II.
**Scope:** Celtic allows 3 of the 4 GN Healers. **Preacher is not playable in
Dál Riata** and is not authored here.

Three healers who keep a party alive on three different clocks:

| class | heals by | timing | fails when |
|---|---|---|---|
| **Squire** | oath and triage — guarding one ally, mending the rest | reactive | the damage is spread evenly across five people |
| **Truthspeaker** | binding oaths that pay out while kept | proactive | the party breaks formation and the oaths lapse |
| **Volva** | foresight — spending power before the blow lands | pre-emptive | she reads the fight wrong |

---

## Squire — the Oathbound

The Squire is a martial healer sworn to someone. Its best healing is aimed at one
guarded ally and its worst problem is a party taking damage everywhere at once. Mail,
one-hand and shield, and enough spine to stand in the second rank rather than the back.

**Core (auto-granted at the class quest):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Field Dressing** | standard | 12 mana | 2 s | heals 40 — instant, unlike the ladder's Mend |
| **Shield of Faith** | standard | 15 mana | 12 s | ward an ally for 45; your **guard** target |
| **Rebuke** | standard | 10 mana | 4 s | 18 damage; the Squire is not helpless |

### Branch A — The Oath *(one ally, kept alive at any cost)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Stand Fast** | grant | your guarded ally cannot be knocked down or moved, 10 s; 20 s cd |
| 1 | Shield of Faith II | rank | wards 75 |
| 1 | Oath of Service | modifier | healing your guarded ally costs 30% less mana *(was a passive)* |
| 1 | Close Enough to Hear | modifier | within 5 m of your guarded ally, both of you take 10% less damage |
| 2 | **Interpose** | grant | take the next blow aimed at your guarded ally *(reactive, 25 s)* |
| 2 | Stand Fast II | rank | 20 s, also grants 20% damage resistance |
| 2 | Interpose II | rank | absorbs the blow entirely instead of taking it |
| 2 | The Vow Is Mutual | modifier | your guarded ally's kills heal you 20 |
| 3 | **Knight's Vigil** | grant | your guarded ally cannot be critically hit, 20 s; 45 s cd |
| 3 | Knight's Vigil II | rank | 30 s, also 25% resistance to crowd control |
| 3 | Devoted Heart | modifier | your heals on the guarded ally crit 25% more often *(was a passive)* |
| **C** | **Sanctuary** | grant | 12 s zone, 8 m: every blow inside it lands softened by 40% *(cornerstone, 120 s)* |

### Branch B — Field Medicine *(the practical trade)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Bind Wounds** | grant | 66 healing over 12 s; 6 s cd |
| 1 | Field Dressing II | rank | heals 56 |
| 1 | Steady Hands | modifier | Field Dressing is off-GCD while its target is below 30% health |
| 1 | Hearthkeeper | modifier | out of combat, your party heals at triple rate *(was a passive)* |
| 2 | **Blessed Water** | grant | thrown flask: 45 healing in a 5 m splash; 15 s cd |
| 2 | Bind Wounds II | rank | 92 over 12 s |
| 2 | Blessed Water II | rank | 65 healing, 7 m |
| 2 | Litany of Dawn | modifier | Circle of Healing *(ladder)* heals a second wave at 50% after 4 s |
| 3 | **Triage** | grant | heals your most wounded party member for 70, wherever they are; 10 s cd |
| 3 | Triage II | rank | heals the two most wounded |
| 3 | Sort the Living | modifier | Triage costs no mana below 25% target health |
| **C** | **Field Chapel** | grant | consecrate 8 m for 20 s: 12 healing per second to everyone inside |

### Branch C — The Vigil *(the saves)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Squire's Duty** | grant | strip one ailment from an ally; 8 s cd |
| 1 | Rebuke II | rank | 26 damage, interrupts on a caster *(reactive)* |
| 1 | Absolution | modifier | Squire's Duty cleanses the whole party instead of one ally |
| 1 | Watchful | modifier | Purify *(ladder)* also heals 25 |
| 2 | **Censure** | grant | silence the target 6 s; 30 s cd |
| 2 | Squire's Duty II | rank | strips two ailments |
| 2 | Censure II | rank | 8 s, also 25% slow |
| 2 | Nothing Unclean | modifier | cleansing an ailment grants that ally a 30-point ward |
| 3 | **Lay on Hands** | grant | instant 140 healing *(cornerstone, 60 s)* |
| 3 | Lay on Hands II | rank | 200 healing, also clears all ailments |
| 3 | Martyrdom | modifier | Lay on Hands may be cast at 0 mana by spending 60 of your own health |
| **C** | **The Vow Kept** | grant | 8 s: no party member within 10 m can die *(cornerstone, 180 s)* |

---

## Truthspeaker — the Binder of Oaths

The Truthspeaker heals by holding people to their word. An oath laid on an ally is a
contract: keep it and it pays in health, break it and it lapses. Nothing here is
reactive — a Truthspeaker who waits until someone is hurt has already lost. Cloth, staff,
and a voice that cannot be lied to.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Oath of Iron** | standard | 18 mana | 4 s | 20 s: while this ally keeps striking the same target, they heal 8 per second |
| **Name the Wound** | standard | 12 mana | 3 s | heals 45 and reveals what is killing them (damage type) for the party |
| **Gainsay** | **reactive** | 15 mana | 12 s | interrupt a cast; the caster cannot lie about it — that school locks 8 s |

### Branch A — Oaths *(contracts that pay)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Oath of Stone** | grant | 20 s: while this ally does not retreat, they take 20% less damage |
| 1 | Oath of Iron II | rank | 12 healing per second |
| 1 | Witness | modifier | you may hold two oaths at once |
| 1 | The Word Holds | modifier | oaths persist 5 s after the condition breaks, giving a grace window |
| 2 | **Oath of Blood** | grant | 20 s: this ally deals +15% damage and heals you for 10% of it |
| 2 | Oath of Stone II | rank | 30% reduction |
| 2 | Oath of Blood II | rank | +25% damage |
| 2 | Three Bound | modifier | you may hold three oaths at once |
| 3 | **Oath of the Line** | grant | party-wide: while nobody breaks 10 m from you, everyone heals 6 per second |
| 3 | Oath of the Line II | rank | 10 per second, 15 m |
| 3 | Kept in Full | modifier | an oath held unbroken for its full duration heals its bearer 80 at the end |
| **C** | **The Unbreakable Word** | grant | 15 s: every oath you hold pays double and cannot be broken *(cornerstone, 150 s)* |

### Branch B — Unmaking *(against lies and spells)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Unsay** | grant | strip one beneficial effect from an enemy; 10 s cd |
| 1 | Gainsay II | rank | 6 s cd, also deals 25 damage |
| 1 | Plainly Spoken | modifier | Purify *(ladder)* becomes instant and off-GCD |
| 1 | Nothing Hidden | modifier | your party sees enemy cast bars and durations |
| 2 | **Silence the Room** | grant | 8 m: all enemies silenced 4 s; 30 s cd |
| 2 | Unsay II | rank | strips two effects |
| 2 | Silence the Room II | rank | 6 s, 12 m |
| 2 | The Cost of Lying | modifier | interrupted casters take 40 damage |
| 3 | **Undo** | grant | remove every ailment from the party and heal 40 per ailment removed; 45 s cd |
| 3 | Undo II | rank | 60 healing per ailment |
| 3 | It Was Never True | modifier | effects you strip cannot be re-applied for 10 s |
| **C** | **Recant** | grant | the target enemy's last 8 seconds are undone: damage it dealt is healed *(cornerstone, 180 s)* |

### Branch C — Witness *(healing measured in harm seen)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Testimony** | grant | heals 30, +1 per 10 damage the target has taken in the last 10 s; 3 s cd |
| 1 | Name the Wound II | rank | heals 63 |
| 1 | Ledger | modifier | Testimony's bonus counts 20 s of damage instead of 10 |
| 1 | Seen and Counted | modifier | Name the Wound makes the party deal +10% against that damage type for 15 s |
| 2 | **Weregild** | grant | 20 s: damage dealt to this ally is stored; when it ends, half is healed back |
| 2 | Testimony II | rank | heals 45 base |
| 2 | Weregild II | rank | stores 30 s, returns 75% |
| 2 | Paid in Full | modifier | Weregild also returns 25% of the stored damage to whoever dealt it |
| 3 | **The Reckoning** | grant | heal the party for 15% of all damage they have taken in the last 15 s; 60 s cd |
| 3 | The Reckoning II | rank | 25% |
| 3 | Long Memory | modifier | The Reckoning counts the whole fight, capped at 400 |
| **C** | **Nothing Is Forgotten** | grant | 12 s: every point of damage your party takes is healed back 3 s later *(cornerstone, 180 s)* |

---

## Volva — the Seeress

The Volva heals the future. Her power is spent *before* the blow lands — wards read
from fate, harm redirected, deaths that simply do not take. She is the strongest healer
in the realm when she reads a fight correctly and the weakest when she does not, which
makes her the one healer whose skill ceiling is about knowledge rather than reflexes.
Cloth, staff, no armour worth the name.

**Core (auto-granted at 10):**

| skill | response | cost | cd | effect |
|---|---|---|---|---|
| **Seidr Ward** | standard | 15 mana | 3 s | absorbs 55 for 20 s; you may hold one per ally |
| **Read the Thread** | standard | 10 mana | 8 s | 12 s: the next attack that would hit this ally is shown to you and heals 50 when it lands |
| **Rune of Mending** | committed (2 s) | 14 mana | 2 s | heals 48 |

### Branch A — Seidr *(wards read from fate)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Foreward** | grant | ward the party for 30 each, 15 s; 20 s cd |
| 1 | Seidr Ward II | rank | absorbs 80 |
| 1 | Thread-Sight | modifier | your wards show you what will break them |
| 1 | Nothing Wasted | modifier | a ward that expires unbroken heals its bearer for half its remaining value |
| 2 | **Turn Aside** | grant | the next blow on this ally misses entirely; 25 s cd |
| 2 | Foreward II | rank | 50 each, 25 s |
| 2 | Turn Aside II | rank | the next two blows |
| 2 | Woven Together | modifier | when one party ward breaks, all others gain 20 |
| 3 | **The Long Sight** | grant | 20 s: incoming damage to the party is reduced 25% and healed 10% |
| 3 | The Long Sight II | rank | 35% and 20% |
| 3 | Before It Falls | modifier | your wards apply 1 s before the damage they were cast against |
| **C** | **What Was Never Struck** | grant | 10 s: the party cannot be critically hit and all damage is capped at 40 per blow *(cornerstone, 180 s)* |

### Branch B — The Weave *(fate, luck and redirection)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Snarl the Thread** | grant | the enemy's next attack misses and it is slowed 30%; 15 s cd |
| 1 | Read the Thread II | rank | heals 75 when the attack lands |
| 1 | Loom | modifier | Read the Thread may be held on two allies |
| 1 | Fair Weather | modifier | your party's critical chance rises 5% while you are above 50% mana |
| 2 | **Share the Burden** | grant | 15 s: damage to this ally is split evenly with you |
| 2 | Snarl the Thread II | rank | the next two attacks |
| 2 | Share the Burden II | rank | split three ways with your healthiest ally instead |
| 2 | Slack in the Line | modifier | damage you take from Share the Burden heals for 50% |
| 3 | **Recut the Cloth** | grant | swap the health percentages of two party members; 90 s cd |
| 3 | Recut the Cloth II | rank | may target yourself and an enemy |
| 3 | Knotwork | modifier | Snarl the Thread spreads to an adjacent enemy |
| **C** | **The Norns' Favour** | grant | 15 s: every attack against your party has a 40% chance to simply not have happened |

### Branch C — Wyrd *(death, and what comes back)*

| tier | node | grade | effect |
|---|---|---|---|
| 1 | **Not Yet** | grant | 10 s: the next lethal blow on this ally leaves them at 1 health; 60 s cd |
| 1 | Rune of Mending II | rank | heals 67 |
| 1 | Grave-Cold | modifier | allies saved by Not Yet deal +20% damage for 10 s |
| 1 | Second Sight | modifier | you see which party member will die first at current rates |
| 2 | **Call Back** | grant | return a fallen ally to life at 30% health *(committed, 6 s cast, 60 s cd)* |
| 2 | Not Yet II | rank | leaves them at 25% health instead of 1 |
| 2 | Call Back II | rank | 60% health, 4 s cast |
| 2 | The Dead Are Patient | modifier | Call Back may be cast from 30 m and is not interrupted by damage |
| 3 | **Guardian Spirit** | grant | 30 s: a spirit follows this ally and heals 20 per second below half health |
| 3 | Guardian Spirit II | rank | two spirits, or one at double strength |
| 3 | Ancestral Debt | modifier | each ally you resurrect grants you a stacking +10% healing for the fight |
| **C** | **The Thread Not Cut** | grant | 20 s: party members who would die are instead removed from the fight and returned at full health when it ends *(cornerstone, 300 s)* |

---

## Balance check — the same boss, three healers

150-second boss, one tank taking 35 DPS, party chip damage 12 DPS across four:

- **Squire** covers the tank comfortably (guard + Oath of Service discount) and runs
  out of answers when the boss switches targets. Best with a Knight.
- **Truthspeaker** out-heals both over the full fight *if* the party holds position,
  and collapses in a fight with heavy movement. Best with disciplined groups.
- **Volva** is the only one who can survive a burst mechanic outright (Turn Aside,
  What Was Never Struck) but wastes most of her power when she guesses wrong.

Mana: all three run 100 pool / 2 per second in combat, so none of them can heal for
150 seconds straight. Every one of these kits assumes a Support feeding mana — which
is the interdependence the system doc is built on.

---

## Open items for Daniel

1. **Volva's rez (`Call Back`) versus the Squire's `The Vow Kept`.** Both are
   death-answers. Volva's is a true resurrection, the Squire's is prevention. The
   system doc says only Healers rez — all three of these are Healers, so it holds, but
   Truthspeaker has no rez at all in this draft. Deliberate or wrong?
2. **`Recut the Cloth`** (swap two party members' health percentages) is the single
   most abusable node in this file. It is fun and very Volva. Flagging it now rather
   than discovering it in a raid.
3. **Truthspeaker's oath conditions** ("does not retreat", "keeps striking the same
   target") need engine support for tracking ally behaviour. That is real work — if it
   is too much, the oaths degrade gracefully into plain buffs and the class loses its
   point.
4. **Preacher** is the fourth GN Healer and is not Celtic-allowed, so it is unbuilt.
   If Dál Riata is meant to host all four archetypes' full rosters, the race×class
   matrix is the thing to change, not this file.
