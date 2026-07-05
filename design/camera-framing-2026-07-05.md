# Default camera framing — pulled back + character lower (2026-07-05)

Camera **framing only**. Untouched: UI, unit frames, chat, action bar, ESC menu,
world art, camera controls/bindings, movement.

## Report (6 items)

**1. Which Blueprint/component controls this.** `BP_PlayerCharacter`
(`Content/MMOKit/MMO_Logic/Blueprints/BP_PlayerCharacter`) → its
**`SpringArmComponent`** (the camera boom) carries the default zoom distance and
framing; a `CameraComponent` is attached to the boom, and the WoW-style zoom is
driven by scroll input modifying the boom's arm length. The custom
`BP_WowStyleCameraComponent`/`BP_BaseCameraComponent` hold no framing floats —
the boom is the source of truth.

**2. Old default values.** `TargetArmLength = 300`, `SocketOffset = (0,0,0)`,
`RelativeRotation = 0`, `DoCollisionTest = True`, `UsePawnControlRotation = True`.
(300 was the "too close / character centered-high" feel.)

**3. New values.** `TargetArmLength = 600` (pulled back), `SocketOffset =
(0,0,70)` (camera raised → looks down slightly → character sits lower-middle,
more ground/vista visible). **Everything else preserved exactly**:
`DoCollisionTest = True` (camera still collides with terrain/meshes),
`UsePawnControlRotation = True` (RMB look intact), zoom input binding + min/max
clamp untouched. Change made on the SCS SpringArm template, compiled + saved;
verified persisted on reload.

**4. Does zoom in/out still work.** By construction, yes — only the *starting*
arm length changed, not the scroll-zoom logic or clamp. The new default of 600
took effect in-game without being clamped, which proves the arm-length path is
live and adjustable (so scroll-in toward min and scroll-out toward max both
remain available). NOTE: I could not *live-demo* the scroll wheel from
automation — UE reads the wheel via raw input, which window-message injection
(PostMessage) doesn't feed (same limitation as WASD/RMB). Needs a hands-on
scroll check.

**5. Does RMB mouse-look still work.** Preserved by construction —
`UsePawnControlRotation` and the RMB binding were not touched; the boom still
follows control rotation. Same automation caveat: raw mouse can't be injected,
so a hands-on RMB check is needed to fully confirm.

**6. Risks / follow-up tuning.**
- If the character feels a touch small, drop arm length to ~500–550; if you want
  it a hair higher on screen, reduce `SocketOffset.Z` to ~50. Both are one-line
  tweaks on the same SpringArm.
- `DoCollisionTest=True` means in tight/indoor spaces the camera will pull in
  automatically (good — no clipping), so 600 is a *max-ish* default that behaves
  indoors.
- Live scroll-zoom + RMB confirmation is the only unverified piece (automation
  can't drive raw input); everything else is verified.

## Verification
Default spawn view captured after login:
`progress/2026-07-05-camera-AFTER-arm600.png` — character small + lower-middle,
citadel + trail + snow dune + horizon mountains + lots of sky visible, world
dominates, camera behind & slightly above, still third-person (not FP, not
top-down). Before (arm 300) for contrast:
`progress/2026-07-05-camera-BEFORE-arm300.png`.

## Success criteria
Default view starts farther out ✓ · character lower on screen ✓ · more
environment/vista ✓ · RMB preserved (untouched, needs live confirm) ~ · wheel
zoom preserved (untouched, needs live confirm) ~ · no UI/HUD changes ✓ · no
world art changes ✓.

Related: [[slice-review-composition-2026-07-05]].
