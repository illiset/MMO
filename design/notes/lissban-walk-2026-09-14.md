# Lissban walk, 2026-09-14 morning — Daniel's notes (verbatim in substance) and the fix list

Daniel walked Lissban at 09:05–09:45 after night shifts 3/3b. Verdicts: the cabbage field and the grain field are "good job";
the huts are not. Every item below is a MUST for the next Lissban pass, in this order.

## What he said, item by item
1. **Two gated entrances on opposite sides of Lissban.** "I don't want them to have to walk around the whole thing every
   time. The game's gonna be a little bit grindy, shouldn't be too much of a walking simulator." Both gates operated with
   the action key **F** (toggle open/shut), plus an auto-close after ~30 s.
2. **Hut collision is wrong everywhere.** "This is the collision radius on this hut, I can't get any closer to the one on the
   right let alone go inside." "Better but I can walk through the wall? … also where's the door?" "Can't even fit in this
   door." "Collision on this one is too far and can't go in and it's too low; couldn't fit in if it was more functioning
   even, cause it's too low." → The hidden collider rings are DISPLACED from the visible huts (the Celtic House pivot offset
   again: colliders were built around the pivot, not the bounds centre) and their doorway gap does not coincide with the
   mesh's real door. Fix: build every collider from the mesh's world-space bounds and the ACTUAL door opening found by
   probing the post ring; the door must clear a 2.0 m × 0.9 m capsule; the hall (f_house_071 at 0.62) is too low for the
   door — raise the scale until the door is ≥ 2.1 m or pick the variant whose door is taller; prove every hut with the
   capsule sweep AND an in-game walk in through the visible door.
3. **Ground under every hut must be level, with a wooden floor inside.** "The ground should be level inside and wooden
   floor." "This hut is mostly not aligned with the ground, needs fixed" (a roundhouse buried to its eaves). → Cut a level
   pad per building (terrain), seat by bounds-bottom on the pad, add a plank/board floor mesh inside at pad height.
4. **Water trough underground** in the pen (only a corner showing). Re-seat by bounds; the pen fence has open gaps between
   rail sections (posts with no rails) — close them except the one deliberate 3 m gap; the pen floor should be trodden
   dirt, not grass.
5. **Wheat spills outside its fence** on the right of the grain field. Crops must be clipped to the field polygon (inset
   0.5 m). "I'm okay with it not being perfectly square with the one to the right of it."
6. **The ground is too green for this farm** — every field floor is tilled soil, no grass under crops; check all four.

## The bigger picture he gave in the same session (for the night brief)
- "Before we add MetaHumans I'd like to improve the world still and get at least a few areas in Dál Riata to 85% as good
  as launch. Right now organisation has increased but we're closer to 20%."
- "The fog still looks very ugly and basic."
- "Something about the ground still looks single-A, not triple-A — probably the lack of trees and shrubs, but I don't
  like how perfectly flat the whole thing is, and how overly open it is. Lissban should be mostly flat of course, but the
  terrain isn't boundarying anything like in Durotar."
- "Thicker patches of forest, higher trees; I don't know why all these trees have white trunks — not like the pictures I
  gave; thicker trunks, thicker foliage in branches, more branches. I want canopies. Shanderry Forest NEEDS to be what I've
  visioned."
- "Dál Riata is almost all overcast except some coastal areas; some coastal areas are still overcast. Seasons later."
- God mode: F8 free camera, F9/F10 named places, F7 back over the character (built 2026-09-14 09:45).
7. **Field floors: all dirt, right to the fence.** (Top-down of the cabbage field, 09:55) "This is good, but the inside of it
   needs to be all dirt — a more vivid difference. The colour of the dirt that is there is good, but the green remnants on
   the border aren't aesthetic." → Tilled mask covers the whole enclosure and overshoots the fence line by 0.5 m with a
   HARD edge (no blend); same for the pen. Keep the current dirt colour.
8. **Same for the grain field** (top-down, 09:58): green inside the fence line must go — "only dirt for ground and then the
   plants that are being farmed." **Farm tools** in and around the fields would be good: a plough, hoes/rakes leaning on the
   fence, a hand cart, baskets, a hay pile — whatever the packs have (CelticHouse baskets, Medieval_Megapack tools/carts).
9. **Crops outside the fence on the east side of the wheat field** (red-marked top-down, 10:00): three patches of wheat
   rows run past the fence into the lane between the wheat field and the next field. Crops must be clipped to the fence
   polygon (inset 0.3 m) — the crop rows were laid on a rectangle that is bigger/rotated relative to the fenced quad. Also:
   the fence on the near (south) side has a gap in the middle; close it unless it is a deliberate 3 m gate opening, then
   put a gate there.

## TERRAIN BUG found from god cam (10:05) — top of the night list
10. **The roads were carved as canyons.** The Boherath between the ford and Lissban runs along the floor of a trench 20-40 m
    deep with near-vertical rock walls; from the air the road corridor shows rectangular cut blocks / mini-mesas beside
    it, and the coast terrace reads as a straight brown scar with hard edges. Daniel: "why such a valley for the road?"
    Cause: night 3's road benching (grade ≤ 12°) and terrace carving cut into the heightfield with no depth limit and no
    shoulder blend. FIX: restore the pre-cut heightmap in every road corridor and along the terrace, then re-bench with
    limits — max cut/fill 2.5 m, shoulders ≥ 25 m each side blended with noise, side slopes ≤ 25°, no rectangular
    footprints; where a road would need more than 2.5 m of cut, re-route the road around the rise instead (paths follow
    contours). The coast terrace: blend its inner edge 60-120 m into the slope, break its line with noise. Re-run delta_z
    re-seating and the sightline audit after. Prove with the same god-cam poses (aerial over the ford-Lissban road; the
    trench pose).
11. **Delete the seven standing stones outside Lissban** ("still wondering what this is", 10:10). Placeholder slabs, never
    asked for; canon has no stone circle at Lissban (the only standing stone is the Cromcross waystone). Remove the
    LB_*/DRV2_Lissban_Menhir actors and the menhir step from the Lissban scripts. A future stone circle, if Daniel wants
    one, is a named landmark built from scanned boulders.
12. **"Way more of this please"** (10:12, the meadow clumps outside Lissban: tall grass tufts, white wildflower heads, blue
    lupin-like spikes, low herbs). The lowland meadows need dense ground cover everywhere, not a few clumps on a lawn:
    grass tufts, wildflowers, nettle, bilberry, gorse/heather patches, ferns at the forest edge, rocks — clustered in
    drifts (Poisson with clumping), thinning into the fields and the yard, so no open lawn is visible at eye level.
    Density target: ground cover in every 3 x 3 m of meadow, taller drifts along fences, hedges and the forest edge.
13. **Flatten the whole inside of the palisade** (aerial with the red ring, 10:15): "we just flatten out the inside of the
    gates/fence of the town, and make it a small grass [space] with pathways going into the E and W entrances, should make
    the design easier. I want it to feel immersive." → ONE level pad for the entire enclosure (cut/fill to the mean height,
    blended 15 m outside the fence); the interior ground is short trodden grass, not a dirt sheet, with worn DIRT PATHS:
    a main path from the EAST gate to the WEST gate through the yard, forks to every hut door, the fire, the pen and the
    barn; the two gates are on the EAST and WEST sides (the current gate = west); the huts, barn, pen, fire sit on the pad
    with wooden floors inside the huts. Paths continue outside each gate: west to the fields and the track, east toward the
    Boherath / the ford.
14. **East entrance with a baffle** (aerial with red marks on the south-east of the ring, 10:20): "make an east entrance and
    then a little fence so to get in you have to walk left or right around it — get creative but immersive and realistic."
    → A second gate on the east/south-east side where he marked, with a SCREEN: a free-standing palisade section 7-9 m
    long standing 3-4 m outside the gate, so the way in is a dogleg left or right around it (the Iron Age hornwork /
    baffle entrance — real Celtic forts did exactly this). Dress it: a low earth bank under the screen, a torch post or
    brazier at each end, a hurdle or two, the path splitting round it and rejoining at the gate; the dirt path continues
    east from it toward the ford road. Both gates F-operated with auto-close.
15. **The forest edge is a ruler line** (god-cam shot along Shanderry's west edge, 10:25): the trees stop dead on the
    polygon edge and the duff floor ends on the same straight line. → The polygon is a CORE, not a boundary: outside it a
    150-300 m gradient of falling density with domain-warped noise on the edge, outlier trees, copses and hedgerow trees
    running out into the meadow, saplings and bilberry under the outliers; the duff/moss mask feathered the same way so
    the floor colour never shows a straight line. No straight edge anywhere on the island - same rule for fields (hard
    fence edges are the exception, by design) and the coast terrace.
16. **The lowland outside the forest looks pockmarked** in the same shot: hundreds of small pits and mounds with bare-dirt
    rims (the erosion pass's droplet craters) — reads as a moonscape, not meadow. → Smooth the lowland (< 90 m) with a
    wide low-pass that keeps the big rolls and removes the pits, keep the dirt-on-slope rule only for real slopes; the
    coast terrace line visible on the horizon is item 10's scar (blend it).
    Daniel's refinement (10:27): "it should keep going out further to the left just more scattered, and end quickly
    though — not such a stark or contrasted transition. Same with ground colour as the mountains begin." → Edge gradient:
    trees continue ~100-150 m past the core, scattered (a few per 100 m²) then gone within another ~50 m; the duff-to-grass
    and grass-to-heath/rock colour transitions are wide noise-broken blends (50-150 m), never a contrast line, including
    where the meadow meets Benlea's lower slopes.
17. **The forest trees are clones with low branches** (10:30): "1 out of every 4-6 should be about twice the diameter re.
    trunk size; I don't want the branches to begin so low; thicker branches and leaves/fur, but the canopy should begin
    quite a bit higher — maybe 4 times higher before the ceiling of the forest begins if you were standing on the ground
    looking up." → Targets: lowest branches on canopy trees ≥ 15-20 m (now ~6 m median), forest ceiling 25-40 m; giants
    1-in-5 at ~2x trunk diameter (scale 1.6-2.0 of the tallest asset, taller and thicker, crowns above the rest); the
    other 4-in-5 vary scale 0.8-1.3, random yaw, 3-4 mesh variants, per-instance colour/tint variation (PerInstanceRandom
    in the bark and needle materials) so no two neighbours match; thicker branch/needle density in the canopy. HOW: (a)
    object-space height mask on the needle/branch material that hides branch geometry below a per-instance threshold
    (bare trunk to 2/3 height, per the reference photos) — cheap, instant, per-instance; (b) giants by scale; (c) Norway
    Spruce (static Megascans) the moment Daniel adds it to the project — its forest-grown variants have the high crowns
    natively; (d) understory stays at ground level (ferns, bilberry, saplings) so the gap between floor and canopy reads
    as a hall, like the photos.
18. **Rivers and streams** (aerial of the Owenfinn inside Shanderry, 10:35): "nice but need improved drastically with
    detail and beauty, and to actually function and seem real and flow." What the shot shows: the river bed is a straight-
    walled brown trench cut through the forest (item 10's carving), the water is patches of flat pale-blue polygons (a
    stray rectangular water piece too), trees stand inside the channel. → Rivers are built as SPLINES with a continuous
    water ribbon that follows the bed (UE Water plugin river bodies if they run on this project, otherwise a spline-mesh
    water ribbon with our M_TR_Water), FLOW along the spline (panning normals + foam streaks in the flow direction, faster
    at drops), depth colour from bank to centre; the bed carved as a gentle meandering channel (banks ≤ 30°, no vertical
    walls, gravel bars on the inside of bends); trees cleared from the channel + 4 m of bank; banks dressed with mossy
    boulders, reeds, alder/willow, ferns, fallen logs across narrow stretches; the waterfall with a mist emitter and a
    plunge pool; forest streams the same at 1-3 m width; the river mouth at Portcorr widens into shingle. Prove with an
    eye-level capture standing on a bank and a low aerial along a bend.
19. **Shanderry is uniformly dense** (10:38): "a little too dense — it should be that dense, but there should be areas where
    you go to do things that open up slightly too." → Keep the closed-canopy density as the baseline but compose the forest
    with GLADES and CLEARINGS: 20-30 openings of 30-80 m (wind-throw gaps with fallen giants and light, mossy boulder
    fields, a bog/pond, the bandit camp clearings, the stream-side meadows, the Cromcross waystone in its own glade),
    connected by game trails; the mob camps and gathering spots sit in the openings; density falls to ~40% within 20 m of
    each glade edge; ferns/bilberry thicken in the light. Glades are placed on the map (named where canon allows) — not
    random holes.
20. **The mountain road is paint on a 45° rock face** (Bohermara across Benlea's flank, 10:42): "love it, needs to be flat
    on the pathway though so people don't just slide down." → Every road on a slope gets a BENCH: a 3.5-4 m carriageway
    cut level ACROSS the slope (small outward camber), an uphill cut face ≤ 2.5 m high that reads as rock/scree, a
    downhill fill edge with a few boulders as kerb, along-grade ≤ 12°; the bench follows the painted line; foliage/rocks
    cleared from the carriageway; the look of the rock face stays. This is the correct form of item 10's benching: a
    shelf across the slope, never a trench into it.
21. **The forest road** (Bohermara/Boherath corridor through Shanderry, 10:50): "love this forest path" — KEEP the corridor
    feel (a wide dirt hollow-way with trees pressing in on both sides), but: (a) the road surface "looks too flannel /
    patterned" — the dirt layer tiles visibly; break it with a second dirt/gravel texture at a different scale, wheel-rut
    and puddle detail down the middle, stones and leaf litter at the edges, so the road reads as a defined worn track,
    not a flat patterned sheet; (b) transitions again: "remember transitions in terrain type need to ease into each
    other — not plains with shrubs and grass then one step later dense forest — unless it's man-made"; (c) **a halfway
    rest**: flatten a widening about midway along the forest road — a clearing with a table/benches, a fire ring, a cart,
    a merchant or two (roster: travelling traders or a Dunadd merchant's stall), a signpost; this is also a glade for
    item 19. Same treatment for every long road: a rest every ~1.5-2 km (a shrine, a well, a herder's hut, a waystone).
