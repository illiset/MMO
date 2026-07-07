# Backlog — small decisions and polish captured from playtests

## Settings (build when a settings menu exists)
- [ ] Gameplay settings checkbox: "Abilities engage auto-attack" (default ON;
      Daniel likes the behavior but wants it optional — 2026-07-01)

## Design decisions parked
- [ ] Max level: TBD. XP bar (20 segments × 5%) works regardless. Decide when
      the leveling curve gets real numbers.

## Inventory (v1 shipped 2026-07-01, PoE-style; spec clarified 2026-07-07)
- [ ] **One PoE2-style window** (I/B): equipment paper-doll on top showing
      equipped items' art in-slot, **5 potion/flask slot row**, bag grid
      below — Mythic Earth's own visual identity (see controls.md)
- [ ] Drag-and-drop item placement (v1 is click-to-equip/unequip)
- [ ] Make remaining paper-doll slots functional as armor items exist
- [ ] Per-item click handling once bags hold multiple items

## Polish
- [ ] Death animation gets cut short by the 5s respawn — hold the corpse pose
      longer / fade camera
- [ ] HUD atmosphere pass: bars are functional, need faction texture, fonts,
      class-colored accents once visual identity exists
- [ ] Combat debug messages → real scrolling combat log window
