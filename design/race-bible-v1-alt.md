> **Alternate draft.** Written by the race-bible helper agent late on 2026-09-13 and found on disk uncommitted after `race-bible-v1.md` (1056 lines, the first shift's version) had been committed. Kept side by side so nothing is lost; Daniel (or a design session) merges or picks. Heights, palettes and level-1 clothing in BOTH drafts are invented proposals, not locked.

# Race Bible v1 — the 16 Great North races

**Drafted 2026-09-13 by the overnight build session. Status: DRAFT, awaiting Daniel's review.**

---

## 0. What this is, and how to read it

This is the visual bible the character-art lane builds against: what each of the 16 Great North
races looks like, on both sexes, concretely enough that two different artists (or an artist and an
image model) produce the same person.

**Body tech: PROPOSED, not decided.** Working assumption is Epic's MetaHuman (free with UE 5.8,
parametric height/build, adaptive outfits) for the 12 human and elf races, with the 4 non-human Dew
Hollow races (Woodling, Gobbledrift, Fae, Centaur) needing bespoke models. This has **not** been put
to Daniel — every "MetaHuman-feasible" note below is a bet engineering still has to confirm, not a
green light. See §6.

**Realistic, never stylized.** Photoreal proportions, skin, and cloth at every size from Gobbledrift
to Centaur. No cartoon proportions, no chibi scaling, no oversized-catalogue silhouettes — the
Advanced Village Pack was rejected on sight for reading cartoony, and that is the bar.

**Clothes first.** Players start in plain clothes, no armor. "Clothing at level 1" is the cheapest,
plainest version of the culture's dress. "Palette" describes the culture's full dye range — what a
veteran or noble might wear later — so the art lane can see the ceiling the level-1 floor sits
under.

**Data check.** `data/factions/great-north.json` confirms the 4 culture groups and 16 races exactly
as briefed — no disagreement: **Crusaders** (8: Celtic, Germanic, Romance, Hellenic, Slavic, Baltic,
Armenian, Aethiopes), **Elves** (3: Mythic, Sidhe, Alfar), **Hillback Empire** (1: Hillback Dwarves),
**Dew Hollow** (4: Woodling, Gobbledrift, Fae, Centaur). Matches `progression-v1.md` §3a exactly.
Per `vision.md`, Great North is the European-mythic faction, which is why every human culture below
is grounded in a real regional variation (Caucasus for Armenian) rather than a generic default.

**Canon, not re-litigated.** `progression-v1.md` §3a is APPROVED and quoted verbatim below. Nothing
here contradicts it — where a stat tilt and an obvious physical read would clash, the stat tilt wins
and the description was built to fit it.

> Quoted from `progression-v1.md` §3a, "The 16 Great North races" (APPROVED):
>
> | race | base profile | Swift | Slow |
> |---|---|---|---|
> | **Celtic** | spirit +1, survival +1, impulse +1, detail −1, calmness −1, logic −1 | spirit, survival, impulse | detail, calmness, logic |
> | **Germanic** | strength +2, conditioning +1, finesse −1, elements −1, calmness −1 | strength, conditioning, discipline | elements, finesse, calmness |
> | **Romance** | knowledge +2, logic +1, strength −1, survival −1, impulse −1 | knowledge, logic, detail | strength, survival, impulse |
> | **Hellenic** | athleticism +2, logic +1, spirit −1, constitution −1, wisdom −1 | athleticism, logic, calmness | spirit, constitution, wisdom |
> | **Slavic** | constitution +2, conditioning +1, finesse −1, logic −1, elements −1 | constitution, conditioning, survival | finesse, logic, elements |
> | **Baltic** | awareness +2, survival +1, strength −1, knowledge −1, discipline −1 | awareness, survival, finesse | strength, knowledge, discipline |
> | **Armenian** | spirit +2, discipline +1, athleticism −1, impulse −1, awareness −1 | spirit, discipline, wisdom | athleticism, impulse, awareness |
> | **Aethiopes** | detail +2, calmness +1, strength −1, conditioning −1, spirit −1 | detail, calmness, knowledge | strength, conditioning, spirit |
> | **Mythic** | elements +3, wisdom +1, strength −1, conditioning −1, constitution −2 | elements, wisdom, logic | strength, conditioning, constitution |
> | **Sidhe** | finesse +2, awareness +2, strength −1, conditioning −1, constitution −2 | finesse, awareness, impulse | strength, conditioning, constitution |
> | **Alfar** | survival +2, impulse +1, spirit +1, knowledge −1, calmness −1, conditioning −2 | survival, impulse, spirit | knowledge, calmness, conditioning |
> | **Hillback Dwarves** | constitution +2, strength +2, athleticism −1, elements −1, impulse −2 | constitution, strength, detail | athleticism, elements, impulse |
> | **Woodling** | finesse +2, survival +1, awareness +1, strength −1, conditioning −1, discipline −2 | survival, finesse, knowledge | strength, conditioning, discipline |
> | **Gobbledrift** | impulse +2, athleticism +1, detail +1, wisdom −1, discipline −1, strength −2 | impulse, detail, athleticism | strength, wisdom, discipline |
> | **Fae** | elements +3, spirit +2, strength −1, athleticism −1, conditioning −1, constitution −2 | elements, spirit, calmness | strength, conditioning, constitution |
> | **Centaur** | athleticism +2, conditioning +2, finesse −1, detail −1, elements −2 | athleticism, conditioning, strength | finesse, detail, elements |

**Reading each entry:** height first (what reads at distance), then palette (what a costume
department stocks), then features (face, hair, markings, ornament, sex differences), then the
level-1 outfit, then two reference-image prompts, then a build note on what's easy or hard for the
proposed tech.

---

## 1. Summary table

| Race | Culture group | Male height | Female height | Build | Silhouette read |
|---|---|---|---|---|---|
| Celtic | Crusaders | 170–184 cm | 158–171 cm | average, balanced | Baseline human — easy stance, nothing exaggerated |
| Germanic | Crusaders | 178–193 cm | 166–179 cm | heavy, broad | Big-boned wall of a person, squared shoulders |
| Romance | Crusaders | 166–178 cm | 155–166 cm | slim, upright | Unhurried courtly elegance |
| Hellenic | Crusaders | 173–186 cm | 161–173 cm | athletic, lean | Athletic taper, gymnasion posture |
| Slavic | Crusaders | 176–190 cm | 164–177 cm | broad, sturdy | Broad and grounded, low centre of gravity |
| Baltic | Crusaders | 174–187 cm | 162–175 cm | tall, wiry | Tall, rangy, watchful stillness |
| Armenian | Crusaders | 169–182 cm | 157–169 cm | stocky, compact | Compact, upright, monastic stillness |
| Aethiopes | Crusaders | 171–183 cm | 159–171 cm | lean, drilled | Parade-ground spine, at-attention even at rest |
| Mythic | Elves | 185–199 cm | 174–187 cm | willowy, attenuated | Very tall, attenuated, floats rather than walks |
| Sidhe | Elves | 180–193 cm | 169–182 cm | lithe, agile | Tall and coiled, fox-quick |
| Alfar | Elves | 182–195 cm | 171–184 cm | lean, hardy | Tall, weather-hardened hunter-elf |
| Hillback Dwarves | Hillback Empire | 140–155 cm | 133–147 cm | short, dense | Short and wide as a door |
| Woodling | Dew Hollow | 125–138 cm | 119–132 cm | small, nimble | Child-sized adult, quick and alert |
| Gobbledrift | Dew Hollow | 109–122 cm | 104–117 cm | tiny, spindly | Smallest, hunched, jittery |
| Fae | Dew Hollow | 155–168 cm | 148–161 cm | reed-thin, willowy | Drifts, barely displaces the air |
| Centaur | Dew Hollow | 215–232 cm total / 152–168 cm withers | 200–217 cm total / 142–158 cm withers | powerful, quadrupedal | Half again a mounted rider's height |

---

## 2. Crusaders

### Celtic — Dál Riata

**Silhouette and height.** Male 170–184 cm, female 158–171 cm. Deliberate baseline —
`progression-v1.md` calls Celtic "the flattest profile," first race a new player meets. Medium
build, easy weight-bearing stance, nothing exaggerated either sex. At 50 m: proportionate and
unremarkable until they move.

**Palette.** Skin fair with ruddy wind-flush, `#E8C4A2`. Hair auburn `#8B4513`, dark brown
`#3B2A20`, black, or true red `#A0522D`. Eyes blue `#4A6D8C`, green `#4C7A5A`, grey, hazel. Dyes
from a wet Atlantic island: madder red-brown, woad blue (dull, small-batch, never bright), walnut
brown, lots of undyed cream wool. Weaves are simple two/three-colour checks, not clan tartan.

**Features.** Widest face-shape range of the eight humans, by design — it's the baseline. Men
bearded or clean-shaven, hair tied back for work more than short-cropped. Women loose, braided, or
half-bound, no norm either way. Freckling common. Ornament is small worked-bronze cloak brooches,
functional. No tattooing — the signature is textile, not skin.

**Clothing at level 1.** Undyed linen shirt/shift, oatmeal or grey wool tunic (men) or dress to the
calf (women), leg wraps, plain leather shoes. No brooch yet. Cream, grey-brown, faded oat-yellow
only.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
early-30s, Irish/Scottish Gaelic coloring, 178 cm, medium working build, fair windburned skin,
medium-brown hair tied back, short beard, hazel eyes, relaxed stance in an undyed cream linen shirt
and oatmeal wool tunic, overcast daylight, neutral grey backdrop, natural skin texture, no armor, no
jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
late-20s, Irish/Scottish Gaelic coloring, 165 cm, athletic-average build, fair freckled skin, auburn
hair in a loose braid, green eyes, relaxed stance in an undyed linen shift under a grey wool dress
to mid-calf, overcast daylight, neutral grey backdrop, natural skin texture, no armor, no jewellery,
no retouching.

**Build note.** MetaHuman-feasible, the easiest race here — "flattest profile" needs the least
deviation from stock defaults. Use it to validate the pipeline first.

### Germanic — Miklagarðr

**Silhouette and height.** Male 178–193 cm, female 166–179 cm — tallest, heaviest human, matching
strength+2/conditioning+1. Broad shoulders, thick neck, weight forward in chest and forearms; female
build is tall and strong-framed, not slight. Square, settled posture. At 50 m: the widest human
shoulder line on the roster.

**Palette.** Skin fair `#F0D5B8`. Hair flax-blond `#D8C08A` to light brown `#8A6642`, blond
dominant. Eyes blue `#5A85B0`, steel-grey. Dyes from a frost-forest mountain kingdom: indigo/woad
blue for status, iron-oxide rust-brown, heavy undyed browns/greys for everyday, fur trim (wolf,
bear) practical rather than decorative.

**Features.** Strong squared jaw both sexes. Men wear beards long, often braided at the chin
(status/age marker, not universal on the young); hair long, sometimes half-braided back. Women in
thick single or double braids, occasionally pinned up. Worked silver/bronze arm rings and cloak
pins, sized for work. No facial tattooing; forearm scarring from labour is unremarkable.

**Clothing at level 1.** Heavy undyed brown or grey wool tunic and trousers (men) or overdress
(women), belted with rope or plain leather, no fur trim yet.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
mid-30s, Scandinavian/Norse coloring, 186 cm, heavy broad-shouldered build, pale skin, long
flax-blond hair tied back, full braided beard, blue eyes, square weight-bearing stance in a heavy
undyed brown wool tunic and trousers, cold overcast daylight, neutral grey backdrop, weathered skin
texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
early-30s, Scandinavian/Norse coloring, 172 cm, tall strong-framed build, fair skin, light-brown
hair in a thick double braid, grey eyes, square confident stance in a heavy grey wool overdress
belted at the waist, cold overcast daylight, neutral grey backdrop, natural skin texture, no armor,
no jewellery, no retouching.

**Build note.** MetaHuman-feasible — heavy/broad sits inside default sliders. Braided-beard groom
needs custom work, not a stock preset.

### Romance — Italics Romana

**Silhouette and height.** Male 166–178 cm, female 155–166 cm — shortest, leanest human, matching
knowledge+2/logic+1 against strength−1. Slim, upright, unhurried; mercantile-scholarly rather than
martial. Composed posture, not stiff. At 50 m: looks like they arrived by carriage.

**Palette.** Skin olive `#D9B48F`. Hair dark brown `#3C2A1E` to black, almost no fair hair. Eyes
brown `#4B3221`, hazel. Valmonde sits in orchard/vine country (Marvigne = "Sea Vine"): wine-lees
red-purple, olive green, sun-bleached cream linen, gold ochre trim for the syndicate-merchant
wealth.

**Features.** Narrower faces, straighter noses, defined cheekbones. Men keep hair short-to-medium,
oiled/combed, clean-shaven or a shaped beard. Women wear hair up or elaborately bound more than
loose. Most visibly ornamented Crusader-human race short of Armenian — rings, ear ornaments, fine
chains, matching the syndicate/relic-master class fit. No tattooing.

**Clothing at level 1.** Unadorned cream linen shirt/shift, dark wool trousers (men) or ankle-length
undyed linen dress (women), plain woven belt — the gold ochre and wine-red are earned, not starting.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
late-20s, Mediterranean French/Italian coloring, 172 cm, slim upright build, olive skin, short dark
hair neatly combed, close shaped beard, brown eyes, composed relaxed stance in an unadorned cream
linen shirt and dark wool trousers, warm daylight, neutral grey backdrop, natural skin texture, no
armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
mid-20s, Mediterranean French/Italian coloring, 160 cm, slim graceful build, olive skin, dark hair
bound at the back of the head, hazel eyes, composed stance in a plain cream linen floor-length
dress, warm daylight, neutral grey backdrop, natural skin texture, no armor, no jewellery, no
retouching.

**Build note.** MetaHuman-feasible — low-end body-fat/muscle sliders cover it. Groomed hair and ear
ornaments are texture/prop tasks.

### Hellenic — Leukopolis

**Silhouette and height.** Male 173–186 cm, female 161–173 cm — athletic and lean, matching
athleticism+2/logic+1. Visible muscle definition without Germanic bulk — runner's/wrestler's build.
Upright, open-chested, gymnasion-trained posture. At 50 m: shoulders taper cleanly to the waist.

**Palette.** Skin olive-tan `#CBA07C`. Hair dark brown to black, often waved. Eyes brown `#3F2A1A`,
hazel-green `#5C6B3E`. Sun-bleached cream/white linen and wool, olive-green and saffron-yellow
accents from local plants. Tyrian purple exists but is rare temple/noble trim, never starting cloth.

**Features.** Straight-nosed "classical" profile, defined jaw. Men short-to-medium curled hair,
clean-shaven or short beard — groomed athleticism. Women wear hair bound up with a simple fillet,
neck exposed. Understated bronze/terracotta ornament — the body is the display, not the jewellery.
No tattooing.

**Clothing at level 1.** Undyed or lightly bleached linen chiton pinned at the shoulder and belted,
knee-length (men) or ankle-length (women), plain sandals. No purple or saffron yet.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
mid-20s, Mediterranean Greek coloring, 179 cm, athletic lean build with visible muscle definition,
olive skin, short dark curled hair, clean-shaven, brown eyes, open-chested confident stance in an
undyed linen chiton pinned at one shoulder and belted, sandals, bright daylight, neutral grey
backdrop, natural skin texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
early-20s, Mediterranean Greek coloring, 166 cm, athletic lean build, olive skin, dark hair bound
with a simple cloth fillet, hazel-green eyes, upright stance in an ankle-length bleached linen
chiton belted at the waist, sandals, bright daylight, neutral grey backdrop, natural skin texture,
no armor, no jewellery, no retouching.

**Build note.** MetaHuman-feasible — athletic-lean is a core preset. The single-pinned chiton needs
real cloth sim to avoid looking stiff.

### Slavic — Borograd

**Silhouette and height.** Male 176–190 cm, female 164–177 cm — broad and sturdy, matching
constitution+2/conditioning+1. Weight carried low and wide, thick torso, sturdy legs. At 50 m: broad
and grounded, the opposite lean from Baltic next door.

**Palette.** Skin fair-medium `#E3C1A0`. Hair ash-blond `#C2A876` to brown. Eyes blue-grey
`#7C93A0`, hazel. Pine-wood dyes: bark and onion-skin browns, forest green — but the real signature
is red thread embroidery on undyed white linen, a small saturated accent on a natural-white field,
not an overall dyed garment.

**Features.** Broad, rounder faces, strong cheekbones. Men wear fuller, less-groomed beards than
Germanic's braids; hair under a simple cap outdoors. Women braid hair, often covered with a plain
kerchief (especially married women) — common, not universal. Embroidery on cuffs/collars is the
primary ornament, textile over metal.

**Clothing at level 1.** Undyed white/cream linen shirt with no embroidery yet, plain wool trousers
(men) or skirt (women), woven belt, optional plain headwrap.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
mid-30s, Eastern European Slavic coloring, 183 cm, broad sturdy low-centre-of-gravity build, fair
skin, ash-blond full beard, brown hair under a simple cap, blue-grey eyes, grounded solid stance in
an undyed white linen shirt and plain wool trousers, overcast daylight, neutral grey backdrop,
weathered natural skin texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
late-20s, Eastern European Slavic coloring, 170 cm, sturdy broad-framed build, fair skin, brown hair
braided under a plain cloth headwrap, hazel eyes, grounded stance in an undyed white linen blouse
and plain wool skirt, overcast daylight, neutral grey backdrop, natural skin texture, no armor, no
jewellery, no retouching.

**Build note.** MetaHuman-feasible — broad/sturdy sits inside default sliders. Embroidery is a
texture-map task for later gear tiers.

### Baltic — Laukapils

**Silhouette and height.** Male 174–187 cm, female 162–175 cm — tall and lean, matching
awareness+2/survival+1 against strength−1. Rangy, long-limbed, economical muscle. Alert posture,
weight balanced slightly forward. At 50 m: tall and watchful, scanning the treeline.

**Palette.** Skin fair `#EAD0B0`. Hair flaxen `#E0C88E` to light brown, fairest range alongside
Germanic. Eyes pale blue `#A9C4D6`, grey. Regional signature good is literal Baltic amber, worn as
beads/pendants, paired with pale undyed linen and muted moss-green and madder-brown.

**Features.** Long faces, high cheekbones, pale brows/lashes. Men wear hair short-to-shoulder,
usually unbound (scouts, rangers), light stubble to short beard. Women wear single long braids
threaded with amber beads. Amber is the default ornament for both sexes. No tattooing.

**Clothing at level 1.** Undyed pale linen shirt/shift, muted moss-green or undyed wool overlayer,
no amber yet — that's earned. Practical travelling cut.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
late-20s, Baltic (Lithuanian/Latvian) coloring, 180 cm, tall lean rangy build, fair skin, flaxen
hair loose to the shoulder, light stubble, pale blue eyes, alert forward-weighted stance in an
undyed pale linen shirt and moss-green wool overlayer, cool daylight, neutral grey backdrop, natural
skin texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
mid-20s, Baltic coloring, 168 cm, tall lean build, fair skin, flaxen hair in a single long braid,
pale grey eyes, alert watchful stance in an undyed linen shift under a plain wool overdress, cool
daylight, neutral grey backdrop, natural skin texture, no armor, no jewellery, no retouching.

**Build note.** MetaHuman-feasible — tall/lean is a stock combination. Amber-bead props are a
jewellery-asset task for later gear.

### Armenian — Lusavank

**Silhouette and height.** Male 169–182 cm, female 157–169 cm — compact and stocky, matching
spirit+2/discipline+1 against athleticism−1. Dense through shoulders and torso, not tall. Upright,
unhurried, monastic stillness rather than martial readiness. At 50 m: the person who doesn't fidget.

**Palette.** Skin olive-tan `#C99B72`. Hair black `#1C140F` to dark brown, almost always dark. Eyes
dark brown `#2E1D10`. Signature dye is a deep saturated red unique to the Armenian highlands (native
cochineal, visually distinct from Dál Riata's madder or Slavic red), paired with black monastic wool
and warm apricot/gold-brown for everyday wear.

**Features.** Strong brow, aquiline nose, dark hair/eyes as a near-fixed type — least varied face
shape of the eight humans, deliberately, for a tight-knit highland read. Men wear short, neatly kept
beards, rarely clean-shaven. Women's hair covered or bound in devotional settings, loose or braided
otherwise. Minimal symbolic ornament — a small cross or carved-stone pendant. No tattooing.

**Clothing at level 1.** Undyed dark wool tunic/dress over unbleached linen, no red dye yet
(status/ceremonial colour) — near-monochrome black-brown-cream until earned.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
mid-30s, Armenian/Caucasus coloring, 176 cm, stocky compact build, olive-tan skin, black short beard
neatly kept, dark short hair, dark brown eyes, strong brow and aquiline nose, upright still stance
in an undyed dark wool tunic over cream linen, soft daylight, neutral grey backdrop, natural skin
texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
late-20s, Armenian/Caucasus coloring, 163 cm, compact sturdy build, olive-tan skin, dark hair
covered with a plain cloth wrap, dark brown eyes, strong brow, calm upright stance in an undyed dark
wool dress over cream linen, soft daylight, neutral grey backdrop, natural skin texture, no armor,
no jewellery, no retouching.

**Build note.** MetaHuman-feasible — compact/stocky sits inside default sliders. The tight
facial-type range means fewer head presets needed than Celtic.

### Aethiopes — Crucivallum

**Silhouette and height.** Male 171–183 cm, female 159–171 cm — lean and upright, matching
detail+2/calmness+1 against strength−1/conditioning−1. Drilled posture, straight spine, minimal
wasted motion — the Empire's administrative-military core. At 50 m: the only human silhouette that
reads "at attention" even at rest.

**Palette.** Skin Mediterranean/Anatolian olive `#C9A17A`. Hair dark brown to black, greying early
on veterans. Eyes brown `#4A3320`, hazel. Institutional dye, not folk: iron-grey and dark maroon-red
from Empire workshops, undyed black leather — restrained next to Romance's ochre and Armenian's
scarlet.

**Features.** Angular, disciplined faces. Men close-cropped or shaved-side hair, clean-shaven or a
short regulation beard — legionary-cut, not folk. Women who serve wear hair bound tightly back,
functional. Ornament is rank-marking, not decorative — a discreet brand or tattooed unit mark
(forearm/nape) reads correct here specifically, unlike anywhere else in the Crusaders.

**Clothing at level 1.** Undyed grey-brown linen shirt, plain dark wool trousers/skirt, no unit mark
or maroon trim yet — Tirocastra is a recruit camp and dresses everyone the same.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, male
early-30s, Anatolian/Levantine Mediterranean coloring, 177 cm, lean upright drilled-posture build,
olive skin, close-cropped dark hair, short regulation beard, brown eyes, at-ease military stance in
a plain grey-brown linen shirt and dark wool trousers, flat even daylight, neutral grey backdrop,
natural skin texture, no armor, no jewellery, no retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, female
late-20s, Anatolian/Levantine Mediterranean coloring, 165 cm, lean upright build, olive skin, dark
hair pulled tightly back, hazel eyes, at-ease military stance in a plain grey-brown linen shirt and
dark wool skirt, flat even daylight, neutral grey backdrop, natural skin texture, no armor, no
jewellery, no retouching.

**Build note.** MetaHuman-feasible — lean/upright is a stock preset. Main risk is genericness:
without the grey/maroon palette and drilled posture it can read as re-skinned Romance or Hellenic.

---

## 3. Elves

### Mythic — Argyrion

**Silhouette and height.** Male 185–199 cm, female 174–187 cm — tallest and most attenuated race
short of Centaur, matching the sharpest malus stack in the table (strength−1, conditioning−1,
constitution−2 against elements+3). Willowy to the edge of underweight without reading sickly —
narrow shoulders, minimal visible muscle, unnaturally still and composed. At 50 m: the tallest thing
in the crowd that isn't a Centaur.

**Palette.** Skin cool porcelain `#F1E6DA`, near-luminous. Hair silver `#D8D6D2` or pale gold
`#E4D9A8` — the naming doc's "silvered" register. Eyes silver-grey `#B8C0C4` or pale violet
`#B7A8C4` — the one race group where an unusual eye colour is appropriate, since Mythic is
explicitly non-human. Dyes in moon-white, pale gold, washed-out pale blue only — nothing saturated.

**Features.** Long narrow faces, high fine cheekbones, pointed ears (see build note). No beards on
Mythic men — clean-faced is itself a distinguishing marker. Hair long and unbound or a single simple
plait, either sex; elaborate styling reads too "worked" for this culture's effortless affect.
Minimal worked silver, thin chains, no gemstones. No tattooing — skin stays visually unmarked.

**Clothing at level 1.** Undyed pale linen or raw-silk-look tunic/dress in moon-white or oat, floor-
or ankle-length even at level 1, no silver thread yet — plain but always composed.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, apparent
late-20s male, very tall 192 cm, extremely slender narrow-shouldered build, cool pale porcelain
skin, long straight silver-white hair loose, clean-shaven, pale silver-grey eyes, subtly pointed
ears, perfectly still composed stance in an undyed moon-white linen tunic, soft diffused daylight,
neutral pale-grey backdrop, natural skin texture despite the pale tone, no armor, no heavy
jewellery, no fantasy glow effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, apparent
mid-20s female, very tall 180 cm, extremely slender willowy build, cool pale porcelain skin, long
straight pale-gold hair loose or in a single plait, pale violet-grey eyes, subtly pointed ears,
composed still stance in an ankle-length undyed pale linen dress, soft diffused daylight, neutral
pale-grey backdrop, natural skin texture, no armor, no heavy jewellery, no fantasy glow effects.

**Build note.** Two real gaps: (1) MetaHuman ships **no pointed-ear morph** — every elf race needs a
custom ear attachment or modified head, multiplied across all three; (2) at 185–199 cm male, Mythic
sits at or past MetaHuman's default height-slider range and needs the extended/custom skeletal scale
verified before art starts.

### Sidhe — Tara

**Silhouette and height.** Male 180–193 cm, female 169–182 cm — tall and agile, matching
finesse+2/awareness+2 against the same strength/conditioning/constitution malus as Mythic, but reads
coiled and quick rather than merely thin — a fencer's frame. Alert, weight on the balls of the feet.
At 50 m: tall, but moving before you finish noticing.

**Palette.** Skin pale, cool undertone `#EBDFD4`. Hair raven-black `#100C0A` or copper-red
`#B5551D`, little in between. Eyes green `#3E7A52` or violet-grey `#8477A0`. Tara's register is
"mounds, dreams, quarters" — deep moss green, dusk purple, worked bronze/copper (Celtic-adjacent,
since Sidhe pairs with Celtic mythologically). Nothing saturated; everything reads dusk-lit.

**Features.** Fox-like — pointed chin, high sharp cheekbones, pointed ears. Men wear hair long/loose
or in narrow temple braids, little to no facial hair. Women wear hair deliberately unbound and wild
— the opposite of Mythic's composed plait, marking Sidhe as the fae-wild elf. Bronze/copper spirals
and knotwork at wrist and throat. Faint natural grey-green freckling is a species trait, not applied
art.

**Clothing at level 1.** Undyed dark-grey or moss linen, close-fitted (never loose enough to snag on
branches), no bronze ornament yet.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, apparent
late-20s male, tall 186 cm, lean athletic coiled build, pale cool-toned skin, long raven-black hair
loose with a narrow temple braid, no facial hair, green eyes, sharp fox-like cheekbones, subtly
pointed ears, alert weight-forward stance in an undyed dark-moss linen tunic close-fitted to the
body, dusk-toned soft daylight, neutral grey backdrop, natural skin texture, no armor, no heavy
jewellery, no fantasy glow effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, apparent
mid-20s female, tall 175 cm, lean agile build, pale cool-toned skin, long copper-red hair loose and
windblown, violet-grey eyes, sharp cheekbones, subtly pointed ears, alert poised stance in an undyed
dark-grey linen wrap close to the body, dusk-toned soft daylight, neutral grey backdrop, natural
skin texture, no armor, no heavy jewellery, no fantasy glow effects.

**Build note.** Same missing pointed-ear morph as Mythic, but Sidhe's height range sits closer to
MetaHuman's normal bounds, so skeletal-scale risk is lower. The wild windblown hair groom is
higher-effort than Mythic's simple straight styles.

### Alfar — Vetrholt

**Silhouette and height.** Male 182–195 cm, female 171–184 cm — tall, and the hardiest elf: no
strength or constitution malus at all (only conditioning−2, knowledge−1, calmness−1), so it should
read tougher and more weathered than Mythic or Sidhe, not frailer. Lean but sinewy, built for cold
and distance. Upright, enduring posture rather than coiled. At 50 m: elf-tall, but looks like it
could survive a winter outdoors.

**Palette.** Skin frost-pale `#F3ECE4`, flatter than Mythic's luminous porcelain. Hair white-blonde
`#EDEAE2` or silver. Eyes ice-blue `#AEDDE8`. "Colder and cleaner than the Germanic" per the naming
doc — pure white, ice-blue, pale grey, silver-fox or white fur trim echoing Germanic's logic in a
paler key.

**Features.** Angular but broader-jawed than Mythic or Sidhe — the hunter-elf, not the dream-elf.
Smaller, subtler pointed ears. Men wear hair cropped short or in a tight braid, short or no beard
(elves stay beardless as a species convention). Women in tight practical braids, rarely loose.
Simple geometric worked silver, echoing the Old Norse register. Genuine cold-weather chapping at
cheeks/nose, unlike Mythic's untouched skin.

**Clothing at level 1.** Undyed white or pale-grey wool, close-fitted and layered for cold, no fur
trim yet — the plainest of the three elf starting outfits.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, apparent
early-30s male, tall 188 cm, lean sinewy weather-hardened build, frost-pale skin with slight
cold-chapping, white-blonde hair cropped short, no beard, ice-blue eyes, subtly pointed ears,
enduring upright stance in undyed white layered wool, cold flat daylight, neutral pale-grey
backdrop, natural skin texture including chapping, no armor, no heavy jewellery, no fantasy glow
effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, apparent
late-20s female, tall 177 cm, lean hardy build, frost-pale skin, silver-white hair in a tight
practical braid, ice-blue eyes, subtly pointed ears, upright enduring stance in undyed pale-grey
layered wool, cold flat daylight, neutral pale-grey backdrop, natural skin texture, no armor, no
heavy jewellery, no fantasy glow effects.

**Build note.** Same pointed-ear gap as the other elves. Alfar's no-constitution-malus build is the
easiest of the three to keep reading as tough rather than fragile.

---

## 4. Hillback Empire

### Hillback Dwarves — Brakmor

**Silhouette and height.** Male 140–155 cm, female 133–147 cm — short and extremely broad, matching
the sharpest positive tilt in the table (constitution+2, strength+2 against
athleticism−1/impulse−2). Dense, not squat-cartoonish: adult head-to-body ratio stays adult, just
compressed and thick through torso and limbs — the oversized-head caricature is explicitly off the
table. Planted, low centre of gravity, unhurried (impulse−2 reads as deliberate). At 50 m: short and
wide as a door, and just as hard to move.

**Palette.** Skin weathered ruddy tan `#C48A5E`. Hair dark brown `#2B1D12`, black, or red `#7A3B1E`;
eyes brown to near-black. Forge-and-mine culture (Gornruk, "the Ironworks," is the entry
settlement): iron-black, undyed heavy leather, dark oxblood forge-pigment accents, dense undyed
wool. Little bright colour.

**Features.** Broad strong-jawed faces, heavy brow. Men wear beards long and thick, simply braided
or clasped, kept realistic in scale — a real adult-status marker, not floor-length costume. Women
don't share the beard convention; hair practical, braided close for forge/mine safety. Functional
iron/bronze beard clasps and rings, usually self-made. Forge scars and soot-staining are badges, not
blemishes.

**Clothing at level 1.** Heavy undyed wool tunic, thick leather trousers/skirt, no beard clasps yet,
plain hobnailed or leather boots.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, apparent 40s
male, short 148 cm and extremely broad dense-muscled build with adult body proportions, ruddy
weathered tan skin, thick dark-brown beard with a simple braid clasp, brown eyes, heavy brow,
planted low-centre-of-gravity stance in a heavy undyed wool tunic and thick leather trousers, warm
forge-adjacent lighting, neutral grey backdrop, natural skin texture with soot smudging, no armor,
no oversized head or childlike proportions.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, apparent
late-30s female, short 140 cm and broad dense-muscled build with adult body proportions, ruddy
weathered tan skin, dark hair braided tightly to the head, brown eyes, heavy brow, planted sturdy
stance in a heavy undyed wool tunic and thick leather skirt, warm forge-adjacent lighting, neutral
grey backdrop, natural skin texture, no armor, no oversized head or childlike proportions.

**Build note.** Hardest of the 12 "feasible" races, genuinely borderline. MetaHuman's custom-body
workflow supports short stature, but wide-ribcage-relative-to-short-height with adult limb ratios
sits outside default presets and needs hand-tuned proportions per sex, checked against "not
cartoony, not childlike" before approval. Budget an extra review pass.

---

## 5. Dew Hollow

### Woodling — Amberknot

**Silhouette and height.** Male 125–138 cm, female 119–132 cm — small forest folk, matching
finesse+2/survival+1/awareness+1 against strength−1/conditioning−1/discipline−2. Slight and nimble,
adult proportions kept carefully adult — the race most at risk of reading as a child if scaled
naively. Quick, restless, weight forward on the toes (discipline−2 as fidgeting, never settled). At
50 m: a child-sized adult that would rather already be gone.

**Palette.** Skin tawny bark-brown `#A9764F`. Hair auburn, gold, or brown `#7A4B23` — leaf colours,
matching Amberknot's "round gold-leaved thicket-town." Eyes amber `#A6752E` or green `#55702E`. Dyes
with autumn scrub: amber, russet, gold-leaf, brown — nothing that stands out against dry bracken,
since Woodlings dress to disappear into their own territory.

**Features.** Sharp small features, large watchful eyes relative to face (a real small-body-plan
trait, not stylization), subtle pointed ear tips (a Dew-Hollow-specific marker, subtler than the elf
races). Hair short or practically tied, both sexes. Faint natural bark-like skin mottling — species
trait, not tattoo — distinguishes Woodling from a simply-shrunk human. Minimal cord or carved
wood/seed-pod pendant.

**Clothing at level 1.** Undyed brown or russet rough-spun cloth, minimal cut, no leaf-toned dye yet
— drab on purpose, camouflage before craft.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, adult male
(small stature, adult proportions, not a child), 131 cm, slight nimble build, tawny bark-toned skin
with faint natural mottling, short auburn hair, amber eyes, subtly pointed ear tips, alert
forward-weighted restless stance in undyed russet rough-spun clothing, dappled forest daylight,
neutral grey backdrop, natural skin texture, no armor, no jewellery, no childlike proportions.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, adult
female (small stature, adult proportions, not a child), 125 cm, slight nimble build, tawny
bark-toned skin, short gold-brown hair tied back, green eyes, subtly pointed ear tips, alert
watchful stance in undyed brown rough-spun clothing, dappled forest daylight, neutral grey backdrop,
natural skin texture, no armor, no jewellery, no childlike proportions.

**Build note.** Bespoke model expected. Core problem is proportion at scale: MetaHuman's height
slider wasn't built for a 125–138 cm *adult*, and naive downscaling reads either as a scaled child
or as proportionally wrong. A bespoke/heavily-custom rig is safer; the bark-mottling skin is a
custom texture regardless.

### Gobbledrift — Rattledrift

**Silhouette and height.** Male 109–122 cm, female 104–117 cm — smallest race in the bible, matching
impulse+2/athleticism+1/detail+1 against wisdom−1/discipline−1/strength−2 (the single lowest
strength malus of all 16). Wiry, spindly, minimal muscle, slightly hunched — a scavenger's posture,
low and quick. Movement reads jittery and impulsive, never composed. At 50 m: the smallest,
twitchiest silhouette on the roster.

**Palette.** Skin sallow grey-green to grey-tan `#8E8368` — a genuine muted skin-tone variant, not a
cartoon-green cue. Hair sparse and dark `#221E18`. Eyes amber-yellow `#B08A2E` or dark. Rattledrift
is "roofed in salvaged sheet" — clothing follows: patchwork, mismatched scavenged and re-dyed cloth,
soot-black and rust dominant because it's salvageable, not chosen.

**Features.** Angular, sharp-featured, prominent ears — larger and more expressive than any other
race, kept proportion-realistic rather than comically oversized. Sparse patchy facial/head hair on
men. Both sexes show a built-in stooped, neck-forward posture. Scavenged found-object ornament — a
bent nail, wire, a button — not crafted jewellery.

**Clothing at level 1.** Patchwork rough cloth in muted browns/greys, deliberately mismatched (two
visibly different scraps is correct), no found-object jewellery yet — collected as the character
plays.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and profile, adult male
(very small stature, adult proportions, not a child), 115 cm, wiry spindly build with a stooped
neck-forward posture, sallow grey-tan skin, sparse dark patchy hair, amber-yellow eyes, prominent
proportionally-realistic ears, hunched restless stance in mismatched patchwork brown-grey rough
cloth, dim workshop-toned lighting, neutral grey backdrop, natural skin texture, no armor, no
cartoon-oversized features, no childlike proportions.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and profile, adult
female (very small stature, adult proportions, not a child), 110 cm, wiry spindly build, sallow
grey-green skin, sparse dark hair cropped short, dark eyes, prominent proportionally-realistic ears,
hunched alert stance in mismatched patchwork rough cloth, dim workshop-toned lighting, neutral grey
backdrop, natural skin texture, no armor, no cartoon-oversized features, no childlike proportions.

**Build note.** Bespoke required, more definitely than Woodling. At 109–122 cm the adult-proportion
problem is more acute, and the prominent-ear, sallow non-human skin tone push the head outside
MetaHuman's human head library regardless of what happens with the body.

### Fae — Hollowbell

**Silhouette and height.** Male 155–168 cm, female 148–161 cm — short-to-medium but reads
tall-and-thin from extreme slenderness, matching elements+3/spirit+2 against
strength−1/athleticism−1/conditioning−1/constitution−2 — mechanically the frailest stat combination
in the table alongside Mythic. Reed-thin, minimal mass, closer to a plant stem than a human frame.
Drifts rather than stands, weight barely settled. At 50 m: barely displaces the air around it.

**Palette.** Skin very pale, faintly translucent `#F4EDEA` with a hint of blue/green at temples and
wrists (a subsurface-scattering cue, not paint). Hair silvery-lilac `#C9B8D6` or moss-green
`#8FAE8A` — appropriate since Fae is explicitly non-human. Eyes large and pale, luminous `#CDEDE6`
or `#D8CDEF`. Hollowbell sits in "the Bloom" (crystal flowers) beside Dewglass (a still reflecting
pool): opalescent pale blue, lilac, dew-silver, nothing earthy or saturated.

**Features.** Delicate, finely-boned, large eyes relative to face (more pronounced than Woodling's),
minimal body hair, faint natural sheen to the skin. Hair worn loose and long, moving as if
underwater even in still shots. Naturalistic ornament — worked crystal or glass-like formations,
dew-drop shapes — never forged metal. No tattooing; the skin's translucency does that visual work.

**Clothing at level 1.** Undyed pale grey-white gauze-weight cloth, minimal cut, no opalescent
shimmer yet — even "plain" should look finer/thinner than any human race's linen.

**Reference prompt — male.** Photorealistic-leaning reference photo, three-quarter and profile,
apparent late-20s male, 161 cm, extremely slender reed-thin build, very pale skin with a faint cool
translucent quality at the temples, long silvery-lilac hair loose, large pale blue-green eyes,
drifting barely-weighted stance in minimal pale grey-white gauze-weight cloth, soft diffused
overcast light, neutral pale backdrop, subtle subsurface-scattering skin rendering, no armor, no
metal jewellery, no glitter or sparkle effects.

**Reference prompt — female.** Photorealistic-leaning reference photo, three-quarter and profile,
apparent mid-20s female, 154 cm, extremely slender reed-thin build, very pale translucent-toned
skin, long moss-green hair loose, large pale lilac eyes, drifting weightless-looking stance in
minimal pale gauze-weight cloth, soft diffused overcast light, neutral pale backdrop, subtle
subsurface-scattering skin rendering, no armor, no metal jewellery, no glitter or sparkle effects.

**Build note.** Bespoke required — not mainly for proportion (height is within human range) but for
materials: translucent, faintly luminous skin needs a custom subsurface-scattering shader beyond
MetaHuman's standard preset, and the large-eye proportion sits outside the head library. Body alone
might have survived on MetaHuman; skin and eyes push it to bespoke.

### Centaur — Longmane

**Silhouette and height.** Quadrupedal — both numbers matter. Withers height male 152–168 cm, female
142–158 cm (large draft/warmblood horse range). Total height (crown of head, torso upright) male
215–232 cm, female 200–217 cm — tallest race in the bible by a wide margin, matching
athleticism+2/conditioning+2 against finesse−1/detail−1/elements−2. Powerful, heavy-boned throughout
both halves — the strongest-reading race on the roster. At 50 m: half again the height of a mounted
rider, unmistakable before any other detail resolves.

**Palette.** Equine coat follows real horse genetics — bay `#6B3E22`, chestnut `#8B4A2B`, black,
dapple-grey `#A9A9A0`, dun `#B79A6B` — with natural markings (blaze, socks) as a real horse would
carry them; the strongest "ground it in reality" opportunity in the document. Human-torso skin is
independently variable, defaulting to sun-worked outdoor tan `#C69C6D`. Hair dark brown to black.
Tack is practical leather and rope, not dyed cloth — Centaurs have no torso-heavy clothing
tradition.

**Features.** Broad, strong-jawed human-torso face matching the powerful build; no pointed ears —
Centaur isn't part of the elf-mythology cluster. Hair short or tied back, clear of tack.
Functional-length facial hair on males. The equine-human waist transition is the single most
important sculpt point in the race and needs its own dedicated reference pass beyond text. Ornament
is functional tack only — leather straps, a woven girth-band — never jewellery.

**Clothing at level 1.** Simple leather or rope harness/vest across the torso, no dye, no tack
ornament yet. Least "clothing" of any race by design — most visual surface is coat, not cloth.

**Reference prompt — male.** Photorealistic reference photo of a centaur reference maquette: human
torso, adult male early-30s, broad powerful build, sun-worked tan skin, short dark hair tied back,
brown eyes, strong jaw, joined at the waist to a bay-coloured (`#6B3E22`) quadrupedal horse body
with black mane, tail, and a natural white blaze, withers height ~160 cm, standing four-square
relaxed on all four legs, wearing only a simple leather torso harness, natural daylight on an open
grassland plateau, realistic skin/coat texture with visible musculature at the join, no armor, no
fantasy glow, no exaggerated transition.

**Reference prompt — female.** Photorealistic reference photo of a centaur reference maquette: human
torso, adult female late-20s, strong athletic build, sun-worked tan skin, dark hair tied back, brown
eyes, joined at the waist to a dapple-grey (`#A9A9A0`) quadrupedal horse body with black mane and
tail, withers height ~148 cm, standing four-square relaxed, wearing only a simple leather torso
harness, natural daylight on an open grassland plateau, realistic skin/coat texture with visible
musculature at the join, no armor, no fantasy glow, no exaggerated transition.

**Build note.** Bespoke, unambiguously, by the widest margin of any race here. Needs a fully custom
skeleton (human spine grafted to a quadrupedal body), a custom four-legged locomotion rig, and a
full bespoke animation set (walk/trot/canter/gallop plus combat moves with no bipedal equivalent).
Realistically its own production line with its own schedule, not something the character-art lane
picks up alongside the other 15.

---

## 6. Open questions for Daniel

1. **Is MetaHuman actually the answer**, even for the 12 "feasible" races? This assumed it because
   it's free and fast — nothing has been decided. Full bespoke across all 16 for visual consistency
   is a materially different budget and timeline; settle this before anyone opens MetaHuman Creator.
2. **Elf ears.** No stock pointed-ear morph exists in MetaHuman. Mythic, Sidhe, and Alfar all need
   one — custom attachment mesh (cheaper, riskier close-up) or a fully custom head (safer, slower).
   Blocks all three elf races equally.
3. **Height range vs. slider limits.** Mythic tops out at 199 cm male; Gobbledrift bottoms out at
   104 cm female. Neither tested against MetaHuman's actual bounds — needs an engineering spike, not
   a design guess, before art starts on either.
4. **Fae's skin shader** is new work, not a reuse of the standard human skin preset. Who owns
   building it, and is it built once and shared or once per race that needs something similar?
5. **Centaur is a separate production line** — custom skeleton, quadrupedal rig, full bespoke
   animation set. It cannot ride on the same schedule as the other 15 without slipping something.
   Needs its own estimate and probably its own owner.
6. **Adaptive-outfit stress test.** Epic's adaptive clothing is assumed to resize cleanly across a
   body's sliders, untested at the extremes this bible requires (Hillback breadth, Mythic height,
   Centaur's torso-only coverage). One test garment on one extreme body before calling level-1
   clothing solved.
7. **Every hex value here is a proposal**, internally consistent and grounded in real dye/material
   sources, but nobody outside this session has signed off on them. React to this as a first draft,
   not a locked spec.
8. **Facial markings and invented-language conflicts.** No race in this draft got tattooed script or
   invented glyphs, deliberately — that's `names/great-north-places.md` territory (invented tongues
   for Hillback, Woodling, Gobbledrift, Fae, Centaur). Any future script-based marking needs a
   naming-doc check-in first, so glyphs aren't invented twice, differently, in two documents.

