# Controls — official standard (updated 2026-07-07)

**Classic WoW/DAoC MMO controls. Not action combat.** Daniel's call, locked.
This file is the authoritative control/keybind spec (supersedes the
2026-07-01 draft; deltas noted at the bottom).

---

## PHASE 0A — CORE MMO CONTROLS (official standard, 2026-07-07)

**Status: specification only — NOT yet implemented/verified except where
marked "already works." Preserve existing working controls; do not rebuild
them unless a task explicitly says so.**

### Movement
| Key | Action |
|---|---|
| W | move forward |
| A | **turn** left (not strafe by default) |
| S | move backward |
| D | **turn** right (not strafe by default) |
| Q | strafe left |
| E | strafe right |
| Space | jump |
| C | toggle crouch |
| X | sit |
| F | interact (confirmed 2026-07-07) |
| Num Lock | auto-run toggle |

### Mouse
| Input | Action | Status |
|---|---|---|
| LMB hold | look without moving | **already works** |
| RMB hold | camera/look control (mouse-look) | **already works** |
| RMB + LMB hold | look and move forward | **already works** |
| Mouse wheel | camera zoom | **already works** |

### Targeting / Combat
- **Tab** = basic MMO target cycling
- Clear-target behavior (drop current target)
- Auto-attack behavior
- **Main action bar: 12 slots, old-school MMORPG style**, hotkeys
  `1 2 3 4 5 6 7 8 9 0 - =`

### Panel hotkeys
| Key | Panel |
|---|---|
| U | progression / reputation |
| I | inventory |
| B | inventory (alias) |
| O | character stats |
| P | party |
| J | skills |
| K | specialization / spec tree |
| L | quest log |
| M | map |
| N | guild |
| Escape | escape/settings menu |

**Important correction (2026-07-07): C is NOT character. C = crouch.
O = character stats.**

### Chat slash behavior
- `/p ` + Space → input switches to **Party** chat
- `/g ` + Space → input switches to **Guild** chat
- `/1 ` + Space → input switches to **General** chat
- `/w Name ` + Space → input switches to **Whisper** to Name

Expected behavior on recognition:
1. The raw slash command **disappears from the input body** after
   command + space.
2. The chat-mode indicator changes (e.g. `[Party] |`).
3. The input/message color changes to the channel color.
4. The typed message sends to the selected channel.

Example: user types `/p ` → input becomes `[Party] |` in party color; the
text box no longer contains "/p ".

### Preserve (already working — do not rebuild)
- WASD movement
- LMB hold look
- RMB + LMB move-forward
- RMB mouse-look
- Mouse wheel zoom
- Space jump

### Add / verify (not yet implemented)
- A/D turn left/right, not strafe by default (verify current behavior)
- Q/E strafe left/right
- F interact
- Num Lock auto-run toggle
- C toggle crouch
- X sit
- Tab targeting + clear target + auto-attack
- Main action bar hotkeys 1–9, 0, -, = (12 slots)
- All panel hotkeys above (U I B O P J K L M N)
- Chat slash channel-switch behavior above

---

## Why (load-bearing)

The target audience is DAoC/classic-MMO refugees. Familiar controls are
part of the comfort-food promise, and tab-target keeps group PvE about
role coordination (positioning, interrupts, threat) rather than twitch
aim — which also keeps the server-authoritative netcode simpler and
cheaper than action-combat hit registration.

## UI windows — decided 2026-07-01 (hotkeys updated 2026-07-07)

- **I / B — Inventory window, PoE2-style, ONE window (clarified
  2026-07-07)**: not just bags — it shows **what you have equipped** plus
  carried items together, in this vertical order:
  1. **Equipment paper-doll (top)**: main hand + off hand flanking the
     body — head, amulet, chest, belt, gloves, boots, 2 rings. Equipped
     items render their art in-slot (you can see your loadout at a glance).
  2. **Potion row: 5 potion/flask slots** (Daniel likes PoE2's 5-slot row —
     keep it).
  3. **Bag grid (bottom)**: items occupy width×height cells
     (longsword = 1×4). Drag-and-drop when loot variety demands it;
     click-to-equip v1.
  Reference: PoE2 inventory screenshot (2026-07-07) for layout ONLY —
  visual identity must be **Mythic Earth's own** (dark + gold, faction
  flavor), not a PoE clone.
- **O — Character sheet** (moved off C, which is now crouch): name/class/
  faction/level, vitals, the 16 design stats grouped by category,
  equipment summary.

## Implementation notes (Phase 2)

- Enhanced Input: contexts for "world" vs "UI focus"; rebindable from day
  one (data-driven input config, not hardcoded keys).
- Server-authoritative movement via CharacterMovementComponent defaults;
  tab-target = server-validated target handle, not client raycasts.

## Deltas from the 2026-07-01 draft
- **C** was character sheet → now **crouch**; character stats moved to **O**.
- **B** added as inventory alias alongside **I**.
- **X** = sit added.
- Action bar formalized as **12 slots** with `1–9 0 - =`.
- Panel hotkey map (U/P/J/K/L/M/N) formalized.
- Chat slash channel-switch spec formalized.
- Q/E strafe **confirmed kept** (Daniel, 2026-07-07); A/D remain turn, not
  strafe.
- **F = interact** added (Daniel, 2026-07-07).
