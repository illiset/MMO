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
- [ ] Finish JSON→kit AbilityAsset generator (schema archaeology on
      AbilityAsset_C properties; python bridge already proven)
- [ ] P1 BP wiring: realm select + class-type select in the kit's
      character creation flow (StartLevel widgets) — likely needs some
      GUI Blueprint work; plan a co-driving session or careful python
- [ ] P4 runtime: implement The Accolade quest in kit quest/NPC systems
- [ ] P5: classic UI reskin of kit widgets (dark + gold pass)
- [ ] Git LFS + private GitHub remote for MMOKitEval
- [ ] Port classic-MMO controls (design/controls.md) onto kit player BP
- [ ] Skill tree UI panel (classic talent layout) reading our skill JSON
- [ ] Daniel review: 21 draft class trees in data/skills/great-north/
      (slice four are authored; rest need his eye eventually, no rush)

## Open questions for Daniel (answer whenever)
- Keep "Aldric" as your GM character name or pick your real main's name?
- MMO Kit's stat set differs from our 16-stat system — mapping ours onto
  their character sheet is a design+code task; confirm priority.
