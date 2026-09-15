# Day editor pass — 15 Sep 2026, 13:05 → 16:20: the canopy test plot + the quick fixes Daniel found

Daniel walked Lissban and the island this morning and reported live. This is the editor pass for everything
that does not need the water plugin or the landscape-material rebuild (those are their own slots after this).
Editor ONLY (the play stack is down; bring it back at the end). Hard stop for editor work 16:00, stack up by 16:20.

## Hard rules (unchanged)
- Machine clock only (`date` before every phase). One heavy process at a time. Delete `Saved\Autosaves` before launch.
- Nothing counts without a capture or a log line. Blockers: 20 min, write them down, move on.
- The landscape MASK re-import is a known trap (night 4b broke the landscape material twice via AssetImportTask).
  If a mask must be repainted, use ONLY the proven night-3 route (`Tools/dalriata/n3/gen_masks.py` →
  `n3_reimport_mask.py`) and, if `T_TR_GroundMask` compiles to the Default material, `git checkout` the texture and
  both material instances and relaunch. Never leave the island grey.
- Never invent place names or people's names. Explicit `git add` paths only. Never commit vendor packs.
- Never touch Lissban's knoll / NE hill heights, Daniel's approved landforms.

## A. THE CANOPY TEST PLOT (Daniel's priority, ≤ 100 min)
Daniel: "the canopy of the trees in Shanderry should almost feel like a ceiling, like there is no sky while you're in
there unless in a clearing", branch line "4–8x the height of a human", "do a test of that somewhere before we
scrap what you've done cause I do like what you've done in many ways".
- Plot: a 200 × 200 m square inside Shanderry next to the forest-road halfway rest at (−568, 834) m (offset it
  so the rest's own glade stays open; mark the plot's corners with four stumps so he can find it).
- Method (free, our own assets): take `SM_TR_Fir_Canopy` (28.3 m local, the SilverFir scan) and CUT its branch
  geometry below the line for real with Geometry Script (`GeometryScriptLibrary_StaticMeshFunctions.copy_mesh_from_static_mesh`
  → select triangles with local z below the cut AND radial distance from the axis > ~0.5 m → delete → save as a
  NEW static mesh `SM_TR_Fir_HighCrown` in `/Game/ThreeRealms/World/Trees/`; leave the original untouched). Cut
  height: 12 m at scale 1.0 (so 10–16 m across the scale band). Then a second crown tier: a crown-only mesh
  (the same cut with the trunk also removed below the crown) placed ON the same trunk positions at 12–18 m so
  each tree carries two tiers and the roof closes. Density in the plot: 260–320 stems/ha with giants 1-in-5,
  needle mask OFF on the cut meshes (they no longer need it). Understory as the rest of Shanderry. Keep everything
  outside the square exactly as it is.
- THE MEASURE: from three points inside the plot (not in a gap) capture straight UP (pitch 89) and compute the
  sky fraction (bright sky-coloured pixels / all) — do the same at three points in untouched Shanderry as the
  baseline. Report both. Target inside the plot: under 10 % sky. Also an eye-level interior capture and one from
  the road looking into the plot, and a 400 m aerial that shows the plot edge against the old forest.
- If Geometry Script is not enabled: enable the `GeometryScripting` plugin in the .uproject (it ships with 5.8),
  relaunch once. If it cannot cut, fall back to the mask route with the threshold back at 0.055 PLUS the crown
  tier, and say so.

## B. THE QUICK FIXES (scripts mostly exist under Tools/dalriata/n4c/; ≤ 70 min total)
1. `n4c_30_trees_out_of_rocks.py` — trees through boulders, island-wide.
2. `n4c_31_camera_blocks.py` — buildings block the Camera channel (the C++ side is already built: the spring arm probe is always on).
3. Hut walls and roof two-sided: the f_house_01 wall material (`f_house_01_mat`), `thatched__transparent_mat`,
   `house_roof_01_mat` and the barn's — two-sided material instances the way `n4c_22` did the wattle, assigned on
   the hut/hall/barn components. Daniel sees the far wall vanish through the doorway.
4. Delete `DRV2_GroundPatches` entirely (the shore discs read as polka dots from the air). The shore texture comes
   with the landscape-material slot.
5. The blue boulders: every bank/glade boulder instance on the ApexNature Dolomites meshes (`SM_APXN_DOLR_*`, whose
   material needs a runtime virtual texture we do not have) swaps to the Roman & Celtic `landscape_rocks_*` meshes;
   cap the bank boulders at ~1.2 m and thin them by half. Sky light colour → neutral overcast grey (it is blue and
   tints every grey surface).
6. The roads end at the EAST gate, not the palisade: in `data/zones/dal-riata.json` both `boherath` and
   `boherath_coast` end at the village centre. Re-end them at `LB_Gate_East_01`'s outside point with the last 40 m
   square to the gate, repaint the road mask near Lissban only (night-3 route, see the trap above). The west gate
   keeps its field track.
7. The pooled `DRV2_FogPool_*` LocalFogVolumes show their walls from the air (Daniel saw a brown column at Athgorm
   Ford): delete them; valley mist from the height fog only.
8. The lake: replace the 3,596 8 m tiles with ONE smooth polygon mesh traced from the 58 m basin contour
   (ProceduralMeshComponent, ear-clipped; extend 2 m under the bank). Same for the plunge pool. If it takes more
   than 25 min, log and skip — the water pass will redo it with the Water plugin anyway.
9. A wild pig was inside the palisade: wildlife spawners within 250 m of any settlement move out to 300 m, and
   note in the report that the wander leash needs a settlement keep-out in C++ (not tonight).

## C. RESTORE + REPORT
Save the level, quit the editor, `C:\dev\PlayMythicEarth.bat` (launch it from PowerShell `Start-Process`, never
with `/min` from Git Bash), Celtictest left where the DB has him. Report: `design/progress/2026-09-15-day-editor-pass.md`
with captures in `design/progress/captures/2026-09-15-day/` (the canopy pair first: plot look-up vs baseline
look-up with the sky percentages printed on them). Commit both repos with explicit paths; push.
