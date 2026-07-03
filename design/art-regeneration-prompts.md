# Art regeneration prompts — 4K masters + clean scenery plates

Written 2026-07-03. Purpose: raise the source-art ceiling (the #1 visual
blocker). Two deliverables per mock: **(A)** a 4K regeneration of the mock as
STYLE REFERENCE for native UI chrome, and **(B)** a clean NO-UI scenery plate
we actually ship as the backdrop (all chrome is drawn natively in-engine).
The B plates are the load-bearing ones — prioritize them.

## Global specs (apply to every generation)

- **Resolution:** generate at the tool's max, then upscale so the SHORT edge
  is ≥ 2400 px (full-screen plates ≥ 3840×2400). Client runs 1680×1050
  (16:10) — deliver 16:10 for full-screen plates, 2:3 for portrait cards.
- **Format:** PNG, no compression artifacts.
- **Drop folder:** `C:\dev\art-drop` (punchlist wrote "C:\devrt-drop" —
  any folder works, just tell Claude where).
- **CRITICAL negative prompt on EVERY generation** (this is what poisoned
  the current set — 8 of 9 mocks have engine debug text baked into the art):

```
text, words, letters, typography, captions, watermark, signature, logo, user interface, UI, panels, buttons, input fields, health bars, menus, frames, window borders, debug text, screenshot overlay, blurry, soft focus, jpeg artifacts, low resolution, pixelated, oversaturated, deformed hands, extra limbs
```

- **Base style block** (prepend to every prompt below where it says [STYLE]):

```
epic dark-fantasy MMORPG key art, painterly oil rendering with fine visible brushwork, dramatic volumetric lighting, ultra-detailed, razor-sharp focus, cinematic composition, AAA concept-art quality
```

- Composition note for full-screen plates: menu panels sit in the CENTER
  60% of the screen, so put the interesting silhouettes and light sources in
  the outer thirds and keep the center readable but not busy.

---

## B-PLATES — clean scenery (ship these; highest priority)

### B1 — Great North night-siege plate (backs Choose Path / Choose People / GN Name screens; replaces backdrops of f0cff90e, a4efba48, 5e77ac2d)
```
[STYLE], moonlit frozen battlefield before a gothic ice citadel, armored knight seen from behind at far left edge gazing at distant spires, tattered midnight-blue war banners with a silver lion on tall poles framing left and right edges, falling snow, cold blue-steel palette with faint warm campfire embers low in the frame, dark storm clouds with moon glow, empty dark center for interface readability, no people in center frame --ar 16:10
```

### B2 — Mystic Lands golden-terrace plate (backs ML Race / ML Name; replaces backdrops of e7ce2c7f, 1d81c051)
```
[STYLE], golden desert-jewel city of domes and minarets built into terraced cliffs with waterfalls, hanging gardens and palms, robed guardian with ornate staff at far left edge, tall indigo silk banners with gold embroidered eye sigil framing left and right edges, warm amber sunset light, birds circling distant domes, empty darker center for interface readability --ar 16:10
```

### B3 — Honorguard ember-fortress plate (backs HG Race / HG Name; replaces backdrops of 77424456, 0733b487)
```
[STYLE], colossal dark stone crusader fortress under ember-red storm clouds, ranks of knights with tower shields and crimson cloaks lining a torchlit processional avenue at the left and right edges seen from behind, tall blood-red banners with gold lion and sword-cross sigils, floating embers and torch flame, deep crimson and black-iron palette, empty dark center for interface readability --ar 16:10
```

### B4 — Realm-select stage plate (replaces backdrop of b591c31d)
```
[STYLE], vast dark ceremonial stone terrace at night viewed straight-on, weathered flagstone floor in foreground, sky split into three subtle weather fronts: icy blue blizzard glow at left, warm golden sunset break in the center, ember-red storm at right, faint distant silhouettes of three different castles one under each sky, very dark restrained composition, empty center for interface readability --ar 16:10
```

### B5 — Login triptych plate, no UI, no text (replaces d27e7ebd backdrop)
```
[STYLE], three vertical painted panels separated by thin ornate gold pillar dividers: LEFT panel a frost-blue gothic ice citadel on a cliff with two fur-clad warriors at a campfire; CENTER panel a radiant golden city of domes, bridges and waterfalls in a green valley under parting storm clouds; RIGHT panel a black-iron fortress city under ember-red skies with crimson banners and armored sentinels; unified horizon line across all three panels, no lettering anywhere --ar 16:10
```

### B6/B7/B8 — Portrait key-art cards (for realm-select cards + future loading screens), one per realm
```
B6: [STYLE], towering gothic ice citadel on a jagged cliff over a frozen fjord, aurora and moonlight, lone armored sentinel with spear on a snow ledge in foreground, midnight-blue banner with silver lion, frost-blue palette --ar 2:3

B7: [STYLE], golden domed palace city rising from terraced desert cliffs with waterfalls and hanging gardens, amber sunset, robed pilgrim on a bridge in foreground, indigo-and-gold banners, warm golden palette --ar 2:3

B8: [STYLE], black-iron crusader fortress city with a thousand torchlit windows under ember storm clouds, crimson banners with gold lion, armored honor guard with tower shield in foreground, deep red and iron palette --ar 2:3
```

---

## A-REGENS — 4K mock regenerations (style reference for native chrome)

Same composition as the existing mocks, WITHOUT the debug line, at 4K. Use
image-to-image on the existing file at low-medium strength if the tool
supports it, plus the negative prompt above. One per mock:

- **A1 (d27e7ebd login):** img2img the login mock; prompt = B5 text + `, ornate dark parchment login panel with gold filigree frame in lower center` — keep title lockup OUT (native).
- **A2 (b591c31d realm select):** img2img; prompt = B4 + `, three tall ornate gold-framed painted realm cards centered`.
- **A3 (f0cff90e path):** img2img; prompt = B1 + `, large dark stone panel with gold compass-rose crest and four horizontal ornate option bars`.
- **A4 (a4efba48 people GN):** img2img; prompt = B1 + `, large dark stone panel with gold frame and grouped list rows`.
- **A5 (5e77ac2d name GN):** img2img; prompt = B1 + `, dark stone panel with gold frame, single ornate input field and two ornate buttons`.
- **A6 (0733b487 name HG):** img2img; prompt = B3 + same panel suffix as A5.
- **A7 (e7ce2c7f race ML):** img2img; prompt = B2 + same panel suffix as A4.
- **A8 (77424456 race HG):** img2img; prompt = B3 + same panel suffix as A4.
- **A9 (1d81c051 name ML):** img2img; prompt = B2 + same panel suffix as A5.

---

## ORNAMENT KIT — unlocks crisp native chrome (high value, cheap)

These let Claude build zero-pixelation UI at any resolution:

### O1 — Gold filigree frame kit
```
ornate antique gold filigree UI ornament sheet on pure black background, arranged in a grid: four corner flourishes, straight border segments, diamond stud gems in sapphire blue and ruby red and topaz gold, small compass-rose medallion, horizontal divider scrollwork with center diamond, symmetrical, engraved metal texture, razor sharp, no text --ar 1:1
```

### O2 — Title compass crest (login title backing, replaces baked title art)
```
massive ornate gold compass-rose war crest with crossed spears and laurel detail, engraved dark bronze center disc, on pure black background, centered, symmetrical, jewelry-grade detail, razor sharp, no text --ar 1:1
```

### O3 — Realm sigils (one generation each, pure emblem)
```
GN: heraldic silver eight-pointed frost star sigil, engraved metal, on pure black background, centered, symmetrical, razor sharp, no text --ar 1:1
ML: heraldic gold tree-of-life sigil inside a thin gold shield outline, engraved metal, on pure black background, centered, razor sharp, no text --ar 1:1
HG: heraldic gold rampant lion sigil inside a thin gold shield outline, engraved metal, on pure black background, centered, razor sharp, no text --ar 1:1
```

### O4 — Button plate states (hover/press polish)
```
ornate fantasy UI button plate set on pure black background, three identical long horizontal plates stacked vertically: brushed dark iron with thin gold trim, same plate glowing warm gold, same plate pressed darker with inner shadow, engraved corner details, razor sharp, no text --ar 4:3
```

---

## Order of value (if time is short)

1. **B1** (unblocks three GN screens at once) → 2. **B5** (login) →
3. **O1+O4** (native chrome everywhere) → 4. B2, B3 → 5. B4, B6–B8 →
6. O2, O3 → 7. A-regens (nice-to-have references).

## O5 — SKILL ICON BATCH (action bar; requested 2026-07-03)

One generation per SKILL KIND first (10 icons unlock the whole bar); per-skill
uniques come later. Square 1:1, generate large, deliver ≥512px each, PNG,
drop in C:\dev\MMOKitEval\RawArt\icons\ named kind_<kind>.png
(kind_strike, kind_dd, kind_dot, kind_heal, kind_hot, kind_buff, kind_debuff,
kind_cc, kind_taunt, kind_utility).

Base prompt for every icon:
```
fantasy MMORPG spell icon, painted in the style of classic WoW ability icons,
rich saturated color on a dark vignetted background, thin dark inner border,
razor sharp, centered single subject, no text --ar 1:1
```
Subjects per kind:
- strike: crossed sword slash with white impact arc
- dd: hurled fireball with trailing sparks
- dot: green poison droplet over cracked skull
- heal: radiant golden holy light burst
- hot: soft green regrowth leaves with light motes
- buff: upward golden shield glow on a raised gauntlet
- debuff: purple downward-spiral curse mark
- cc: ice-blue shackles/frozen chains
- taunt: roaring horned war-horn
- utility: swirling arcane compass rune
