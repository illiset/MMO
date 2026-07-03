# 2026-07-03 morning — TWO SESSIONS DETECTED, coordination + verified state

Written by the NEW morning session (started ~10:00 AM from Daniel's pasted
run-prompt). All claims below are capture- or log-verified this session.

## The situation (needs Daniel's call)

Two Claude sessions are live on the same stack:

- **Session A** ("Three Realms project rules and setup", running since early
  morning): started the servers at 9:56, wrote design/art-regeneration-
  prompts.md, committed 5e2d405 (backdrop inpaint) at ~10:10, and is doing
  in-world debugging as Celtictest right now (joins at 10:13 and 10:42).
- **Session B** (this one): Daniel pasted the morning run-prompt at ~10:00
  ("Begin. Verify everything."). Independently cleaned the login backdrop
  (superseded by A's 5e2d405 — no loss), killed A's client once (didn't know
  A existed yet), relaunched its own, then detected the race via A's commit.

Session B messaged Session A at ~10:15 proposing A stand down; B has done
READ-ONLY work since. **Daniel: kill one session.** Two agents cannot share
this stack (process kills, DLL-locked builds, PNG overwrites, git races).

## Capture-verified state (Session B's own eyes)

- **Login screen: GOOD.** Captured live at 10:12 (commit 668b001 client +
  5e2d405 art): crisp native title, clean scrims where the baked title/panel
  ghosts were, single footer, no debug text. Shippable as interim; real bar
  needs Daniel's 4K art (see art-regeneration-prompts.md).
- **Server-select screen: was BAD at 10:00** (smears + doubled footer) —
  backdrop fix should cover it; NOT re-verified since 5e2d405. Re-capture.

## Log-verified findings (fresh, this morning)

1. **Pawn possession is STILL BROKEN in a connected session.** Client
   MMOKitEval_3.log: joined GN_Frostmarch 10:13:37, KitHud assets loaded
   (subsystem bootstrap ran), but the [TRCamera] pawn dump — which fires
   2s after GetPawn() is non-null — NEVER appeared in 24 min in-world.
   F7 camera fix is downstream of this; fix possession first.
2. **ConnectionTimeout at 10:37:40**: the world server dropped the client
   ("Elapsed: 14.34" — client hitched >14s, likely heavyweight tooling on
   the client side). Client auto-bounced to TRStartMap "?closed".
3. **Creation-flow backdrops still carry full baked UI** (panels, buttons,
   AND non-canon invented race names: "Sunborn", "Dawnkin", "Veilborn",
   "Ashen", "Lionguard", "Ironbound" — NOT in MMOStats.xlsx). 5e2d405 only
   removed debug text + footers from them. These screens will read as
   double-UI over wrong lore until scrimmed or replaced by Daniel's B1-B3
   plates.
4. **Action bar is display-only**: TRActionBarWidget is HitTestInvisible,
   TriggerSlot() has no caller — keys 1-0 are not bound. The "keybinds
   trigger kit abilities" bug is real work, not a regression.
5. **Widget-sweep HUD patch ran but is UNVERIFIED visually** (no capture of
   a connected session exists from either session yet this morning).

## Ready-to-apply next steps (whoever owns the stack)

- Possession — NARROWED (10:50): the whole spawn path is
  APlayerControllerCpp::CustomPlayerStart(), a BlueprintImplementableEvent
  implemented in kit BP_PlayerController (plugin source readable at
  C:\Program Files\Epic Games\UE_5.7\Engine\Plugins\Marketplace\
  MMOKitCo078f5105de88V7\Source\MMOKitCode). GameModeBaseCpp aborts loudly
  on failure (AbortPlayerStart destroys the controller) — but our client
  stayed connected 24 min with no pawn and no error, so the BP is STALLING,
  not failing. Prime suspect: our persistence fork repurposed RPC slots
  11 (SetEmail) / 12 / 13 (realm-classtype-race meta) — if the kit BP spawn
  path calls one of those slots expecting stock kit semantics, it hangs
  waiting on a reply shape that never comes. Action: diff the fork's RPC
  table against upstream MMOKitPersistence for slots the kit BPs consume,
  and/or open the editor + UnrealMCP (port 55557) and trace
  BP_PlayerController::CustomPlayerStart.
- Action bar keybinds: bind 1-0 in TRUIWorldSubsystem::Tick next to the K
  bind; route TriggerSlot -> kit ability activation (kit exposes abilities
  on the pawn; enumerate via reflection like the [TRCamera] dump does).
- Server-select + create-account + charselect screens: re-capture against
  5e2d405 art; expect clean, but verify before telling Daniel anything.
