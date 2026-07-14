# Great North Overworld — v1 read (Inkarnate WIP, 2026-07-14)

> **PARKED (Daniel, 2026-07-14): disregard this whole doc for now.** The
> map it reads is already outdated — Daniel is actively expanding it in
> Inkarnate with the real allocations. When he delivers the accurate
> Great North map, redo the read from scratch against that export; keep
> this file only as background reasoning.

Daniel's first Inkarnate pass at the Great North overworld. Unfinished by
his own note — "possibly just part of the Great North, governments and race
starting locations not fully allocated." This doc is the design read of
what's on the canvas, a WoW-Classic-style sector cut, and starting-location
proposals anchored to the authored culture groups in
`data/factions/great-north.json`. Nothing here is final until Daniel signs
it; treat every name as a candidate.

**Canvas status:** map art lives in Inkarnate (cloud). ACTION: export
full-res PNG into `design/` as `great-north-overworld-v1.png` so the repo
versions each iteration. (v1 was shared in-chat only.)

---

## What's on the map (inventory)

- **NORTH MASSIF** — snow-capped range with evergreen skirts, a fortress
  high in the passes, red camps along the roads, a mountain lake, and a
  carved **bear-head rock face** at the summit line (instant landmark).
- **STARK PEAKS** — a second, barren white range running south off the
  massif. No forests, no settlements. Reads hostile.
- **THE PENTAGON HEARTLAND** — center of map: a five-sided **water-moat
  wall** enclosing farmland, woods, ~8 village clusters, and a white
  church. The most "built" civilization on the canvas.
- **WEST VASTWOOD** — enormous deciduous forest spanning the left edge,
  with a hidden **statue/monument** deep inside and cliffs at its south rim.
- **SW ELDER PLATEAU** — raised rocky shelf of old-growth forest around a
  **giant gnarled elder tree**, a red tower at its NE corner, and a straight
  **aqueduct/canal** with a bridge running along its north edge.
- **NW ISLES** — two islands in a dark sea: a large one with a castle town,
  a smaller one with road, windmill, and a small keep.
- **EAST COAST TOWNS** — two orange-roofed towns + keep + windmills on the
  right edge, linked by roads that run the whole eastern seaboard.
- **CENTRAL STEPPE** — wide yellow-green plains crossed by rivers and the
  north–south road. Mostly empty (unfinished on purpose).
- **SE LAKELANDS** — river-fed lake system, fishing hamlets, autumn groves.
- **THE BLOOM (SE corner)** — dark pines giving way to purple/blue
  crystalline flora and glowing red-orange trees. Reads as magical
  corruption/fey incursion spreading from the south edge.

## Proposed sector cut (WoW-Classic zones + level bands)

Daniel's call: "sectors like in WoW Classic." Cut below gives each of the
four authored culture groups a 1–10 homeland, funnels everyone through
shared mid zones, and points the danger at the Bloom and the high peaks.
Names are CANDIDATES (pick/veto freely).

| # | Zone (candidate name) | Map area | Band | Role |
|---|----------------------|----------|------|------|
| 1 | **The Moathold** (alt: Hearthmoor) | pentagon heartland | 1–10 | Crusaders start; human capital province |
| 2 | **Eldenwood** (alt: Silverbough) | west Vastwood | 1–10 | Elves start; statue = elf holy site |
| 3 | **Hillback Reach** | north massif foothills + citadel | 1–10 | Hillback Empire start; citadel = dwarf capital |
| 4 | **Dew Hollow** | SW elder plateau | 1–10 | Dew Hollow start; elder tree = the Hollow itself |
| 5 | **The Goldenmoor** | central steppe | 10–20 | first shared zone; all four roads meet here |
| 6 | **The Meres** | SE lakelands | 12–20 | shared; fishing hamlets, river quests |
| 7 | **Amberstrand** (alt: the Freeports) | east coast towns | 15–25 | trade towns, neutral-ish hub, boats |
| 8 | **The Skerries** (alt: Mistholm) | NW isles | 8–15 | adventure isles; castle = first mini-dungeon? |
| 9 | **Bjornfell** | upper massif, bear-head rock | 20–30 | elite camps in the passes; the bear head IS the zone icon |
| 10 | **The Ironteeth** | stark white peaks | 25–35 | "Land of Ice and Iron" — mining, hostile, group content |
| 11 | **The Veilbloom** | SE corruption | 30+ | mystery/threat zone; ties to the veil-tamer class fantasy |

**Frostmarch placement:** the playable slice (snow + citadel) maps
naturally to the **Hillback Reach / Bjornfell** snowline — proposal: the
slice citadel is canonically the Hillback citadel's outer march, i.e.
"Frostmarch" is the militarized snow frontier of zone 3/9. Gives the slice
a real place on the world map from day one.

**"Part of the Great North":** agreed — this canvas reads as the
*temperate south* of the GN. The true Land of Ice (30+ endgame ranges,
raid-tier cold) extends past the TOP edge beyond the massif. That's the
next Inkarnate canvas northward, not a rework of this one.

## Starting locations

> **DANIEL'S DIRECTION 2026-07-14 — supersedes the v1 proposals below.**
> He is annotating the Inkarnate map with this now; the exported map is
> the authority once it lands. Recorded from chat so nothing is lost:
> - Starts are **culture-paired, not culture-group-blocked**: each elf
>   race starts beside its mythologically-linked human culture.
> - **Celtic** start: top right of the map; **Sidhe** start nearby
>   (Celtic myth pairing).
> - **Baltic + Slavic** start: also the top-right region.
> - **Germanic + Alfar** (Alfar = snow elves): the snowy mid-north.
> - **Mythic elves = high elves**: start near the **Hellenic** culture.
> - Remaining allocations (Romance, Armenian, Severus, Hillback, Dew
>   Hollow races) still being placed on the map.
> - This allocation is VITAL input for in-game terrain/world building —
>   transcribe into `data/zones/` once the annotated map is exported.

### v1 proposals (SUPERSEDED — kept for the zone-cut reasoning only)

`great-north.json` defines exactly four culture groups → four starts:

- **Crusaders** (Celtic, Germanic, Romance, Hellenic, Slavic, Baltic,
  Armenian, Severus) → **The Moathold.** Eight human cultures inside one
  walled province = eight villages already drawn inside the pentagon; each
  village can flavor one culture (Celtic village = the reference start,
  matching Celtictest + the Knight/4-class slice picks). Church = shared
  chapel of the crusade.
- **Elves** (Mythic, Sidhe, Alfar) → **Eldenwood.** Three races, three
  groves; the hidden statue anchors the Mythic elves' story.
- **Hillback Empire** (Hillback Dwarves) → **Hillback Reach.** The
  mountain citadel is the empire seat; "hillback" is literally the massif.
- **Dew Hollow** (Woodling, Gobbledrift, Fae, Centaur) → **Dew Hollow**
  zone. Woodlings/Fae in the elder tree, Gobbledrift camps under the
  plateau rim, Centaurs ranging the plateau edge onto the Goldenmoor.
  The aqueduct: who built it, and why toward the Hollow? Free lore hook.

## Landmark identity anchors (keep these — they're the memorable bits)

1. Bear-head rock (Bjornfell) — faction-defining vista, visible for zones.
2. Elder tree (Dew Hollow) — the "world tree in miniature" every MMO needs.
3. The pentagon moat — no other MMO heartland is a five-sided canal. Keep.
4. The Bloom — creeping corruption = built-in live-content dial (it GROWS
   patch over patch).
5. Forest statue — mystery breadcrumb; do not explain it early.

## Scale sanity (giant map, WoW-classic sectors)

WoW-Classic zones average roughly 1–1.5 km² with a continent of ~15–20.
This canvas cuts cleanly into ~11 zones = a proper southern half of one
faction's continent — right-sized for "GN-first, ML/HG later" (vision.md).
Slice-first discipline still applies: only Frostmarch exists in-engine;
zones get built when the loop earns them.

## Open questions for Daniel

1. Zone names above: keep/kill/rename? (Celtic-vs-Norse flavor dial.)
2. Is the Bloom the Veil (veil-tamer class tie-in) or something else?
3. Which pentagon village is the Celtic reference start?
4. NW isles: tutorial isle, or level 8–15 adventure detour?
5. Does the frozen "true north" get its own canvas next, or extend this one?
6. Government names for the four starts (Moathold crown? Hillback emperor?)

## Next steps

- [ ] Daniel: export full-res PNG → `design/great-north-overworld-v1.png`
- [ ] Annotated overlay (zone boundaries + names) once names are picked
- [ ] `data/zones/great-north.json`: zone list + adjacency + level bands
      (same xlsx→JSON→engine pipeline as everything else)
- [ ] Iterate canvas in Inkarnate: fill the steppe, mark the four capitals,
      draw the road loop connecting all four starts through the Goldenmoor
