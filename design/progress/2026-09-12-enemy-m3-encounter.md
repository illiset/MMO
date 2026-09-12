# Enemy M3 evidence package — the Rimethralls on the live stack (2026-09-12)

Game repo: ThreeRealmsKit `9965b6c` (harness in `Tools/frostmarch/m3`). Stack: fresh
PersistenceServer + dedicated `Playable_FrostmarchSlice` server + windowed client, driven
background-safe by posted keys; all numbers from `Content/Data/mobs/rimethralls.json`.
Contact sheets: `2026-09-12-enemy-m3-run1-walk-in.png`, `2026-09-12-enemy-m3-run2-melee.png`.

## Run 1 — walk in from 16.5 m (tell / approach / shots)
Server:
```
[TRAI] Rimethrall Stalker acquired BP_PlayerCharacter_C_0 at distance 1348 (aggro radius 1400)
[TRAI] Rimethrall Stalker alerted (tell 1.2s)
[TRAI] Rimethrall Stalker alerted (tell 1.2s, social pull)
[TRAI] Rimethrall Stalker entered combat            (x2, 1.2 s later)
[TRAI] Rimethrall Stalker attack 0 accepted (impact in 0.45s, x1.00)
[TRAI] Rimethrall Stalker hit BP_PlayerState_C_0 for 4 damage. Player HP 196/200
[TRAI] Rimethrall Stalker attack 1 accepted (impact in 1.40s, x1.15)   <- 0.9 s draw + 0.5 s loose
... 2.6 s cadence per archer, 4-8 damage, HP 200 -> 1 in ~45 s ...
[TRAI] player at 1 HP floor (player death is a future lane)
```
Client: `tell shown` 1.9 s after the server alert (asset streaming hitch at the tell — fixed in
run 2 by the dress-time preload). Player never closed to melee: the full-quality client ran
at 2-3 fps on the laptop's integrated GPU, so a 1 s posted key hold landed inside one frame.

## Run 2 — spawned at melee reach (kill / death / respawn / leash), low scalability client (~7 fps)
Server:
```
[TRAI] Rimethrall Stalker acquired BP_PlayerCharacter_C_0 at distance 200 (aggro radius 1400)
[TRAI] Rimethrall Stalker alerted (tell 1.2s)  /  alerted (tell 1.2s, social pull)
[TRCombat][SERVER] auto-attack ON (target=BP_Minion_C_1)
[TRFeel] Shield Bash impact damage: hit BP_Minion_C_1 for 38. HP 14/70 (direct)
[TRFeel] Frontline Strike impact damage: hit BP_Minion_C_1 for 23. HP 0/70 (direct)
[TRCombat] BP_Minion_C_1 died
[TRCombat][SERVER] auto-attack stopped: target died (sequence reset to A)
[TRXP] Awarded 12 XP ... for killing Rimethrall Stalker. Total XP 12/100
[TRAI] Rimethrall Stalker died — combat over
[TRCombat] corpse hidden: BP_Minion_C_1 (respawn in 42s)          <- 3 s corpse + 42 = authored 45
[TRAI] BP_Minion_C_1 AI logic restarted on respawn                <- 45.05 s after death
[TRCombat] BP_Minion_C_1 respawned (HP 70/70)
[TRAI] Rimethrall Stalker acquired BP_PlayerCharacter_C_0 at distance 200 (aggro radius 1400)
[TRAI] Rimethrall Stalker attack refused: out of range (1247 > 1100)   <- player back-pedalling
[TRAI] Rimethrall Stalker leash exceeded — returning home           (x2)
[TRAI] Rimethrall Stalker reset complete. HP 70/70                  (x2)
```
Client:
```
[TRAI][CLIENT] Rimethrall Stalker tell shown            <- 0.27 s after the server alert
[TRAI][CLIENT] preloading 21 presentation assets for Rimethrall Stalker
[TRAuto] Swing A montage started (Attack_PrimaryA_Montage)
[TRFeel] client saw target HP 70 -> 52 (Δ18)   hit-react on BP_Minion_C_2 (Δ18, rate 1.25, front)
[TRFeel] client saw target HP 52 -> 14 (Δ38)   hit-react on BP_Minion_C_2 (Δ38, rate 0.80, front)
[TRFeel] client saw target HP 14 -> 0 (Δ14)    Rimethrall Stalker death sequence (backward)
[TRXP] (client) XP now 12/100
```

## Fixes that fell out of the evidence (all in 9965b6c)
- `socialPullRadius: 2000` on the three archer castes (G1 pair 1628 uu apart, G3 flanks 1825 uu).
- def `dmgMin/dmgMax/respawnDelay` parsed and used (kit stats never exposed DmgMin/DmgMax).
- `ClientPreloadDefAssets` at dress time (no first-use hitch on tell/attack/hit/death).
- Harness: traced spawn height (the hardcoded z=320 was 20 cm inside the hill), possession-line
  wait, fresh PersistenceServer per run, low-scalability client profile for logic runs.

## Not yet evidenced
The death animation itself is not visible in the run-2 frames: the archer stood 2 m directly
in front of the player, i.e. behind the mannequin from the camera's view (nameplate present at the
kill, gone while hidden, back on respawn). A side-angle capture needs mouse-look injection.
Warden / Huntress / Halvard encounters, the G2 fire-camp composition, and the player's own
Shield Bash VFX still shows a one-off "Preparing Shaders (1)" on first use.
