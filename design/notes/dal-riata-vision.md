# Dál Riata — Daniel's vision notes (2026-09-13)

Direction given in conversation after the first night build. Treat as authoritative; numbers are open.

## Shanderry Forest — the island's grind ground
- **Very tall, very thick.** A tall closed canopy; some trees quite large, but nothing like the giants
  of the Sidhe starting area. Dark under the canopy; beautiful from above. Fireflies at night, large
  shrubs, and terrain you have to walk around (fallen trunks, boulders, root walls, gullies), not a
  flat floor with trees on it.
- **Danger by design.** So thick it is a grind spot approaching Catacombs-dungeon difficulty:
  aggressive mobs, neutral wildlife, some aggressive wildlife, and bandits — some hidden in fixed
  lairs, some wandering. The Bohermara Road skirts the forest's east edge so a level-1 character
  never has to enter; the interior is where groups go to farm.
- **Open question for Daniel:** the forest's level band (proposal: 6–12, overlapping the dungeon's
  9–15 so a group has two places to be at 9–10), and who the bandits are (proposal: an outlaw
  family of the same wild stock as Dál Riata's own people — see lore below; until human bodies
  exist they can be built on re-dressed Paragon skins the way the Rimethralls were).

## Carrigrua — a castle, not a fort
- A **large keep**: not the Crusader castle (the biggest in the Great North), but big — think a
  whole wing of Stormwind. The keep of *Tristan and Isolde*, not Camelot.
- **An outer ward** inside the walls: merchants, livestock, an inn, working life.
- **Castle walls all the way round and a drawbridge.**
- Dunadd village sits at its gate (names doc: the royal seat on the crag; the village keeps the
  Dunadd name, the castle is Carrigrua on Kingshill).
- **Asset gap:** no castle kit is in the project. The overnight shift can block out the massing
  (walls, gate, keep volumes) from existing stone pieces, but a real modular castle kit is a
  purchase (Hivemind "Modular Castle" was in the Fab search; price to check).

## Lore — why Dál Riata is wild
- Dál Riata did not want to join the Crusaders at first; its people were more wild, closer in
  temper to the Sidhe across Kyleshee Strait.
- Its army historically waged war on the Crusader castle before the two became aligned. That
  history belongs in Carrigrua (scars, trophies, old banners), in Dunadd's dialogue, and in the
  Celtic race-bible entry.

## Consequences for the build
- Night 2 forest work: tall-canopy scatter (baked Megaplant oaks/hornbeam/beech scaled up),
  dense understory shrubs, obstacle layer from the Quixel scans (Large Fallen Tree, Mossy Forest
  Roots, stumps, boulders), canopy shadow density for darkness, a firefly emitter for night.
- Night 2 Carrigrua: blockout only (walls, gate, keep) until a castle kit lands.
- Creatures lane: forest mob families (bandits + aggressive wildlife) join the wildlife defs.

## Look and weather — Pacific Northwest (Daniel, 2026-09-13, from reference photos)
- **The forest is a PNW temperate rainforest**, not an English wood: very tall straight conifers
  (Douglas-fir / cedar / hemlock scale, trunks bare for the first 20 m, canopy far overhead),
  moss-draped trunks and hanging moss, ferns and huge shrubs on the floor, nurse logs and fallen
  giants, root walls, gullies and streams, waterfalls where the ground drops, sun shafts through
  fog, mossy wooden footbridges and boardwalks over the wet ground. Dark under the canopy;
  beautiful from above.
- **Weather:** Dál Riata is overcast about 70% of the time; Sidhe Territory 85–90%. Dál Riata's
  clear weather lives on the south, south-east and east shores and the coastal fields (Portcorr,
  the Moyree, Dromcairn) and almost nowhere else. The north (Benlea, Rinnbeg, Cuaseen) is foggy.
- Daniel's reference images are in the chat of 2026-09-13; drop copies into `design/reference/
  dal-riata-pnw/` to keep them (mood-board use only, never shipped).

### Consequences
- Tree mix: conifer-dominant. Baked tall Norway Spruce + Baltic (Scots) Pine as the canopy, scaled
  up; birch, alder, willow, rowan only at edges and water; oak/hornbeam/beech become rare.
- Floor: moss materials (vault has Nordic Moss, Mossy Forest Floor, Mossy Grass), ferns (asset to
  source — check free Megaplants for a fern; otherwise a purchase), large shrubs (elder, hazel).
- Obstacles: Large Fallen Tree ×2, Nordic Forest Tree Fallen ×2, Old/Rotten Tree Stump, Mossy
  Forest Roots, Mossy Forest Boulder, Nordic Forest cliffs — all already in the vault.
- Water: the Owenfinn gets a waterfall where it leaves the forest onto the lowlands; streams and
  gullies inside the forest; a plank footbridge or two (kitbash) — Athgorm stays a ford.
- Light: overcast PNW baseline atmosphere (soft grey-white sky, low sun, volumetric fog, light
  shafts), fog density graded stronger to the north, clearer on the S/SE/E coast.
- Weather system (later lane): dynamic weather + time of day with per-region overcast probability
  (Dál Riata 70%, Sidhe 85–90%) and regional clear pockets. Fastest path = Ultra Dynamic Sky (Fab,
  paid, Daniel's buy) vs a homegrown controller on SkyAtmosphere + VolumetricCloud + fog.
