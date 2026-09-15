# ESC menu + settings v1 (2026-09-14) — what a triple-A MMORPG shows on Escape, plus the addon features we build in

Principle: everything a player would otherwise install an addon for, if it is not game-breaking, is built in and switchable.
Game-breaking = automation (rotation bots, auto-target/aim assist, auto-loot-from-afar), reading hidden server state, or
public shaming tools. Personal information is always allowed; information about others needs their opt-in.

## The ESC menu
Return to Game · Settings · Key Bindings · Macros · Interface Layout (edit mode: drag frames) · Help/Support · Log Out ·
Character Select · Exit Game. (Ticket/report player lives under Help.)

## Settings — tabs

### Graphics
Display mode (fullscreen / borderless / windowed), resolution, refresh rate, VSync, FPS cap (30/60/120/144/unlimited),
brightness/gamma, quality preset (Low → Cinematic) and per-item: view distance, shadows, textures, effects, foliage density,
water, post-processing, anti-aliasing (TAA/TSR/MSAA), upscaling (DLSS/FSR/XeSS + sharpness), ambient occlusion / global
illumination (Lumen on/off), reflections, motion blur, depth of field, field of view, render scale, show FPS/ping overlay.

### Sound
Master, music, ambience, effects, dialogue/voice, UI, output device, music in combat, mute in background, sound in
background, subtitles, footstep volume.

### Controls
Mouse sensitivity X and Y, invert Y, mouse smoothing off/on, camera follow-behind on release (WoW default), camera max
distance, camera collision, auto-run key, click-to-move OFF (locked off for WoW controls), sprint = hold / toggle /
double-tap on auto-run, interact key (F), key bindings profile, controller support later. **Sticky targeting**, target
nearest enemy behaviour, tab-targeting scope (enemies only / all), auto-face target on attack, quick-cast (skills fire on
key down), self-cast modifier (Alt), mouseover casting (healers), focus target key, target-of-target.

### Interface
UI scale, action bars (number, rows, position, show key labels, show cooldown numbers), unit frames (style, show
percentages, class colours), **nameplates** (friendly/enemy/NPC on-off, names + roles, health bars, cast bars, con colours,
stacking), **floating combat text** (damage/heal numbers on/off, size, colours, crits), chat (font size, timestamps, tabs,
channels, profanity filter, copy text, chat bubbles), minimap (rotate vs north-up, zoom, coordinates, clock), tooltips
(gear comparison, item level, sell price), cast bar position, buff/debuff durations on icons, quest tracker (on/off, auto
track, waypoints — no auto-pathing), XP bar style (+ XP-per-hour and time-to-level), map coordinates.

### Gameplay
Auto-loot, loot method defaults (group loot / need-greed), auto-sell junk at vendors, repair all, auto-attack on target
select, tutorial tips, dismount on cast, camera zoom on combat, show con ring, show helmet/cloak, mark corpses lootable,
dungeon/lair run counters + lockout timers display, PvP flag confirmation.

### Accessibility
Colour-blind modes (protanopia/deuteranopia/tritanopia) for con colours and UI, text size, high-contrast targets, screen
shake, flash reduction, hold-vs-toggle for all holds, subtitles, cursor size, camera motion reduction.

### Social
Whispers from friends only / everyone, guild/party invites policy, chat filters, block list, hide other players' pets,
name display of other players, "away" auto-reply.

### Account / Network
Show ping/FPS, server region, logout timer, two-factor (later), streamer mode (hide names).

## Addon features built in (allowed)
- **Damage/healing meter**: personal always; group meter only with the group's opt-in; no public leaderboards.
- Cooldown, buff and debuff timers on icons; enemy cast bars; interrupt alerts; low-health screen edge glow.
- Threat indicator on the target frame (tank/DPS), target-of-target, focus target.
- Floating combat text styles; nameplate customisation; range indicator on action buttons (red when out of range).
- Mouseover casting and click-casting on unit frames (healers); self-cast modifier.
- Map/minimap coordinates, waypoint pins on the map (no auto-run to them), quest arrow to a pin.
- Bag search, one-bag view, sort, junk marking; gear comparison tooltips; item level on gear.
- Macro editor with modifiers (shift/alt/ctrl), key-binding profiles, UI layout edit mode with grid snapping.
- Chat timestamps, tabs, copy, link items; guild calendar and notes; LFG board.
- XP-per-hour / time-to-level on the XP bar; session clock; repair cost warning.
- Dungeon/Lair run counters, lockout timers, recent kill log.

## Not built in (game-breaking or against the pillars)
Rotation helpers / one-button rotations, auto-targeting/aim assist, auto-loot from range, boss-fight timers that call every
mechanic (light "encounter journal" text is fine), public DPS shaming, anything that reads what the server hides.

## Build order
1. Controls tab: mouse sensitivity X/Y + invert (this week). 2. Interface: nameplates (name + role), floating combat text,
UI scale. 3. Graphics: presets + FPS cap + resolution. 4. Sound. 5. Gameplay + Accessibility. 6. Key bindings + macros.
7. Social/Account. Addon features roll in with the systems they belong to (meters with group play, timers with dungeons).
