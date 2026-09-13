# Dál Riata — quests v1, DRAFT SKELETON

**Status: EVERY LINE IS A PROPOSAL.** Written 2026-09-13 (night-3 prep) so Daniel has
something concrete to argue with, not a blank page. Nothing here is approved, nothing is
implemented, and no quest id exists in `Content/Data/quests.json` yet — that file still
holds exactly one prototype (`class-quest-frontline-knight`).

Sources this is built on, all already approved: `design/gn-ladders-1-9-v1.md` (the four
1–9 ladders), `design/progression-v1.md` (the curve, the trial gate, death), the canon
place names in `design/names/great-north-places.md` §1, `design/notes/dal-riata-vision.md`
(the forest, the castle, the lore) and `design/notes/dal-riata-accents.md`.

**Quest ids below match `Content/Data/npcs/dal-riata-npcs.json`.** The two files are a
matched pair of drafts; if you rename a quest, the roster's `givesQuests` moves with it.

---

## The one rule this draft follows

> **A quest exists to teach the rung the ladder just handed you.**

The 1–9 ladders give a character a new skill at levels 1, 2, 4, 5, 6, 8 and 9, and an
armour or cloak unlock at 3 and 7. So there are nine beats to fill, and each one already
knows what it is about. That is the whole spine. Where a level's beat is armour rather
than a skill, the quest is about *getting the thing* rather than using it.

The second rule, smaller: **a start's quests never leave that quarter until level 7.**
The four hamlets are supposed to feel like four different places with four different
accents, and they stop feeling that way the moment everyone is sent to Dunadd at level 2.

---

## The island's arc — one page

| band | where | what |
|---|---|---|
| 1–6 | your own start (Lissban / Rinnbeg / Tobarglas / Dromcairn) | seven quests, your quarter only |
| 7–8 | **Dunadd** | the four lines converge; cloak, then the AoE beat |
| 9 | your trainer, then the road | rank-up, weapon unlock, and the walk to Carrigrua |
| **10** | **Carrigrua** | **the class quest. The tree opens. The trial ends.** |
| 8–10 | the beached camp at **Camasmore Bay** | the Fomorian raiders — group content, teaches the dungeon |
| 6–12 | **Shanderry Forest** | the grind ground: lairs, wanderers, the hag, Cairbre |
| 9–15 | **Uaimh na Scáth** | the 5-man; its first leg sits inside the trial at 9–10 |
| 10 | **Portcorr** | the boat. Leaving the island is the paid gate. |

Level 10 arrives at about 3.4 hours (progression-v1 §1). Everything above is meant to fit
inside one long evening, twice.

---

## 1. The four starts, 1–9

Each line is seven quests in the quarter plus two shared ones at Dunadd. The table gives
the id, the giver (from the NPC roster), the level, the ladder rung it teaches, and the
beat. Quest *names* are placeholders in the same register as the ladder docs — the ladders
doc already flags that a Celtic-register naming pass is owed, and these need it too.

### 1.1 Lissban — Frontline — south-west, Welsh-ish

The lime-washed muster yard. Everything here is about a line that holds.

| id | giver | L | rung | beat |
|---|---|---|---|---|
| `dr-lissban-1` | Gwilym Penlan | 1 | signature + auto-attack | Take a shield off the rack and stand in the line while Bedwyr walks the drill. Three practice bouts in the yard. |
| `dr-lissban-2` | Bedwyr ap Rhys | 2 | 2nd skill | Something is killing lambs on Blunt Head's neck. Foxes, they hope. Four kills, the first real fight. |
| `dr-lissban-3` | Angharad Wen | 3 | **leather** | Carry the hides Nest cured down to Angharad and she cuts you a jerkin. No combat. The reward IS the armour. |
| `dr-lissban-4` | Gwilym Penlan | 4 | **interrupt** | A wolf that has learned to howl the flock into a panic. Kill it *before it finishes the howl* — the quest text says so, and the wolf's tell is 0.9 s. |
| `dr-lissban-5` | Meirion the Thatcher | 5 | 5th skill | Set the boundary stones back up along the old field wall; three of them have things living under them. |
| `dr-lissban-6` | Bedwyr ap Rhys | 6 | 6th skill | Stand the gate at Athgorm Ford for one crossing. A scripted three-wave hold — the first time the game asks you to *not move*. |
| `dr-lissban-9` | Bedwyr ap Rhys | 9 | rank-up + weapon | The warband's old sword has been in the ford silt since the Crusader war. Fetch it, and Bedwyr ranks up your signature over it. |

### 1.2 Rinnbeg — Damage — north-west, Irish-ish

A hunters' camp on the cape. Everything here is about the first strike.

| id | giver | L | rung | beat |
|---|---|---|---|---|
| `dr-rinnbeg-1` | Cormac the Gull | 1 | signature | Gulls have taken the drying fish. Kill six crows on the cliff — deliberately trivial, deliberately fast. |
| `dr-rinnbeg-2` | Niamh Sharpeye | 2 | 2nd skill | Track a stag down the cape and bring back the hide. Teaches *neutral* mobs: it will not fight you until you start it. |
| `dr-rinnbeg-3` | Ruairi the Fletcher | 3 | **leather** | Three hides, one for each of the drying frames. Ruairi cuts the leather. |
| `dr-rinnbeg-4` | Cormac the Gull | 4 | **interrupt (ranged)** | Something is calling the wolves down off Benlea. Throw Stone is the DPS's only pull tool and this quest is where you learn that pulling is a thing. |
| `dr-rinnbeg-5` | Sorcha of the Boats | 5 | **Ambush** | A pig the size of a boat has been rooting up the shore garden. It hits hard from the front. Get behind it. |
| `dr-rinnbeg-6` | Niamh Sharpeye | 6 | bleed | Wolves at Cuaseen, in threes. The first pull that punishes you for grabbing two. |
| `dr-rinnbeg-9` | Niamh Sharpeye | 9 | rank-up + **bow or sword** | Sit a night watch on Grey Head alone. Choose your weapon at the turn-in — the ladders doc says the choice is flavour, not a gate. |

### 1.3 Tobarglas — Healer — north-east, Scottish-ish

The spring-shrine at the foot of the Bealanard Shoulder. Everything here is about keeping
someone else alive, which is hard to teach solo and is the real design problem in this line.

| id | giver | L | rung | beat |
|---|---|---|---|---|
| `dr-tobarglas-1` | Ailsa of the Well | 1 | **Mend** | Torquil has cut his hand open on the shrine stones. Cast Mend. That is the whole quest, and it should take ninety seconds. |
| `dr-tobarglas-2` | Murdo the Truthspeaker | 2 | Renew | Three goats have been at the aconite. Renew each one and walk them back up. A moving heal target, before any enemy exists. |
| `dr-tobarglas-3` | Ishbel Greenhand | 3 | **leather** | Gather bilberry and nettle on the Shoulder; Ishbel trades the herbs for a leather kirtle. |
| `dr-tobarglas-4` | Ailsa of the Well | 4 | **Purify** | Something in the upper spring is fouling the water and the flock is sick. Purify is not an interrupt — teach it as the thing that *undoes* a state. |
| `dr-tobarglas-5` | Eachann Slowfoot | 5 | **Ward** | Eachann is going up for a lost goat and will not be talked out of it. Escort him. Ward him *before* the wolves, not after — the quest fails him if you heal reactively. |
| `dr-tobarglas-6` | Murdo the Truthspeaker | 6 | Greater Mend | The first oath over the water. A scripted fight where Murdo tanks and you hold him up; the 3 s cast is the point. |
| `dr-tobarglas-9` | Murdo the Truthspeaker | 9 | rank-up + **Yew Staff** | Cut the yew yourself, from the tree above the Green Well, and take the second oath. |

> **The Healer problem, stated plainly:** six of these seven need an NPC ally with a
> health bar you can affect. Nothing in the engine does that today. Either the Healer's
> 1–9 line gets a lightweight "friendly NPC that can take and lose HP" system, or the
> Healer spends nine levels casting Smite at rabbits. **This is the biggest single piece
> of engineering hiding in the quest lane, and it is worth deciding before content is
> written.**

### 1.4 Dromcairn — Support — south-east, English-ish

The cairn behind the landing, where the bards meet every boat. Everything here is about
managing a situation rather than winning a fight.

| id | giver | L | rung | beat |
|---|---|---|---|---|
| `dr-dromcairn-1` | Edmund the Reeve | 1 | **Chant of Swiftness** | Carry the tide-word from the cairn to the pier before the boat casts off. You cannot make it at walking speed. |
| `dr-dromcairn-2` | Rowena Longsong | 2 | **Lullaby** | A dog at the pier will not let anyone near the nets. Do not kill it. Sleep it. The identity button in the first ten minutes, exactly as the ladders doc wants. |
| `dr-dromcairn-3` | Wulfric Oarhand | 3 | **leather** | Row out to the Garveen Shallows and back with Wulfric; he pays in a leather coat. |
| `dr-dromcairn-4` | Edmund the Reeve | 4 | **Cut Short** | A hedge-witch on the Moyree edge is midway through something. Interrupt her. She is a single caster with a visible bar. |
| `dr-dromcairn-5` | Aldith Saltwife | 5 | Chant of Vigor + **Concentration 2** | Two chants, one aura, and the first real choice in the archetype: which two? |
| `dr-dromcairn-6` | Rowena Longsong | 6 | Mock | Crows have taken the Whitemill grain. Debuff, then kill — teaches that your damage is small and your subtraction is large. |
| `dr-dromcairn-9` | Rowena Longsong | 9 | rank-up + **Ash Spear** | Learn the island's argument well enough to sing it: the Crusader war, and why Dál Riata stopped. Pure lore delivery, deliberately, as the Support's rank-up. |

### 1.5 The two shared quests at Dunadd (7 and 8)

The four lines converge here. This is the first time a Lissban character meets a Rinnbeg
character, and it should feel like arriving somewhere.

| id | giver | L | rung | beat |
|---|---|---|---|---|
| `dr-island-1` | Fiachra the Grey | 7 | **cloak** | Four errands, one per quarter, and the cloak is cut from wool each of them contributed. Walks the whole island once — the first time the player sees the map as one place. |
| `dr-island-2` | Fiachra the Grey | 8 | **the AoE beat** | The Moyree is overrun; whatever the archetype's level-8 AoE is, this is where it is handed over and immediately needed. Packs of 4–6 weak mobs. |
| `dr-island-3` | Cadwal the Steward | 9 | bridge to 10 | Carry the muster word up Kingshill to Carrigrua. No combat. Ends standing in front of the gate at level 9, which is exactly where the class quest wants you. |

---

## 2. The level-10 class quest

**Proposed location: Carrigrua, and specifically the OUTER WARD, not the hall.**
Reasoning, for Daniel to shoot at:

- The trial ends here, so it has to look like the biggest thing the player has seen. The
  castle is that. A hamlet's hut is not.
- The vision doc's outer ward already has merchants, livestock and an inn in it. Fourteen
  class masters standing among that reads as a working household, not a quest hub.
- It puts the lore in the right mouth: **Lady Muirenn is the one who took the Crusader
  alliance after Dál Riata warred on the Crusader castle.** A character being made a
  Knight *by the woman who fought the Knights* is the island's argument, delivered once,
  at the moment it matters most.

**Proposed beat, one shape for all fourteen classes:**

1. **The claim.** Your archetype master at Dunadd sends you to the class master who
   matches what you have actually been doing. (Not a menu: the master names the class.)
2. **The proof.** One task in the class's own register, out on the island, at the top of
   the trial's difficulty — the raider camp or the forest edge, so the level-10 quest
   sends you back through the level 8–10 content rather than inventing new geography.
3. **The refusal.** The master says no the first time. Something small is missing — a
   token, an oath, a name. This is the beat that makes it a story instead of a checkbox.
4. **The making.** Back at Carrigrua, in front of Muirenn. The tree opens. The title lands.
5. **The door.** Muirenn's last line points at Portcorr and the boat.

Per-class flavour, one line each (all proposals):

| archetype | class | the proof |
|---|---|---|
| Frontline | Knight | hold the Carrigrua gate alone through one wave |
| Frontline | Zealot | walk into the Fomorian camp and come out |
| Frontline | Wizard *(flagged: the faction data really does file wizard under Frontline)* | break something the island thinks cannot be broken |
| Frontline | Reaver | take the chief's axe off the beach and keep it |
| Healer | Squire | carry a wounded man from the forest to Tobarglas without letting him fall |
| Healer | Truthspeaker | take the oath over the Green Well with Oisín, not Murdo |
| Healer | Völva *(flagged: a Norse word at a Celtic court)* | sit a night alone at Cromcross |
| Support | Provocateur | turn a bandit lair against itself; leave with no kills of your own |
| Support | Bard | learn the war-song and sing it in front of Muirenn |
| DPS | Knave | take back something Carrigrua lost, from people who will not admit having it |
| DPS | Draoi | bring the hag of the northern wood a thing she asked for |
| DPS | Frontiersman | map the forest interior: five markers, no escort |
| DPS | Ranger | kill Cairbre's second, at range, before the lair wakes |
| DPS | Veil-tamer | stand at the mouth of Uaimh na Scáth and listen |

**Open: fourteen bodies or four?** The roster carries all fourteen with a
`consolidateTo` field pointing at the archetype master, so collapsing them is a data edit,
not a rewrite. Fourteen makes the ward feel like a court; four makes it navigable.

---

## 3. The Fomorian raider camp — 8–10

Camasmore Bay, on the cliffs below Shanderry. Five defs, thirteen bodies, one named chief
(`Content/Data/mobs/dal-riata-fomorians.json`). Level 8–10, **group content by design** —
social pull is 2200–2600 uu, so a careless pull is the camp.

| id | giver | L | beat |
|---|---|---|---|
| `dr-camp-1` | Cadwal the Steward | 8 | A boat from Cuaseen never came back. Go and look at the beach from the clifftop. Scouting only — no fight, one long walk, and a first sight of Uaimh na Scáth's mouth from above. |
| `dr-camp-2` | Captain Torcall | 9 | Thin them. Ten raiders, any kind. The quest that teaches "pull two, not five". |
| `dr-camp-3` | Captain Torcall | 10 | **Muirgarv the One-Eyed.** The chief, at the fire. Repeatable weekly or on a long timer. |

Torcall's line after `dr-camp-3` is the first time anyone says out loud what the Fomorians
are camped *beside*, and it is the hook into the dungeon.

---

## 4. Shanderry Forest — 6–12

The grind ground. Four fixed lairs, fourteen wanderers, a boss and a hag
(`Content/Data/mobs/dal-riata-bandits.json`). Level band **6–12 is a proposal** — the
vision doc lists it as an open question for Daniel.

The forest deliberately carries **fewer quests than its size**, because Daniel's brief for
it is a *place you farm*, not a place you complete. Three quests point you in, and after
that the reason to be there is XP.

| id | giver | L | beat |
|---|---|---|---|
| `dr-forest-1` | Cadwal the Steward | 6 | Cromcross has been robbed twice. Clear the lair under it. The introduction, at the bottom of the band, closest to the road. |
| `dr-forest-2` | Captain Torcall | 9 | Carrigrua wants to know how many. Count the lairs — four markers, deep, no escort. |
| `dr-forest-3` | Lady Muirenn | 12 | **Cairbre the Wolfshead.** A bounty, and an argument: Muirenn's own words are that he is kin. Offer a way to bring him in alive that costs the player something. |

Standing content, no quest attached: the hag **Morag the Cailleach** in the northern wood
(level 10 elite, and currently blocked — ParagonMorigesh is not on disk), the wanderers,
and the wolves already placed on Benlea's south slope.

---

## 5. Uaimh na Scáth — the first leg, inside the trial

Progression-v1 §6 puts the dungeon's 9–10 band inside the free trial, so a level 9–10
group must be able to clear the first leg. That leg is the only part of the dungeon this
draft touches; the rest belongs to the Dungeons v1 lane.

**Proposed shape of leg one — the tidal caves:**

- Entry is the mouth on the Camasmore cliffs, visible from the water, so players have
  been looking at it since the boat.
- Fomorians hold it: the same five defs as the outdoor camp, which is the point. The camp
  teaches the mechanics, the cave tests them.
- **The tide is the mechanic.** The first leg floods on a timer. Not instant death — the
  water rises, the floor route closes, and the ledge route opens. A group that dawdles
  takes the harder path. It teaches "the room changes" without a boss doing anything.
- **Leg boss: a Fomorian Bonebreaker with a name**, standing where the fresh water meets
  the salt. Two adds that must be handled first, which is the group-content lesson the
  camp already taught with social pull.
- Behind him, visible and unreachable at level 10: the Otherworld bleed. The thing the
  raiders are squatting beside. That is the 11–15 half, and the trial ends looking at it.

| id | giver | L | beat |
|---|---|---|---|
| `dr-dungeon-1` | Captain Torcall | 9 | The key to the first gate is on the beach, not in the cave. Sends a group to the camp first. |
| `dr-dungeon-2` | Lady Muirenn | 10 | Clear the tidal caves. The trial's last quest, and the first thing a paid character will re-run. |

---

## 6. The boat at Portcorr

Progression-v1 §6: **the gate is a boat.** A level-10 trial character can stand on the
pier and cannot board.

| id | giver | L | beat |
|---|---|---|---|
| `dr-boat-out` | Godric Sailmaster | 10 | Muirenn's word gets you a berth. Godric asks where you are going and the answer is the rest of the Great North. |

Design notes on the gate, all proposals:

- **The refusal must be in the fiction, not in a dialog box.** Godric has a reason: the
  crossing is paid, the boat is full, Muirenn's word covers one passage and you have not
  earned it. A grey "Subscribe" button on a pier is the worst version of this.
- A trial character keeps everything: the island stays open, the dungeon stays open at
  its 9–10 band, the forest stays open. They are not locked out, they are *not leaving*.
- The boat should be visible and should actually come and go. A gate you watch work is a
  better advertisement than a gate that is a locked door.

---

## 7. What this draft deliberately does not do

- **No dialogue.** Every beat above is one sentence of intent. The voice — Welsh in the
  south-west, English in the south-east, Scottish in the north-east, Irish in the
  north-west, mixed at the court — is a separate pass and it needs Daniel's ear, not a
  first draft from me.
- **No rewards table.** XP per quest falls out of progression-v1's curve once the beats
  are agreed; item rewards need `items.json`, which holds exactly one item today.
- **No Frontline ladder detail.** `design/frontline-gn-1-9.md` holds the real Frontline
  1–9 table and this draft has not been checked against it — the Lissban line above is
  built from the *shared rhythm* only, so its levels 2, 5 and 6 may name the wrong skills.
- **No repeatables, no dailies.** Progression-v1's dungeon limits (5 runs/day on boss
  5-mans) imply a daily structure that has not been designed.

---

## 8. Open questions — for Daniel

1. **The Healer's ally problem** (§1.3). Six of seven Tobarglas quests need a friendly
   NPC with a health bar. Build that, or rewrite the Healer's 1–9 line around self-heal
   and Smite? This is the one item here with real engineering behind it.
2. **Forest level band: 6–12?** Still open from the vision doc.
3. **Fourteen class-quest givers at Carrigrua, or four archetype masters?**
4. **Lord or Lady of Carrigrua?** This draft commits to Lady Muirenn because it gives the
   Crusader-war lore its best mouth. Say the word and it is Lord Domnall.
5. **Does the level-10 class quest send you back through the camp and the forest** (this
   draft's proposal, so the 8–10 content gets used twice), **or does it get its own new
   place?**
6. **Is the tide mechanic in leg one welcome**, or does that belong to the Dungeons v1
   session rather than here?
7. **Skill names.** The ladders doc already flags that Mend / Smite / Renew / Ward are
   placeholder plain-register names and that Dál Riata is Gaelic. Quest names have the
   same problem and the same fix — one naming pass over both, or neither.
