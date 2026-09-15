# The Lissban pass — 14 Sep 2026, evening

Level `/Game/ThreeRealms/Maps/GN_DalRiata_v2`. Editor session 18:17–19:0x, one heavy process at a
time, the play stack down throughout and left down. Scripts and full-size captures:
`Tools/dalriata/lb/` in the game repo. Small captures:
`design/progress/captures/2026-09-14-lissban-pass/`.

A two-hour window against a twelve-step plan. What follows is what actually landed, the numbers
that back it, and — at the end — an honest list of what did not.

---

## 0. The code: F opens the gates, F climbs the ladders

`Source/MMOKitEval/TRGateActor.*` and a new `TRLadderActor.*` (commit `9b41e31`,
`Build.bat MMOKitEvalEditor Win64 Development` → **Result: Succeeded**).

**The gate** now implements `ITRInteractable`: verb "Open"/"Close", interact point the centre of
the gap, reach 400 cm, `CloseDelaySeconds` **30** with the timer armed by the OPEN rather than by
the last pawn leaving. **Proximity opening is gone** — walk-up-and-it-swings was item 1's whole
complaint.

The trigger sphere survives, and the reason is the one thing worth knowing about this change: a
level actor has **no owning connection**, so a client's Server RPC is dropped on the floor before
it ever reaches `ServerToggleGate_Implementation`. The server therefore hands ownership of the
gate to the nearest player's controller while he is inside the trigger (700 cm, deliberately
wider than the 400 cm reach so a player at the edge of reach still owns it) and clears it when he
leaves. Without that, F on a gate would have done nothing on a real client and worked perfectly
in the editor — the worst kind of bug to ship.

**The ladder** is new: a static-mesh ladder plus two landing points — the foot (local XY offset,
traced-ground Z) and the deck (local XY offset, Z from the TOP of the referenced `DeckActor`'s
bounds, so moving an archer post moves its landing with it). F at whichever end the player is
nearer moves him to the other. Two details:

- `TRInteractPoint` returns the **nearer** of the two landings to the local pawn. The interface
  hands the actor no pawn, and a 250 cm reach measured to the foot can never be satisfied from a
  270 cm deck — the prompt would have worked going up and never coming down.
- the move is `TeleportTo` on the **server**, not `SetActorLocation`, so the character movement
  component sends the client a proper correction instead of the client predicting itself straight
  back down. Instant, per the brief's option B. The ladder mesh carries no collision so the player
  cannot wedge himself against the rungs at the foot.

Both actors re-check the reach on the server — the client's F is a request, not an instruction —
and log the refusal when it fails. **Neither has been driven by a human yet**: the play stack was
down for this window by design, so F-on-a-gate and F-on-a-ladder are proven by construction and by
the deck's capsule test, not by a walk. That is the first thing to try tomorrow.

---

## 1. The terrain: a flattened knoll, and a hill that hides Kingshill

`Tools/dalriata/lb/gen_terrain_lb.py` — a **surgical edit written on top of** the forest-edge
heightmap (`fe/dal_riata_fe_g16.png`), not a re-run of the generator. Two circles change and
nothing else on the island does: **0.487 % of the island's vertices**, 35,201 of 7,231,381.

**The knoll** (Daniel 14:05, walk item 13). The measurement that decided its height: the ground
inside the palisade averages **33.99 m** and the meadow in a 45–75 m ring around it averages
**38.76 m**. The village site is a **hollow**, so "slightly higher than the ground around it" is a
**fill**, not a cut — the pad is laid at **39.96 m**, 1.20 m above the surrounding meadow, which
means up to **7.63 m of fill** at the centre and **zero cut** anywhere. Flat top out to the fence
+3 m, then a noisy skirt of **10.2–14.7 m**, plus ±4 cm of noise on the pad itself because a
glass-flat pad reads as a mesh and Daniel never wants plain smooth earth.

**The NE hill** (walk item 38). Centre 330 m out on bearing 42, radius 180 m (≈360 m wide, near
edge ~150 m from the village, which is what Daniel drew), crest **58.2 m** above the meadow, an
eroded broken top, plus a far broader low apron so it has a foot.

That hill was cut **twice**, and the first cut is the lesson. Version one put it 265 m out with a
235 m radius — so its own skirt still reached the village — and used a `smoothstep(140, 210)` mask
on distance-from-village to keep it off the huts. The mask sheared 46 m of hill away over 70 m and
built a **cliff with a flat top**: the three-quarter capture showed a rocky mesa. Moving the hill
out until its own profile does the work, and demoting the mask to a safety net, fixed it. Judge it
from `AFTER_lb_hill_from_yard_s.jpg` — a broad wooded crest behind the village, which is the shot
Daniel sketched.

The Boherath is **not** buried: the road corridor is masked out of the hill over 40 m untouched
blending to 110 m, and the measured **maximum rise inside the road corridor is 0.00 m**.

Imported through the RG texture → RGBA16F render-target route with `force_layers_full_update()`,
then `delta_lb.f32` re-seated every actor and every foliage instance under it. Probed after:

| point | before | after | source image |
|---|---|---|---|
| village centre | 32.64 | **39.94** | 39.95 |
| west gate | 34.96 | **39.96** | 39.97 |
| east gate | 35.08 | **39.86** | 39.95 |
| meadow 60 m W | 39.12 | **39.15** | 39.12 — unchanged |
| NE hill crest | 40.08 | **99.08** | 99.08 |
| forest road (control, 4 km away) | 63.80 | **63.80** | unchanged |

### The two sightline audits

`lb/audit_sightlines_lb.py` re-run offline against the new heightmap: **PASS — every required pair
blocked**, tightest tobarglas↔carrigrua **+3.1 m**, and Carrigrua↔Lissban improved from +25.6 m to
**+48.5 m** because of the new hill. Dromcairn↔Portcorr, the one allowed pair, +22.9 m.

`lb/audit_landform_lb.py` is the stricter test walk item 38 actually asked for — not "is the castle
POINT hidden" but "is Kingshill's CROWN hidden", from nine eye positions inside the palisade rather
than from one anchor: **18/18 lines blocked**, tightest 28.6 m of terrain standing above the line.

---

## 2. Two gates, a baffle, three archer posts

- **The east gate** is cut through the palisade opposite the west one (2 segments removed), a
  second `TRGateActor` at bearing 67.5. Both gates configured for F with a 30 s auto-close.
- **The baffle** (item 14): three palisade sections 3.5 m outside the east gate on a low earth
  bank, a torch post at each end, and the dirt path **splitting round both ends** and rejoining at
  the gate — the dogleg is in the mask, not just in the timber.
- **Three archer posts**, one behind each gate and one on the north side. Deck top **2.70 m** above
  the pad: a standing archer's eye is then 4.4 m, over a 3.6 m palisade. Four legs, six plank
  boards, rails on the three sides that are not the ladder, and a hidden slab so the capsule walks
  the deck as one surface instead of catching between boards. **All three decks catch a player
  capsule** and land it at 43.55–43.57 m, which is exactly the ladder's computed deck landing.
- **The seven standing stones are gone** (item 11).

These were built **twice** as well, and the bug is worth recording because it will recur:
`/Engine/BasicShapes/Cube` is **one metre**, so its scale *is* the size in metres. The first pass
multiplied by 0.01, so the deck collider came out 3 cm across and the baffle's earth bank came out
as a **2.6 cm white cube** sitting in the grass. The same pass also scaled `SM_Wooden_Plank`
without compensating its pivot, which is **1.99 m off centre** — so every deck board, and every
hut floor board, was shoved 1.5 m sideways out of the building. Both are fixed; the pivot
compensation is now in the scripts.

---

## 3. The ground, the buildings, the detail

**The floor** (`lb/gen_mask_lb.py`, a surgical edit of the live `T_TR_GroundMask.png`): the whole
enclosure is **trodden dirt**, not grass with paths through it — weight ~0.80 with a pebble grain,
1.0 on the packed east–west line between the gates and at both gate mouths, dropping to ~0.30 in
five quiet pockets against the walls where grass still struggles up. Tracks run out of both gates:
west through the fields to the cart track, east round the baffle and away to the Boherath. Island
dirt coverage 0.169 % → **0.197 %**. The four field enclosures are tilled to the fence, each
polygon grown 0.5 m outward with a **hard edge, no feather** (items 7/8).

**The buildings.** All four dwellings are `f_house_01` (not the meshes the 13 Sep pass recorded —
they had been swapped, and assuming otherwise briefly shrank the hall to 6.8 m before the survey
caught it). Now: **hall 17.6 m**, three family huts **12.8 m**, barn **9.5 m**, every one re-seated
so its **bounds centre** stays put through the scale change and its bounds bottom sits on the pad.

The collider rings were rebuilt from the **mesh's own local extent × scale**, not from the actor's
world AABB. This matters: HutB is rotated ~45°, so its AABB is √2 too big and the old ring stood
**6.97 m** from the centre of a 6.3 m building. That *is* Daniel's "I can't get any closer to this
hut", reproduced exactly. The rings are now 3.68–6.81 m and sit under the eaves.

And the reason he could not get **in**: taking collision off the mesh *asset* is not enough. With
no simple collision the engine falls back to the **complex (render) geometry** for capsule queries,
so the post ring blocked a 40 cm capsule at every bearing including the ring's own 5 m gap. The
mesh **component** on each actor is now `NoCollision`, and the hidden ring is the only thing that
blocks.

**Interiors**: 45 props — a central hearth in every dwelling, log benches, quern, pots, baskets,
grain sacks, a drying rack, torches in the hall, stores in the barn — on **77 plank floor boards**
laid at pad height inside the rings.

**Detail everywhere** (item 12, Daniel 14:26): a 3 × 3 m grid out to **300 m** from the anchor,
skipping the enclosure and the crops — **30,961 instances**: 19,218 grass tufts, 5,617 shrubs,
3,713 ferns, 2,413 stones. Inside the palisade, **2,152 pebbles** pressed into the trodden dirt and
**192 struggling tufts** against the walls. On the hill: **1,194 conifers** (crest-weighted,
9–22 m, thinning down the flanks), **2,825 gorse/heath**, **26 boulders** in a crest outcrop.

**The graveyard** (the coordinator's addition): `LB_Graveyard`, one `BP_Graveyard`
(`/Game/MMOKit/MMO_Logic/Blueprints/Misc/BP_Graveyard`), outside the **west** gate beside the
track at **(−3527.3, −1091.7, 38.88) m = (−352732, −109174, 3888) uu**, yaw **53.5°** facing the
gate. The class has only a billboard and a scene root — no separate spawn arrow — so the actor's
own yaw is the facing.

---

## 4. The audits

| audit | result |
|---|---|
| **Grounding** | **759 actors checked, 0 floating over 5 cm, worst 0.000 m.** 30 actors sit 2.52–3.64 m up **by design** (the archer decks and rails) and are reported separately, not as failures. Deliberate sinks (a palisade post is buried 40 cm) are not failures either — floating is the bug, burying is a placement choice. |
| **Overlaps** | **131 structural actors, 0 overlapping pairs.** Run neighbours are excluded on purpose: a 3.15 m palisade mesh laid every 3.02 m *must* overlap. The gate actors are excluded too — their bounds are the 7 m ownership trigger, not timber, and counting it made everything near a gate read as an overlap. |
| **Palisade sweep** | **360 bearings swept with a player capsule (r 40 cm, half-height 88 cm); 2 got through** — bearings 242 and 253, i.e. the **west gate**. The east gate holds. **Control: 4/4 clear in open meadow**, so "0 holes" and "the test is broken" cannot look the same. |
| **Hut doors** | All five buildings are now **enterable**: Hall 16° arc at bearing 228 (ring gap 230), HutA 22° at 272/342 (gap 300), HutB 46° at 12/348 (gap 355), HutC 22° at 134 (gap 122), Barn 62° at 156 (gap 165). Before the component-collision fix every roundhouse read **0° passable**. |
| **Sightlines** | PASS, every required pair blocked, tightest +3.1 m. |
| **Landform** | PASS, 18/18 eye→Kingshill-crown lines blocked, tightest 28.6 m. |
| **Nav** | `RebuildNavigation` issued over the village. |

The eight villagers are present and were re-seated onto the pad by the delta pass. They are still
engine-cube placeholders; hiding them was tried for one capture and immediately reverted, because
an empty village is worse than a visible placeholder.

---

## 5. Evidence

`design/progress/captures/2026-09-14-lissban-pass/`, BEFORE and AFTER at **identical** camera poses
where a pose existed (camera Z is absolute, so the pairs are directly comparable — and the village
floor rising ~5 m is part of what the pair shows).

| pose | pair | what it shows |
|---|---|---|
| `lb_yard` | BEFORE/AFTER | the trodden dirt floor with pebbles, the bigger roundhouses, the chieftain at his door |
| `lb_threequarter` | BEFORE/AFTER | the whole village on its knoll, the fields, the tracks |
| `lb_gate_from_field` | BEFORE/AFTER | the approach from the SW field to the west gate |
| `lb_track_fields` | BEFORE/AFTER | the cart track and the tilled fields |
| `lb_pen_and_barn` | BEFORE/AFTER | the pen, the barn |
| `lb_hall_interior` | BEFORE/AFTER | the old interior pose |
| `lb_hall_inside_new` | AFTER | inside the enlarged hall, on the plank floor |
| `lb_baffle_outside` | AFTER | the east baffle from outside, the dogleg track, the meadow detail |
| `lb_archer_post` | AFTER | an archer post from the yard |
| `lb_hill_from_yard` | AFTER | **the shot Daniel sketched** — the wooded crest standing behind the village |

---

## 6. NOT DONE — read this list before the walk

1. **Nothing has been walked in-game.** The play stack stayed down for the whole window by design.
   F-on-a-gate, F-on-a-ladder, walking in through a hut door and standing on an archer deck are all
   proven by capsule test and by construction, **not** by a human. Celtictest is seated on the track
   outside the **west** gate at `(−350872, −108288, 3968)` uu facing the gate (traced ground + 120),
   written while PersistenceServer was stopped.
2. **The west gate leaks.** Two of 360 bearings let a player capsule through at the west gate while
   it is shut. The east gate does not. Likely the leaf mesh scale not quite closing a 3.2 m gap.
3. **The wrong-site castle mound is still there** and it is the ugliest thing in
   `AFTER_lb_threequarter_s.jpg` — the dark, flat-topped, bare-rock cone NW of the village. It is
   **pre-existing**, not this pass's hill; the hill was moved 65 m and re-cut and the mound did not
   budge, which is how it was identified. Removing it (blend the natural ground back over its
   footprint + 60 m, drop its boulders) was the brief's optional step 13 and was **not started** —
   the gate for it was "step 12 finished", and step 12 was not.
4. **The lake was not clipped to its basin contour** (the other optional step).
5. **The hut doorway gap is on the yard side, not provably on the mesh's real door.** The plan
   wanted the gap found by probing the post ring. That probe was written and it **failed**: with
   collision removed from the meshes it reported 324° of 360 open on every building, i.e. it was
   measuring nothing. The rings are correct and every hut is enterable, but which opening in the
   post ring the player walks through is not yet matched to the modelled door.
6. **The baffle's earth bank is collision-only.** An untextured engine cube reads as a white box in
   a screenshot, so it is hidden. It owes a real turf mesh.
7. **The pebbles in the yard may read too large and too evenly spread** — worth a look at eye level
   before the next pass hardens them.
8. **The interior camera cutaway is not mine** (the coordinator's) and is not in this level.
9. **No BEFORE pose exists** for the baffle, the archer post, the hill or the new hall interior —
   those four are AFTER-only, because the things they show did not exist this morning.
10. **Farm tools, the plough, the hay pile and the hand cart** asked for in item 8 were not added
    beyond the yard's cart and log pile; the pen fence gaps (item 4) were not re-closed this pass.
