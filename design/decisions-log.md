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

11. **Three Realms start flow SHIPPED (v1, function-first)**: C++ game module
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
