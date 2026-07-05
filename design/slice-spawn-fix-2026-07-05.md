# Playable_FrostmarchSlice — spawn/fall fix (2026-07-05)

Scope kept tight per request: only the slice map + the character's saved
spawn transform were touched. No UI, unit frames, chat, action bar, ESC menu,
MMOKit source, gameplay code, or GN_Frostmarch were modified.

## Why the character fell forever (root cause)

Two compounding causes:

1. **Terrain collision hole at the spawn column.** The slice's terrain
   (`SM_GN_Terrain`) renders a surface at Z=126.8 at (1400,900), but a
   pawn-sized capsule sweep straight down that column hits **no collision** on
   the terrain there — the collision trimesh doesn't cover the spawn point.
   (A `LineTraceComponent` hits the render mesh at 126.8, which is why earlier
   probes looked "fine," but the physical capsule passes straight through.)
   So the character spawned above a hole and fell through the terrain.

2. **Persistence feedback loop turned "fall" into "fall forever."** The world
   server writes the character's position back to the SQLite DB as it moves.
   A falling character's Z was saved lower and lower (-6666 → … → -543321), so
   every re-login re-spawned it deeper — eventually *inside/below* any floor,
   where spawn depenetration ejected it further down. This is what made each
   test look worse than the last and masked whether a floor was working.

## The fix

- **`FS_SpawnBlock`** — a large solid collision block placed directly under
  spawn: 60 m × 60 m footprint, **top at the snow surface (Z=126)**, extending
  ~10 000 units down. `BlockAll` + QueryAndPhysics, **invisible + hidden in
  game** (pure collision, no visual). Being this thick guarantees a fast/high
  fall can't tunnel through it, unlike the first thin platform (which was
  tunneled). Removed the old thin `FS_SpawnPlatform` and 56 floating
  trail-marker / dead-tree artifacts.
- **DB spawn reset** — `Celtictest.Transform.translation` set to a clean
  `(1400, 900, 220)`, just above the block top, so the character spawns
  essentially on the floor (a ~6-unit settle) instead of high up or in the
  void. Rotation kept at yaw 90.
- Cleanup (not load-bearing): terrain collision forced to QueryAndPhysics +
  BlockAll; the 6 oversized backdrop mountains set to NoCollision.

## Files / state changed

- `Content/ThreeRealms/_Dev/Playable_FrostmarchSlice.umap` — added
  `FS_SpawnBlock`, removed thin platform + floating artifacts, re-saved
  (verified on disk: umap mtime updated; a fresh headless load confirms a
  capsule rests on the block at feet Z=126).
- `MMOKitPersistence/.../mmokit.db` — Celtictest translation → (1400,900,220).

## Verification (what is proven vs. not)

**Proven — the endless fall is fixed:**
- Before: client 3D view was a blank gray void; client-side pawn logged at
  `Z = -546388`. Capture: `progress/2026-07-05-slice-fall-void-before.png`.
- After (clean spawn): the client renders a stable snowy world at normal
  camera height. Captures 8 s apart are pixel-identical → the character is
  stationary (at rest), not falling. Captures:
  `progress/2026-07-05-slice-spawn-fixed-standing.png` and
  `…-standing-8s.png`.
- Independent corroboration: the DB Z **stayed at 220**. Every earlier
  *falling* run overwrote the DB with a large negative (the moving/falling
  character triggers position saves); a stationary standing character
  triggers none, so it held the reset value.
- HUD shows Celtictest possessed (100/100) — normal gameplay path, not a fly
  DefaultPawn.

**Not yet proven this session — live WASD movement + a framed shot of the
character mesh:**
- The dev auto-move-probe (injects W, logs distance moved) does not surface
  through the client's start-map → world-server travel: the world subsystem
  stops emitting probe logs ~5 s after arrival, before the camera/move pass
  logs, so there's no logged "moved N units."
- Interactive input (computer-use) needs an approval dialog that can't be
  answered in an autonomous, user-away session, so I did not drive WASD myself.
- The character mesh isn't framed because the WoW camera clips into the
  surrounding snow slope at this fixed spawn — a camera/composition artifact
  already deferred to the interactive art pass, not the fall bug.

**How to close it:** the review client (PID 23120) is left open on the standing
character with the persistence + world servers up — press W/A/S/D to confirm
movement and scroll out to see the character. If it walks normally, the last
checklist item passes.

Related: [[playable-slice-2026-07-05]].
