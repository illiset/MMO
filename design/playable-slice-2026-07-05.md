# Clean playable Frostmarch slice — result (2026-07-05)

**GN_Frostmarch untouched** (git confirms clean). Abandoned the contaminated
MW-example lookdev; built a fresh slice from a GN_Frostmarch duplicate.

## Headline
The CORE goal is achieved: a clean map that runs in **normal MMO gameplay
mode with the full HUD and a possessed character** — the thing the
example-derived lookdev could never do. What's NOT done: a polished, framed
hero composition — the citadel/trees are placed but spread across GN's big
smooth terrain and don't compose into a vista from the fixed spawn. That
part needs an interactive art pass.

## Deliverables (10 requested)

1. **From scratch or duplicate?** Safe **duplicate of GN_Frostmarch** (via
   new_map_from_template + save_map), NOT the MW example. Verified a test edit
   persists (spawn→save→reload→still there) — the example map's non-persistence
   bug is gone.
2. **Exact path:** `/Game/ThreeRealms/_Dev/Playable_FrostmarchSlice`.
3. **GameMode / PC / Pawn / HUD:** inherits GN's `BP_GameMode_C` →
   `BP_PlayerController` → `BP_PlayerCharacter` (third-person WoW cam) → kit
   HUD + our TR HUD suite. World Partition **disabled** (normal map).
4. **HUD in PIE?** **YES** — `progress/2026-07-05-slice-gameplay-hud.png`
   shows the full HUD live (Celtictest player frame, party Mira/Elowen, target
   Training Dummy, raid frames, chat, action bar) on snowy terrain.
5. **Spawns as normal third-person character?** Yes — Celtictest possessed via
   BP_GameMode (player frame reads Celtictest 200/200). Validated by hosting
   the slice on the world server + auto-entering (persistence + login flow).
6. **Fly/DefaultPawn gone?** Yes — this uses the kit's real gameplay path, not
   GameModeBase/DefaultPawn. (The old lookdev's fly-mode is not present here.)
7. **Assets used:**
   - Iceland_Environment: `SM_Mountain_01–06` (framing, pushed to ~60–90 km).
   - Abandoned_Cathedral: `SM_tower_5/1/3` (citadel landmark, ~140 m N of spawn).
   - Stylized_Tree_Pack: Spruce_01–05 + Cathedral Dead_Tree_01–03 (winter
     forest — deliberately NO bright-green pines).
   - MWLandscapeAutoMaterial: snow ground textures → new `M_FrostmarchSnow`
     surface material on the terrain.
8. **Objects removed / avoided:** stripped **807** placeholder graybox props
   (GN's OBJ pines/rocks/cabins/keep/walls). No cine cameras, color checkers,
   preview spheres, or text labels (a GN duplicate never had them). One known
   artifact: a trail-marker stone (`SM_Iceland_Crest`, scale 0.05) whose
   ground-trace failed and floated to Z≈30 k — cosmetically negligible, trivial
   to delete; it's the "floor under spawn" the probe reported.
9. **Clean enough to be the GN_Frostmarch recipe?** **The PIPELINE yes, the
   ART no yet.** Proven recipe: GN-duplicate base (correct gameplay, persists) +
   strip graybox + snow surface material + grounded Iceland mountains +
   Cathedral citadel + winter spruces + cold light. But the terrain is GN's
   large smooth static mesh, so the composition doesn't frame into a tight
   150 m camp vista — that needs a sculpted Landscape and by-eye placement.
10. **What still looks weak:**
    - No framed vista from spawn — citadel/trees spread over a big smooth
      terrain and occlude; the in-game camera (fixed character spawn) can't
      pose to frame them, so the gameplay hero shot shows terrain/sky, not a
      composed landmark view.
    - Terrain is a static mesh with a flat-ish snow material, not a sculpted
      Landscape with the MW auto-material (that needs interactive Landscape
      creation — headless landscape creation is unreliable).
    - One floating trail stone (see #8).
    - Mood still on the warm side (no cold color-grade yet — same interactive
      need as the lookdev).

## Captures
- `progress/2026-07-05-slice-gameplay-hud.png` — **the key proof**: gameplay
  mode + full HUD + snow + Celtictest in-world.
- `progress/2026-07-05-slice-editor-view.png` — editor viewport: snowy slice,
  "World Partition disabled", 73 actors, clean (no demo junk).

## Recommendation
The slice is a valid CLEAN PLAYABLE base (correct gameplay/HUD, persists, no
junk) — a real improvement over the contaminated lookdev. But it is NOT a
finished hero-shot slice: the vista composition + sculpted snow Landscape +
cold grade are interactive art work. Recommend a co-driving editor session to
(a) sculpt/replace the terrain into a real Landscape with the MW auto-material,
(b) compose the citadel + winter forest into a framed camp vista, (c) apply the
cold grade — all with live feedback, then this becomes the true GN_Frostmarch
recipe. Do NOT touch GN_Frostmarch until that's approved.
Related: [[lookdev-polish-2026-07-05]], [[asset-scan-2026-07-05]].
