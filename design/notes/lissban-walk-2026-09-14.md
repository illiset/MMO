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
22. **Swimmable water, and a real underwater view** (lake shots, 10:55): "this does look kinda natural but my issue is the
    underwater view — it looks like a mistake instead of intentional, and we need swimmable water, not just a surface
    plane of flowing water." What the shots show: the lake plane runs out over the meadow/forest with trees standing in
    the water (the plane is bigger than the carved basin); from below, the surface is a dark sky-like ceiling with the
    world in full clarity. → (a) SWIMMING: water volumes (physics volumes with WaterVolume on) over the lake, the sea and
    the deeper river reaches so CharacterMovement switches to swimming; a swim animation in the ABP (placeholder loop is
    acceptable for now); this REPLACES the wading-floor idea — the far sea still needs a boundary (fatigue/kill after N
    seconds beyond the shallows, or an invisible wall at the map edge); (b) UNDERWATER LOOK: a post-process volume inside
    each water volume — blue-green tint, heavy fog (10-25 m visibility), slight blur, light shafts if cheap, muffled
    ambient — and the water surface TWO-SIDED with a darker, wavy underside seen from below; the lake bed textured (silt,
    stones, weeds); (c) the lake plane clipped to the basin contour with a 2 m margin, no foliage instances below water
    level; (d) river reaches: the same, at their depth. Prove: a capture from 2 m under the lake surface and one swimming.
- (11:05) Daniel, flying over Kingshill: "you've got a great start on Kingshill." Keep the hill's form and the gorge; the
  castle is rebuilt on its shoulder (v1 spot) after the Lissban sign-off.
- (11:08) DUNGEONS, Daniel: Uaimh na Scáth is confirmed the LOOT 5-MAN (9-15). "The other 5-man on Dál Riata will be
  something I establish in a bit" — a second 5-man (plus the grind dungeon and, later, a raid site) is his to name and
  site; nothing is built or named for them until he does.

## CARRIGRUA concept (Daniel's sketch over the god-cam top-down, 11:15) — for the castle pass after the Lissban sign-off
- "Concept for Carrigrua layout with road additions; should feel like you're not in the wild anymore while inside these walls."
- Sketch, north up: a road comes in from the NORTH (a spur off the Bohermara/Cromcross line) and curves into a GATE on the
  north side of the enclosure. Inside, the NORTH half is the COURTYARD ringed by small buildings (tavern, inn, stores drawn
  as small rectangles on its west and north sides, a long building on its south edge). The SOUTH half is the KEEP: one big
  rectangular block inside its own inner wall. The curtain wall runs round everything, labelled "castle walls" down the
  east side, and continues south past the keep with the wall line turning west at the bottom (room for a second gate on
  the south/west, toward Dunadd's castle road). Towers at the corners and the gate.
- Inside-the-walls rules: flagstone/cobble ground, no grass, no wild plants; buildings close-set with lanes; torches/
  braziers, market stalls, barrels, carts, a well; the roster's Carrigrua people (Muirenn the ruler, Ollamh Aneirin, guards,
  merchants) at their posts; town sounds. Outside the gate the road returns to dirt and the wild resumes within 50 m.
- Site: Kingshill's shoulder at the v1 spot (data/zones/dal-riata.json settlements.carrigrua); the sketch's water on the
  left is the sea seen from above — keep the sightline audit passing when the keep's height is added.
- (11:20) ROAD CARVING, corrected by Daniel: "for the forest road I actually like the carved-out earth for it, just not for
  Lissban to Portcorr and Lissban to Kingshill or anywhere else unless I say." → Item 10 applies to every road EXCEPT the
  forest road: the hollow-way (sunken, carved) profile stays on the Bohermara/Boherath stretch INSIDE Shanderry only;
  everywhere else (Lissban–ford–Kingshill/Carrigrua, Lissban–Dromcairn–Portcorr, Dunadd spur, the coast road, the
  mountain bench) the road sits on the ground with the 2.5 m cut/fill limit and wide shoulders. No other road gets the
  carved profile unless Daniel names it.
23. **Aerial of the lake (11:22, no words needed):** (a) the lake is a perfect ELLIPSE of flat turquoise — it must take the
    basin's own contour (irregular, with a reed margin and a shingle bay), item 22c; (b) a huge brown sheet to its west:
    the forest-floor (duff) mask painted far beyond where trees stand — the duff mask must be derived from the ACTUAL tree
    instances (canopy coverage), not the biome polygon, and must fade out with the edge gradient (item 15); no bare brown
    where there is no canopy; (c) the road through it is item 10's trench.
- (11:30) Daniel: "sprinting and turning are good." **Mouse sensitivity options must be in the ESC settings menu** (camera
  look sensitivity X/Y, invert Y, and the god-cam look speed while we have it), saved per account. Add to the HUD/settings
  backlog as a MUST before any wider playtest.
24. **A blue debug line runs from the character while moving** (11:35): drawn by the kit's
    Content/MMOKit/MMO_Logic/Blueprints/Camera/BP_PointNClickCameraComponent (a DrawDebugLine node for click-to-move).
    We use WoW controls, not click-to-move: disable that component on BP_PlayerCharacter (or delete the debug-draw nodes
    in the BP) so nothing debug is ever visible in game.
25. **Sprint on auto-run** (11:36): "while Num Lock/auto-run is on, double-tapping Shift should make the character sprint
    when able, but always preserve 15% of stamina." → Double-tap Shift (≤ 0.3 s apart) toggles sprint during auto-run;
    holding Shift keeps working when driving manually; sprint cuts off at 15% stamina (not 0) and cannot restart until
    stamina is above ~25%; regen unchanged (12/s when not sprinting).
26. **Wolf fight (11:45):** "the time it took for it to die was good but it did zero damage to me — maybe increase kill
    time slightly but make it do damage to me too." → BUG: wolves (and probably every AnimalVarietyPack mob) deal 0 damage.
    Likely cause: the kit applies mob melee damage from an animation notify that the animal montages do not carry (the
    Rimethrall on a humanoid skeleton did hit in M3). Fix: server-side timer-based melee for mobs (damage applied on a
    swing timer with range + facing checks, independent of notifies), then the animal attack anim just plays; verify with
    the harness that player HP drops. Tuning: wolf HP +15-20% (kill time slightly longer), wolf damage per the def
    (6-10) so a fight costs ~1/3 HP.
27. **Deer walk animation "headbanging at a rock concert"** (11:52): "animations need to be so much better; it's
    embarrassing if I showed anyone this." → The animal locomotion is still wrong in the way that matters: the wrong
    clip or the wrong play rate for the speed (a walk clip played at run rate / a run clip at walk speed), and no blend.
    Requirements: use the AnimalVarietyPack's OWN animation blueprint per species (they ship with locomotion blendspaces
    walk/trot/run keyed to speed); mob speeds set to the clip's native speeds (deer walk ~1.2 m/s, trot ~3.5, run ~7);
    play rate = speed / clip's authored speed (stride-matched, no foot sliding); blend 0.2-0.3 s between states;
    idle/graze/look-around when stopped; turn-in-place below 30°/s. PROOF is a 10 s capture sequence (or short video) of
    a deer walking and running judged by eye, not a log line. Until this passes, no animal placement is "done".
28. **LMB changes the walking direction** (11:55): "LMB should change view but not the direction the character's walking
    in; right now it does not." → Same root as item 24: the kit's BP_PointNClickCameraComponent implements CLICK-TO-MOVE —
    an LMB press sends the character toward the clicked ground point (and draws the blue line to it). Fix in C++ at
    take-over time: find any component on the pawn whose class name contains "PointNClick" and destroy/disable it (no
    Blueprint edit needed), so LMB is camera-orbit only. Build with items 25 (double-tap sprint, 15% floor) and the F
    gates. Prove with the harness: LMB press while auto-running leaves the heading unchanged and no [click-to-move] log.
    (11:57) Clarified: "right now LMB does nothing with the view." → LMB orbit was never actually implemented in our
    code; the kit only mouse-looks on RMB. Implement in TickMovementPass: while LMB is held (and RMB is not), apply the
    raw mouse delta to the control rotation (yaw + pitch, clamped) — camera only, body untouched; on release the
    camera-follow-behind eases back if moving. Prove: LMB drag changes the camera yaw in the log while heading and body
    yaw stay constant.
29. **RMB look is "skippy"** while walking (auto-run or not) (12:00): "something's off, it's not a smooth view change."
    → Likely the hard snap of the body yaw to the control yaw each tick (our RMB rule) running a frame behind the kit's
    mouse-look, at the 30 fps cap: the camera moves this frame, the body next frame, so the view stutters relative to the
    body. Fix: drive BOTH from one place — while RMB is held read the raw mouse delta ourselves, apply it to the control
    rotation AND the body yaw in the same tick (no kit look), with the body interpolated at ~720°/s so it never pops;
    frame-rate-independent (delta-time scaled); mouse smoothing off; expose sensitivity (item on ESC settings). Prove at
    the 30 fps cap with a capture sequence during a 180° RMB drag while auto-running.
30. **FOREST TONIGHT — the standing order (12:05):** "the canopy of the forest MUST be better by the end of tonight. I want
    the forest to look more diverse and not just exactly the same everything — not every single tree the same exact
    copy, shrubs everywhere, and some slightly less dense areas where in-game activities are done, like a grinding spot
    or two. The dense forest should be RARER and just slightly more open should be the NORM, with some areas that are
    more defined and obvious areas of interest." → This REPLACES the closed-canopy-everywhere baseline of items 2/19:
    norm = moderately open woodland (~150-250 stems/ha, canopy gaps, light on the floor, shrubs/ferns/bilberry everywhere,
    fallen logs, rocks); dense pockets (400+/ha, dark, mossy) as the exception, placed deliberately; clearings/glades as
    obvious points of interest (grind camps with mob packs, a ruin, a pond, the waystone, the bandit camp), each with its
    own dressing so they are recognisable; canopy character per item 17 (giants 1-in-5, bare trunks, high crowns, no
    clones: 3-4 variants x scale x tint). Judged by god-cam flyover AND eye-level captures before the report.
31. **The coast (12:10):** "not every single part of the coast needs to be like the cliffs of Dover; also it's too
    perfectly straight lines, not natural looking at all — fix it tonight." → The coast terrace and the cliff bands were
    cut on straight lines. Coast recipe per stretch (from the plan): cliffs only at the headlands (Blunt Head, Grey Head)
    and Benlea's north/west faces; everywhere else a mix of shingle and boulder shores, low rocky platforms, pocket
    strands of sand, dune/machair grass, low grassy banks; the shoreline itself, the terrace edge and every cliff top
    broken with domain-warped noise at several scales (50 m, 200 m, 800 m) so no line is straight; wave-cut notches and
    coves; the sea bed sloping unevenly. Judged from the god cam along the whole coast before the report.
32. **The yellow blob under the wolf** (12:20): our target-ring decal projected on a slope from the capsule centre reads
    as a smeared yellow "face". → Attach the ring at the traced ground point under the target, aligned to the ground
    normal, with a deeper projection box, and re-align while the target moves; the ring becomes the CON RING
    (design/hud-targeting-v1.md) with Daniel's colours in a cartoony, solid, saturated style (clear flat colour ring, thin
    dark outline, ~60% alpha), not a gold glow.
33. **XP bar reference** — design/reference/ui/experience-bar.png (11:36): a long bronze-bound bar with Celtic-knot end caps;
    the filled part is warm gold/amber with tick marks in ten segments and finer sub-ticks, the empty part dark charcoal
    with bronze dividers; a small bronze plaque hangs under the middle reading "28 / 60". Build the HUD XP bar from this
    image (transparent PNG: use it as the frame + a masked gold fill that grows left to right; the plaque text = current /
    next). Replace the current plain bronze bar.
34. **Wolf still dies too fast to a level 1 with two attacks + auto-attack** (12:22): wolf HP raised 40% (160 → ~225) and
    it should hit back (item 26). Animal leg animations: "so hot garbage" — item 27 is a MUST tonight; the code cause is
    in TRUIWorldSubsystem (single-node loops at FIXED WalkRate/RunRate, two states, no blend): play rate must be
    speed / clip speed, with walk/trot/run thresholds and 0.25 s blends, or use the pack's own animation blueprints.
35. **CRITICAL — visible polygons on the terrain silhouettes** (12:30, two shots with red-marked ridgelines): "must be
    fixed early on or explained; a complete no-go for my MMORPG; I shouldn't see the polygons, it's 2026." CAUSE: (a)
    the landscape is 4 m per vertex (the 2 m generation was skipped on the laptop); (b) the laptop play profile forces
    aggressive landscape LOD (ViewDistance quality 1) so ridges a few hundred metres away render at 8-16 m per vertex and
    every crest becomes a straight segment; (c) erosion arêtes are knife-sharp, which a coarse mesh cannot round. FIX
    (tonight + PC): (1) Nanite landscape ON (UE 5.8 supports it: dense geometry at any distance, no LOD popping), (2)
    regenerate at 2 m/quad (the generator's 2 m pass: run it tonight in the background or on the 5090), (3) play
    profile: r.LandscapeLODDistributionScale 2.5 / r.LandscapeLOD0DistributionScale 3 (added to PlayMythicEarth.bat
    now), full LOD on the PC, (4) a ridge-crest smoothing pass in the generator (round arêtes over 8-12 m). Prove with the
    same two poses at 30 fps on the laptop and again on the PC.
