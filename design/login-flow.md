# Login & character creation flow — Daniel's spec, 2026-07-02

## Style direction
- **Login screen: WoW-style** — fullscreen, immersive, game-world backdrop —
  but **our own art direction, NOT cartoony** (Great North winter-realistic
  tone; dark + gold classic UI). Not DAoC's small-window login.
- **Character creation: mimic DAoC's** — step-down flow, portrait/model
  focus, stat/class info panels, sober classic presentation.
- Button copy: **"Create Account"** (never "I don't have an account yet").

## Flow
1. **Login** — account name + password, Login button, Create Account button.
2. **Server select** — list of servers (one for now: the local/dev server;
   architecture supports many later).
3. **Realm select** — Great North / Mystic Lands / Honorguard.
   **REALM LOCK RULE:** once an account creates a character on a server,
   that account is LOCKED to that realm ON THAT SERVER — other realms
   grayed with explanation — unless the account deletes ALL characters on
   that server or transfers them off. (Classic DAoC rule.)
4. **Character creation (DAoC-style)** — class type (archetype) → race
   (filtered by realm) → name → confirm. True class comes at level 10
   in-game (see quests.json), so creation shows class TYPE prominently and
   lists the classes it can become (filtered by race matrix) as flavor.
5. **Loading screen** → enter world.

## Backend implications (persistence server is ours, C#)
- Realm-lock needs account+server→realm binding in DB (extend accounts or
  new table). Enforce server-side on character creation, not just UI.
- Character rows need realm + classType + race + name (already in our
  serialized blob shape).

## Status
- Spec recorded 2026-07-02; loop implementing. Screens = C++ UMG in kit
  project; kit stock StartMap UI is dev-only scaffolding, not player-facing.
