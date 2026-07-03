# Punch list — needs Daniel (or visible-mode session)

## Tonight's visible session (~20 min, the good stuff)
1. Run `C:\dev\StartThreeRealmsServers.bat` (or tell Claude "start the
   servers").
2. Open `C:\dev\MMOKitEval\MMOKitEval.uproject` in UE 5.7, open StartMap,
   press Play: **create an account, log in, create a character, enter the
   world.** Your first real login to Three Realms. Expect MMO Kit's stock
   UI and demo world — realm/class-type customization comes next.
3. Walk around, fight a Paragon minion, open the kit's inventory/loot.
   Verdict notes on: combat feel vs our ThreeRealms build, UI, anything
   that offends the DAoC soul.

## Claude follow-ups (next runs)
- [x] **OUR OWN login/creation screens — SHIPPED** (login, create account
      w/ email, server select, realm select+lock, DAoC creation, char
      select, world travel; gold-rim styling pass done)
      — Three Realms branded, DAoC-style: login -> realm select (3 realms,
      GN playable) -> class type -> race -> name -> loading screen. Build
      as C++ UMG widgets in the kit project driving the kit's C++
      WebSocket login; classic dark+gold skin from the start. Kit's stock
      StartMap UI is NOT acceptable as the player-facing flow.
- [x] JSON→kit AbilityAsset generator DONE (112 assets: slice-four +
      classtype trees; damage logic wired for strike/dd/dot kinds)
- [ ] P1 BP wiring: realm select + class-type select in the kit's
      character creation flow (StartLevel widgets) — likely needs some
      GUI Blueprint work; plan a co-driving session or careful python
- [ ] P4 runtime: implement The Accolade quest in kit quest/NPC systems
- [~] P5: start-flow reskin done; in-world kit widgets (inventory/HUD) still stock
- [ ] Git LFS + private GitHub remote for MMOKitEval AND private remote for the MMOKitPersistence fork
- [ ] Port classic-MMO controls (design/controls.md) onto kit player BP
- [x] Skill tree UI panel SHIPPED (K in world: tabs, tiers, unlock levels,
      cost/cd cards; wired to Frontline/Knight until class identity lands)
- [ ] Daniel review: 21 draft class trees in data/skills/great-north/
      (slice four are authored; rest need his eye eventually, no rush)

## Open questions for Daniel (answer whenever)
- Keep "Aldric" as your GM character name or pick your real main's name?
- MMO Kit's stat set differs from our 16-stat system — mapping ours onto
  their character sheet is a design+code task; confirm priority.

- [ ] Creation flow: SEX choice (currently defaults Male/Human body)
- [ ] Client: merge GetCharacterMeta (RPC 13) into char select; realm lock from columns
- [ ] lfs checkout WBP_HUD after Daniel's session closes

## 2026-07-03 morning session (A)
- [x] MOVEMENT/POSSESSION BUG FIXED (kit ca199b9): kit BP_GameInstance needed
      Cookie+CharId set before travel; persistence-verified spawn chain
- [x] F7/WoW camera verified live: BP_WowStyleCameraComponent active after
      PC->InputKey injection (log-proven)
- [x] Kit chat box collapsed (banned sight); TR chat panel = future work
- [x] Backdrop PNGs de-textified (debug line + footers inpainted, 5e2d405)
- [x] TRStartMap unbuilt reflection capture deleted (overlay source)
- [ ] Pawn fell through Nanite placeholder terrain: Nanite disabled on all
      SM_GN_* (complex collision can't work under Nanite) — verify in-game
- [ ] TR health/unit frame to replace kit green bar (banned default look)
- [ ] Action bar keybinds 1-0 (Session B sketch in coordination doc;
      unblocked now that possession works)
- [ ] Scrim/replace creation-flow backdrops (baked panels + NON-CANON race
      names in art; B1-B3 art regen is the real fix)

## Daniel's playtest notes (2026-07-02, round 2)
- [ ] Login backdrop: triptych realm key-art per his mock (art files ->
      C:\devrt-drop; wire as background textures + realm columns)
- [x] Login button copy -> EARN YOUR DESTINY; tagline updated; epithets added
- [x] Input fields unreadable (too dim) -> dark fields, light text
- [x] BACK button on every screen (server/charselect/realm/creation)
