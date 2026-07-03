# 2026-07-03 — The Possession Bug: root cause, fix, proof (Session A)

The oldest open bug (client joins, camera renders, pawn never moves) is
fixed, plus three downstream bugs found hiding behind it. Every claim below
carries its proof artifact.

## Chain of causes (each verified before moving on)

1. **Kit spawn chain wants a numeric char id** — persistence `GetCharacter`
   is `(cookie, charId)`; our travel URL sent only `charname`.
   Fix: `?charid=` + refetch-list-before-travel for fresh characters.
2. **The kit reads identity from BP_GameInstance, not the URL.** Instrumented
   persistence printed the smoking gun: `GetCharacter request: charId=0,
   cookie='' (len 0)` — the in-world kit BP sends what's in the GameInstance
   `Cookie`/`CharId` vars, which only the stock kit login UI ever set.
   Fix (kit ca199b9): `TravelToWorld` calls `SetCookie`/`SaveCharId` via
   reflection. Proof: `GetCharacter processed for: Celtictest` (persistence
   console), `[TRCamera] pawn class: BP_PlayerCharacter_C` (client log).
   Bonus kill: the 1/s WebSocket reconnect loop was the same empty cookie.
3. **F7/WoW camera now lands**: Slate injection never reached pawn input;
   `PC->InputKey(CreateSimulated(F7))` works. Proof: `[TRMove] camera comp
   after F7: BP_WowStyleCameraComponent_C`.
4. **Pawn fell through the world** (movement probe: Z -11k and dropping).
   Two-layer cause on the placeholder OBJ meshes:
   - Nanite was ON (UE 5.7 import default) — Nanite can't serve
     complex-as-simple collision. Turned OFF on all SM_GN_*.
   - OBJ triangle winding is flipped (same axis mess that lays pines
     sideways) — Chaos culls back-face raycasts, so the cooked tri-mesh
     (trimeshes=1, created=1) never hit downward traces.
     `bDoubleSidedGeometry=True` on all 7 meshes (kit 50b42de).
   Proof: server probe went from `NO floor under spawn column` to
   `floor under spawn at Z=126.8 actor=StaticMeshActor_0`.

## New tooling that survives this session

- Client flag `-TRAutoEnter=<char>`: saved-credentials login -> world with
  zero keyboard input. The verify loop is now fully hands-free.
- `[TRGround]`/`[TRMove]`/`[TRCamera]` probes in TRUIWorldSubsystem (first
  30s of any Frostmarch world, both client and server) — cheap, log-only.
- Persistence fork logs every GetCharacter with its received identity.

## Proof captures in this folder

- `2026-07-03-login-clean.png` — login screen, single footer, no debug text.
- `2026-07-03-first-possessed-session.png` — first connected session with a
  real possessed pawn: name + real 200/200 stats from DB on the health bar.
  (Viewport is fog-white: this capture predates the collision fix — the pawn
  was falling. Post-fix standing capture lands in the next report.)

## Still open (honest list)

- Standing-on-ground capture pending (client probe running as this is
  written). Terrain is placeholder-smooth either way; props unverified.
- Action bar keys 1-0 unwired (sketch in coordination doc).
- Kit green health bar replaced by Session B's TRUnitFrameWidget — visual
  verify pending. Chat: kit box collapsed; B's TRChatWidget lands next.
- Start screens: interim art (inpainted); real bar blocked on Daniel's 4K
  regens (design/art-regeneration-prompts.md).
