# Dál Riata — current focus list (2026-09-13)

Scope: only what Dál Riata needs to be a complete level 1–15 starter island. Order = priority.
Nights = engine work (from the main session as background agents); days = design docs (Opus chats).

## 0. Bugs from Daniel's walk test (fix first tonight)
- A/D turn: camera turns but the walk direction doesn't follow (or the body turns and movement keeps going straight). WoW rule: A/D rotate the character, camera follows, W moves along facing, Q/E strafe relative to facing.

## 1. World polish (night 2, in this order)
1. Tobarglas re-sited on a natural shelf under the Bealanard Shoulder; all four starts re-checked.
2. Ground cover: real grass, ferns (Fern Collection + Quixel ferns), heath (bilberry/nettle/anemone),
   moss floor, reeds at Portcorr and Cuaseen, mud round the village and roads.
3. Shanderry Forest as PNW temperate rainforest: tall conifer canopy (Norway Spruce + Baltic Pine
   bakes, material wind), moss-draped trunks, big shrubs, nurse logs / fallen giants / root walls /
   gullies (vault scans), streams, a waterfall where the Owenfinn leaves the forest, plank
   footbridges, canopy darkness, fireflies. Broadleaves only at edges and water.
4. Stones: a real standing-stone circle at Lissban (few, tall, spaced), cairns from the scans;
   Carrigrua walls from the Modular Castle kit (keep + curtain wall + gate + drawbridge + outer ward).
5. Grounding pass on every placed actor; cliffs' rock projection fix; sea with waves + wet-sand shore.
6. Village dressing: paths, fences, woodpiles, carts, hearth smoke; Iron-Age earthwork rampart +
   timber palisade at each start (no stone walls at Celtic hamlets).
7. Weather baseline via Ultra Dynamic Sky: overcast PNW, fog thick in the north, clear pockets on the
   S/SE/E shores and coastal fields (Dál Riata ~70% overcast).
8. Full-quality captures with gizmos hidden.

## 2. Creatures on the island (data-driven mob defs; all new models)
- Neutral wildlife (have): stag, doe, fox, pig, crow — wander by biome. Ambient life via FX: birds,
  seagulls on the coast, insects, fish.
- Aggressive wildlife: wolves (have). Boar/bear later if the $50 Forest Animals pack is bought.
- Fomorian raiders (Grux + Rampage re-dressed): the beached camp outside Uaimh na Scáth (8–10) and
  the cave's first act. Sea-giant palette: barnacle, kelp, salt-white, one-eyed/one-armed variants.
- Shanderry bandits (6–12): outlaw kin of Dál Riata who refused the Crusader alliance; fixed lairs +
  wanderers; built on Paragon Sparrow/Greystone re-dressed until human bodies exist.
- The hag of the northern wood (Morigesh re-dressed): a bog-witch, level 8–10 elite.
- Otherworld fae: DEFERRED to the MetaHuman race recipe (Sídhe both sexes from one recipe); the
  Banshee MetaHuman as a single unique being when bodies land. No Paragon "The Fey".
- Uaimh na Scáth interior + bosses: designed in the Dungeons v1 chat; built in the dungeon lane.

## 3. NPC roster (define as data now; bodies come with the MetaHuman lane)
- Each start: an archetype trainer/quest-giver, a merchant, 3–5 villagers, a dog/livestock.
- Dunadd: village elder, innkeeper, smith, general merchant, a bard (Support flavour), children.
- Carrigrua: the lord/lady of Dál Riata, the captain, gate guards, the level-10 class-quest givers for
  the 14 Celtic-reachable classes (or their trainers), a healer at Tobarglas's Green Well.
- Accents by quarter (design/notes/dal-riata-accents.md) drive voice, idiom, names, dress details.

## 4. Quest and content design (Opus chat: "Dál Riata Quests v1")
- 1–9 quest lines per start feeding the archetype ladder; the level-10 class quest (where, what beat);
  the raider camp 8–10; the forest 6–12 grind ground; the 5-man 9–15 with its 9–10 first leg inside
  the trial; the boat at Portcorr as the gate.

## 4b. HUD navigation (Daniel 2026-09-13): compass + minimap + zone map
- Compass strip at the top (heading, N/E/S/W, markers for the starts, Dunadd, Carrigrua, the ford, Portcorr, the cave).
- Minimap: rotating crop of the as-built map texture centred on the player with a player arrow; M key opens the full labelled zone map with the player dot. Map texture = the render from Tools/dalriata/render_labeled_map.py (regenerate when the island changes).

## 5. Systems the island needs
- Done: first-entry placement, wander AI, hostile policy, movement pass, camera clamp.
- Next: Ultra Dynamic Sky integration; death/rez v1 (XP debt, rally points, Healer rez); the boat
  gate; XP table + con + group XP + debt from progression-v1; instance tech for the dungeon.

## 6. Player bodies (gaming PC)
- MetaHuman Celtic male + female from the race bible, starter clothes (no armour), retarget the kit
  animations, hook equipment. This is the "can't stand the character" item and the fae race recipe.

## Purchases outstanding for this list
- Bought: Modular Castle, Ultra Dynamic Sky. Free to grab: Norway Spruce, Fern Collection, Lady/Beech
  Fern, Sharur's village, ElderBoom Hollow, Sevarog (optional), Morigesh.
- Later: Forest Animals ($50, boar/bear), the Banshee MetaHuman ($15), Modular Elves ($450, when the
  elf races go playable).
