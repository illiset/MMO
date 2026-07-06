# Camera system tuning pass — the real blocker (2026-07-06)

## Headline
The reason "just change the SpringArm" doesn't work is now proven with a live
runtime number: **the kit's WoW-style camera overrides the SpringArm's
`TargetArmLength` at runtime and holds the default zoom at a hardcoded 400**,
inside the `BP_WowStyleCameraComponent` Blueprint **graph** — which cannot be
read or edited through headless Python tooling. So distance/zoom-range tuning
is a Blueprint-graph edit, not a property tweak.

## How this was proven
Added a temporary runtime probe (our subsystem, since removed) logging the live
camera boom each second:
```
[TRCamProbe] arm=200 -> 400 (settles), socketZ=70, targetZ=0, collision=1
```
I authored `TargetArmLength = 1200`; runtime read back **400**. Controlled A/B
(arm 600 vs 1200 with identical offsets) showed no "farther = smaller" — the
authored arm is ignored for distance. The reframe that looked "pulled back"
last turn was the `socket_offset` lowering the character, not real distance.

## Report (8 items)

**1. Exact system controlling the default view.** `BP_PlayerCharacter` →
`SpringArmComponent` ("camera boom") + child `CameraComponent`. But the **zoom
distance is driven by `BP_WowStyleCameraComponent`'s event graph**, which sets
the boom's arm length at runtime (ramps 200→400 on spawn), overriding the
authored value. `BP_BaseCameraComponent`/`BP_PlayerController` expose no camera
variables. The zoom min/max/step are graph literals — not properties.

**2. Old values (authored, on the boom).** `TargetArmLength=300` (pre-work),
`SocketOffset=(0,0,0)`, `TargetOffset=0`, `DoCollisionTest=true`,
`ProbeSize=12`, `ProbeChannel=ECC_Camera`, camera lag off,
`UsePawnControlRotation=true`; `CameraComponent FOV=95`.

**3. New values (this session, clean state).** `TargetArmLength=600` (authored;
**overridden at runtime → has no effect on distance**), `SocketOffset=(0,0,70)`
(**respected** → character sits lower), `TargetOffset=0`, FOV back to `95`.
Verified at runtime: **socket offset, target offset, FOV, and collision ARE
respected** — only the arm length (distance) is graph-overridden.

**4. Min / default / max zoom behavior.** **Default = 400** (graph constant, not
the authored 600). Min/max/step live as literals inside the WowStyle graph and
are not exposed as properties, so they can't be read/changed headlessly. Scroll
still adjusts within that graph range.

**5. Is zoom distance saved or reset?** Reset — on spawn the graph ramps the arm
to its own 400 default regardless of the authored value; it is not persisted
from the authored SpringArm setting.

**6. Is collision active and how does it behave?** Active — `DoCollisionTest=
true` on `ECC_Camera`, `ProbeSize=12`. In the open snowfield captures it never
collapsed the camera (no constant shove-in); it only pulls in when geometry is
actually behind the character. Behavior looks correct.

**7. Does RMB turning still work?** Not changed and not breakable by these edits
(`UsePawnControlRotation` untouched). Couldn't live-demo it — raw mouse input
can't be injected from the sandbox — so a hands-on RMB check is still needed.

**8. Tweak guide.**
- **too high / too low on screen** → `SpringArm.SocketOffset.Z` (up = character
  lower; down = higher). *Works today, no graph needed.*
- **more world / character smaller** → `CameraComponent.FOV` (raise toward
  100–110). *Works today.* (Tested 95→100; subtle. Real "smaller" wants
  distance, which is graph-locked.)
- **too close / too far / zoom range / scroll speed / too top-down** → require
  editing `BP_WowStyleCameraComponent`'s graph: the default (400), the min/max
  clamp, and the scroll step. **Graph edit — GUI or the project's UnrealMCP
  plugin.**
- **collision too aggressive** → lower `ProbeSize`, or raise `SocketOffset.Z`
  so the boom rides higher above slopes. *Works today.*

## Recommended next step (needs your go-ahead)
To get a real pulled-back default (700–900) + generous zoom range (e.g.
150–1600) + tunable step, the `BP_WowStyleCameraComponent` graph must be edited:
change the default-zoom constant, the min/max clamp, and the scroll step, and
ideally promote them to named variables (`DefaultZoomDistance`, `MinZoom`,
`MaxZoom`, `ZoomStep`) so future tuning is a property change, not graph surgery.
This project ships an **UnrealMCP plugin** (Blueprint graph automation) that
could do this programmatically; alternatively a short GUI Blueprint session.
Both touch the zoom logic you asked me not to break, so I want your explicit OK
(and which route) before editing that graph.

Captures: `progress/2026-07-06-camera-runtime-arm400.png` (arm authored 1200 →
runtime 400), `…-fov100.png` (FOV lever).

Related: [[camera-framing-2026-07-05]].
