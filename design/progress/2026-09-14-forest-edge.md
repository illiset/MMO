# The Shanderry forest edge — 14 Sep 2026, afternoon pass

Daniel, 13:15, on a god-cam shot of the north-east corner of Shanderry: the forest stops on a
straight line of pines along the top of a dark escarpment, and the floor colour switches on the
same line. Approved at 13:20: "go for it, fix it up, then let's get back on track."

Level `/Game/ThreeRealms/Maps/GN_DalRiata_v2`. Scripts, data and full-size captures:
`Tools/dalriata/fe/` in the game repo. Small captures: `design/progress/captures/2026-09-14-forest-edge/`.
Editor session 18:07–18:52; one heavy process at a time, editor closed with QUIT_EDITOR before
the play stack went up.

---

## 0. What the escarpment actually was — and it was not the road bench

Before changing anything I measured the night-3 terrain against the pre-night-3 (v2) heightmap
along every road corridor (`fe/measure.py`, `fe/measure_before.json`):

| corridor | inside Shanderry | outside Shanderry | worst 60 m cross-section relief, outside |
|---|---|---|---|
| bohermara | −34.6 m, mean \|edit\| 29.7 m | **−35.6 / +17.6 m, mean \|edit\| 12.6 m** | 106.6 m |
| boherath_coast | — | **−29.7 / +7.9 m, mean 13.3 m** | 31.5 m |
| dunadd_spur | — | −20.2 / +9.9 m | 19.4 m |
| boherath | — | −10.4 / +4.0 m | 10.6 m |
| whitemill_lane | — | −2.5 / +9.9 m | 6.1 m |
| Owenfinn (river) | −3.6 m | −3.6 m | — |

Then I probed one point of the trench directly, at (−1317, 1384) on the forest road: the ground
is 97.0 m on the v2 terrain and 63.7 m after night 3 — 33.3 m of cut. **The road bench only
accounts for 2.0 m of that.** The other 31 m came from night 3's *shore terrace* step, which was
written for the coast road and also ran along **bohermara** — a road that crosses the entire
island. Anything it passed between 40 and 130 m of elevation was dropped by up to 32 m.

That is the 20–40 m canyon with rectangular cut blocks in the morning's aerials (item 10), the
straight brown coastal scar (item 10 again), and the escarpment the forest stops on in Daniel's
13:15 shot. One bug, three complaints.

It is also, *inside* Shanderry, the carved earth Daniel kept at (11:20): "for the forest road I
actually like the carved-out earth for it, just not for Lissban to Portcorr … or anywhere else."

## 1. No cut at the edge

`Tools/dalriata/fe/gen_terrain_fe.py` regenerates the whole night-3 terrain pass with two rules
changed. Everything else — the lake basin, the Owenfinn bed and fall, the Tobarglas shelf,
Benlea's broken rock — is regenerated bit-identically; `fe/verify_repro.py` reproduces
`dal_riata_n3_g16.png` from the v2 source with **max diff 0**, which is what makes a surgical
re-run safe.

1. **Roads.** A signed-distance field to the Shanderry polygon gives `HOLLOW`, 1 at 150 m inside
   the forest falling to 0 at the rim. Inside, the road keeps night 3's deep 224 m-smoothed
   bench. Outside, the road is put back on the pre-cut ground and re-benched to a **local 64 m
   profile with cut/fill clamped to 2.5 m and shoulders blended over 25–43 m** of noise-varied
   width. The hollow-way therefore climbs out of the forest over 150 m instead of ending on a
   wall.
2. **The terrace.** Weighted by the same `HOLLOW`, so it survives only deep inside Shanderry
   (13,581 vertices, against 47,319 island-wide on night 3) and `boherath_coast`, which lies
   entirely outside the polygon, loses it completely.

Measured on the result (`fe/measure_after.py`, `fe/measure_after.json`):

| corridor | before (in / out) | after (in / out) |
|---|---|---|
| bohermara | −34.6 / **−35.6 … +17.6** | −34.6 (kept) / **−4.1 … +8.0**, road edit itself clamped at 2.50 m |
| boherath_coast | — / −29.7 … +7.9 | — / **−2.5 … +2.3** |
| dunadd_spur | — / −20.2 … +9.9 | — / **−2.2 … +4.0** |
| boherath | — / −10.4 … +4.0 | — / **−3.0 … +1.3** |
| whitemill_lane | — / −2.5 … +9.9 | — / **−2.7 … +4.0** |

(The residual on bohermara outside the forest is not the road: it is the Benlea roughening and
the lake basin overlapping the corridor's bounding box. The road's own edit is clamped at 2.50 m
on every road, printed per road in `fe/gen_terrain_fe.json`.)

**The river was left alone, deliberately.** Measured, the Owenfinn corridor's deepest edit
outside the forest is 3.6 m over a 40 m graded bank — a river bed, not a trench, and the water
surfaces are seated to it. Raising the bed by the 1.1 m that a 2.5 m rule would demand risks
pushing the bed through the water planes. Flagged rather than done.

**In the editor** (`fe/fe_01_height.py`): heightmap imported through the RG texture → RGBA16F
render target route, `force_layers_full_update()` flushed, and the ground re-probed:

| point | before | after | source image |
|---|---|---|---|
| (209.7, 1994.8) road at the NE forest boundary | 61.9 | **90.35** | 90.3 |
| (−1880.5, 902.1) road at the west boundary | 39.8 | **55.96** | 56.0 |
| (−1317.4, 1384.0) forest road, hollow-way | 63.7 | **63.80** | 63.8 — unchanged |
| (−3547, −227) coast road | 17.8 | **47.46** | 47.5 |

`delta_fe.f32` (new − live, per landscape vertex, −15.1 … +34.2 m over 76,900 vertices) then
shifted **77,307 foliage instances and 944 actors**. 15 actors moved more than 5 m: four deer
spawners above the old coast cut (+23 m) and eleven Dunadd props (±6–7 m) where the spur road's
bench was removed. Water bodies and the gate actor are excluded from the shift, per night 3's
rule that nothing whose height is defined by a PLAN may be moved by a grounding pass.

**Sightline audit re-run offline against the new heightmap** (`fe/audit_sightlines_fe.py`,
`fe/fe_sightline_audit.json`) — every required pair still blocked:

| pair | dist m | clearance m | pair | dist m | clearance m |
|---|---|---|---|---|---|
| carrigrua ↔ dunadd | 892 | +6.3 | lissban ↔ dromcairn | 2900 | +39.4 |
| carrigrua ↔ dromcairn | 2647 | +5.6 | lissban ↔ portcorr | 3635 | +40.5 |
| carrigrua ↔ portcorr | 3271 | +16.2 | rinnbeg ↔ tobarglas | 2846 | +304.2 |
| carrigrua ↔ lissban | 1695 | +25.6 | rinnbeg ↔ dunadd | 7629 | +361.7 |
| dunadd ↔ lissban | 1700 | +21.3 | rinnbeg ↔ carrigrua | 6855 | +215.4 |
| dunadd ↔ dromcairn | 1761 | +16.3 | rinnbeg ↔ lissban | 8168 | +210.3 |
| dunadd ↔ portcorr | 2410 | +19.9 | rinnbeg ↔ dromcairn | 9109 | +415.8 |
| tobarglas ↔ dunadd | 5969 | +6.9 | tobarglas ↔ lissban | 7024 | +59.3 |
| tobarglas ↔ carrigrua | 5410 | +3.1 | tobarglas ↔ dromcairn | 7105 | +5.2 |

`PASS — every required pair is blocked.` Dromcairn ↔ Portcorr, the one allowed pair, +22.9 m.

## 2. A wandering line

`Tools/dalriata/fe/gen_edge.py`. The polygon is treated as the CORE, and the effective boundary
is that polygon plus a domain-warped noise offset, **±120 m, rms 54 m**.

The first attempt used 2 km noise cells and failed in an instructive way: sampled at the tree
positions the offset ran −26 … +60 m and only **24** stems were affected — the line had *moved*,
not *wandered*. The scale is what matters. The field now has its lobes at ~790 m and its bays at
~355 m, so the boundary swings in and out several times along every stretch of rim, and **735**
core stems fall inside the new bays (glades biting into the forest).

Tongues of forest run out along the water: `shanderry_burn_n`, `shanderry_burn_w`,
`kingshill_burn`, `lake_feeder`, `lake_outflow` and the upper Owenfinn each push the boundary out
by up to 150 m within 90 m of the stream, and each stream path is extended 220 m beyond its last
node so the tongue actually leaves the forest.

## 3–5. The mantle, the thinning, and the floor

Placed as `DRV2_Forest_Edge`, one actor, 14 HISM components, **91,610 instances**:

| band | what | count |
|---|---|---|
| 0–25 m outside the effective edge | edge stems in the mantle | 2,826 |
| 25–140 m | thinning outward | 8,935 |
| 140–260 m | outliers, copses, hedgerow trees | 1,317 |
| 0–22 m (ragged, noise-modulated) | mantle shrubs 1.5–3.0 m: bilberry, germanic bush, two bush variants | **46,354** |
| under the outer trees, clumped at the trunks | bilberry / bush / grass tuft / eagle fern, mixing from litter to grass outward | **32,482** |
| at the edge | snags and fallen logs | 250 |

Trees: **12,524** in 8 variants — fir canopy 3,565, fir sub 2,363, silver birch 2,137 + 1,583,
four Roman/Celtic pine variants 2,876 — heights **2.9–26.9 m**, derived per instance from each
mesh's own bounding box so a "12 m birch" is 12 m, with yaw and scale randomised (no clones).
Density falls 0.55 → 0.15 of core across 140 m and to zero over the next 55 m; a clump field
gives copses and gaps; crown spacing is enforced by a 4.2 m grid thin. Nothing stands on a slope
over 35°, in a road corridor (dirt mask), or within 120–150 m of a settlement or landmark.
46 copses of 5–12 trees and 22 hedgerow trees along the roads outside the forest.

**The floor mask is now derived from the actual tree instances.** Crown area from each of the
432,458 final stems (radius 0.22 × height, clamped 1.5–7.5 m) is accumulated on the mask grid,
feathered at 32 m and 56 m, broken by noise at two scales, and **zeroed wherever canopy coverage
is below 0.06** — no brown where nothing stands. Duff coverage drops from **12.54 % to 10.30 %**
of the island, and what remains follows the canopy rather than the polygon (item 23b, item 39b).

The floor *material* is not fixed: `MI_TR_DR_Island` and `MI_DalRiata_V2_Landscape` expose only
the MWAM `MW_*` scalars, no per-layer TR tiling parameter, so the second detail scale asked for
in item 39a needs a master-material edit. The mask's own two-scale noise is all that breaks the
tiling today. **Owed, and named.**

## 6. Crossings

The road copses come out of the same pass: the clump field plus the 46 placed copses put groups
of trees at the two bohermara boundary crossings, and the hedgerow trees run single trees along
the road out into the meadow. The road still meets the boundary on its authored heading — turning
the road to enter at an angle is a change to `data/zones/dal-riata.json` and was not made.

## Evidence

`design/progress/captures/2026-09-14-forest-edge/`, BEFORE and AFTER at identical camera poses
(`fe/poses.json`; camera Z is absolute, so the pairs are directly comparable):

| pose | what it shows |
|---|---|
| `a_road_exit_cromcross` | **Daniel's shot.** Before: the dark escarpment running diagonally, the pines stopping dead along its top, the floor colour switching on the same line. After: no escarpment, the road a track on the ground, outlier trees scattered into the meadow, no colour line. |
| `a2_road_low` | the same crossing from the road itself |
| `b_west_edge` | the west boundary where the road leaves for Dunadd |
| `c_south_carrigrua` | the south-west edge facing Carrigrua |
| `d_walkin_eye` | eye level, 1.75 m, walking in from the meadow into the mantle |
| `f_hollow_way` | inside Shanderry — the carved forest road and the closed canopy, untouched |
| `i_edge_oblique_ne` | oblique over the north-east edge |
| `preview_edge.png` | offline plan view: core (dark), mantle (olive), edge stems (light) — the wandering boundary, the bays and the tongues |

**A limitation to know about when reading the aerials:** the canopy HISMs cull at 340 m
(`HISM_Fir_0`), 780 m and 220 m, so any god-cam shot from more than ~400 m up renders the forest
as bare ground. `e_aerial`, `g/h/j` are therefore not useful for judging the edge and are kept
only for honesty. Judge the edge from the ground-level pairs and `preview_edge.png`.

## Counts

| | before | after |
|---|---|---|
| core canopy (`DRV2_Forest_Canopy`) | 419,434 | **418,699** (735 taken by the bays, all re-seated on the new ground) |
| forest edge (`DRV2_Forest_Edge`) | — | **91,610** |
| forest floor + undergrowth | 256,776 | 256,776 (delta-shifted) |
| other vegetation | 117,365 | 117,365 (delta-shifted) |
| **total foliage instances** | 793,575 | **884,453** |

## Owed

1. **The floor material** (item 39a): a proper blend — needle litter + moss + dark soil + roots,
   two detail scales and a macro breakup. Needs the master material, not a parameter.
2. **The Owenfinn bed** outside the forest is still 3.6 m at its deepest; correct to 2.5 m only
   together with a re-seat of the river water surfaces.
3. **The coast** (items 10, 31): the terrace cut is gone from the road corridor, but the coastline
   itself, the cliff bands and the pocket strands are still the straight-line versions.
4. **Road headings at the crossings**: entering the forest at an angle is a zone-data change.
