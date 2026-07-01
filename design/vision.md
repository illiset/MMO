# Vision

## The gap we're filling

Dark Age of Camelot (Mythic, 2001) had a world soul — group dungeons, raid
content, a PvE experience worth logging in for — and it was killed by Mythic
over-prioritizing RvR/PvP at the expense of that PvE content. Every modern
"successor" (Camelot Unchained, Pantheon, Ashes of Creation) is either
vaporware or chasing the same PvP-first mistake. The PvE niche DAoC once
filled is empty. This project fills it.

**PvE-first is the reason the project exists.** It is not a phase-one
compromise before "real" PvP content arrives.

## Design pillars

1. **Group PvE is the core loop.** Dungeons, raids, and a world that rewards
   being in it together.
2. **Three factions with real identity.** Great North (European-mythic),
   Mystic Lands (Persian/African/nomadic-mythic), Honorguard (East/South-Asian
   -mythic and the outcast). Faction identity shows up in class flavor
   (Knight ↔ Immortal ↔ Samurai), race rosters, and culture, not just map
   color.
3. **Meaningful character building.** 16 stats in 4 categories, 100-point
   budgets, archetype minimums, race×class gating — choices that matter at
   creation and keep mattering.
4. **Earn everything.** No purchase can make a character stronger, prettier,
   or faster-leveling. The only product is the subscription.

## Business model (locked)

- Free download + free trial on Steam (content-gated, FFXIV-style)
- $15/month subscription, billed outside Steam via account portal
  (Stripe/Paddle) — Steam handles distribution and trial flow only
- Zero microtransactions of any kind, forever. Brand promise, not a lever.

## Scope philosophy

Ship like **Project Gorgon**, not like DAoC launch: a vertical slice deep
enough to earn the first 100 devoted players, then grow outward over years.
Solo dev + Claude. Field of dreams.

## Current state (2026-07)

- Design data: three faction sheets fully extracted to `data/` — factions,
  culture groups, races, classes, archetype stat minimums, race×class matrix.
- **Great North is the reference faction**: it has numeric per-class stat
  minimums. Mystic Lands and Honorguard have key-stat markers (`keyStats`)
  where numbers aren't assigned yet — filling those in is open design work.
- Engine: UE5 5.7.4 installed, project not yet created.

## Open design work (short list)

- [ ] Assign numeric class stat minimums for Mystic Lands + Honorguard
      (Great North pattern: each class gets minimums on ~4–6 of its key stats)
- [ ] Decide what the 100-point budget buys at character creation (point-buy
      mechanics, racial modifiers?)
- [ ] Name the game (repo name `three-realms` is a placeholder)
- [ ] First playable slice definition: which faction, which zone, which
      handful of classes
