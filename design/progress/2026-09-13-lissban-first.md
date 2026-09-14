# Lissban, rebuilt — night shift 3 (2026-09-13, 21:53 → 00:30)

Brief: `design/briefs/2026-09-13-lissban-first.md`. Level `/Game/ThreeRealms/Maps/GN_DalRiata_v2`,
anchor `data/zones/dal-riata.json` settlements.lissban = **(-3493.4, -1045.9)**, island scale
11 × 6 km (untouched). Nothing outside Lissban's 300 m was altered.

Daniel's words this shift: *"we're not perfecting but making serious progress on Lissban before the
rest of the map because I want you to understand what I want."* This is written to be read against
the spec, so the failures are listed as plainly as the wins.

---

## 1. The one thing that mattered most

**The whole village was up to 32 m away from where the layout put it, and I only found it because
the overlap audit disagreed with my own arithmetic.**

The audit reported `LB_Hall_01` and `LB_HutB_01` interpenetrating at a centre distance of 11.10 m,
while the two placement points are 29.7 m apart. Both numbers were right: the audit measures
**bounds centres** and the placement code set **pivots**, and these Celtic House meshes do not have
their geometry centred on their pivot. Measured pivot → bounds-centre offsets:

| building | mesh | offset from pivot |
|---|---|---|
| Hall  | `f_house_071` @0.62 | (6.27, −16.14) m |
| HutA  | `f_house_02` @1.10  | (2.89, −32.15) m |
| HutB  | `f_house_02` @1.05  | (26.72, −15.34) m |
| HutC  | `f_house_02` @1.10  | (−4.01, 32.03) m |
| Barn  | `f_house_granarie_01` @1.70 | (19.97, 17.02) m |

So "a hut at bearing 120°, radius 18 m" was actually standing 32 m away — outside the palisade, in
a different part of the field. This is almost certainly a large part of why the afternoon's Lissban
read as random scatter to Daniel: the layout code was sane and the world did not match it.
`Tools/dalriata/lissban/lb_12_recentre.py` now measures each building's offset and shifts the actor
so its **bounds centre** lands on the planned point. Every future settlement script must place in
bounds-centre space, not pivot space.

---

## 2. What is built (as-built inventory, from `lb_08_audit.json`)

655 actors placed by this rebuild, all labelled `LB_*`, all in outliner folder `DalRiataV2/Lissban`.

- **Palisade** — 61 timber segments (`fort_palisade_wall1/v2_exp_SM`) on a wobbly ring,
  radius 26.5–33.5 m, circumference 192.2 m, walked by arc length at a 3.02 m pitch with a 3.15 m
  mesh so the run is continuous by construction and never doubled. **One** opening, 4.2 m clear,
  facing **WSW (247.5°)** toward the farms, as the brief requires.
- **The gate** — a new C++ actor, `ATRGateActor` (below), leaves shut at rest.
- **Chief's hall** — `f_house_071` @0.62 → 22.3 × 21.8 × 7.4 m, the largest building by a wide margin.
- **Three family huts** — `f_house_02` @1.05–1.10 → ~9.8–10.7 m across.
- **The barn** — `f_house_granarie_01` @1.70 → 8.6 × 8.7 × 6.5 m, with a cart, grain sacks and a
  drying rack beside it.
- **Yard** — fire pit at the centre, three sitting logs, woodpile, chopping block, quern.
- **One pen** — 17 straight fence pieces on an irregular quadrilateral with a **3 m gap on the yard
  side** so the player can walk in to the animal, plus a water trough. (The afternoon's three
  overlapping circular pens are gone.)
- **Interiors** — 25 props: hearth, bed/hide, bench, table, pottery, barrels, distributed inside the
  hall (8), each hut (5) and the barn (2).
- **Farms** — four irregular quadrilateral enclosures W/SW right outside the gate, 42–50 m on a side,
  laid out in the cart track's own frame so they flank it with a 7 m track corridor and 4–6 m hedge
  lanes: 281 wattle hedge pieces (1.16 m high, continuous) and 201 crop plants (wheat, millet,
  cabbage, flax, woad), each field with a gate gap facing the track.
- **Trees** — 49 at **12.0–19.9 m, mean 16.2 m** (birch + highland pine), in a broken windward belt
  and a copse, not a row.
- **People** — all 8 Lissban roster entries (below).
- **NavMeshBoundsVolume** `LB_NavBounds_Lissban`, 440 × 440 × 300 m, real brush (`hasBrush: true`).
- **PlayerStart_DRV2_Lissban** restored with tags `[DalRiataV2, lissban, frontline]`.

Kept, not ours: the **7 standing stones** (`DRV2_Lissban_Menhir_*`, 164–185 m out, 2.6–3.6 m tall)
stand where they were, well clear of the fields. Nothing else inside 300 m was Daniel's — the clear
step listed **0** foreign actors, so his hand-edits before the 20:58 crash had removed things
(the closed-door gate piece, floating pen segments) rather than added any.

## 3. The audits (the numbers the brief asks for)

Both measured with a ground trace that **ignores every actor this rebuild placed**, so it cannot be
fooled by a hut roof.

- **Grounding: 655 actors checked, worst gap 0.000 m, 0 over the 0.05 m limit.**
- **Overlap: 414 structural actors, 2 overlapping pairs** — both `Palisade/Gate`, which is the gate
  actor's bounds meeting its own jambs, i.e. by design. **Zero** building-to-building,
  building-to-wall, hut-to-pen or pen-to-pen overlaps. A further 46 tree-canopy overlaps are
  reported separately and are intentional (it is a copse).

Run neighbours are excluded from the overlap test on purpose and the reason is in the script: a
3.15 m palisade mesh laid every 3.02 m *must* overlap — that is what makes the run continuous. The
test flags a **doubled** run (two pieces nearly on top of each other), not a butted one.

Getting to those numbers took three wrong answers first, all logged in the scripts:
`lb_08` first reported a 7.0 m worst gap (it was measuring decals, which are projectors and are
supposed to hover); `lb_11`'s landscape filter never fired because `line_trace_multi` stops **at**
the first blocking hit, so inside a complex-as-simple roundhouse it returns only the roof; and
`lb_13`'s "drill to the lowest surface" fell **through** the landscape onto the sea plane at z=0,
read the ground as −0.60 m everywhere and pushed 304 actors down to sea level. `lb_14_restore.py`
undid that (XY was never touched) and established the trace that is actually correct.

## 4. The gate — new C++ actor

`Source/MMOKitEval/TRGateActor.h/.cpp`, built clean (`Result: Succeeded`, 20.8 s, 2026-09-13 21:55).

The Roman & Celtic pack's gate piece is a single 2.32 m mesh with the doors modelled **shut** and
one convex hull around the lot — under the brief's 3 m minimum and an invisible wall besides. So the
gate is an actor: a root, two leaves hinged at their **outer** edges, and a 4 m sphere trigger.
Server-authoritative `bOpen` is replicated; every machine eases the leaves to ±100° over ~1 s when a
player pawn overlaps and shuts them ~3 s after the last pawn leaves. Leaves are Movable with
`BlockAll`, so the doorway is genuinely solid when shut and genuinely open when not. Leaf mesh,
gap width, open angle, swing time, close delay and trigger radius are all editable properties;
leaf mesh/offset/rotation/scale are exposed so one actor fits any door mesh whose pivot is not on
the hinge edge. Currently `SM_Gate_SM_Door` scaled to a 1.60 m leaf, 2.60 m tall, in a 3.2 m gate.

## 5. Collision — the honest verdict

**What is proven.**
- **The palisade has no holes.** A player-sized capsule (r 40 cm, half-height 88 cm) swept from
  inside to outside at **every one of 360 bearings**: 0 got through. That result is only worth
  anything because the same sweep was first run as a **control** in open ground, where it correctly
  reported clear at 3 of 4 bearings — without that control, "0 holes" and "the test is broken" look
  identical, and the first version of this test was reported before the control existed.
- **Trees: trunk only.** The fir/birch/pine meshes now carry **no** collision at all (my first
  attempt used `add_simple_collisions(CAPSULE)`, which wraps the whole **canopy** — a 4 m invisible
  cylinder, worse than shipping) and each tree instead has a hidden 0.6 m cylinder at its bole,
  covering 80% of its height, set to `BlockAll` with shadows off. Canopy never blocks; trunk always does.
- **Nothing floats:** grounding audit above.

**What is NOT proven, and is the main open risk.** Whether a player can actually **walk inside a
hut**. Three probes disagree and I ran out of shift before an in-game answer:

- A vertical section through each roundhouse finds **one surface per column — the roof.** There is
  **no floor mesh** (the landscape is the floor, which is fine) and **no wall crossing** below the
  eaves at 60/100/140/180 cm; the shell only closes at ~220 cm where the thatch comes down.
- A horizontal ray scan at those heights reports 64–68 of 72 bearings **open**.
- A player-sized **capsule** sweeping inward reports **0** of 72 bearings passable.

The consistent reading is that these are **open-sided roundhouses on a post ring**: a thin ray slips
between the posts, a 40 cm capsule never does. The yard capture supports it — the hut walls are
visibly posts with dark gaps between them. If that is right, the huts are not enterable anywhere,
including at the door, and the fix is per-mesh custom collision with the doorway cut out (or a
different roundhouse asset). `CTF_UseComplexAsSimple` is applied and saved on all seven Celtic House
meshes, which is strictly better than the shipped single convex hull that sealed them, but it is not
sufficient on its own.

## 6. People

All 8 Lissban roster entries placed from **anchor + offset_m**, footprint-checked, and their
`position_m` / `position_uu` / `offset_m` / `facing_yaw_deg` **rewritten in
`Content/Data/npcs/dal-riata-npcs.json`** with a `positionFrame` stamp — the old values were v1
3 km-island coordinates and were meaningless here.

Hywel Fawr (chieftain) at the hall door / yard fire, Bedwyr ap Rhys (Frontline trainer), Angharad
Wen (merchant), Gwilym Penlan (start guide), Meirion the Thatcher, Nest Goch, Cadog Hir, and the
cattle placeholder. Bodies are deliberate plain capsules with a floating name — the kit mannequin is
rejected and real bodies belong to the MetaHuman lane; what is true tonight is that the right person
stands in the right place with a readable name.

## 7. Not done — say it plainly

1. **The dirt layer.** The brief asks for a landscape dirt layer on the yard, paths and track and a
   tilled layer in the fields. UE 5.8's Python exposes no landscape weightmap painting, and painting
   it properly would mean regenerating the island's weightmaps, which the brief forbids. I placed
   161 decals instead — and **they rendered as flat white sheets** over the fields and track (not
   texture streaming: a 6 GB pool and `FullyLoadUsedTextures` changed nothing; `MI_decal_dirt_01` is
   authored for walls). Shipping worn ground that looks like spilled paint is worse than shipping
   none, so **the decals were deleted and the ground is still grass.** Needs a proper landscape
   layer edit or a decal material authored for terrain.
2. **Grass is not switched off inside the palisade.** Same root cause.
3. **The NavMesh is not baked.** The volume is placed with a real brush, but `RebuildNavigation`
   ran 14 minutes without finishing and the log says why: *"Navmesh bounds are too large! Limiting
   requested tiles count (2284200) to: (1048576)"* — the level still carries an island-wide nav
   bounds volume from night 1, so any bake is a >1M-tile job. Shrinking or removing that volume is a
   level-wide scope decision and I did not take it unasked. **Recommend:** restrict navigation to
   per-settlement volumes, or raise the RecastNavMesh tile size, then bake.
4. **Hut interiors may be unreachable** (§5). The props are placed and grounded either way.
5. **No well and no haystack** exist in any owned pack; the trough stands in for the well.
6. **`f_house_07` is a material, not a mesh**, and **`f_house_granarie_02` is the *small* granary**
   (3.5 × 2.8 × 3.3 m) — both stated the other way round in the brief. Hall and barn use
   `f_house_071` and `f_house_granarie_01` accordingly.
7. **`SM_SilverFir_*` renders as bare white trunks** (the known white-material bug, already on the
   focus list). Trees were swapped to Abandoned_Cathedral birch + R&C highland pine to avoid it.

## 8. Evidence

Editor captures, gizmos hidden, game view, Epic scalability, ray tracing off —
`design/progress/captures/2026-09-13-lissban/`:

| file | pose |
|---|---|
| `lb_gate_from_field.jpg` | from the SW field looking at the gate |
| `lb_yard.jpg` | inside the yard |
| `lb_threequarter.jpg` | high three-quarter: fence + huts + farms + track |
| `lb_hall_interior.jpg` | inside the hall |
| `lb_track_fields.jpg` | down the cart track between the fields |
| `lb_pen_and_barn.jpg` | the pen and the barn |

In-game walk captures: see §9.

Scripts and machine-readable reports: `Tools/dalriata/lissban/` in the game repo
(`lb_00`…`lb_17`, `lblib.py`, plus `lb_*.json` for every step's numbers).

## 9. In-game walk

<!-- WALK RESULTS -->

## 10. Verdict against the spec

Built to spec: the wobbly single-gated palisade facing WSW, the hall + three family huts at the
sizes asked for, the barn, the yard with its fire, one pen with a gap, four irregular field
enclosures with hedges and a crop flanking a cart track out of the gate, the standing stones left
standing, the roster placed and rewritten, trees at real scale, a working swinging gate, and both
audits clean (0 floating, 0 real overlaps).

Short of spec: the worn-dirt ground layer is absent, the NavMesh is unbaked, and hut enterability —
the thing Daniel explicitly added to the brief at 20:30 — is **unresolved**, with strong evidence
that the pack's roundhouses have no walkable doorway at all. That last one should be the first item
of the next shift, and it may be an asset decision rather than a collision setting.
