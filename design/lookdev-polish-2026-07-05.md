# LookDev_Frostmarch polish pass — result + a real tooling finding (2026-07-05)

Throwaway map only. **GN_Frostmarch untouched** (git confirms clean).

## Headline (honest)
The visual DIRECTION is proven (snow valley + gothic ice-citadel ruin +
conifers + mountains). But this polish pass hit a real wall: **headless
level edits to this example-derived map do NOT reliably persist to disk.**
Verified in one session: loaded the map → spawned a cold-grade PostProcess
volume + deleted the 4 demo cine-cameras → saved → **reloaded from disk →
the new volume was gone and the cine-cameras were back.** Asset edits (the
snow landscape material) persist; new-actor spawns and actor deletions from
later passes do not. So the cold color-grade, winter pine-tint, and demo
cleanup could not be committed via script.

## Deliverables (against the 8 requested)

**1. Updated LookDev_Frostmarch** — composition on disk: snow ground,
gothic-tower ice-citadel landmark, scattered pine/spruce, framing mountains,
a stone trail toward the citadel. Final mood-grade + cleanup did NOT persist
(see headline).

**2. Clean hero screenshot** — `progress/2026-07-05-lookdev-polish-attempt.png`.
Atmospheric snowy scene with the citadel; proves direction. NOT the final
cold grade (that didn't persist) — still reads warm, pines still green.

**3. Gameplay-validation screenshot** — the hero shot IS from a pawn at
eye/gameplay height (the flying DefaultPawn spawns at the PlayerStart, aimed
at the citadel). No HUD, and it's a flying pawn, because of #5.

**4. Objects/artifacts identified & removal attempted** — found and targeted
for removal: **4× CineCameraActor** (their `SM_CineCam` bodies are the "sky
streaks"), **SM_MW_ColorChecker** (the color test-card near the camp), and a
**TextRenderActor** (demo label). Also found my own **5 Iceland mountains
floating at Z=58547** (never ground-snapped in the first build — the other
"overhead strips"). Deletions/reseats ran but did NOT persist (headline).

**5. What causes first-person/fly/no-HUD** — the map's DefaultGameMode is
`GameModeBase`, which spawns the flying `DefaultPawn` and no HUD. The real
MMO camera + HUD (WoW-style third-person cam, unit frames, action bar) is
driven by the kit's `BP_GameMode` + `BP_PlayerController` + `BP_PlayerCharacter`
+ the persistence & world servers + the login flow — none of which run on an
isolated standalone lookdev map.

**6. What GameMode/Pawn/HUD the dev map uses now** — `GameModeBase` /
`DefaultPawn` / no HUD. I deliberately did NOT switch it to the kit gamemode:
that needs the servers + a logged-in character, and the instruction was not to
force gameplay systems. Wiring it would make the standalone map try to connect
to the persistence server and hang/fail.

**7. What still looks weak** — warm/tan mood (cold grade didn't persist),
bright-green pines (winter tint didn't persist — and note pine variants use
several different leaf MIs: MI_Leaf_Pine_01/02/04, so a real fix tints the
shared parent, not one instance), brown (non-icy) citadel, uniform snow, no
falling-snow VFX (none in the imported packs — deferred). Meta: headless
persistence on this map is unreliable.

**8. Ready to apply as a recipe to GN_Frostmarch?** — **NO, not yet.** The
STRUCTURE/recipe is proven (Landscape + snow auto-material + Iceland mountains
+ Cathedral citadel + conifers + trail). But the final mood grade + winter
pines must be done in an INTERACTIVE editor session, because (a) headless
edits aren't persisting on this example-derived map, and (b) color/mood
grading is genuinely faster and better on live sliders than blind 3-minute
headless round-trips. Recommend: a co-driving session (editor open, Daniel or
Claude tuning the PostProcess white-balance/saturation + the pine parent
material live), OR Daniel does the ~10-minute color grade himself. Once a
final cold look is dialed and SAVED interactively, that same recipe applies
cleanly to a fresh GN_Frostmarch slice.

## Conifer verdict (unchanged)
Not an import gap — Stylized_Tree_Pack Pine+Spruce is enough. Pines need a
winter material tint on the shared leaf parent; spruces already read wintry.

Related: [[lookdev-frostmarch-2026-07-05]], [[asset-scan-2026-07-05]].
