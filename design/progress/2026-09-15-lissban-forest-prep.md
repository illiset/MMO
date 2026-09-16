# Lissban Forest — the offline preparation shift, 2026-09-15 18:30–19:50

**Nothing was opened, launched or built.** The Epic launcher was installing into the engine folder, so
the editor was never started, the play stack was never touched, no `UnrealEditor*.exe` ran and no C++
was compiled. This was pure Python and numpy on disk, against the live heightmap as a file.

**Everything below is measured on the array.** Nothing here has been seen in the editor or in game,
and that is the single biggest caveat on the whole shift — read "NOT DONE, and what is unresolved"
before trusting any of it as finished.

Deliverables: `Tools/dalriata/lf/` in the game repo. The plan is
`data/zones/lissban-forest-concept.json` v3 and `design/progress/2026-09-15-lissban-forest-plan.png`.
Frame: metres, x = north, y = east.

| capture | what it shows |
|---|---|
| `captures/2026-09-15-lissban-forest-prep/A_terrain_before_slope_delta_s.jpg` | three panels, north up: the LIVE ground \| the new slope bands (green ≤ 15°, amber 15–40°, **red > 40° = impassable**) \| the delta (red raise, blue cut). Red outline = the forest polygon, orange = the crest line, white rings = the five clearings, cyan = Lissban and its fields. |
| `captures/…/B_forest_density_s.jpg` | the stem density field with the stems on it (yellow = the giants), the clearings punched out, the black band through the middle = the ridge's own > 35° face, where nothing is planted |
| `captures/…/C_trail_and_stones_s.jpg` | the trail at 1 m per pixel over the painted mask, blue = stepping stones, yellow = the field fences it goes round |

---

## The headline numbers

| | |
|---|---|
| base heightmap | `n4b/dal_riata_n4b_g16.png` — night 4b's, still the live landscape |
| delta vs live | **−3.66 … +79.12 m over 66,114 vertices (0.914 % of the grid, 106 ha)**, mean \|edit\| **17.26 m** |
| crest, above the meadow floor it rises from | **60 … 87 m, median 73 m** — 98 % inside the brief's 60–110 m |
| the impassable band, meadow side | **88 % of it over 40°, median 48.2°**; unbroken run **25–49 m, median 35 m**; **98 % of stations reach the 25 m rule** |
| the runnable skirt | **90.4 % at or under 15°, median 12.2°, p95 16.5°**, over 74–146 m |
| stems | **18,127** (15,167 inside the polygon) — **136 /ha** over 111.4 ha of plantable core |
| ground life | **135,683** instances — 892 /ha, **one clump every 3.4 m** |
| clearings | 5, **four of them ≤ 6.3° at every vertex**; 885 dressing props |
| trail | **2,043 m**, median grade 1.7°, **0 m of carriageway** |
| sightline audit | **PASS — every required pair blocked** |
| landform audit | **PASS — 18/18** |
| Lissban knoll / NE hill / the fields / the cart track | **0.00 m moved, all four** |

---

## 1. THE TERRAIN — `gen_terrain_lf.py`

A surgical rule on top of the live heightmap, in four parts, with everything Daniel has approved
masked out of all of them.

### The containing ridge

The concept's ridge line, Catmull-Rom'd at 8 m and then made to stop being a drawn curve: the
centreline wanders **−34 … +20 m** laterally from two noise octaves at 300 m and 80 m, and every
parameter of the cross-section is noise-varied **along** the line at the brief's 80 / 300 / 900 m.

| | designed | **measured on the finished ground, 58 stations** |
|---|---|---|
| skirt | 74–146 m at 5.0–11.4° | **90.4 % ≤ 15°, median 12.2°, p95 16.5°** (6,285 vertices) |
| impassable band | 35–55 m at 46.0–55.8° | **88 % over 40°, median 48.2°, p10 38.4°** (3,067 vertices) |
| unbroken > 40° run, meadow side | ≥ 25 m | **24.6 … 48.8 m, median 35.0; 98.3 % of stations** |
| crest above the inner toe | 60–110 m | **59.6 … 87.2 m, median 73.0; 98.3 % inside the rule** |
| crest, absolute | — | **120.3 … 156.9 m, median 143.1** |
| outer flank | 21–31° | — |

The measurement excludes the **150 m taper at each end of the arc**. The crescent's two ends are its
mouth — the way in from the meadow and the village — so the wall eases to nothing there rather than
stopping dead, and counting those stations against the crest rule would be counting a doorway as a
hole in the wall. 58 of 66 stations are measured; the other 8 are the two tapers.

The band statistic also excludes vertices standing on a **spur** (a spur is a designed 20–28°
landform, not a failed skirt), inside a **clearing**, or inside a **mask**. Those exclusions are
23,959 / 12,665 / 40,173 vertices and they are in the JSON.

**Spurs:** five, crests **27.5–36.0 m** above the floor, flanks **20.3–27.2°**, symmetric and
tapering to nothing at the tip.

**Road gaps: zero, because no road crosses this ridge.** The rule is implemented (the crest tapers
to nothing within 35 m of a road centreline, easing out by 95 m) and it fires on nothing: the nearest
road, the Boherath, ends at Lissban's west gate 340 m away.

### The two cave sites, as clefts

| | cave A (−3250, −1900) | cave B (−4400, −1800) |
|---|---|---|
| mouth → back | (−3262.5, −1895.0) → (−3234.7, −1906.1) | (−4389.3, −1795.2) → (−4413.0, −1805.9) |
| length | **30.0 m** | **26.0 m** |
| floor below the ground it cut into | **0.1 … 7.45 m** | **0.8 … 7.76 m** |
| mouths | **1** | **1** |
| wall slope, on the wall band | p90 **48.8°**, max **52.4°**, **4 %** over 50° | p90 **61.4°**, max **63.6°**, **48 %** over 50° |
| trail | yes, to Lissban's west gate | none, by the concept |

**Cave A misses the ≥ 50° wall rule and this is a grid limit, not a rule I weakened.** At 4 m per
landscape vertex the steepest wall expressible for a 7.4 m drop is 62°, and only if the whole drop
falls between two adjacent vertices; a 9.2 m-wide slot has two vertices across its floor, so the lip
rounding eats most of the angle. Cave B clears it because it cuts into the ridge's own 46° face,
where the terrain is already doing the work. Both clefts are **sites**, not caves — the mouth itself
is a mesh from the Cave Environment Modular kit (still downloading), set into the recess the terrain
provides. That is where the 50°+ rock face will actually come from.

### The five clearings — and the one design call this shift made

Three of the five clearings sat **within 10–26 m of the concept's ridge or spur lines**: C1 at 26 m,
C4 at 22 m, C5 at **9.5 m**. A 50° crest through a levels 2–5 grind camp is unplayable, and a gap in
the wall at each of them is not containment. So:

* the **crest was diverted outward** around each clearing, smoothed along the line, until its
  centreline stands **143–376 m** from every clearing centre (the required clearance is 145 m; C1 at
  143.4 and C5 at 144.0 are within half a metre of it). **Max offset from the concept's line 157 m,
  mean 45 m** over a 2.6 km arc;
* two spurs were **trimmed back** at the tip (168 m and 200 m; a third by 328 m) so no finger reaches
  a clearing;
* inside each clearing the ridge profile is eased to zero — the profile reads **0.000 at all five
  clearing centres**, so the floor is the natural ground and the wall rises from its edge.

That is a deliberate departure from the drawn line and it is the only one. It is recorded here rather
than asked about because the shift was told to decide.

| | natural | **finished** | |
|---|---|---|---|
| C1 (−3150, −1500) | 3.81° tilt | **mean 4.01°, max 6.29°, 1.3 % over 6°** | z 49.99 |
| C2 (−3600, −1900) | 2.64° | **mean 2.78°, max 4.50°, 0 %** | z 59.91 |
| C3 (−4050, −1750) | 2.92° | **mean 2.96°, max 4.83°, 0 %** | z 63.78 |
| C4 (−4350, −1450) | 3.49° | **mean 3.53°, max 5.07°, 0 %** | z 71.42 |
| C5 (−3350, −2050) | **7.18°** | **mean 5.81°, max 8.18°, 48 % over 6°** | z 78.74 |

The floor of each is a least-squares plane through the live ground with its tilt capped, plus a
damped share of the ground's own short-wavelength texture put back — **not** a level bench. A bench
is the stamped flat pad Daniel rejected twice (walk items 24 and 40), and a clearing on a hillside
should be a gentle slope, not a terrace. **C5 fails the ≤ 6° rule at its rim** and that is written up
in the unresolved list rather than papered over.

### The masks — all four hold at 0.00 m

| | |
|---|---|
| Lissban knoll (r 60 m) | **0.0000 m**, 39.96 → 39.96 m |
| NE hill (r 120 m) | **0.0000 m**, 99.18 → 99.18 m |
| the LB fields, **inside the fence lines** (513 vertices) | **0.0000 m** |
| the cart track out of the west gate (233 vertices) | **0.0000 m** |
| nearest edit of any kind to the field centre | **162 m** |

Masked: the knoll (150→260 m), the NE hill (330→470 m) — night 4b's own numbers, unchanged — every
settlement footprint, the four field enclosures + 40 m, the cart track + 10→34 m, all 5 roads +
12→37 m (the benches stay), and all 12 river/stream reaches + 20→48 m, including the centrelines the
18:35 offline commit traced off the DEM. **56,276 vertices protected.**

### Slope bands over the whole region of interest

| | mean | > 15° | > 35° | > 40° |
|---|---|---|---|---|
| before | 8.30° | 17.39 % | 2.64 % | 1.51 % |
| **after** | **10.40°** | **25.16 %** | **4.33 %** | **3.04 %** |

### Audits — both PASS, offline, against the new heightmap

```
SIGHTLINE AUDIT: PASS - every required pair is blocked
  tightest  tobarglas <-> carrigrua   5410 m   +2.3 m
LANDFORM AUDIT: PASS - 18/18 eye->Kingshill-crown lines blocked
  tightest  from r28 b270, terrain stands 28.6 m above the line
```

Both are unchanged from night 4b's values, which is the right answer: the edit is 4 km from every
audited pair and adds terrain rather than removing it, so it could only ever have helped. They were
run **before** any import, so a failure would have cost nothing.

---

## 2. THE FOREST — `gen_forest_lf.py`

Daniel's reference look is his **own NE hill**, from the air: *"this is beautiful."* So this is not a
new recipe. It is `lb/lb_22_dress.py`'s recipe — the same five conifers, the same
`want = 9–22 m` height rule, the same blueberry/germanic/bush understory over the same
grass-patch-and-fern floor at the hill's "something in every 3 × 3 m" — taken off that 180 m hill and
spread across 132 ha, with the brief's numbers laid over the top.

| | |
|---|---|
| polygon | **132.1 ha**; plantable core after the clearings, the trail, the cave mouths and the 35° cut: **111.4 ha** |
| stems | **18,127**, of which **15,167 inside the polygon** and 2,960 as the outward edge gradient |
| density | **136 /ha** in the core; the field itself runs **126–189 /ha** (brief: 130–190) |
| heights | **7.0 … 32.0 m, median 17.0** |
| giants | **3,659 = 20.2 %**, at 24–32 m |
| sub-canopy | 19.7 %, at 7–11 m |
| meshes | **8**, every one verified to exist on disk before use |
| no clones | 8 meshes × a continuous height × non-uniform xy jitter 0.86–1.16 × random yaw × per-instance tint |
| ground life | **135,683** — 38,028 shrubs, 28,901 ferns, 65,408 grass, 3,346 logs and stumps |
| | **892 /ha = one clump every 3.4 m** |
| boulders | **2,780 placed, 1,174 rejected for standing on a trunk** (the n4c_30 rule), 18 /ha, scale 0.35–2.30, sunk 0.5 × scale as the hill does |
| clearing dressing | **885 props** across 5 clearings — 3 grind (fire ring, three log seats, camp stones, flowers, rocks, a log) and 2 open |

**The mesh list, all verified on disk:** `pine_tree_highland_v1_final`, `pine_tree_highland_v2_final`,
`pine_tree_v3_final`, `pine_tree_v4_final`, `SM_TR_Fir_Canopy`, `birch_tree_final`, plus
`pine_tree_small_v1_final` and `birch_tree_small_final` for the sub-canopy. Understory:
`blueberry_shrub_final`, `germanic_bush_final`, `SM_Bush_01/02`; ferns `SM_EagleFern_01/02/03` and
`fern_exp5_SM`; floor `grass_patch_1/3/5/7/9_SM` and `SM_WildGrass_S_01/02`; deadwood
`trunk_log_exp7_SM`, `pine_tree_stump_exp2_SM`, `SM_Wood_Debris_01/02/03`; boulders the seven Roman &
Celtic `landscape_rocks_*` the day pass swapped the blue ApexNature rock for. **Zero missing.**

**The canopy .f32 stores a wanted HEIGHT in metres, not a scale**, because six meshes of six
different sizes given the same scale give six wrong heights — `lb_22_dress.py` divides by the mesh's
own bounds and so does `lf_02_forest.py`.

### The checks, all of which come out at zero

| check | |
|---|---|
| stems on slopes over 35° | **0** |
| stems inside the 2.1 m trail corridor | **0** |
| stems inside a clearing | **0** |
| stems within 18 m of a cave mouth | **0** |
| **stems in the meadow** | **0** |
| ground-life instances inside the path | **0** |
| ground life in the 1.5 m margin, as a share of normal | **25.6 %** (rule: thinned to 30 %) |

The meadow between the crescent's inner edge and the village is left open, by the brief. Daniel's
forest-edge rule (walk item 15 — "the polygon is a CORE, not a boundary") is applied **outward only**:
a 110 m noise-warped gradient with outliers off the crescent's outer arc, and nothing at all on the
inner arc, because that side is the meadow.

---

## 3. THE TRAIL — `gen_trail_lf.py`

*"A TRAIL (1.2 m worn footpath, trodden grass, stepping stones at wet spots) … Never a road."*

| | |
|---|---|
| total | **2,043 m** — trunk gate→fork 889.3 m, branch to cave A 675.6 m, south arm 478.5 m |
| grade | median **1.7°**, p95 **6.6°**, max 37.8° |
| carriageway | **0 m.** No verge wear. **No heightmap edit at all.** |
| mask paint | R channel, **852 pixels**, max weight **0.39**, mean **0.26**, 0.6 m feather, 64 subsamples per pixel |
| stepping stones | **26 cobbles at 4 wet crossings** |
| the fields | **7.98 m of clear ground** from the nearest fence line, minimum, anywhere |
| the south arm | ends **150.2 m** from cave B |

**The south arm's open question is answered.** The concept asked whether it stops short of cave B or
reaches it; the approved brief says it stops 150 m short, so it does — its own drawn end was already
146.7 m out and it is trimmed to exactly 150.2 m.

**"Round the north side of the fields" is done by construction, not by nudging.** The first attempt
repelled the drawn line out of the enclosures iteratively; it fought its own smoothing, grew the
trunk from 914 m to 1,350 m and still left 5.8 m of trail inside a fence. The trunk now follows the
field cluster's **convex hull offset 12 m**, on whichever arc has the greater x — the north side. The
cluster spans x −3600 … −3469; the arc's mean x is **−3473.5**.

The 37.8° sample is the last four metres of the branch into cave A's cleft, at (−3256, −1902). Only
**0.5 %** of the trail is over 20°. A footpath may drop into a ravine; a road may not.

### The resolution problem, stated rather than hidden

`T_TR_GroundMask` is 4096 × 2048 over a 14.2 km island — **4.0 m per pixel**. A 1.2 m path is 0.30 of
one pixel and the 0.6 m feather is 0.15 of one. Painting the pixel at the brief's weight would give a
**4 m band**, which is a road. So the line is rasterised at 8 × 8 subsamples per pixel and weighted by
coverage, lifted to the brief's 0.35 floor only where the path genuinely runs through a pixel. Max
weight written **0.39**, mean **0.26**.

The honest consequence: **the mask alone cannot render this trail.** Its real width on screen has to
come from the instance layer — the cleared corridor, the thinned margin, the stones and the grit that
`lf_03_trail.py` lays. The permanent fix is a ≥ 1 m mask near the settlements, which is night 4's walk
item 39 and is still open.

---

## 4. THE PLAN — `lf_plan.json`

Everything the editor session needs: the run order, every file path with its size, all the terrain and
forest and trail numbers, both audit verdicts, each clearing's dressing with **every mesh path checked
against `Content/` on disk** (`clearing_dressing_all_meshes_exist: true`), and the spawner positions.

**Wildlife, levels 2–5: 93 spawners** from `Content/Data/mobs/dal-riata-wildlife.json` —
Doe 20, Red Fox 5, Wild Pig 32, Red Stag 25 **inside** the clearings, and Grey Wolf 11 **on the rim
only**, so a level 2 can use the floor. Counts come from each def's own `group` block.

**The caves are PLACEHOLDER POSITIONS. Nothing is placed and no definition exists yet.**

* **cave B, the wolf den, 8 positions:** three yearlings at 4, three greys at 5 (the real Grey Wolf
  def), a den mother at 6 and the alpha at 7 at the back of the cleft. Level 6 for the den mother is
  my reading — the brief gives "yearlings 4, greys 5, den mother, alpha 7" and does not level her.
  **The alpha is left unnamed on purpose**: naming the wolf den's alpha is on Daniel's own open list
  and nothing here invents one.
* **cave A, the Shanderry bandit family re-banded 4–7, 5 positions:** lookout at 4 standing **on the
  trail 41 m out from the mouth**, three poachers at 5–6, the leader at 7 at the back. They keep the
  names they already have in `dal-riata-bandits.json`; only the levels are overridden.

`lf_04_dress.py` ships with `PLACE_CAVES = False` for exactly this reason.

---

## 5. THE EDITOR SCRIPTS — written, not run

`lf_01_import.py` → `lf_02_forest.py` → `lf_03_trail.py` → `lf_04_dress.py`, modelled on
`n4_01_height.py` / `n4_02_forest.py` / `n4_05_ground.py` and night 4b's mask handling. Every one
compiles clean. Three traps are written into their headers because they have each cost a night before:

* **`T_TR_GroundMask` must be `TC_VECTOR_DISPLACEMENTMAP`, not `TC_MASKS`** — night 4b's note is
  wrong, `TC_MASKS` turned the island white. Import with `save=False`, set the compression, save the
  texture, re-pin it on the master's samplers **and** both material instances, then recompile the
  master, in that order.
* **`add_instances(batch, False, False)` is LOCAL space** — the holder actor must be spawned at the
  origin or the whole scatter is offset by its location.
* **A fresh `BP_MobSpawner` comes out of the CDO with `MobClass = None`** and spawns nothing; and
  `FStatsMob` cannot be written from python — it goes through `TRMythicToolset SetMobSpawnerStats`.

---

## NOT DONE, and what is unresolved

1. **Nothing has been seen.** No editor, no client, no capture of the actual world. Every number here
   is measured on a numpy array. The first thing the next editor session should do after
   `lf_01_import.py` is fly the god cam along the inside of the wall and stand in C3, because a
   40-metre-high wall that measures correctly can still look wrong.
2. **C5 fails the ≤ 6° clearing rule at its rim** — 5.81° mean but 8.18° max, 48 % of its core over
   6°. It sits on ground with a 7.18° regional tilt; getting the whole 170 m disc under 6° means
   cutting a bench, which is the stamped pad Daniel rejected twice. I chose the gentle tilted floor
   over the rule. If he wants the rule instead, the fix is one number (the plane's tilt cap) and a
   bigger clamp.
3. **Cave A's cleft walls are 48.8° at p90 against a ≥ 50° rule** — a 4 m landscape cannot hold a
   50°+ face across a 9 m slot. The rock face has to come from the Cave Environment Modular meshes,
   not the heightfield. That pack is still on the download list.
4. **The trail's mask line is 4 m per pixel** and can only be a faint tint; its width must come from
   instances. Walk item 39 (a ≥ 1 m mask near settlements) is still open and this is now a second
   reason to do it.
5. **The ridge was diverted up to 157 m off the drawn line** to clear three clearings, and two spurs
   were trimmed. Deliberate, measured, and the only departure from the concept — but it is a change to
   something Daniel drew, and he should see the map before it is imported.
6. **The cave interiors do not exist.** The clefts are the sites. The mob definitions for the 4–7
   re-band do not exist either: both jsons need new entries or level overrides before anything can
   be placed.
7. **The heightmap, the RG texture, the mask and the .f32 instance data are LOCAL, not committed** —
   the standing rule is no binary array over 2 MB in the repo. All of them regenerate bit-for-bit by
   re-running the three `gen_*_lf.py` scripts; every input is seeded and there is nothing
   machine-dependent.
8. **Not started, and out of scope for an offline shift:** the ridge has no rock/scree material
   treatment on its face (it will read as grass at 50° until the landscape material gets a slope
   rule), and the forest has no per-instance tint parameter wired — the .f32 carries the tint value
   but `MI_TR_SilverFir_*` has no `PerInstanceRandom` hook on the Roman & Celtic pines.

## Four defects found and fixed inside this shift, recorded so they are not repeated

* **The ridge was standing on a 150 m-smoothed base**, so `max(live, base + profile)` quietly filled
  every hollow inside the ridge's footprint up to the regional mean — a 5 m step at the footprint
  edge. The landform is now *added* to the live ground, and the base eases from the live ground at the
  toe to the regional surface up on the flank.
* **The clearing floors were being dragged up by the new crest.** The slope-cap relaxation is a
  diffusion, and its boundary values were the wall 145 m away: 90 passes pulled C1 up **6.9 m** and C5
  up **5.4 m**, straight into the clamp. The whole clearing pass now runs on the live ground and is
  composited into the ridge surface only at the end.
* **The "runnable" skirt measured 15.4° median where 12° was designed**, from three causes, each
  measured and each fixed: a log-sum-exp smooth-max put a 2.8 m bump on the knee between skirt and
  cliff (now a polynomial smooth-max, biased k/4 instead of k·ln2); the skirt's width swung 76→148 m
  inside one 80 m noise wavelength, which is 23 m of height over 40 m of walking (now smoothed along
  the line at 90 m); and the profile was added to ground that already tilts, so the base's own outward
  gradient (0.6–6.9°) is now subtracted from the design. Result: **90.4 % ≤ 15°, median 12.2°**.
* **Cave B's cleft cut 35 m deep.** Its floor was referenced to the mouth, and the cleft drives into
  the ridge's own 46° face. "6–10 m below the local ground" now means exactly that — the floor climbs
  with the hill. Max cut **7.76 m**.

## The file list

Committed under `Tools/dalriata/lf/` in the game repo:

```
gen_terrain_lf.py  gen_forest_lf.py  gen_trail_lf.py  gen_plan_lf.py
audit_sightlines_lf.py  audit_landform_lf.py
lf_01_import.py  lf_02_forest.py  lf_03_trail.py  lf_04_dress.py
gen_terrain_lf.json  lf_forest.json  lf_trail.json  lf_plan.json  lf_ridge_line.json
lf_sightline_audit.json  lf_landform_audit.json
lf_terrain_preview.png  lf_density.png  lf_trail_preview.png
```

Local only, regenerated by re-running the generators: `dal_riata_lf_g16.png` (4.6 MB),
`T_TR_Height_RG.png` (5.0 MB), `T_TR_GroundMask.png` (0.6 MB), `delta_lf.f32`, `_z_lf.npy`, and the
six `lf_*.f32` instance files.
