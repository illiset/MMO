# Dál Riata — current focus list (2026-09-13)

Scope: only what Dál Riata needs to be a complete level 1–15 starter island. Order = priority.
Nights = engine work (from the main session as background agents); days = design docs (Opus chats).

## 0. Bugs from Daniel's walk test (fix first tonight)
- A/D turn: camera turns but the walk direction doesn't follow (or the body turns and movement keeps going straight). WoW rule: A/D rotate the character, camera follows, W moves along facing, Q/E strafe relative to facing.
- LMB+RMB together = walk forward (and it must cancel Num Lock auto-run); auto-run must also stop on S.
- THE LAKE (Daniel likes where it is — keep the placement): it needs a feeder STREAM coming down from the high ground, more distance from the ocean (push it inland), and a natural basin — gentle banks, shallow margins with reeds, no crater walls; it sits far too deep below the surrounding ground, like something dug. Give it an outflow to the river or the sea. Clean up its shores.
- SPRINT (Daniel likes it: barely faster, keep that) must DRAIN ENDURANCE slowly while held and stop when it runs out; the endurance/stamina pool is the master program's 100 with 7/12 regen (gold bar on the frame). First real use of the resource bar; regen resumes when not sprinting.
- GROUND LAYER TRANSITIONS are hard straight lines (grass ends and rock begins along a ruler edge on Benlea): the auto-material's height/slope thresholds need wide, noise-broken blend zones — rock creeping into grass as scattered outcrops and patches, grass climbing the rock in tufts and heath, scree fans and gullies crossing the line, moss in the seams — never a clean contour. Same for the beach-to-grass edge. Tune the MWAM blend widths and add a noise mask; verify from a mid-distance capture.
- ANIMALS BELONG TO BIOMES (a Wild Pig on Benlea's bare face): every wildlife def gets a habitat rule — allowed biome bands, max slope, distance from home — and wander must stay inside it (pigs and deer in lowland forest edge and meadow, foxes in scrub and field margins, crows anywhere, wolves in the forest and its edge; nothing on bare rock above the tree line except crows and, later, goats). Spawners placed only inside their habitat; the wander leg picker rejects steep or out-of-biome targets.
- PURGE the Roman & Celtic pack rocks from the level entirely (the smooth putty boulders, now floating on Benlea's face too): every rock on the island becomes a scanned rock (Dolomites, Nordic Forest, mossy boulders) at natural size, slope-aligned and sunk into the ground; a rock that floats or sits like a dropped toy fails the grounding audit.
- MOUNTAINS ARE A SMOOTH RAMP (Daniel on Benlea): real mountainsides are broken — outcrops and ledges, scree fans, gullies and terraces, boulder fields, cliff bands, heath and bare-rock bands by height. Fix in the rebuild: erosion/roughness in the heightmap generator (not a smoothed cone), the vault's Nordic Forest cliff/ledge/rock-shelf scans placed as outcrops with slope alignment, scree material where it's steep, cliff layer with proper projection. Stumps and trees never on bare 35°+ slopes and never lying sideways: props align to the slope normal only when they're rocks; plants stay upright and only on ground that could grow them.
- ANIMAL DEATH: the wolf died standing and vanished — every animal needs a death animation (the packs ship them; the wildlife defs must reference death sequences like the Rimethrall defs do), a corpse that lingers, and LATER a harvest interaction (skin/butcher with an animation and loot) — harvesting is on the to-do list, not tonight.
- COMBAT PACING (Daniel vs a wolf: dead in 2–3 hits, and it hit him too hard — "not a WoW or DAoC fight"): an even-con solo fight must last roughly 15–25 s (6–10 player actions) and cost the player about a third of his HP. So mob HP up substantially and mob damage per hit down for the low-level animals; the early skill burst (Bash 38 + Strike 23 at level 1) is also too big for level-1 pacing. Numbers belong in MMOStats (a time-to-kill table by level), but the wildlife defs get a first correction tonight.
- WILDLIFE DENSITY far too low (Daniel crossed most of the island and saw one hog, one fox, one wolf): populate for the 8–10 km island in HERDS and PACKS — deer in groups of 3–6, pigs in sounders, foxes solitary but frequent, crows in flocks, wolves in packs of 2–3 that are HOSTILE (the one he met did not attack — verify the wolf spawners' reaction flip and aggro radius ~15 m in the server log). Target: an animal in view most of the time in fields and forest edge.
- A Training Dummy stands in the middle of the island — remove it (dev leftover); the practice dummy belongs at Lissban's muster yard only, if anywhere.
- ANIMAL LOCOMOTION is unacceptable (the fox: "disgusting, not natural even slightly"): use the pack's own animation blueprints / speed-matched blends instead of our single-node loops; movement speed must match the animation's stride (no sliding), turning must be rate-limited (no snapping), wander legs must ease in/out with idle-look-around beats, and animals must react to the player (flee radius for deer/fox, threat for wolves). Root-motion or speed-warp; foot IK later.
- CONTROL SPEC (WoW, exact): the character MOVES IN ITS FACING DIRECTION, always. LMB drag orbits the CAMERA ONLY (facing and movement unchanged). RMB drag turns the CHARACTER (camera follows behind). A/D turn the character. LMB+RMB together = move forward and cancels Num Lock auto-run. With auto-run on, an LMB camera orbit must NOT change where the character runs (Daniel saw: walking left while facing forward). Q/E strafe relative to facing.
- Stairs are not walkable (the stilt granary's stair and the roundhouse steps): collision + step height/ramp; doors don't open: an interact-to-open door (F) on the Celtic houses.
- Locomotion animation looks lifeless: replace the kit mannequin walk/run/idle set with a proper locomotion set (Epic's free Lyra / Animation Starter Pack retargeted, or the MetaHuman set when bodies land); sprint and turn-in-place included.
- Character-to-tree scale is wrong: the Roman & Celtic scatter trees read as shrubs; every tree must be 8–25 m against a 1.8 m character (scale audit script).
- XP bar: replace the light-blue aurora skin with a bold solid fill on a stone-textured plaque (Daniel: "bolder solid colour, stone background").

## 0b. Composition standard for hamlets (Daniel's Lissban verdict 2026-09-13: "one of the shittiest towns")
- What went wrong: multiple identical stone circles/cairn clusters scattered everywhere, lone palisade gate segments standing in the open with no wall, watchtowers dropped at random, houses with no paths, yard, fire or fences, nothing grounded. Floating stones. No composition rule.
- The rule from now on: ONE sacred circle per hamlet at most (real menhirs, spaced, outside the gate), an ENCLOSURE (bank + ditch + continuous palisade with a single gate) or none at all — never a lone gate; houses around a yard with a central fire, paths worn between doors, fences/pens with the pig and dog, woodpiles, racks; a watchtower only where it guards the gate or the shore; everything traced to the ground; trees at real scale around and inside; a composition captured and checked from the road before the night ends.
- Identity check: the stone-circle hamlet is LISSBAN (Frontline start). Carrigrua is the fort on the rise NE of Dunadd and is currently only a blockout.

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
