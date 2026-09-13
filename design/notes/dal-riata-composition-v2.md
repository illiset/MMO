# Dál Riata — composition plan v2 (11 km × 6 km rebuild)

Written 2026-09-13 afternoon shift, before any engine work, because of Daniel's verdict on v1:
*"God threw MMO parts like dice"* and *"this map is way too small for what I wanted Dál Riata to be."*
Machine twin: `data/zones/dal-riata.json` (schema `dal-riata-zone/2`). Plan map:
`design/progress/2026-09-13-dal-riata-plan-v2.png`.

**Every place name here is canon** (`design/names/great-north-places.md` §1). Where this plan needs a
landform that has no canon name, it stays unnamed and is described by position — no name is invented.
The lake is **unnamed**; it needs a name from Daniel.

**Frame:** metres, origin at island centre, **X = north, Y = east**, Z = 0 at mean sea level.
Unreal centimetres = metres × 100 on the same axes. Canvas −7000..+7000 × −4250..+4250 (14 × 8.5 km);
land ≈ 11 km N–S × 6 km E–W; 2 m/quad.

---

## 0. The one rule

Nothing is scattered. Every settlement, road, biome edge and landmark below is followed by **why it is
there**, and the reason is always one of: water, shelter, defensible ground, a harbour, a crossing, a
pass, or soil. If a thing cannot be justified that way it does not get placed. This is the
"craps table" test from `dal-riata-focus.md` §0b applied to the whole island instead of one hamlet.

The second rule, added by Daniel this shift: **terrain and vegetation must be natural.** The heightmap
is noise + domain warp + hydraulic and thermal erosion, and the plan's hollows and ridges are *blended
into* the eroded field, never stamped onto it. Vegetation is placed ecologically — by slope, height,
moisture and canopy — not scattered.

---

## 1. Why the island is shaped the way it is

An 11 × 6 km Atlantic island with a 620 m massif at one end. The long axis is N–S because that is what
Daniel's Inkarnate map shows, and it gives the zone the thing it most needs: **a north half and a south
half that cannot see each other**, separated by a mountain range and a forest.

- **North third (X +1800 → +5450): the Benlea Mountains.** Two summits (620 m at 3300,+250 and 545 m at
  2600,−450) plus a north top at 430 m, so it reads as a *range* and not a cone. Cliff bands 380–560 m,
  heath 250–420, rough pasture 120–250. Gullies radiate off it with alluvial fans at their feet.
  *Why:* the island needs a real height band so there is somewhere with no trees, no pigs and only crows,
  and so the two northern starts are sealed off from everything south.
- **Middle third (X +1900 → −1900): Shanderry Forest.** A closed conifer canopy stretching nearly the
  full width. *Why:* it is Daniel's PNW rainforest and the grind ground, and structurally it is the wall
  that makes the southern settlements a journey away from the northern ones rather than a view away.
- **South third (X −1900 → −5480): the lowlands.** The Owenfinn's valley, Kingshill across the middle of
  it, the Moyree farmland in the south-east, Blunt Head's neck in the south-west.
  *Why:* this is the only ground with soil, shelter and slope under 5°, so it is where people live.

**Coast** (`coast.shore_recipe`): rock platforms and boulder-shingle are the *default*; dry sand exists
only in four sheltered strands (Cuaseen, the Camasmore bay head, the two small south-coast bays either
side of Lissban's neck, the Portcorr spit) with dune/machair grass behind them. Cliff headlands at Grey
Head (95 m), Blunt Head (60 m) and Camasmore Bay's south horn (72 m). *Why:* Daniel — *"not what the
beach looks like in Ireland."*

---

## 2. Settlements: site, sightlines, first minute

Full detail (including the composition recipe for each) is in the zone JSON. Summary:

| Place | Position (X,Y) | z | Why there |
|---|---|---|---|
| **Lissban** (Frontline) | −3750, −1650 | 26 | Blunt Head's neck, 900 m wide — spring line, two beach landings, defensible, and the head takes the weather. Iron-Age duns sit exactly here. |
| **Rinnbeg** (Damage) | 4250, −400 | 38 | A corrie floor under Benlea's NW flank; the only flat watered shelter on the north coast, 900 m from the Cuaseen landing. |
| **Tobarglas** (Healer) | 2350, 1550 | 212 | **Re-sited.** A natural rock shelf at the foot of the Bealanard Shoulder where a spring line breaks out — the Green Well. Holy wells sit on spring lines. |
| **Dromcairn** (Support) | −4350, 2300 | 14 | The pier hamlet (canon), in a dip behind the shore bank, 900 m west of the harbour it serves. |
| **Dunadd** (village) | −3050, 600 | 32 | The Owenfinn's north-bank terrace where the valley opens. Ford upstream, mill downstream, harbour road east, castle road NW — a market grows where roads cross a river. |
| **Carrigrua** (castle) | −1900, −1500 | 158 | **Moved 2.1 km NW.** A crag on Kingshill's NW flank over the Owenfinn gorge: holds the river chokepoint and the road north, cliffed on three sides, Kingshill's 250 m crest at its back. |

### The Carrigrua decision (the load-bearing one)

Daniel: *"Carrigrua and Dunadd are WAY too close — you shouldn't be able to see one from the other"*, and
*"from Carrigrua you must not see Dromcairn or Portcorr AT ALL."*

A castle on the **crown** of Kingshill would see the entire island — which is what a hilltop castle is
for, and exactly what Daniel does not want. So Carrigrua goes on a **crag on the ridge's north-west
flank**, above the Owenfinn gorge, with the higher wooded crest of Kingshill behind it. This is not a
compromise; it is how real castles are actually sited — on the chokepoint (the river, the only ford
approach, the road north), not on the highest point. It keeps everything the castle needs militarily
and blocks the whole south-east.

Geometry: Carrigrua → Dunadd is 2.18 km; the Kingshill crest at the midpoint stands ~140 m above the
sight line. Carrigrua → Dromcairn 4.5 km and → Portcorr 4.9 km, both behind Kingshill *and* the Moyree
drumlins. **This contradicts one line in `dal-riata-vision.md`** ("Dunadd village sits at its gate") —
the walk-test verdict supersedes it. Dunadd is now the village of the castle's district, a 20-minute
walk and a wooded saddle away, and the castle only appears at the last bend.

### Sightline devices used elsewhere

- **Dunadd ↔ Lissban** — the *Athgorm rise* (85 m, unnamed, wooded), which the road climbs before dropping to the ford.
- **Dunadd ↔ Dromcairn/Portcorr** — the **Moyree drumlins** (70–95 m). Drumlin swells with hedge belts on their crests are authentic Irish farm country *and* they solve the problem that a flat farmland plain cannot hide anything.
- **Carrigrua ↔ Lissban** — the Kingshill south-west spur (145 m) with a forest belt on it.
- **Rinnbeg ↔ everything south** — 620 m and 1.5 km of Benlea.
- **Tobarglas ↔ everything south** — the Bealanard south spur (240–270 m, unnamed) deliberately closes the southward view so the Healer start looks *east to the sea*, which is the better shot anyway.
- **Dromcairn ↔ Portcorr** — deliberately *not* blocked; they are one place-cluster. But the Portcorr headland hides the harbour until you round it, so the last leg of the Boherath Road ends in a reveal.

A **sightline audit script** line-traces all 18 required-blocked pairs at 1.7 m eye height; terrain is
iterated until every one is blocked.

### First minute at each start

- **Lissban** — out of the single gate onto a worn yard with a live fire; sea noise from two directions; the standing stones on the seaward rise ahead-left; the road leaving through the cattle pen and climbing into trees. Nothing else. The island has not shown itself yet.
- **Rinnbeg** — cold light off the water behind you and a mountain in front that disappears into cloud. A stream comes down the corrie past the houses. Two ways out: the shore path east, the track up the shoulder.
- **Tobarglas** — high and wet. A spring runs out of rock into a stone basin and off the shelf edge. Sea to the horizon 400 m below; mountain behind. Three houses, a shrine, and a road visible a long way in both directions.
- **Dromcairn** — flat water, a wooden pier, two boats; the sky actually breaking up (this is the island's dry corner); field walls climbing behind; a cart track east round a low headland.

---

## 3. Roads (painted worn dirt, not data polylines)

Daniel walked the island and said *"no roads"* — v1 had them only as JSON. In v2 a road is a **painted
dirt layer along the spline with broken worn edges**, plus verge wear.

- **Bohermara Road** — Rinnbeg → over the **Bealanard Shoulder** (the only crossing of Benlea under 400 m) → past Tobarglas → down the east-shore terrace → **Cromcross** → Dunadd. ~9 km. It stays on the *seaward* side of Shanderry the whole way, so a level-1 character never has to enter the forest.
- **Boherath Road** — Carrigrua → off the castle saddle → the Owenfinn's north side → **Athgorm Ford** (the river's only gravel bar with firm banks) → dogleg SW to **Lissban** → along the south coast → **Dromcairn** → **Portcorr**. ~7.5 km.
- **Dunadd → Carrigrua spur** — climbs the Kingshill saddle. The climb *is* the sightline block.
- **Whitemill lane** — 460 m, village to mill.

Max grade 12°.

---

## 4. Water

- **Owenfinn River** — springs in Shanderry (900,−350) → **waterfall, 26 m, where it leaves the forest** at (−1150,−1250) onto the lowland rock step → the gorge under Carrigrua's crag → **Athgorm Ford** → swings east across the Moyree past **Whitemill** → drowns its mouth at **Portcorr**. Canon route ("forest → past Carrigrua → sea at Portcorr") satisfied exactly.
- **The lake (unnamed)** — kept in its relative position (the lowland east of Kingshill, north of Dunadd) at (−2050, 1250) but **pushed to 1.58 km from the sea**, as a **natural shallow basin**: 760 × 470 m, 6 m deep, gentle banks, a wide reed margin on the north and east, shingle on the wind-blown west, **no crater wall**. A **feeder stream** comes off the forest's SE shoulder; an **outflow** runs SW to join the Owenfinn below Dunadd. All four of Daniel's asks.
- **Streams** — two forest headwaters in gullies (plank footbridges), the Kingshill burn into the gorge.
- **Sea** — UE Water plugin ocean body if it can be enabled headlessly; otherwise the best material-driven surface. Atlantic under overcast: grey-green over the Garveen Shallows, dark offshore, shore foam, wet-sand blend. Never tropical blue.

---

## 5. Biomes by band

| Band | Height | Cover |
|---|---|---|
| Bare rock | 420–620 | rock, scree fans, boulder field. No plants. |
| Heath | 250–420 | heather/bilberry, tussock, boulders; stunted rowan only inside gullies |
| Montane rough | 120–250 | rough pasture, bracken, gorse, birch/rowan in gullies |
| **Shanderry rainforest** | 40–210 | **closed canopy**: straight conifers 20–30 m, bare trunks for the first 12 m; broadleaves only at edges and water; moss floor, ferns, big shrubs; nurse logs, fallen giants, root walls, boulders, gullies, streams; dark inside |
| Forest edge | — | 200 m fringe: hazel, willow, birch, bracken — the canopy must not end at a line |
| Lowland meadow | 8–90 | grass, wildflower, gorse, hedgerow trees |
| Moyree farmland | 4–95 | worked fields, earth banks and hedge belts, drumlin swells, the mill leat |
| Coast | — | see the shore recipe |

Ground layers are assigned by **slope + height + curvature with noise-perturbed thresholds and blends
tens of metres wide** — Daniel's ruler-straight grass/rock contour on Benlea is the specific failure
being fixed. Verified at eye level: no straight edges anywhere.

---

## 6. Wildlife habitats

A Wild Pig on Benlea's bare face is the bug being fixed. Every def gets biome list + max height + max
slope + home radius, and the wander leg picker rejects out-of-habitat or steep targets.

| Species | Bands | z max | slope max | group |
|---|---|---|---|---|
| Wild Pig | lowland meadow, Moyree, forest edge | 120 | 22° | sounder 4–7 |
| Red Stag | forest edge, meadow, forest, heath, montane | 420 | 32° | herd 3–6 |
| Doe | forest edge, meadow, forest | 300 | 28° | herd 3–6 |
| Red Fox | forest edge, meadow, Moyree, forest | 300 | 30° | solitary, frequent |
| Carrion Crow | anywhere | 620 | — | flock 4–9 |
| **Grey Wolf** (hostile) | forest, forest edge, montane, heath | 420 | 30° | **pack 2–3**, 15 m aggro |

Density target: an animal in view most of the time in fields and forest edge. Above the tree line:
crows only.

---

## 7. The dungeon approach

**Uaimh na Scáth** — mouth at (−1050, −2790), z ≈ 6 m, at the foot of the 72 m sea cliffs on **Camasmore
Bay's south horn**, below Shanderry (canon). Visible from the water; reached by a shore scramble from
the north. **Fomorian raider camp** (8–10) beached on the storm shingle 190 m north at (−870, −2700),
under the cliff — raiders pull boats up where the cliff gives them a back wall and the cave gives them
a door. Interior is a later lane.

---

## 8. Open question for Daniel

The **lake has no name**. Canon names 20 features and a dungeon; the lake is not among them. It needs a
Gaelic specific + English generic in the agreed convention (e.g. *"<specific> Lough"*). Not invented here.
