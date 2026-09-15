# Day editor pass — 15 Sep 2026, 13:07–14:05: the canopy test plot, and nine quick fixes

Editor only, play stack down for the whole shift and brought back at the end. Scripts in
`Tools/dalriata/n4c/` (`n4c_40` … `n4c_64`), per-step JSON beside each one, captures in
`design/progress/captures/2026-09-15-day/`.

---

## A. THE CANOPY TEST PLOT — the answer is YES, and the numbers are not the interesting part

**Look at `A0_canopy_pair_s.jpg` first.** Left: inside the test plot, looking straight up. Right:
the same view in Shanderry as it stands today. **2.0 % sky against 6.8 %.**

### What was built

A **200 × 200 m square centred at (−567.6, 659.5) m**, 175 m due south of the forest-road halfway
rest at (−568, 834). The rest's own glade is 58 m in radius and the plot's near edge is 75 m from
its centre, so **the glade stays open** — he walks out of the rest, 17 m south, and he is in it.
Corners are marked with four stumps (`PLOT_Stump_SW/SE/NE/NW`) at
(−666.1, 561.0), (−469.1, 561.0), (−469.1, 758.0), (−666.1, 758.0).

**The trees were cut for real, not masked.** Geometry Script is enabled and works from Python (the
libraries are `unreal.GeometryScript_*`, not `GeometryScriptLibrary_*Functions`). Two new meshes in
`/Game/ThreeRealms/World/Trees/`, the original `SM_TR_Fir_Canopy` untouched:

| mesh | what it is | tris (LOD0) | cut away |
|---|---|---|---|
| `SM_TR_Fir_HighCrown` | trunk kept, every branch below the line deleted | 21,601 | 2,707 source triangles |
| `SM_TR_Fir_CrownTier` | the same cut with the trunk gone too — a floating crown | 11,766 | 12,542 source triangles |

The cut plane is **local z = 12 m** (the mesh is 28.3 m tall in local space, z −2.0 … 26.2 m). The
kept trunk column was **measured, not guessed** (`n4c_43`): the trunk is 0.46 m half-width at z 1–2 m
and 0.6–0.8 m at 2–4 m, and branch wood starts at z ≈ 4–5 m — so the column tapers 1.10 m → 0.55 m
over 0 → 12 m and everything below z = 0 (the root flare) is kept whole. Branch stubs of half a
metre survive against the trunk, which is what a limbed-up conifer actually looks like.

**Density and tiers.** 1,160 stems at **290 stems/ha** (943 ordinary, **217 giants, 1 in 5**), minimum
3.4 m apart so a person can still walk. Each stem carries a **second crown** — a `CrownTier`
instance on the same trunk, lifted 1.5–6.0 m, its own yaw, ±1.6 m of lateral offset and 0.88–1.08×
the stem's scale — so the crown underside lands at **12–18 m** and the two tiers interleave instead
of stacking. Needle mask **off**: the cut meshes use a new `MI_TR_FirNeedle_NoMask` (same master,
`BranchMaskZ` pushed below the mesh), because the geometry is genuinely gone and no longer needs
clipping. Understory untouched. 2,320 new instances; everything outside the square is exactly as it
was.

Result: **tree heights 24.4–50.4 m (median 32.5)**, **branch line 10.3–21.4 m (median 13.8 m)** —
ordinary trees 10.3–15.8 m, giants 17.4–21.4 m. That is Daniel's "4–8× the height of a human" for
the ordinary trees, and higher for the giants, which is how real old growth reads.

### THE MEASURE — and why the first method was thrown away

The first attempt classified "sky" by colour. **It was wrong and the numbers were garbage** (it
reported 11–16 % everywhere, including frames with no visible sky at all): under a blue skylight the
needles themselves are blue-dominant and bright, so a colour rule counts the canopy as sky.

The method actually used is exact. From each pose two frames are captured from the identical camera:
the real one, and one with **every dressing actor temporarily hidden** so the frame is bare sky. A
pixel counts as sky when the two frames agree within 12/255 on all three channels — i.e. nothing
came between the eye and the sky there. Exposure is locked (`r.EyeAdaptationQuality 0`) or the
all-sky frame auto-darkens and the comparison collapses. `foliage.LODDistanceScale 1.0`.
**Validated**: the same measurement in the open halfway-rest glade returns **85.9 %**.

Every look-up point is chosen the same way — at least 3 m clear of the nearest stem, so the camera
stands where a person could stand, not inside a trunk — and every camera is at ground + 1.7 m,
pitch 89.

| where | stems/ha | sky straight up | mean |
|---|---|---|---|
| **THE TEST PLOT** (`plot1/2/3`) | 342–358 local | **1.8 / 2.0 / 1.9 %** | **1.9 %** |
| Shanderry at its NORM (`basen1/2/3`) | 263 | 3.4 / 7.5 / 6.8 % | **5.9 %** |
| Shanderry in its DENSEST pockets (`basem1/2/3`) | 485–517 | 2.4 / 1.6 / 1.6 % | **1.9 %** |
| the same pockets, 5 m clearance (`base1/2/3`) | 438–493 | 3.1 / 1.8 / 4.5 % | 3.1 % |

**Target was under 10 %. The plot is at 1.9 %.** Contact sheets: `A1_plot_lookups_s.jpg`,
`A2_shanderry_lookups_s.jpg`, `A3_shanderry_dense_lookups_s.jpg`.

### The honest reading of those numbers — this is the part that matters

**Shanderry already blocks the sky.** At the norm it is at 5.9 % and in its closed pockets it is at
1.9 %, the same as the plot. So "no sky overhead" was never really the problem, and the plot does
not win by blocking more sky — it *ties* the old forest's densest pockets **at 40 % fewer stems**.

What the plot actually changes is the **volume underneath**, and that is what Daniel was describing
when he said "ceiling". Compare `plot_interior_s.jpg` with `old_interior_s.jpg`:

- The built forest's needle mask is effectively **off** — the live `MI_TR_FirNeedle_Masked` has
  `BranchMaskZ = 0.03` (centimetres; night 4b dropped it from 13 m chasing the bare-crown fault).
  Branches therefore hang to the ground. Walking through Shanderry today you are pushing through
  needles at eye level; the sky is blocked by the bush you are standing inside, not by a roof.
- In the plot there is **10–21 m of clear air between the floor and the underside of the crown**,
  columns of trunk, a dark closed roof above, and the eye can see 40–60 m through the stand. That is
  a hall. It is the difference between a thicket and a cathedral, and it is the thing worth keeping.

**So the recommendation is: do not scrap what is there — re-cut it.** The plot is the whole of
Shanderry's recipe (same asset, same understory, same glades, same density band) with the branch
line raised by real geometry. Rolling it out is a re-run of the canopy step against the two new
meshes, which is one script, not a rebuild.

### What else the plot shows, said plainly

- **From the air the plot is invisible** (`aerial_plot_edge_s.jpg`, `aerial_plot_down_s.jpg`). The new
  roof joins the old roof seamlessly. The change is felt from underneath only.
- `plot_edge_inside_s.jpg` (standing at the north edge, a corner stump on the left) and
  `plot_interior2_s.jpg` are the two shots that sell it.
- `approach_from_rest_s.jpg` is the view south out of the halfway rest. **The brief asked for a view
  "from the road": there is no road there.** `halfway_rest` was planned "on the forest road" but the
  nearest road in `data/zones/dal-riata.json` (`bohermara`) passes **1,009 m away**. Worth deciding
  whether the glade moves to the road or the road bends to the glade.
- The two cut meshes have **one LOD each**. For a 200 × 200 m test that is fine and the captures are
  honest; before a Shanderry-wide roll-out they need an LOD chain or the draw cost will bite.
- Trunks are still the one pale grey (`per-instance trunk tint` is still open from night 4b).

---

## B. THE NINE QUICK FIXES — eight done, one done with a scar

| # | item | what happened |
|---|---|---|
| 1 | trees through boulders | **DONE.** 7,507 boulder footprints indexed, 258,471 tree instances checked, **78 removed** — 33 on the NE hill (5 pine HISMs), 40 in Shanderry's canopy, 5 edge birch. `fix_ne_hill_s.jpg` |
| 2 | buildings block the camera | **DONE.** 101 building parts on hall / HutA / HutB / HutC / barn / hall wattle / hut walls now BLOCK the Camera and Visibility channels; Pawn stays ignored on the huts (their own eave would seal them — the hidden rings carry the walls) |
| 3 | hut walls and roof two-sided | **DONE.** Five two-sided instances in `/Game/ThreeRealms/World/Lissban/`: `MI_TR_2S_f_house_01_mat`, `_thatched__transparent_mat`, `_house_roof_01_mat`, `_granarie_01_mat`, `_granarie_01_roof_mat`, assigned on all five buildings. `fix_hall_interior_s.jpg` — the far wall is solid |
| 4 | `DRV2_GroundPatches` | **DONE.** Actor deleted, **15,538 masked planes gone**. `fix_shore_no_patches_s.jpg` |
| 5 | the blue boulders | **DONE.** Every boulder was one ApexNature mesh, `SM_APXN_DOLR_Rock_Large_02`, whose pack material wants a runtime virtual texture we never set up. **2,309 boulder instances** moved onto four Roman & Celtic `landscape_rocks_*` meshes keeping each instance's world height; **13 bank instances (within 30 m of a river or stream): 6 removed, 7 capped to ≤ 1.2 m**. The grit-sized DOLR instances keep their mesh but take the Roman & Celtic rock material — **48,929 of them** (ground life 42,800, village detail 2,339, yard grit 2,152, lake shingle 1,638). Sky light set to neutral **236 grey**. `fix_ne_hill_s.jpg`, `fix_boulders_fall_s.jpg` |
| 6 | roads to the east gate | **DONE, and the mask trap bit — see below** |
| 7 | `DRV2_FogPool_*` | **DONE.** All six LocalFogVolumes deleted (owenfinn_valley, moyree_north, lake_hollow, shanderry_hollow, north_coast, athgorm_ford). Valley mist is the height fog alone now. `fix_athgorm_ford_s.jpg` — no brown column |
| 8 | the lake as one polygon | **DONE.** 3,596 8 m tiles → **one 461-triangle mesh**. `lake_before_s.jpg` / `lake_after_s.jpg` / `lake_after_air_s.jpg` |
| 9 | wildlife inside the palisade | **DONE.** 18 spawners pushed out to 300 m — 8 at Lissban (including `DRV2_Spawn_WildPig_N3_40_3` at **109 m**, almost certainly the pig he saw), 6 at Dromcairn, 2 at Dunadd, 1 each at Carrigrua and Tobarglas |

### 6 in full: the roads, and the mask that turned the island white

`data/zones/dal-riata.json`: `boherath` ended at the village centre (−3505.7, −1045.9) and
`boherath_coast` started there. `LB_Gate_East_01` stands at (−3482.69, −1020.05) facing yaw 67.5.
Both roads now end at the **gate's outside point (−3481.5, −1017.3)** with the last leg running
**square to the gate from (−3466.2, −980.3)** — 40 m. The west gate keeps its field track,
untouched. (Surgical 18-line edit; the file's formatting is unchanged.)

The mask was regenerated with `Tools/dalriata/n4/gen_ground_n4.py` (the current generator — n3's is
superseded; night 4b's waterfall mask was generated but its import was disabled and never landed, so
nothing was lost). Road dirt 0.197 % → **0.216 %** of the island.

**Then the re-import broke the landscape, exactly as the brief warned.** `mask_before…` is the record:
the whole island rendered white/grey. **Cause found and it is not what night 4b's note says.** The
live texture was `TC_VECTOR_DISPLACEMENTMAP`; n4b_10's note says the master wants `TC_MASKS`, so the
import set `TC_MASKS` — and that is what broke it. Putting the compression back to
**`TC_VECTOR_DISPLACEMENTMAP`**, re-pinning the texture on the master's two `TR_GroundMask` samplers
and on both material instances, and forcing a recompile brought it straight back with no editor
restart and no `git checkout` (`n4c_38`). `mask_island2_s.jpg` is the island green again with the new
road in it; `road_east_gate3_s.jpg` / `road_east_gate2_s.jpg` show the track reaching Lissban.

**Write this down for the next shift:** for `MTL_TR_DR_Landscape_MASTER`, `T_TR_GroundMask` must be
**TC_VECTOR_DISPLACEMENTMAP, sRGB off, no mips, clamp, never stream**, and after any import the
texture must be pushed back onto the master's samplers *and* both instances *and* the master
recompiled. `TC_MASKS` is wrong for this master.

### 8 in full: the lake

The first attempt chained the boundary of the surface **tiles** and fell apart — they do not sit on
an 8 m lattice, so rounding them into cells left a sparse checkerboard, 3,742 boundary edges and no
single loop. The terrain is the honest source: `gen_lake_ring_n4c.py` thresholds the night-4 height
field at the **58 m** surface, takes the component under the lake, fills holes, chains its boundary
into **one** loop (23.9 ha, 696 × 448 m), smooths it with three Chaikin passes and pushes it **2 m
outward** so the sheet runs under the bank. `n4c_62` triangulates that ring with Geometry Script into
`/Game/ThreeRealms/World/Water/SM_TR_Lake_Surface` — **461 triangles, one draw** — and stands it at
z 58 m with `MI_TRW_Lake`; the 3,596 tiles are cleared.

**The plunge pool was already a single plane**, not a tile field (`DRV2_Owenfinn_PlungePool`, one
`SM_SeaPlane` with `MI_TRW_River`), so there was nothing to de-tile. Its outline is still a square;
the water pass owns that.

---

## Level state

- 1,770 actors, **1,911,202 instances** (night 4b: 1,930,665 — the ground patches and the lake tiles
  came out, the plot's 2,320 went in).
- New actors: `DRV2_CanopyPlot`, `DRV2_Boulders_RC`, `DRV2_LakeSurfacePoly`, `PLOT_Stump_*`.
  Gone: `DRV2_GroundPatches`, the six `DRV2_FogPool_*`.
- Level saved, editor closed, **play stack back up** — PersistenceServer, ME-WorldServer and the
  client, Celtictest left where the DB has him, outside Lissban's west gate at full HP.
  `client_final_s.jpg` is that frame, shot from the live client at 14:11 with no input touched.

## Not done, and why

1. **The Shanderry-wide roll-out of the cut canopy.** Deliberate — this was a test plot and Daniel
   asked to see it before anything is scrapped. It needs his word, plus an LOD chain on the two cut
   meshes.
2. **The wander leash needs a settlement keep-out in C++.** Moving the spawners out to 300 m stops
   them *spawning* inside a village; nothing stops a wandering pig walking in. That is a C++ change
   to the mob wander, not tonight's work.
3. **The road surface is still faint** — the dirt layer is a weak paint. That belongs to the
   landscape-material slot, not here.
4. **Per-instance trunk tint** (night 4b's open item 2) — the fir trunks are still one pale grey, and
   it shows more now that the trunks are the whole lower half of the view.
5. **The halfway rest is 1 km from any road** (see above). A data decision, not a fix.
6. The archer towers, gates, grass quality, floating palisade rail — untouched, as before.
