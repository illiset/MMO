# Imported Fab asset scan (2026-07-05) — for Frostmarch Camp slice

Inspection only. No map edits. All six new folders are UE-native `.uasset`
(not raw FBX) — imported clean, no material cleanup needed.

## Priority packs (all usable)

### 1. Content/Iceland_Environment  ("Mountain Tops / Iceland")
- **Meshes (14):** SM_Mountain_01–09, SM_Iceland_Eroded_Mountain,
  SM_Iceland_Mountain_02, SM_Iceland_Crest, SM_Iceland_Plateus_01,
  SM_Mountain_Plateu_01 — large background mountain/cliff bodies.
- **Materials:** MI_Landscape_Arctic, MI_Landscape_Mountain, M_AutoLandscape,
  MI_Iceland_Mountains_01–06, RVT_Blend/Height, M_Elevation_Material.
- **Textures:** Snow (T_Snow), T_Mountain_01/02, T_Iceland_Eroded/Plateu/
  Dirt/Grass, T_MossyCreekStones.
- **Map:** Lv_Mountain_Tops_Elevation, Lv_Mountain_Tops_VT (demo — ignore).
- **Use:** rocks/cliffs, framing MOUNTAIN WALLS, the distant VISTA silhouette,
  and snow/mountain surface textures. Arctic landscape material as a fallback.

### 2. Content/MWLandscapeAutoMaterial  (landscape auto-material + snow)
- **Master materials:** MTL_MWAM_AutoMaterial_MASTER, MTL_MWAM_CoverSnow,
  MF_MWAM_Snow, MF_MWAM_SnowMask, PM_MW_Snow, MTL_MWAM_Landscape_
  MountainRangeExample, MTL_MW_VolumeClouds_MASTER.
- **Also:** Blueprints, Procedurals, plant meshes, ground/plant textures,
  example maps (Desert/Island/MountainRange — ignore).
- **Use:** THE snowy-terrain solution — auto-blends grass/rock/snow by slope
  and height. Snow-on-top built in. **Requires a real UE Landscape actor**
  (not a static mesh) to apply. This is the terrain material for the slice.

### 3. Content/Abandoned_Cathedral  (633 files — modular gothic kit)
- **Architecture:** SM_tower_1–6 (+glass), SM_wall_1–14, arches, doors,
  windows_1–4, roofs, stairs, handrails, floors, statues, tombs, skeleton,
  furniture, debris, candles — each with Static_Mesh + Material_Instance +
  Texture (full PBR, UE-ready).
- **Foliage (Nanite):** Birch_1-2, Bush_1-2, Dead_tree_1-3, Dead_Bush,
  Grass_1-3, Ivy_01, Dry_Leaves. (Deciduous/dead — NO conifers.)
- **Systems:** Volumetric_Fog BP, Water material, Terrain RVT material,
  Master_Material.
- **Use:** the ICE-CITADEL / KEEP / RUINS landmark (gothic towers = the
  fortress silhouette), sparse stark-winter foliage (dead trees + birch),
  and a ready volumetric-fog BP.

## Lower-priority packs (NOT environment)
- **Content/Elves_Wizard** — Elf Male Wizard character. Future NPC (fits GN
  elf lore); not terrain.
- **Content/ParagonGreystone**, **Content/ParagonSparrow** — Paragon HERO
  characters (~1700 files each). Wrong category for this task, AND these are
  the "recognizable slop" the art stance bans from the SHIPPED game. Usable
  only as quarantined placeholder mobs, never shipped. Ignore for the slice.

## Category coverage for Frostmarch Camp
| Need | Covered? | Best asset |
|---|---|---|
| Snowy terrain | ✅ strong | MWLandscapeAutoMaterial `MTL_MWAM_AutoMaterial_MASTER` (+ snow fns) on a real Landscape; Iceland `MI_Landscape_Arctic` fallback |
| Rocks / cliffs / walls | ✅ strong | Iceland `SM_Mountain_01–09`, `SM_Iceland_Eroded_Mountain`, `SM_Iceland_Crest` |
| Castle / keep / ruins / landmark | ✅ strong | Abandoned_Cathedral `SM_tower_1–6`, `SM_wall_*`, arches |
| Snow / fog | ✅ (fog) | Abandoned_Cathedral Volumetric_Fog BP; MW VolumeClouds |
| Pine / conifer foliage | ❌ GAP | none — use Cathedral Dead_tree/Birch for stark winter, or import a conifer pack |
| Roads / paths | ❌ minor gap | none — paint a trail layer in the auto-material, or decals |
| Falling-snow VFX | ❌ minor gap | none — add a Niagara snow later |

## Import correctness / issues
- All packs imported clean (`.uasset`, mesh+MI+texture per asset). No FBX
  needing cleanup.
- Iceland & Cathedral ship **demo maps + a FirstPerson demo template**
  (Abandoned_Cathedral\Demo\FirstPerson has its own GameMode/PlayerController/
  Input). Harmless but DO NOT use their game mode — ignore demo content.
- Paragon packs = wrong category + slop-flagged (see above).

## Enough to build the slice?
**Yes.** Snowy Landscape (MW auto-material) + mountain walls & vista (Iceland)
+ gothic-tower ice-citadel landmark (Cathedral) + volumetric fog (Cathedral) +
sparse dead-tree/birch winter foliage (Cathedral) = a complete Frostmarch Camp
slice. The only real gap is **snowy conifers** (nice-to-have; dead winter
trees are atmospheric and arguably more fitting for a stark Great North).
Roads and falling-snow VFX are minor and addable later.

## Smallest safe next step (proposed — needs Daniel's approval)
Do NOT touch GN_Frostmarch yet. First build action = a **throwaway lookdev
map** (e.g. `Content/ThreeRealms/_Dev/LookDev_Frostmarch`): drop a real
Landscape with the MW snow auto-material, place a couple of Iceland mountains
as walls + one Cathedral tower on the skyline, add the volumetric fog, tune a
cold winter sun. Capture it. Prove the look in isolation. Only once Daniel
approves that lookdev do we rebuild the real GN_Frostmarch slice against it.
Related: [[world-audit-2026-07-05]].
