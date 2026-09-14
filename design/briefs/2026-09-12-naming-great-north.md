# Brief: names for the Great North's places (for an Opus design session)

**Owner:** Daniel. **Session model:** Opus (design/writing; no engine work).
**Writes to:** this design repo only (`design/names/great-north-places.md` + a JSON twin at
`data/zones/great-north-names.json`). Do NOT touch `C:\dev\MMOKitEval` — the overnight Fable
session is building Dál Riata there and will adopt the names in the morning.

## What exists
- The realm map: `design/Mythic Earth-Great North-2k.jpg` (8k original beside it, untracked).
  Culture territories, each with start points labelled by ARCHETYPE: Frontline / Damage /
  Healer / Support (some combined, e.g. "Frontline/Healer Start"). Named already on the map:
  Tara (Sidhe), Dál Riata (Celtic), Miklagarðr, Hedeby (Germanic), the Crusader Empire (Aethiopes
  Start), Italics Romana, Castrated Plains, Dew Hollow, Thracian Frontier.
- Races and culture groups: `data/factions/great-north.json` (16 races: Crusaders = Celtic,
  Germanic, Romance, Hellenic, Slavic, Baltic, Armenian, Aethiopes; Elves = Mythic, Sidhe, Alfar;
  Hillback Empire = Hillback Dwarves; Dew Hollow = Woodling, Gobbledrift, Fae, Centaur).
- Decided: first zone = Dál Riata, 3 km tip to tip; its village is provisionally **Dunadd**
  (the historic Dál Riata royal seat). Rename if Daniel prefers.

## Deliverable
For every territory: a name for the territory's main settlement, and a name for EACH start
point on the map (the hamlet / camp / hall / grove where a new character of that archetype
appears), with one line of flavour each. Dál Riata first (village + 4 starts), then Sidhe,
then the rest of the map.

## Rules
- Culture-true sound: Celtic → Old Irish/Gaelic; Sidhe → Irish myth; Germanic/Alfar → Old
  Norse; Romance → Latin/Old French; Hellenic → Greek; Slavic, Baltic, Armenian → their
  tongues; Aethiopes → Crusader Latin; Hillback, Woodling, Gobbledrift, Fae, Centaur → invented
  but consistent per race.
- Pronounceable by an English speaker on first read; avoid real modern town names and any
  DAoC / WoW / Warhammer place names.
- Each name unique across the realm (players will say them in chat).
- Output both files; the JSON keys must match `data/factions/great-north.json` race ids and the
  archetype ids frontline / dps / healers / support.
