# World / environment audit — GN_Frostmarch (2026-07-05)

Audit only. No map edits made. Read-only inspection of the live world map,
its actors/materials, and the project's imported content.

## 1. Active map/level
`/Game/ThreeRealms/Zones/GN/GN_Frostmarch` — confirmed from the client
command line and the server "Welcomed by server (Level: …GN_Frostmarch)".
This is the CORRECT playable world map, not StartMap/BasicMap/LargeMap.

## 2. Diagnosis — why it looks empty (NOT a wrong-map/loading issue)
The map is fully populated and has a complete atmosphere stack. The problem
is 100% asset QUALITY, not missing pieces:
- **Terrain** = `SM_GN_Terrain`, a single low-poly **static mesh** (438 KB),
  not a UE Landscape. Smooth, no elevation identity, no sculpt detail.
- **Props present** (dense!): ~650 `GNF_Pine`, ~120 `GNF_Rock`, 6 cabins,
  keep pieces (`GNF_Keep_Main`, `GNF_Keep_Corner`, ~16 walls), 8 stones,
  a campfire, palisade. But every one is a **crude generated OBJ**
  (`SM_GN_Pine/Rock/Cabin/KeepTower/Palisade/Monolith`, 73–78 KB each).
- **Materials** = `MI_GN_Pine/Rock/Snow/Stone/Wood`, **7 KB each** = flat
  color, no textures, no normals, no roughness, no blend. THIS is the
  "graybox" read: untextured geometry lit by a default sky.
- **Lighting/sky/fog ACTORS all exist**: `GN_Sun` (DirectionalLight),
  `GN_SkyLight`, `GN_SkyAtmosphere`, `GN_Clouds` (VolumetricCloud),
  `GN_Fog` (ExponentialHeightFog), `GNF_PPV` (PostProcessVolume). They're
  present but untuned/default — flat white overcast, no cold-winter key light.

**Root cause:** no real environment art has ever been imported. See #4.

## 3. Existing environment assets found
- Placeholder OBJ meshes: `SM_GN_Terrain, SM_GN_Pine, SM_GN_Rock,
  SM_GN_Cabin, SM_GN_KeepTower, SM_GN_Palisade, SM_GN_Monolith`.
- Flat material instances: `MI_GN_Pine/Rock/Snow/Stone/Wood`.
- Full lighting/sky/fog actor stack (listed above) — reusable, just untuned.
- **Kit art** (`Content/MMOKit/MMO_Assets` & `MMO_Content`) is entirely
  CHARACTER/gameplay: arms, mannequins, Paragon minions, swords, icons, UI,
  mobs, buffs, equipment. **No environment/landscape/foliage/architecture.**

## 4. Missing asset categories (the real blocker)
Project `Content/` top level = `Collections, Data, Developers, MMOKit,
ThreeRealms`. **Zero imported environment packs** — no Megascans/Quixel, no
Mountain Tops, no Caves & Dungeons, no Abandoned Cathedral, no landscape
material, no foliage pack, no rock kit. Despite these being owned in the Fab
library and the standing "Add To Project" reminder, **none are in the
project.** Missing, by category:
- Layered **landscape material** (snow ↔ rock ↔ ice with textures+normals).
- Real **rock/cliff kit** (Megascans) for mountain walls and outcrops.
- Real **snowy conifer foliage** (upright, wind, LODs) to replace the OBJ pines.
- **Modular fantasy architecture** (keep/castle/ruins) for the landmark.
- **Ground textures** (snow, packed trail, ice).
- **Roads/paths** decal or mesh kit.
- **Snow particle VFX** (falling snow, ground drift, campfire embers/smoke).
- Optional: **frozen water** material for a fjord/lake vista.

## 5. Best candidate area for first vertical slice
The **spawn camp** around `GN_PlayerStart` (~X 1400, Y 900): it already has a
cabin cluster + campfire + keep pieces nearby. Small, bounded, story-anchored
("your starting camp in the Great North"). Polish a ~150 m bowl here, not the
whole zone.

## 6. Recommended realm/biome for first slice
**Great North / Frostmarch.** Reasons: it's the only playable realm; the zone
already exists; winter is the most forgiving biome to make beautiful with the
fewest assets (one great snow landscape material + snowy pines + a fog/atmos
pass + one distant ice-castle landmark reads as AAA); and it matches Daniel's
own Great North login key art (gothic ice citadel, blue-steel palette,
campfire warmth), giving a locked visual target.

## 7. Vertical-slice plan (Great North "Frostmarch Camp")
- **Vista/landmark:** a distant gothic **ice citadel** on a cliff on the
  skyline (the login key-art castle), framed by mountain walls — the thing
  you see the moment you spawn and walk toward.
- **Terrain:** replace `SM_GN_Terrain` with a real **UE Landscape** — a
  playable valley floor rising to steep mountain walls that frame the vista;
  a gentle bowl at the camp. Sculpt + layered snow/rock material.
- **Road/path:** a packed-snow trail from the campfire, curving toward the
  keep/citadel — gives the eye a line and the player a direction.
- **Foliage/rock/props:** replace OBJ pines with a real snowy conifer
  (scattered denser on slopes, thinner in the bowl); Megascans rock outcrops
  on the walls and as trailside boulders; snow-dusted shrubs; keep the
  campfire, upgrade the cabin/keep to real modular architecture.
- **Lighting/fog/sky:** tune the EXISTING actors — `GN_Sun` to a low, cold
  blue-white winter key (strong shadows), warm the campfire light, tune
  `GN_Fog` for atmospheric depth toward the vista, dial `GN_SkyAtmosphere`
  and clouds to an overcast-with-breaks winter sky, add falling-snow VFX.
- **Assets required:** snow landscape material (Landscape Pro 2.0 / Megascans
  surfaces), Megascans rocks/cliffs, a snowy conifer foliage pack, modular
  keep/castle (Abandoned Cathedral or a castle kit), snow VFX. All owned in
  Fab per memory — **must be imported into the project.**

## 8. Exact maps/files/actors that WOULD be touched (when assets land)
- `GN_Frostmarch.umap` — swap terrain actor, retune `GN_Sun/GN_Fog/
  GN_SkyAtmosphere/GN_Clouds/GNF_PPV`, replace foliage/rock/architecture
  actors, add the trail + landmark.
- New assets under `Content/ThreeRealms/Zones/GN/` (landscape material,
  foliage types) — plus the imported packs' own folders.
- Nothing in `MMOKit/` or any UI/gameplay code.

## 9. What should NOT be touched
UI, unit frames, chat, action bar, Escape/settings menu, camera/input,
kit Blueprints, gameplay systems. This is environment-only.

## 10. Edit now, or wait for asset import?
**WAIT for asset import.** Editing the map now would be polishing graybox —
tuning lights on flat-color OBJs is lipstick on a placeholder and would be
redone the moment real assets arrive. The single highest-leverage action is
importing 3–4 owned packs. Do not fake it with more placeholder props.

### One optional exception (no new assets, fully reversible)
A **lighting/fog/sky tuning pass on the existing actors** (cold winter key
light, real fog depth, sky tuning, snow VFX) would make even the current
graybox read dramatically more atmospheric, and it all carries forward. If
Daniel wants an immediate visible lift while sourcing assets, this is the
only safe edit — but it is not the real fix.

## 11. Smallest safe next step
Daniel imports (Add To Project → this project) a short list he already owns:
1. a **snow landscape material** source (Landscape Pro 2.0 or Megascans snow
   surfaces via Quixel Bridge),
2. **Megascans rocks/cliffs**,
3. a **snowy conifer foliage** pack,
4. one **modular keep/castle** kit (Abandoned Cathedral works).
Tell Claude the folder names once imported; Claude then builds the
Frostmarch Camp slice against them. No map edits until then.
