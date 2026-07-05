# Playable_FrostmarchSlice — review spawn/composition fix (2026-07-05)

Scope kept tight: only the slice map + the character's saved spawn transform.
Untouched: GN_Frostmarch, UI, MMOKit source, gameplay code, chat.

## Problem
Even after the fall fix, the player's spawn view was broken: a black overhead
void + a featureless snow plane, no visible character composition, no landmark.
Not a playable slice.

## Report (7 items)

**1. What caused the black overhead void.** `FS_Mtn_0` — a backdrop mountain
(`SM_Mountain_01`) at **scale 3.2** whose bounding box is ~209,408 units
(~2 km) half-width and towers to **Z=124,376**, centred only ~720 m from spawn.
Its geometry sprawled directly over the spawn column, so the player camera was
looking up into the mountain's dark underside — that was the "void." (All 6
`FS_Mtn` mountains were oversized like this.)

**2. Actors moved/removed.**
- 6 `FS_Mtn` mountains: **scaled 3.2→0.5** and repositioned to a distant
  horizon ring (radius ~68 km) so none overhang the play area.
- 3 citadel towers (`FS_Citadel_Main/Side/Back`): were **floating at Z≈30,000**
  (300 m up in the sky) — brought **down onto the ground** ~150 m north of
  spawn as the landmark.
- Removed the old invisible `FS_SpawnBlock` test box.
- Added `FS_GroundPad` (visible snow ground) and a `FS_Trail_*` stone causeway.

**3. New spawn location.** `(1400, 900, 215)`, facing **+Y (yaw 90)** straight
at the citadel. (Same XY as before, but now sitting on a real snow pad with the
citadel/trail/mountains composed in front.)

**4. Surface/collision the player stands on.** `FS_GroundPad` — a 320 m × 320 m
flat box with the terrain's own **M_FrostmarchSnow** material (visible snow, not
an invisible test box) and **BlockAll** collision, top at Z=126. It spans the
whole spawn→citadel corridor, so the walk to the landmark is on solid, visible
snow. The GN terrain (also snow) provides the far ground + hills behind it.

**5. Is the citadel visible from spawn?** **Yes** — a gothic cathedral ruin sits
dead ahead ~150 m north, full silhouette visible (towers + arched windows), with
a stone trail leading to it. Snowy mountains ring the horizon; bright sky above.

**6. Player-camera screenshot after spawn.**
`progress/2026-07-05-slice-review-AFTER-composed.png` (and `…-7s.png` proving
the character is stationary/standing, not falling). Before-state for contrast:
`progress/2026-07-05-slice-review-BEFORE-void.png`.

**7. Do WASD/RMB/jump still work?** Not verifiable from automation this session:
UE reads movement/camera/jump via **raw input**, which can't be injected without
giving the game window foreground focus, and the sandbox can't grant focus to
the `UnrealEditor` game window. What IS verified: the character **spawns standing
and stays standing** (stable across captures) on a flat solid BlockAll pad, so
the walkable floor is sound. Live WASD/RMB/jump need a hands-on check in the
review client (left running).

## Success criteria — status
HUD ✓ · normal third-person camera + visible character ✓ · no falling ✓ ·
no black overhead void ✓ · no huge mesh blocking view ✓ · visible snow ground ✓
· visible terrain shape (dune + horizon mountains) ✓ · visible trail ✓ ·
citadel landmark ahead ✓ · walkable flat pad (live WASD unconfirmed) ~ ·
looks like a playable slice, not a collision test ✓

## Known deferred (out of scope here)
Snow reads warm/cream under the current sun (cold color-grade is the deferred
interactive art pass); the character has no armor mesh (kit body); the stone
trail is a plain causeway. None are the spawn/void bug.

Related: [[slice-spawn-fix-2026-07-05]], [[playable-slice-2026-07-05]].
