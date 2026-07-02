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

## UI windows — decided 2026-07-01

- **I — Inventory & equipment, PoE1/2 style**: paper-doll equipment slots
  (main hand, off hand, head, chest, gloves, boots, belt, amulet, 2 rings)
  plus a grid bag where items occupy width×height cells (longsword = 1×4).
  Drag-and-drop when loot variety demands it; click-to-equip v1.
- **C — Character sheet**: name/class/faction/level, vitals, the 16 design
  stats grouped by category, equipment summary.

## Implementation notes (Phase 2)

- Enhanced Input: contexts for "world" vs "UI focus"; rebindable from day
  one (data-driven input config, not hardcoded keys).
- Server-authoritative movement via CharacterMovementComponent defaults;
  tab-target = server-validated target handle, not client raycasts.
