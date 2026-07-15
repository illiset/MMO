# Decisions log — autonomous run 2026-07-02

Calls made without Daniel, per run authorization. Flag anything to reverse.

1. **Persistence server built from GitHub source** (Debug-Sqlite config,
   .NET 8 on .NET 9 SDK) rather than any prebuilt download — full source
   control over our backend from day one. Runs hidden on port 3457;
   database file: `MMOKitPersistence/bin/Debug-Sqlite/net8.0/mmokit.db`.
2. **World server boot verified via editor-as-server** (`-server` on
   UnrealEditor-Cmd, BasicMap, port 7779) — packaged server builds come
   later; this is the standard kit dev workflow.
3. **P0 verified at the protocol level, not the UI level**: I spoke the
   kit's WebSocket wire format directly (1-byte RPC id + length-prefixed
   strings) to create an account, log in, and create a character. UI login
   is reserved for Daniel's first visible session — on purpose.
4. **First character: "Aldric"** (Celtic Frontline, Great North) — created
   as protocol proof. The kit auto-granted him GM permissions (first
   character in DB). Rename/delete freely; he's a test row.
5. **Skill generator design**: 4 class-type trees (8 skills, levels 1-9) +
   25 class trees (20 skills, levels 10+). Slice four hand-authored;
   the other 21 classes generated from archetype templates with flavor
   prefixes, all marked `"status": "draft"` for Daniel's review pass.
   Tier N of a class tree unlocks at level 8+2N (levels 10-22 spread).
6. **Class-quest prototype shape**: quests.json with typed steps
   (talk/kill/return) and a rewards block that grants class + tree + title.
   "The Accolade" (Frontline→Knight) is the template.
7. **MMOKitEval is now the primary engine project** (git-initialized
   locally, 998 files; NO GitHub remote yet — needs Git LFS for the asset
   weight, punch-listed). ProjectName rebranded to "Three Realms (working
   title)" with CodeSpartan attribution retained.
8. **PythonScriptPlugin enabled** in the kit project — headless editor
   Python verified working (schema dump ran). This is the bridge for
   generating kit data assets from our JSON.
9. Kit uses **Paragon minion assets** as demo mobs — placeholder question
   resolved by the kit itself; consistent with our _DevPlaceholder policy.

## Loop iteration 1 — 2026-07-02 (day)

10. **Ability generator shipped**: 112 kit AbilityAssets under
    /Game/ThreeRealms/Abilities/. Kit schema read from plugin C++
    (AbilityAssetCpp.h). Mappings: our cost -> kit ManaCost (kit has ONE
    resource; stamina-vs-mana split needs a kit extension later — logged);
    strike/dd/dot get SwordAttackLogic_TargetBased with DamageFrom/To =
    baseValue x0.8/x1.2; heal/buff/cc kinds have no logic instance yet
    (per-kind logic classes = next); casters get 1.5s CastTime.

## Loop iteration 2 — 2026-07-02

11. **Mythic Earth start flow SHIPPED (v1, function-first)**: C++ game module
    added to kit project. TRAuthClient = our own WebSocket protocol client
    (independent of kit BP login). TRStartFlowWidget: login (WoW-shape,
    THREE REALMS title, live 3D scene backdrop via duplicated StartMap) ->
    Create Account (name/email/password/confirm; email captured but not yet
    stored server-side - DB extension pending) -> server select (Three
    Realms Dev GN) -> realm select (3 sigil cards, GN playable, ML/HG
    coming-soon) -> DAoC-style creation (class type -> race by culture
    group -> name + "at level 10 you may become" destiny list from the
    race matrix) -> character created in DB -> travels to 127.0.0.1:7779.
12. **Known seams (next iterations)**: world-server cookie handshake on
    entry (kit BP expects its own login state - travel may bounce);
    realm-lock skip logic needs GetCharacters RPC parse; email persistence;
    button routing uses IsHovered lookup (tech debt); Live Coding blocked
    one build - editor was still open from Daniel's test (killed it).

## Loop iteration 3 — 2026-07-02

13. **Character select + realm lock shipped**: login -> server ->
    character list (from RPC 21) with ENTER WORLD per character; realm
    lock reads the first character's realm and skips realm select for
    new characters (per spec). Empty accounts flow to realm select.
    Tonight Daniel's daniel_test login will show Aldric (Level 1 celtic
    frontline) ready to enter world.

## Loop iteration 4 — 2026-07-02

14. **Email storage end-to-end**: persistence server fork gains SetEmail
    RPC (repurposed unused slot 11) + SetAccountEmail; client captures
    email at Create Account and sends it right after auth. Verified:
    daniel_test row carries a real email in sqlite. NOTE: persistence
    server is now OUR FORK with local-only commits — needs its own
    private remote (punch-listed).
15. Bigger-chunk pacing adopted after Daniel's feedback: each waking
    works multiple pieces; wakeups stay ~90s.

## Loop iteration 5 (long-haul) — 2026-07-02

16. Backups: MMOKitPersistence fork pushed to private ThreeRealmsPersistence
    (upstream remote preserved for kit updates). MMOKitEval migrated to
    Git LFS (1064 binary assets) and pushing to private ThreeRealmsKit
    (in progress, background). World server was stopped to unlock files —
    restart via StartThreeRealmsServers.bat before playing.
17. Styling: gold hairline rims on all panels, 64px sigil diamonds,
    pre-alpha footer. P1 MARKED COMPLETE.
18. Pacing change per Daniel: long hauls per waking, wider gaps between.

## Loop iteration 6 (long-haul cont.) — 2026-07-02

19. Skill tree panel shipped (K toggle via world subsystem — no kit BP
    edits). Two build snags fixed: wrong world-type enum; DLL locked by
    the running world server (stopped, built, restarted — brief outage).
20. All three repos confirmed on GitHub: MMO (public), ThreeRealmsKit
    (private, LFS), ThreeRealmsPersistence (private fork).

## Loop iteration 7 — 2026-07-02

21. MILESTONE: Daniel entered the world through OUR login flow ("Server
    logged in / Client logged in"). Spawn init errors diagnosed: our
    creation blob lacked kit fields; Aldric fell to z=-598km (RIP, saved).
22. Fix built (queued behind Daniel's open editor): creation payload now
    kit-shaped (schema captured from a kit-authored save; Human body
    placeholder; sword equipped); realm/classtype/race moved to dedicated
    DB columns via new RPCs 12/13 because KIT SAVES CLOBBER THE JSON BLOB.
    Client meta-read merge (fix realm lock post-save) = next iteration.
23. Discovered kit-valid appearances: Human, Mannequin, DarkMinion. Sex
    choice missing from our creation flow — punch-listed.
24. LFS pointer incident during Daniel's session (TRStartMap unreadable)
    — fixed via git lfs checkout; WBP_HUD still held by his session,
    auto-fixes at editor close.

## Session B (new morning session) — 2026-07-03 ~11:00

25. DANIEL FLAGGED (crops sent to Session B): status text overlapping baked
    realm taglines; ugly blob-scrim fading on the login backdrop. Fixes by
    Session B:
    - ART (committed 3971bb7): T_Backdrop_login.png reworked — continuous
      anchored center-column dark stage (canopy -> dim city window -> UI
      stage -> clear label zone) instead of two floating soft blobs.
    - CODE (STAGED IN TREE, NOT BUILT): TRStartFlowWidget .h/.cpp — status
      moved 0.86 -> 0.832 with a collapsing dark plate (StatusPlate).
      TO SESSION A: these staged edits are intentional; include them in
      your next build, do NOT revert. Your charid travel fix + TRAutoEnter
      auto-flow WIP looks correct — Session B is staying off C++ builds
      and world logins while your verify loop runs. Dossier:
      design/progress/2026-07-03-morning-coordination.md.

## 2026-07-07 — Game name is MYTHIC EARTH

"Three Realms" was only ever the working title. Daniel confirmed the game
is named **Mythic Earth**. Applied everywhere user-visible: start-screen
title + footer, server row, chat welcome, ESC-menu title, UE ProjectName,
engine source comments, and living design docs (README, CLAUDE.md,
login-flow, punchlist, STATE-OF-THE-GAME). Deliberately NOT renamed
(infrastructure keeps the old working title): repo dir `three-realms`,
GitHub repo illiset/MMO, `Content/ThreeRealms/` asset folder (renaming
breaks asset references), `TR*` C++ class prefix, and dated historical
progress docs. Historical log entries above stay as written.

## 2026-07-14 — Faction XP bar skins
Daniel picked per-faction XP bar identities from mock rounds (generic MMO
skins rejected; "should look mythic"):
- **Great North = "Northern aurora"** — teal→blue→violet ramp across the
  20 bubbles (the North's own sky), shimmer sweep + pulsing tip glow.
- **Honor Guard = "Runeforged ember"** — iron frame, ember fill.
- **Mystic Lands = "Molten gilt"** — liquid gold.
Layout (all factions): full-width 20-bubble strip flush at screen bottom,
cur/req plaque floating above, trim end caps. GN live in-game
(commit dcd779d, MMOKitEval); HG/ML sit in the FTRXpBarSkin table until
their realms are playable. Faction routing note: characters DB already
stores realm; client-side faction id plumbing is a future lane.
