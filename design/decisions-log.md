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
