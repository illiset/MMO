# THREE REALMS — MORNING RUN PROMPT (paste whole thing into a fresh chat)

Read your memory files and `three-realms/design/` (punchlist, decisions-log,
this file) BEFORE your first action. Everything below is binding.

## THE GAME
Three Realms: a DAoC spiritual successor with WoW's leveling soul. Three
realms — Great North (ice/iron), Mystic Lands (magic/wonder), Honorguard
(valor/honor). PvE-FIRST: WoW-style quest-hub leveling, dungeons, raid
endgame. PvP lives ONLY in DAoC-style three-realm frontier warfare — keeps,
relics, realm points — never forced on levelers. One account = one realm per
server (realm lock; locked accounts SKIP realm select). You pick a PATH
(Frontline/Healer/Support/Damage) at creation; your TRUE class is EARNED at
level 10 via quest (The Accolade: frontline→Knight is written). 20 skills
per class; classes and race×class matrix come ONLY from MMOStats.xlsx via
tools/extract_from_xlsx.py — the spreadsheet is canon, never invent lore.
$15/mo, zero microtransactions. Classic WoW/DAoC feel: WoW-style camera
(F7 mode) BY DEFAULT in third person, auto-attack does NOT move the
character, RMB+LMB walks forward, numlock autoruns, shift = run. PoE-style
inventory (I) and character sheet (C) reskinned to Three Realms art.
Stamina bar beside health/mana. XP bar: bottom edge, 20 segments of 5%.

## HARD RULES (Daniel's, non-negotiable, learned the hard way)
1. VERIFY-BEFORE-SHOW: capture the actual window (scratchpad capture_game.ps1
   pattern; PrintWindow flag 2) and LOOK at it before telling Daniel anything
   is done. Never ask him to check something you haven't seen.
2. ANSWER FIRST: when he asks a question, answer it directly before resuming.
3. STALE-BINARY DISCIPLINE: he tests fast. Before inviting him to test, state
   which git commit is live in the running client; kill+relaunch stale ones.
4. NO MMOKIT LOOK ANYWHERE: kit chat box, controls legend, gray health bar,
   default fonts/panels are all banned sights. Runtime widget-sweep patch in
   TRUIWorldSubsystem handles name/legend/chat — verify it fires; finish the
   job in kit Blueprints via the UnrealMCP hook (plugin listens on 55557 when
   an editor is open; speak raw JSON to the socket if the MCP relay is down).
5. ART: Daniel's generated art = the visual bible. Files live in
   `three-realms/design/*.png`. Art is SCENERY; all UI chrome must be crisp
   NATIVE widgets (code-drawn or synthetic hi-res textures) — never rely on
   baked-in painted UI, never stretch art (extend with art or match aspect).
   If quality is capped by source resolution SAY SO and give him the exact
   regeneration ask (he'll make 4K/outpainted versions on request).
6. Serif typography everywhere in the start flow (Georgia interim).
7. Back button on every screen. Readable fields. "EARN YOUR DESTINY" login,
   "CREATE ACCOUNT", remember-my-login. Server: "Three Realms Dev GN".
   Status text ("Entering world...") = gold, readable, never over other text.
   Zero engine debug text on screen, ever.
8. Commit+push after each piece (repos: ThreeRealmsKit=C:\dev\MMOKitEval,
   ThreeRealmsPersistence=C:\dev\MMOKitPersistence, MMO=three-realms design).
   Log decisions in design/decisions-log.md. Blocked >20min → punchlist, move on.
9. Kill ALL UnrealEditor/UnrealEditor-Cmd before builds (DLL locks). Launch UE
   via PowerShell only (Git Bash mangles /Game/ paths). World server port 7779
   is UDP — check readiness via "Bringing World" in MMOKitEval.log, never TCP.
   Asset creation/imports crash in -run=pythonscript; use full editor
   -ExecCmds="py ..." + quit_editor(). Editor screenshots need a visible
   (non-minimized) window.
10. He's granted computer control (computer-use MCP: request UnrealEditor.exe
    by exact basename). Never take the screen without need; captures preferred.

## STACK FACTS
Persistence: C:\dev\MMOKitPersistence\bin\Debug-Sqlite\net8.0\PersistenceServer.exe
(hidden, TCP 3457, SQLite mmokit.db — characters table has realm/classtype/race
columns; Stats.rpgClass must stay "Undefined" for kit compatibility).
World server: UnrealEditor-Cmd.exe <proj> /Game/ThreeRealms/Zones/GN/GN_Frostmarch
-server -unattended -log (minimized). Client: UnrealEditor.exe <proj>
/Game/ThreeRealms/Maps/TRStartMap -game -windowed -ResX=1680 -ResY=1050.
Accounts: Dev1 = Daniel (remember-me saved). Character: Celtictest
(great-north/frontline/celtic). Kit valid appearances: Human/Mannequin/DarkMinion.
UE 5.7.4 ONLY (never 5.8). Data pipeline: xlsx → data/*.json →
tools/sync_data_to_engine.py → Content/Data.

## KNOWN OPEN BUGS (start here)
- F7 auto-camera injection not landing (kit still spawns first person) —
  find the kit's camera-mode var on the pawn BP via MCP and set it directly.
- "REFLECTION CAPTURES NEED TO BE REBUILT" overlay: build/delete the capture
  in the maps (editor Build Reflection Captures), not suppressible by flag.
- Frostmarch props: verify every mesh stands upright in an editor capture
  (some pines read sideways); terrain is placeholder-smooth — needs real
  displacement detail + material work.
- Widget-sweep HUD patch (name/legend/chat): confirm it fires in a CONNECTED
  session (health bar must read "Celtictest").
- Action bar: keybinds must trigger kit abilities; slots need drag/reorder
  eventually; icons interim — request his generator batch for real ones.

## TODAY'S ORDER
1. Bring up stack, verify login screen by capture, fix anything visibly off
   BEFORE inviting Daniel in.
2. Kill the open bugs above, capture-verified one by one.
3. Finish EVERY start screen — and understand the bar: TONIGHT'S LOGIN IS THE
   FLOOR, NOT THE TARGET. Target = modern AAA login (WoW / Diablo IV class):
   zero visible pixelation at native window size, zero smudge/ghost regions in
   the art, consistent spacing/margins, professional type hierarchy, polished
   ornament, satisfying hover/press on everything. FIRST ACTION of the session:
   hand Daniel the exact art-generator prompts for 4K regenerations of every
   mock (plus clean no-UI variants) so he can produce them while you work —
   the source-art ceiling is the #1 blocker to this bar and only he can raise
   it. Rebuild the login itself to the higher bar once new art lands.
4. World beauty era: his Fab packs (Mountain Tops, Caves and Dungeons,
   Abandoned Cathedral — ask him to Add To Project in the Epic launcher, then
   dress Frostmarch with real meshes), lighting pass, snow material.
5. Combat loop: spawn kit minions in Frostmarch, hotbar abilities hitting
   them, XP flow; then The Accolade quest playable start-to-finish.
6. Use subagents for parallel tracks (UI / world / combat) when useful; write
   design/progress reports with proof captures as you go.

Quality bar: nothing reaches Daniel's eyes that you haven't seen in a capture
and would defend as SHIPPABLE IN A COMMERCIAL GAME. "Better than yesterday"
is not the bar; "a stranger would believe this is a real MMO" is. When in
doubt about look/feel: DAoC 2001 dignity + WoW 2004 clarity + Diablo IV
polish, painted in his gold. If you cannot reach that bar with current
assets, say exactly why and exactly what asset unlocks it — never ship a
workaround and call it done.
