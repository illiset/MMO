# Unit-frame UI asset contract — painted art in, Fable wires it

Written 2026-07-04. Workflow per GPT 5.6 + Daniel: image generation produces
the art language; Claude/Fable only places and binds it. The HUD already
loads every visual from `RawArt/ui/*.png` at runtime — drop files in
`C:\dev\art-drop\ui\` with these EXACT filenames, tell Claude, and they're
live in one restart. No code changes needed for a texture swap.

## Rules for EVERY asset (violating these makes them unusable in UMG)

- PNG with real transparency (alpha channel), straight-on orthographic view.
- **NO text, letters, numbers, names, or bar values anywhere** — the engine
  renders all text live.
- **No baked partial fills** — bars are delivered 100% full; the engine crops
  them to the live percentage.
- Match the game's gold: warm aged bronze/gold (#C9A55C family), dark iron,
  charcoal — the same chemistry as the login screen.
- Crisp at 100% scale; no photo noise, no watermark.

## The 12 assets

1. **UF_PlateLarge.png** — 512×256. Player/target panel: charcoal plate,
   aged-bronze ornate border with corner details, subtle inner shadow.
   9-SLICE CONSTRAINT: all ornament within 48px of the edges; the CENTER
   must be plain gradient (it stretches). No center medallions/emblems.
2. **UF_PlateSmall.png** — 256×128. Same family, simpler trim; ornament
   within 24px of edges.
3. **UF_PlateRaid.png** — 256×96. Minimal version; trim within 16px.
4. **UF_PortraitRing.png** — 512×512. Ornate circular portrait frame,
   riveted/engraved bronze, ring band 8–12% of diameter. CENTER HOLE FULLY
   TRANSPARENT (portrait renders behind it), outside the ring transparent,
   perfectly centered.
5. **UF_LevelRoundel.png** — 256×256. Small circular badge matching the
   ring; SOLID dark center (engine draws the number on top).
6. **UF_BarTrough.png** — 512×64. Empty bar: near-black inset trough,
   1px dark metal frame, subtle top inner shadow. Ends within 12px (sliced).
7. **UF_BarFill_Green.png** — 512×64. Rich saturated green fill, glossy top
   sheen, subtle bevel, filled edge to edge. Reference: Option-1 health bar.
8. **UF_BarFill_Blue.png** — 512×64. Deep royal blue, same treatment.
9. **UF_BarFill_Gold.png** — 512×64. Rich gold/amber, same treatment.
10. **UF_BuffSlot.png** — 128×128. Square icon socket: dark inset, thin
    bronze frame (ability icon renders inside; duration text is engine-drawn).
11. **UF_TargetAccent.png** — 512×64. Thin horizontal ornament strip in
    NEUTRAL WHITE/GRAY (engine tints it red/gold/green per disposition).
12. **Portrait_Test.png** — 512×512. ONE painted bust portrait to prove the
    pipeline: rugged Celtic warrior, head slightly angled, dark background,
    face centered in the middle 60% (it gets circle-cropped by the ring).

## Per-asset generation prompt skeleton

"game UI asset on transparent background, dark fantasy MMORPG style, aged
bronze and dark iron with warm gold accents (#C9A55C), [ASSET DESCRIPTION
FROM ABOVE], orthographic straight-on view, crisp edges, no text, no
letters, no numbers, no watermark, PNG with transparency"

Generate at the largest available size, downscale to the exact dimensions.
If the tool can't do true transparency, generate on solid #FF00FF magenta
and Claude will key it out.

## Fonts (not generatable — separate decision)

Palatino Linotype Bold is the current stand-in. The reference's face is a
Friz-Quadrata-class glyphic serif. Options: license Friz Quadrata (~$35,
Adobe/Monotype), or Claude pulls an OFL free alternative (Cinzel for
titles + Alegreya for names) from Google Fonts. Daniel picks.

## Division of labor (locked)

- GPT 5.6 / image gen: paints the 12 assets above.
- Daniel: drops them in `C:\dev\art-drop\ui\`, says "art's in".
- Claude: keys/crops/imports, wires them into the existing widgets,
  capture-verifies against the Option-1 reference, ships.
