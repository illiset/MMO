# Controls — decided 2026-07-01

**Classic WoW/DAoC MMO controls. Not action combat.** Daniel's call, locked.

## The scheme

- **Movement:** WASD (W forward, S backpedal, A/D turn; Q/E strafe).
  Autorun on Num Lock. No dodge-roll, no sprint-stamina bar.
- **Camera:** hold right-mouse = mouselook + character turns with camera;
  hold left-mouse = orbit camera without turning character; mouse wheel
  zoom, full zoom-out for group/raid awareness.
- **Targeting:** tab-target cycle (nearest enemy first), left-click to
  select, target-of-target display. No reticle, no aim requirement.
- **Combat input:** action bars (1–0, shift/ctrl modifiers), abilities fire
  on the current target with range/facing checks. Global cooldown model.
- **UI expectations:** clickable unit frames (party/target), castbars,
  hotbar cooldown sweeps — the vocabulary every MMO player already knows.

## Why (load-bearing)

The target audience is DAoC/classic-MMO refugees. Familiar controls are
part of the comfort-food promise, and tab-target keeps group PvE about
role coordination (positioning, interrupts, threat) rather than twitch
aim — which also keeps the server-authoritative netcode simpler and
cheaper than action-combat hit registration.

## Implementation notes (Phase 2)

- Enhanced Input: contexts for "world" vs "UI focus"; rebindable from day
  one (data-driven input config, not hardcoded keys).
- Server-authoritative movement via CharacterMovementComponent defaults;
  tab-target = server-validated target handle, not client raycasts.
