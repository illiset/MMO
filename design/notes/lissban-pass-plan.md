# Lissban pass — the plan, step by step (2026-09-14)

Needs the editor open ~1.5–2 h (about 5 GB; the game closed), plus one code build for the F-gate. Every step ends with a
saved level and a log line; steps 11–12 are the proof. Daniel's hand-placed actors (anything not LB_*/DRV2_*) are kept.

1. **Survey + backup.** Snapshot the current Lissban actors; list Daniel's hand-placed ones (kept, worked around); delete
   the seven standing stones and the menhir step in the scripts.
2. **The pad.** Take the palisade ring's polygon; flatten everything inside it to one height (the mean), blend 15 m
   outward with noise so the edge is a natural rise, not a step; re-import; re-seat every actor on the new ground.
3. **Palisade + gates.** Keep the wobbly ring. Open an EAST gate opposite the west one (3.2 m). Both gates get the swinging
   gate actor with F to open/shut and a 30 s auto-close. Build the east BAFFLE: an 8 m palisade section 3.5 m outside the
   gate on a low earth bank, torch posts at its ends, a hurdle or two, the path splitting round it.
4. **Buildings.** Hall (bigger), three family huts, barn (large granary): re-seated on the pad by their bounds (the meshes'
   pivots are 20–30 m off), doors checked for a 2.1 m × 0.9 m clearance (scale up or swap the variant), collider rings
   rebuilt from the REAL walls with the gap on the REAL door (found by probing the post ring), wooden floors at pad height,
   interiors furnished (hearth, bench, bed, baskets, tools).
5. **The yard.** Fire pit with logs, woodpile by the hall, ONE pen (fence closed except its 3 m gap) with the boar, trough
   dug up and re-seated, a cart by the barn, tools leaning by doors, a well or water trough.
6. **Ground.** Inside the pad: short trodden grass. DIRT PATHS: east gate ↔ west gate through the yard, forks to every hut
   door, the fire, the pen, the barn; paths run on outside both gates (west to the fields and the track, east toward the
   ford road). The world-space mask is regenerated for these; the pen floor is dirt.
7. **Fields.** The four enclosures W/SW: soil to the fence with a hard edge overshooting 0.5 m; crops clipped inside the
   polygon (the wheat rows that spill east go); the south fence gap closed or made a gate; farm tools, a hay pile, a plough.
8. **Surroundings.** The shelter belt as an irregular 2–3-row stand of mixed heights, the copse kept, hedgerow lines along
   the track, dense meadow ground cover within 300 m (tufts, wildflowers, nettle, bilberry, rocks) thick along fences.
9. **The hill.** A broad rounded hill NE of the village past the tree belt: thick pines on the crest, a big boulder outcrop,
   gorse flanks; the ford road bends round its east foot; from inside the palisade Kingshill and the castle are hidden
   (a landform sightline check, not just the castle point).
10. **People.** The eight villagers placed from anchor + offset at their work spots (the chief at the hall door, the trainer
    in the yard, the merchant, the thatcher, Nest Goch at the barn, the boy, the guide); roster positions rewritten for v2.
11. **Audits.** Grounding ≤ 5 cm on every actor; zero overlaps; a capsule sweep of the whole fence (no holes) and of every
    hut door (opens on the real door only); nav bake for the village area.
12. **Proof.** Fixed-pose captures (SW field → gate, the yard, high three-quarter, inside the hall, the east baffle, the
    hill from the yard) + an in-game walk (west gate in, yard, into the hall, out the east gate round the baffle); the
    character seated on the track outside the west gate; a short report; both repos pushed. Then Daniel's sign-off walk.
