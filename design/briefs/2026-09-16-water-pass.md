# Water pass — Dál Riata rivers, streams, waterfall and lake with the Water plugin

Queued first after the launcher frees the engine (backlog item 1). One editor session, 2–3 h, game down.
Daniel's words: "we're just gonna have to fix water and rivers streams waterfalls etc, needs to be more
realistic and beautiful"; "this river is jacked" (straight legs, right-angle corners, ribbon beside its own
trench); "never turquoise"; the confluence "makes sense physics-wise, I'm open to it if it's fixed";
the "weird stream thing" (a trench with no water) "needs to be" fixed.

## What exists (all of it goes)
- `DRV2_River` — 3,347 flat 4 m quads on a hand path of 3–11 points per reach (`Tools/dalriata/n4/n4_17_river.py`,
  re-seated by `n4b_04_river.py` and `n4c_08`). `DRV2_Owenfinn_Fall` (117-quad chain) + plunge pool + mist +
  three fill lights + 178 fall rocks. `DRV2_Lake` (now one 461-tri contour mesh from the day pass). Water
  volumes + LocalFogVolumes + post-process per body (`n4_07_water.py`, `n4_21_underwater.py`).
- The channel trenches cut on 15 Sep (`Tools/dalriata/n4b/gen_terrain_n4b.py`, 12,878 vertices, max 2.6 m) along
  the OLD straight paths — visible as torn dark scars beside the ribbons. They must be healed before the new
  beds are cut: regenerate the heightmap from `n4/dal_riata_n4_g16.png` with n4b's summit-terrace rule kept
  and its river-channel rule dropped, then let the water tool carve the new beds.
- The zone data paths in `data/zones/dal-riata.json` (water.rivers / water.streams) are the DESIGN law for the
  corridor (the v1 map scaled) — the Owenfinn must still pass Athgorm Ford (−3239, −174) and Dunadd's north-bank
  terrace (−2949, 565) and reach the mouth; the waterfall stays on the real rock step at (−1094, −1234)→(−1154, −1252).

## Inputs prepared offline (15 Sep)
- `Tools/dalriata/water/river_paths_v1.json` — descending centrelines traced off the live heightmap with a pull
  toward the design corridor (`trace_rivers_v1.py`, PULL=3.0): Owenfinn 5.96 km / 68.6 m drop, 4 m samples.
  Known issue: `shanderry_burn_w`'s designed source is LOWER than its mouth (drop −0.5 m) — re-source it on
  the Benlea foot above (700, −1500) so it descends; `kingshill_burn` and `shanderry_burn_n` end on the Owenfinn
  (confluences), `lake_feeder` ends in the lake, `lake_outflow` starts at the lake's 58 m level.
- Plugins already enabled in `MMOKitEval.uproject` (commit fdc0440): Water, Landmass, ProceduralMeshComponent,
  GeometryScripting. First editor launch after this will compile the Water plugin's shaders (several minutes).

## The build (in order; a step is not done without a capture or a log line)
1. Heal: new heightmap = n4 base + n4b's terrace rule only (no channel rule) → import via the proven route
   (`n4_01_height.py`: RG texture → RGBA16F RT → `landscape_import_heightmap_from_render_target` →
   `force_layers_full_update()` → delta re-seat of instances/actors → `Landscape.BuildNanite`). Probe Lissban's
   knoll (39.94) and NE hill (99.05) unchanged. Sightline + landform audits offline BEFORE the import.
2. Rivers as `WaterBodyRiver` actors: one per reach, spline points from `river_paths_v1.json` thinned to ~25 m
   spacing with the 4 m samples as the guide (the Water plugin interpolates); width 7→16 m on the Owenfinn,
   1.8→3.4 m on the burns; depth 1.2–2.0 m / 0.4–0.8 m; velocity set per reach; the plugin's landscape
   brush (Landmass) carves the bed and banks — if the brush cannot run on this laptop, carve the bed with our
   heightmap rule along the NEW centrelines (bed 1.4–2.0 m, 3 m banks, noise-broken) and place the river bodies
   with terrain carving disabled. Material: the plugin's river material with the dark Atlantic grey-green
   (blue below green — `n4b_42_watercolour.py` values), foam at drops, NO turquoise, no shallow-cyan.
3. The confluences: the burns' spline ends on the Owenfinn's spline (the plugin merges river bodies that
   touch); a gravel bar of cobbles on the inside of each join; the Owenfinn widens by ~20 % below each.
4. Athgorm Ford: a 15 m stretch at 0.3 m depth with a cobble bed where Boherath crosses; no bridge.
5. The waterfall: the Owenfinn's spline runs over the real step; the plugin does not do falls — build the
   sheet as a `SplineMeshComponent` ribbon down the measured profile (n4b_fall.json) with the whitewater
   material, a Niagara or cascade-style foam sheet if one exists in the packs (check
   Content/Medieval_Megapack + ApexNature for water/mist VFX), the plunge pool as a `WaterBodyLake` ring,
   mist volume kept, the 178 rocks kept.
6. The lake as a `WaterBodyLake` from the 58 m contour (the day-pass polygon is the outline), reeds and
   shingle margin re-seated on the new shoreline, the underwater grade re-attached to the new body.
7. The sea stays the current plane THIS pass (an ocean body is a separate decision — it re-does the coast).
8. Clear foliage/ground life inside every new channel + 1.5 m; re-dress banks in two bands (waterline
   cobbles/reeds, bank-top boulders ≤ 1.2 m — Roman & Celtic rocks, never the untextured Dolomites).
9. Water volumes + post-process re-fitted to the new bodies; swim test in the client.

## Proof set (captures from `Tools/dalriata/n4/poses.json` river_close, river_bend, river_bank_eye, waterfall,
fall_pool, lake_shore, lake_under_bed + NEW: confluence at eye level, Athgorm Ford, the healed trench site,
an aerial of the whole Owenfinn) and in the CLIENT: the river from the bank, swim, the fall from the pool.
Numbers: total uphill along each spline (must be 0 after carving), depth/freeboard medians per reach,
instances removed from channels, fps at the west gate before/after.

## Rules
Machine clock; one heavy process; never invent names; explicit `git add`; never commit vendor packs; the mask
re-import trap: `T_TR_GroundMask` is TC_VECTOR_DISPLACEMENTMAP (day pass); never touch Lissban's knoll / NE hill;
Daniel reviews from captures first, then walks.
