# Brief: Lissban first (Daniel, 2026-09-13 20:20)

**Daniel's words:** "for now, I just want Lissban to have a wooden fence around it with 3 small huts, 1 large hut and some
farms outside to the west/southwest right outside of the gates. A non-perfect circular formation is fine for the wooden
walls. We're gonna build Lissban first then the rest of Dál Riata."

Working rule from tonight on: **one thing at a time.** Lissban is the whole job until Daniel signs it off in a walk.
Nothing else on the island is touched (no forest pass, no other village, no creatures) unless it is inside Lissban's 300 m.

## The spec (exact)
- Position: the v1 layout spot, `data/zones/dal-riata.json` settlements.lissban = (-3493.4, -1045.9), on Blunt Head's neck,
  facing 35°. Level `/Game/ThreeRealms/Maps/GN_DalRiata_v2`. Scale of the island is CONFIRMED correct (11 × 6 km).
- **Wooden fence (palisade) around the village**, a non-perfect circle: wobbly radius 26–34 m, continuous, ONE gate. The gate
  faces west/south-west, toward the farms. Palisade pieces from the Celtic House pack (or Medieval_Megapack wooden wall
  pieces if they look better up close), slope-following, no gaps, no floating posts, no doubled runs.
- **Inside the fence:** 1 large hut (the hall, the biggest Celtic roundhouse) + 3 small huts, all doors toward a common yard
  with a fire pit; a woodpile; ONE animal pen (the current three overlapping circular pens are deleted); a water trough or
  well if the pack has one. Worn dirt on the yard and the paths (landscape dirt layer), grass gone inside the fence.
- **Farms outside, right outside the gate, to the west and south-west:** 3–4 field enclosures of 40–70 m, irregular
  quadrilaterals, bounded by low wattle/wooden fences or hedges (Bilberry/Hazel rows), a crop or tilled layer inside
  (dirt/crop landscape layer), a cart track from the gate between them. A haystack or two if the pack has them.
- **Standing stones** stay where they are (outside the fence, standing, buried 0.45 m) unless they collide with a field.
- Everything obeys design/notes/dal-riata-focus.md §0b (the composition standard) and §0 (no floating, no putty rocks).
  Every placement script CHECKS ITS FOOTPRINT against existing actors first; the pass ends with an overlap audit and a
  grounding audit (report the numbers).
- **Class trainers** live at the starting villages (Lissban = Frontline trainers); placeholder NPC bodies are fine, the
  names come from Content/Data/npcs/dal-riata-npcs.json. Not required for sign-off, but place the trainer + a merchant if the
  roster has them.

## Proof required
- Fixed-pose captures, gizmos hidden: (1) from the south-west field looking at the gate, (2) inside the yard, (3) a high
  three-quarter view showing fence + huts + farms, (4) an in-game walk capture from PlayMythicEarth.bat with Celtictest
  seated just outside the gate on the track.
- Overlap audit: 0 overlapping pens/fences/huts. Grounding audit: max gap ≤ 0.05 m.
- Editor closed cleanly at the end; PlayMythicEarth.bat left on GN_DalRiata_v2; both repos committed and pushed.

## Rules
- Never run the editor and the play stack together on this laptop (23 GB RAM; that is what crashed the client at 17:13).
- Do not touch the terrain outside Lissban's 300 m. Do not regenerate the heightmap.
- Log lines or captures, or it did not happen. Check the clock with `date`; do not estimate elapsed time.

## Collision (Daniel 2026-09-13 20:30: "people need to be able to walk inside the doors and go inside the huts")
Collision is part of building a thing, not a later pass. Lissban is not done until all of this is true in a walk:
- **Every hut can be entered through its door.** The Celtic House meshes must use per-poly (complex-as-simple) collision or a
  custom simple collision with the doorway open; the floor inside must hold the player; no invisible box across the door.
  Interiors get a hearth, a bed/bench and a few props so entering is worth it.
- **The palisade blocks everywhere except the gate.** No gaps a player can slip through, no invisible walls beyond the posts,
  the gate opening is at least 3 m wide and walkable.
- **Fences/pens block** (as they do now), but the pen has a gate or a gap so the player can reach the animal.
- **Trees: trunk collision on (capsule), foliage/branches off**, so you cannot walk through a trunk but never snag on leaves.
  Small plants, grass, ferns: no collision.
- **No floating props and nothing you can walk under that should be solid** (grounding audit ≤ 0.05 m).
- **NavMesh** covers the village and the fields so NPCs and the pen animal path round the huts; bake at least the Lissban area.
- Proof: an in-game walk capture entering the large hut and standing inside, plus a log/capture of walking the full fence
  line from the inside without finding a hole.
