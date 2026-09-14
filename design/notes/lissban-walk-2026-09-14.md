# Lissban walk, 2026-09-14 morning — Daniel's notes (verbatim in substance) and the fix list

Daniel walked Lissban at 09:05–09:45 after night shifts 3/3b. Verdicts: the cabbage field and the grain field are "good job";
the huts are not. Every item below is a MUST for the next Lissban pass, in this order.

## What he said, item by item
1. **Two gated entrances on opposite sides of Lissban.** "I don't want them to have to walk around the whole thing every
   time. The game's gonna be a little bit grindy, shouldn't be too much of a walking simulator." Both gates operated with
   the action key **F** (toggle open/shut), plus an auto-close after ~30 s.
2. **Hut collision is wrong everywhere.** "This is the collision radius on this hut, I can't get any closer to the one on the
   right let alone go inside." "Better but I can walk through the wall? … also where's the door?" "Can't even fit in this
   door." "Collision on this one is too far and can't go in and it's too low; couldn't fit in if it was more functioning
   even, cause it's too low." → The hidden collider rings are DISPLACED from the visible huts (the Celtic House pivot offset
   again: colliders were built around the pivot, not the bounds centre) and their doorway gap does not coincide with the
   mesh's real door. Fix: build every collider from the mesh's world-space bounds and the ACTUAL door opening found by
   probing the post ring; the door must clear a 2.0 m × 0.9 m capsule; the hall (f_house_071 at 0.62) is too low for the
   door — raise the scale until the door is ≥ 2.1 m or pick the variant whose door is taller; prove every hut with the
   capsule sweep AND an in-game walk in through the visible door.
3. **Ground under every hut must be level, with a wooden floor inside.** "The ground should be level inside and wooden
   floor." "This hut is mostly not aligned with the ground, needs fixed" (a roundhouse buried to its eaves). → Cut a level
   pad per building (terrain), seat by bounds-bottom on the pad, add a plank/board floor mesh inside at pad height.
4. **Water trough underground** in the pen (only a corner showing). Re-seat by bounds; the pen fence has open gaps between
   rail sections (posts with no rails) — close them except the one deliberate 3 m gap; the pen floor should be trodden
   dirt, not grass.
5. **Wheat spills outside its fence** on the right of the grain field. Crops must be clipped to the field polygon (inset
   0.5 m). "I'm okay with it not being perfectly square with the one to the right of it."
6. **The ground is too green for this farm** — every field floor is tilled soil, no grass under crops; check all four.

## The bigger picture he gave in the same session (for the night brief)
- "Before we add MetaHumans I'd like to improve the world still and get at least a few areas in Dál Riata to 85% as good
  as launch. Right now organisation has increased but we're closer to 20%."
- "The fog still looks very ugly and basic."
- "Something about the ground still looks single-A, not triple-A — probably the lack of trees and shrubs, but I don't
  like how perfectly flat the whole thing is, and how overly open it is. Lissban should be mostly flat of course, but the
  terrain isn't boundarying anything like in Durotar."
- "Thicker patches of forest, higher trees; I don't know why all these trees have white trunks — not like the pictures I
  gave; thicker trunks, thicker foliage in branches, more branches. I want canopies. Shanderry Forest NEEDS to be what I've
  visioned."
- "Dál Riata is almost all overcast except some coastal areas; some coastal areas are still overcast. Seasons later."
- God mode: F8 free camera, F9/F10 named places, F7 back over the character (built 2026-09-14 09:45).
7. **Field floors: all dirt, right to the fence.** (Top-down of the cabbage field, 09:55) "This is good, but the inside of it
   needs to be all dirt — a more vivid difference. The colour of the dirt that is there is good, but the green remnants on
   the border aren't aesthetic." → Tilled mask covers the whole enclosure and overshoots the fence line by 0.5 m with a
   HARD edge (no blend); same for the pen. Keep the current dirt colour.
8. **Same for the grain field** (top-down, 09:58): green inside the fence line must go — "only dirt for ground and then the
   plants that are being farmed." **Farm tools** in and around the fields would be good: a plough, hoes/rakes leaning on the
   fence, a hand cart, baskets, a hay pile — whatever the packs have (CelticHouse baskets, Medieval_Megapack tools/carts).
