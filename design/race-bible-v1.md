# Race Bible v1 — the 16 Great North races

**Drafted 2026-09-13 by the overnight build session. Status: DRAFT, awaiting Daniel's review.**

---

## 0. What this is, and how to read it

This is the visual bible the character-art lane builds against: what each of the 16
Great North races looks like, on both sexes, concretely enough that two different
artists (or an artist and an image model) produce the same person.

**Body tech: PROPOSED, not decided.** The working assumption is Epic's MetaHuman
(free with UE 5.8, parametric height/build, adaptive outfits) for the 12 human and
elf-adjacent races, with the four non-human Dew Hollow races (Woodling, Gobbledrift,
Fae, Centaur) expected to need bespoke models instead. This has **not** been put to
Daniel. Treat every "MetaHuman-feasible" line below as a bet the engineering lane
still has to confirm, not a green light. See §18.

**Realistic, never stylized.** Daniel's standing direction, restated because it
governs every choice in this document: photoreal proportions, photoreal skin,
photoreal cloth. No cartoon proportions, no big-head/small-body chibi scaling, no
oversized weapons-catalogue silhouettes. The Advanced Village Pack was rejected on
sight for reading as cartoony — that is the bar every race here has to clear, at
every size from Gobbledrift to Centaur.

**Clothes first.** Players start in plain clothes, no armor. Every "Clothing at
level 1" section below describes exactly that: the cheapest, plainest version of
what the culture wears, before any gear is earned. The richer "Palette" section
describes the culture's full dye range — what a veteran or an NPC noble might
wear — precisely so the art lane can see the ceiling a level-1 outfit is the floor
of.

**Data check, done before writing a word of this.** `data/factions/great-north.json`
confirms the 4 culture groups and 16 races exactly as briefed, no disagreement:

- **Crusaders** (8): Celtic, Germanic, Romance, Hellenic, Slavic, Baltic, Armenian, Aethiopes
- **Elves** (3): Mythic, Sidhe, Alfar
- **Hillback Empire** (1): Hillback Dwarves
- **Dew Hollow** (4): Woodling, Gobbledrift, Fae, Centaur

That is 16 races, matching `progression-v1.md` §3a exactly. Per that doc's own
framing, Great North is the European-mythic faction (`vision.md`) — which is why
every human culture below is grounded in a real-world European (or Caucasus, for
Armenian) regional variation, not a generic fantasy default.

**This document does not re-litigate stats.** `progression-v1.md` §3a ("Races:
different bases, and different growth rates") is APPROVED canon. It is quoted
below verbatim and used only as grounding for build — a race with a strength
malus should not sculpt like a strongman. Nothing here contradicts it; where a
physical read and a stat tilt would visibly clash, the stat tilt wins and the
physical description was adjusted to fit, not the reverse.

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

**How to read each race's section:** height first (the thing that reads at
distance), then palette (what a costume department would stock), then features
(face, hair, markings, ornament, sex differences), then the level-1 outfit,
then two reference-image prompts, then a build note flagging what is easy and
what is hard for the proposed tech.

---

## 1. Summary table

| Race | Culture group | Male height | Female height | Build | Silhouette read |
|---|---|---|---|---|---|
| Celtic | Crusaders | 170–184 cm | 158–171 cm | average, balanced | Average build, easy stance — the baseline human |
| Germanic | Crusaders | 178–193 cm | 166–179 cm | heavy, broad | Big-boned wall of a person, squared shoulders |
| Romance | Crusaders | 166–178 cm | 155–166 cm | slim, upright | Slim, upright, unhurried elegance |
| Hellenic | Crusaders | 173–186 cm | 161–173 cm | athletic, lean | Athletic taper, gymnasion posture |
| Slavic | Crusaders | 176–190 cm | 164–177 cm | broad, sturdy | Broad and grounded, low centre of gravity |
| Baltic | Crusaders | 174–187 cm | 162–175 cm | tall, wiry | Tall and rangy, watchful stillness |
| Armenian | Crusaders | 169–182 cm | 157–169 cm | stocky, compact | Compact, upright, monastic stillness |
| Aethiopes | Crusaders | 171–183 cm | 159–171 cm | lean, drilled | Lean, drilled posture, parade-ground spine |
| Mythic | Elves | 185–199 cm | 174–187 cm | willowy, attenuated | Very tall, attenuated, floats rather than walks |
| Sidhe | Elves | 180–193 cm | 169–182 cm | lithe, agile | Tall, coiled, fox-quick |
| Alfar | Elves | 182–195 cm | 171–184 cm | lean, hardy | Tall, rangy, weather-hardened elf |
| Hillback Dwarves | Hillback Empire | 140–155 cm | 133–147 cm | short, dense | Short and wide as a door |
| Woodling | Dew Hollow | 125–138 cm | 119–132 cm | small, nimble | Child-sized adult, quick, alert |
| Gobbledrift | Dew Hollow | 109–122 cm | 104–117 cm | tiny, spindly | Smallest silhouette, hunched, jittery |
| Fae | Dew Hollow | 155–168 cm | 148–161 cm | reed-thin, willowy | Reed-thin, drifts, barely displaces air |
| Centaur | Dew Hollow | 215–232 cm total / 152–168 cm withers | 200–217 cm total / 142–158 cm withers | powerful, quadrupedal | Half again the height of a mounted rider, unmistakable |

---

## 2. Crusaders

### Celtic — Dál Riata

**Silhouette and height.** Male 170–184 cm, female 158–171 cm. This is the
deliberate baseline: `progression-v1.md` calls Celtic "the flattest profile," the
first race a new player meets, and the physical read follows that — average
build, easy weight-bearing stance, nothing exaggerated. Male build is
medium-framed with working-outdoors muscle, not a bodybuilder's. Female build is
athletic-average, upright, unhunched. At 50 m: the person you'd fail to describe
to a sketch artist — proportionate, comfortable, unremarkable until they move.

**Palette.** Skin fair to lightly weathered, `#E8C4A2` base with a ruddy
wind-flush at cheeks and nose. Hair spans auburn `#8B4513`, dark brown `#3B2A20`,
and black `#1C1410`, with true red `#A0522D` common enough to be a recognized
Dál Riata trait. Eyes blue `#4A6D8C`, green `#4C7A5A`, grey `#7A8A8C`, hazel.
Culture dyes with what a wet Atlantic island grows: madder root for red-brown,
woad for a dull blue-grey (never a bright dye-shop blue — small-batch and
uneven), walnut hulls for warm brown, and a lot of undyed cream and oatmeal
wool because dyeing is labour a farming island doesn't always spend. Checked
weaves (two or three plain colours crossed, not clan tartan) are the local
weaver's default pattern, not decoration.

**Features.** Face structure varies more than any other race here on purpose —
it's the baseline, so it absorbs the widest range: broad or narrow, straight or
slightly upturned noses, no dominant type. Men wear short beards or go
clean-shaven; long hair tied back for work is more common than short-cropped.
Women wear hair loose, braided, or half-bound; no cultural pressure either way.
Freckling is common on fair skin. Ornament is small worked-bronze or silver
brooches (functional, pin the cloak) rather than jewellery for its own sake.
No tattooing or scarification — Dál Riata's visual signature is textile, not
skin.

**Clothing at level 1.** Undyed linen shirt or shift, oatmeal or grey wool
tunic/dress to the knee (men) or calf (women), simple leg wraps or trews, rawhide
or plain leather shoes. No brooch yet — that's earned, not started with. The
only colour is the natural range of undyed fibre: cream, grey-brown, a faded
oat-yellow.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and
profile, adult male early 30s, Irish/Scottish Gaelic coloring, 178 cm, medium
working build with visible forearm and shoulder muscle from manual labour, fair
skin with windburn at cheeks and nose bridge, medium-brown hair to the collar
tied back, short unstyled beard, hazel eyes, standing relaxed weight-bearing
pose in an undyed cream linen shirt and oatmeal wool tunic, natural overcast
daylight, neutral grey backdrop, visible skin pores and minor scarring on
knuckles, no armor, no jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter and
profile, adult female late 20s, Irish/Scottish Gaelic coloring, 165 cm, athletic
average build, fair freckled skin, auburn hair in a loose single braid, green
eyes, standing relaxed pose in an undyed linen shift under a grey wool dress to
mid-calf, plain leather shoes, natural overcast daylight, neutral grey backdrop,
visible skin texture and freckling, no armor, no jewellery, no idealized
retouching.

**Build note.** MetaHuman-feasible, and the easiest race in the bible — the
whole point of "flattest profile" is that it needs the least deviation from
MetaHuman's own defaults. Use this race to validate the pipeline before
attempting anything with a stat-driven extreme.

### Germanic — Miklagarðr

**Silhouette and height.** Male 178–193 cm, female 166–179 cm — the tallest and
heaviest human culture, matching the strength+2/conditioning+1 tilt. Broad
shoulder line, thick neck, weight carried forward in the chest and forearms.
Female build is tall and strong-framed rather than slight; this is a cold
mountain culture and frailty doesn't survive it. Posture is square and settled,
feet planted. At 50 m: the widest human shoulder line on the roster.

**Palette.** Skin fair to pale, `#F0D5B8`. Hair flax-blond `#D8C08A` to light
brown `#8A6642`; darker hair exists but blond dominates. Eyes blue `#5A85B0`,
steel-grey `#8C9AA0`. Dyes lean on what a frost-forest mountain kingdom has:
indigo/woad blue for status colour, iron-oxide rust-brown from bog ore residue,
undyed wool in heavy natural browns and greys for everyday wear, and fur trim
(wolf, bear) as the practical cold-weather answer rather than decoration.

**Features.** Strong squared jaw common to both sexes; broad cheekbones. Men
wear beards long and often braided at the chin — a real marker of status and
age, not universal on younger men. Hair worn long, sometimes half-braided back
from the face for combat practicality. Women wear hair in thick single or
double braids, occasionally wound and pinned. Ornament is worked silver and
bronze — arm rings, cloak pins — sized to be worn while working, not delicate.
No facial tattooing; occasional forearm scarring from labour and combat is
treated as unremarkable, not hidden.

**Clothing at level 1.** Heavy undyed wool tunic in natural brown or grey,
wool trousers (men) or a long wool overdress (women) belted at the waist with
plain rope or leather, no fur trim yet — that's a later-level or crafted item,
not a starting good. Practical, warm, unadorned.

**Reference prompt — male.** Photorealistic reference photo, three-quarter and
profile, adult male mid-30s, Scandinavian/Norse coloring, 186 cm, heavy
broad-shouldered build with thick forearms, pale skin, long flax-blond hair
tied back, full braided beard, blue eyes, standing square weight-bearing pose
in a heavy undyed brown wool tunic and trousers, cold overcast daylight,
neutral grey backdrop, weathered skin texture with wind-chapped lips, no armor,
no jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female early 30s, Scandinavian/Norse coloring, 172 cm, tall
strong-framed build, fair skin, light-brown hair in a thick double braid, grey
eyes, standing square confident pose in a heavy grey wool overdress belted at
the waist, cold overcast daylight, neutral grey backdrop, realistic skin
texture, no armor, no jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. The heavy/broad end of MetaHuman's build
slider covers this without much fuss; the only extra care is the beard groom
(braided sections need a custom groom, not a stock beard preset).

### Romance — Italics Romana

**Silhouette and height.** Male 166–178 cm, female 155–166 cm — the shortest
and leanest human culture, matching knowledge+2/logic+1 against strength−1.
Build is slim, upright, unhurried; this reads as a mercantile and scholarly
culture rather than a martial one. Posture is composed rather than stiff —
courtly ease, not parade discipline (that's Aethiopes). At 50 m: the person who
looks like they arrived by carriage, not on foot.

**Palette.** Skin olive `#D9B48F`. Hair dark brown `#3C2A1E` to black `#1A1410`,
almost no fair hair. Eyes brown `#4B3221`, hazel `#6B4E31`. Valmonde sits in
orchard and vine country (Marvigne is literally "Sea Vine"), so the dye
economy runs on wine-lees red-purple, olive-oil-adjacent olive green, and
cream linen bleached in Mediterranean sun. Gold ochre trim signals the
merchant-syndicate wealth the region is known for.

**Features.** Narrower faces than the Germanic/Slavic cluster, straighter
noses, more defined cheekbones. Men keep hair short to medium, often oiled or
combed rather than left wild; clean-shaven or a close, shaped beard —
groomed, deliberate. Women wear hair up or elaborately bound more often than
loose; this is a culture that dresses for an audience. Ornament is the most
visible of any Crusader human race short of Armenian — rings, ear ornaments,
fine chains — signalling the syndicate/merchant economy (syndicate and
relic-master are both allowed classes here). No tattooing.

**Clothing at level 1.** Cream linen shirt or shift, unadorned — the gold
ochre and wine-red belong to status pieces earned later, not starting cloth.
Simple dark wool trousers (men) or an ankle-length undyed linen dress
(women), a plain woven belt. Neat, not poor — this is a culture where even
the cheapest cloth is cut cleanly.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male late 20s, Mediterranean French/Italian coloring, 172
cm, slim upright build, olive skin, short dark-brown hair neatly combed, a
close shaped beard, brown eyes, standing composed relaxed pose in an
unadorned cream linen shirt and dark wool trousers, warm daylight, neutral
grey backdrop, realistic skin texture, no armor, no jewellery, no idealized
retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female mid-20s, Mediterranean French/Italian coloring, 160
cm, slim graceful build, olive skin, dark hair bound up at the back of the
head, hazel eyes, standing composed pose in a plain cream linen floor-length
dress, warm daylight, neutral grey backdrop, realistic skin texture, no
armor, no jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. Slim body-fat/muscle sliders at the low
end handle the build; the groomed-hair and ear-ornament detailing is a
texture/prop task, not a body-tech problem.

### Hellenic — Leukopolis

**Silhouette and height.** Male 173–186 cm, female 161–173 cm — athletic and
lean, matching athleticism+2/logic+1. Visible muscle definition without
Germanic bulk: a runner's or wrestler's build, not a strongman's. Posture is
upright and open-chested, gymnasion-trained. At 50 m: the athletic taper —
wide shoulders narrowing cleanly to the waist.

**Palette.** Skin olive-tan `#CBA07C`. Hair dark brown to black `#2E2013`,
often with a slight wave/curl. Eyes brown `#3F2A1A`, hazel-green `#5C6B3E`.
Everyday dye is bleached cream/white linen and wool (the famous "white"
Aegean look, achieved by sun-bleaching, not left-undyed grey) with olive-green
and saffron-yellow accents from local plants. Tyrian purple exists in this
world as an extremely rare, expensive trim — reserved for temple and noble
pieces, never a starting-clothes colour.

**Features.** Strong, straight-nosed profile (the "classical" facial line);
defined jaw. Men wear hair short to medium, frequently curled or waved,
clean-shaven or a short beard — the gymnasion aesthetic, groomed athleticism.
Women wear hair bound up, often with a simple fillet/band, exposing the neck.
Ornament is understated bronze and terracotta rather than heavy metal — this
is a culture that shows off the body, not the jewellery box. No tattooing.

**Clothing at level 1.** Undyed or lightly bleached linen chiton-style wrap
for both sexes — a single rectangular cloth pinned at the shoulder(s) and
belted at the waist, knee-length for men, ankle-length for women, plain
leather sandals. No purple, no saffron yet — that comes later.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male mid-20s, Mediterranean Greek coloring, 179 cm,
athletic lean build with visible muscle definition, olive skin, short dark
curled hair, clean-shaven, brown eyes, standing open-chested confident pose
in an undyed linen chiton pinned at one shoulder and belted at the waist,
sandals, bright daylight, neutral grey backdrop, realistic skin texture, no
armor, no jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female early 20s, Mediterranean Greek coloring, 166 cm,
athletic lean build, olive skin, dark hair bound up with a simple cloth
fillet, hazel-green eyes, standing upright pose in an ankle-length bleached
linen chiton belted at the waist, sandals, bright daylight, neutral grey
backdrop, realistic skin texture, no armor, no jewellery, no idealized
retouching.

**Build note.** MetaHuman-feasible. Athletic-lean presets are a core MetaHuman
use case; the chiton is a simulated-cloth/adaptive-outfit task, not a body
problem, though a single-pinned wrap cloth will need real cloth sim to not
look stiff.

### Slavic — Borograd

**Silhouette and height.** Male 176–190 cm, female 164–177 cm — broad and
sturdy, matching constitution+2/conditioning+1. Build carries weight low and
wide: thick torso, sturdy legs, a low centre of gravity built for cold and
labour rather than speed. At 50 m: broad and grounded, the opposite lean from
Baltic next door.

**Palette.** Skin fair to medium `#E3C1A0`. Hair ash-blond `#C2A876` to brown
`#6B4A32`. Eyes blue-grey `#7C93A0`, hazel. Pine-wood country dyes: bark and
onion-skin browns, forest-green from local dye plants, and — the culture's
real signature — red thread embroidery worked onto undyed white linen. The
colour statement here is a small amount of saturated red on a field of
natural white, not an overall dyed garment.

**Features.** Broad, rounder faces than the Baltic cluster; strong
cheekbones. Men wear beards fuller and less groomed than Germanic's braided
style — practical cold-weather growth. Hair medium length, often under a
simple cap or wrap outdoors. Women wear hair braided and often covered with
a plain cloth wrap or kerchief, especially married women — a real and
recognizable regional convention, not universal but common enough to read as
cultural. Embroidery motifs (geometric, floral) appear on cuffs and collars
as the primary ornament — textile, not metal.

**Clothing at level 1.** Undyed white/cream linen shirt, no embroidery yet
(that's earned or crafted, not starting), plain wool trousers (men) or skirt
(women), a simple woven belt, a plain head-wrap available but not required
for the female starting outfit.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male mid-30s, Eastern European Slavic coloring, 183 cm,
broad sturdy build with a low centre of gravity, fair skin, ash-blond full
beard, medium-brown hair under a simple cap, blue-grey eyes, standing
grounded solid pose in an undyed white linen shirt and plain wool trousers,
overcast daylight, neutral grey backdrop, realistic weathered skin texture,
no armor, no jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female late 20s, Eastern European Slavic coloring, 170
cm, sturdy broad-framed build, fair skin, brown hair in a braid under a
plain cloth headwrap, hazel eyes, standing grounded pose in an undyed white
linen blouse and plain wool skirt, overcast daylight, neutral grey backdrop,
realistic skin texture, no armor, no jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. Broad/sturdy sits well inside default
sliders; the embroidery detail is a texture-map task for later gear, not a
level-1 concern.

### Baltic — Laukapils

**Silhouette and height.** Male 174–187 cm, female 162–175 cm — tall and lean
rather than broad, matching awareness+2/survival+1 against strength−1. Build
is rangy: long-limbed, economical muscle, built for watching and walking
long distances rather than close combat. Posture is alert, weight balanced
forward slightly. At 50 m: tall and watchful, the stillness of someone
scanning the treeline.

**Palette.** Skin fair `#EAD0B0`. Hair flaxen `#E0C88E` to light brown
`#9C7B50`, the fairest hair range among the human cultures alongside
Germanic. Eyes pale blue `#A9C4D6`, grey. The regional signature good is
amber — literal Baltic amber, worn as beads and pendants — paired with pale
undyed linen and muted moss-green and madder-brown from local dye sources.
Amber is the one "jewel" material any Great North human culture wears as a
matter of course, not luxury.

**Features.** Long faces, high cheekbones, pale brows and lashes that read
almost invisible against fair skin. Men wear hair short to shoulder-length,
usually unbound for freedom of movement (rangers, scouts); light stubble to
short beard. Women wear hair in single long braids, often threaded with a
strip of amber beads rather than worn loose — practical and decorative at
once. Amber pendants/beads are the primary ornament for both sexes. No
tattooing.

**Clothing at level 1.** Undyed pale linen shirt/shift, muted moss-green or
undyed wool overlayer, no amber yet — amber jewellery is a status/earned
item, not a starting good. Practical travelling cut, nothing loose that
would catch on brush.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male late 20s, Baltic (Lithuanian/Latvian) coloring, 180
cm, tall lean rangy build, fair skin, flaxen hair loose to the shoulder,
light stubble, pale blue eyes, standing alert forward-weighted pose in an
undyed pale linen shirt and moss-green wool overlayer, cool daylight,
neutral grey backdrop, realistic skin texture, no armor, no jewellery, no
idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female mid-20s, Baltic coloring, 168 cm, tall lean build,
fair skin, flaxen hair in a single long braid, pale grey eyes, standing
alert watchful pose in an undyed linen shift under a plain wool overdress,
cool daylight, neutral grey backdrop, realistic skin texture, no armor, no
jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. Tall/lean is a stock combination; amber
bead props are a jewellery-asset task for later gear tiers.

### Armenian — Lusavank

**Silhouette and height.** Male 169–182 cm, female 157–169 cm — compact and
sturdy rather than tall, matching spirit+2/discipline+1 against
athleticism−1. Build is stocky-strong: dense through the shoulders and
torso, not tall enough to dominate a room but built to stand still in one
for a long service. Posture is upright, unhurried, monastic — devotional
stillness rather than martial readiness. At 50 m: compact and grounded, the
person who doesn't fidget.

**Palette.** Skin olive-tan `#C99B72`. Hair black `#1C140F` to dark brown
`#3B2415`, almost always dark. Eyes dark brown `#2E1D10`. The signature dye
is a deep, saturated red historically unique to the Armenian highlands
(cochineal from a native scale insect, distinct from the madder red used
elsewhere in Dál Riata or Slavic lands) — a genuinely different red from
every other Crusader culture's, worth keeping visually distinct. Paired with
black monastic wool, and warm gold-brown and apricot tones (the highlands
are famous for the fruit) for everyday wear.

**Features.** Strong brow, aquiline nose, dark hair and eyes as a near-fixed
type — the least varied face shape of the eight human cultures, deliberately,
to read as a tight-knit highland culture. Men wear short beards, neatly kept,
rarely clean-shaven — a monastery-adjacent culture where grooming reads as
discipline. Hair short to medium for men. Women wear hair covered or bound
under a simple cloth for modesty in devotional settings, loose or braided
otherwise. Ornament is minimal and symbolic — a small worn cross or carved
stone pendant — rather than decorative metalwork. No tattooing.

**Clothing at level 1.** Undyed dark wool tunic or dress, unbleached
linen underlayer, no red dye yet (that is a status/ceremonial colour, not a
starting one) — level-1 Armenian reads almost monochrome, black-brown-cream,
until the character earns the right to wear the culture's red.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male mid-30s, Armenian/Caucasus coloring, 176 cm, stocky
compact build, olive-tan skin, black short beard neatly kept, dark hair
short, dark brown eyes, strong brow and aquiline nose, standing upright
still pose in an undyed dark wool tunic over cream linen, soft indoor-quality
daylight, neutral grey backdrop, realistic skin texture, no armor, no
jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female late 20s, Armenian/Caucasus coloring, 163 cm,
compact sturdy build, olive-tan skin, dark hair covered with a plain cloth
wrap, dark brown eyes, strong brow, standing calm upright pose in an undyed
dark wool dress over cream linen, soft daylight, neutral grey backdrop,
realistic skin texture, no armor, no jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. Compact/stocky sits inside default
sliders; the tight facial-type range (deliberately less varied) means fewer
head presets are needed per sex than for Celtic, which is a net time saver.

### Aethiopes — Crucivallum

> **Renamed from Severus, 2026-09-13 (Daniel).** The Aethiopes are the Empire's Black Africans — *Aethiopes* is the Greek and Roman name for the peoples south of Egypt. They are the Empire-born diaspora of the Crusader realm; their home kingdoms (Kush, Aksum, Mali, the Bantu) sit in the Mystic Lands' Alkebulan. The name is the Empire's word for them: a people named by the state they serve.

**Silhouette and height.** Male 171–183 cm, female 159–171 cm — lean and
upright, matching detail+2/calmness+1 against strength−1/conditioning−1.
This is the Empire's administrative-military core, and it should read that
way: drilled posture, spine straight, minimal wasted motion, not physically
imposing so much as precisely held. At 50 m: the only human silhouette that
reads as "at attention" even at rest.

**Palette.** Skin deep brown to near-black, the range of the Nile Valley and the Sahel inside the Roman world: `#6B4226` through `#3B2314` to `#221410`; no olive end. Hair black `#120C0A`, tight-curled, worn close-cropped in the drilled style (veterans grey early; age-appropriate, not universal). Eyes dark brown `#2E1B10`. This is the one Crusader culture whose dye is institutional rather than folk — iron-grey and dark maroon-red from the Empire's own workshops, not household dyeing, plus undyed black leather; gold and copper are the only ornament (a single earring, a torque of rank). Deliberately restrained next to Romance's ochre and Armenian's
scarlet: an imperial-administrative palette, not a folk one.

**Features.** Angular, disciplined faces; close-cropped hair or shaved
sides on men, clean-shaven or a short regulation beard — a legionary-cut
look, not a folk one. Women who serve the Empire (several allowed classes
here are combat/martial) wear hair bound tightly back, functional rather
than styled. Ornament is rank-marking rather than decorative: a small
brand, badge, or tattooed unit mark is appropriate here specifically — the
one Crusader human culture where a discreet mark (forearm or nape) reads as
correct rather than exceptional, because it signals rank/unit, not folk
identity.

**Clothing at level 1.** Undyed grey-brown linen shirt, plain dark wool
trousers or skirt, no unit mark yet, no maroon trim — those are earned
Empire-issue items, not a recruit's starting kit. Deliberately the most
utilitarian starting outfit among the eight humans: Tirocastra is a recruit
camp, and it dresses everyone the same.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male early 30s, Anatolian/Levantine Mediterranean
coloring, 177 cm, lean upright build with drilled straight posture, olive
skin, close-cropped dark hair, short regulation beard, brown eyes, standing
at-ease military posture in a plain grey-brown linen shirt and dark wool
trousers, flat even daylight, neutral grey backdrop, realistic skin texture,
no armor, no jewellery, no idealized retouching.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female late 20s, Anatolian/Levantine Mediterranean
coloring, 165 cm, lean upright build, olive skin, dark hair pulled tightly
back, hazel eyes, standing at-ease military posture in a plain grey-brown
linen shirt and dark wool skirt, flat even daylight, neutral grey backdrop,
realistic skin texture, no armor, no jewellery, no idealized retouching.

**Build note.** MetaHuman-feasible. Lean/upright is a stock preset;
close-cropped hair and any rank-mark tattoo are texture tasks. The main
risk is genericness — without the grey/maroon institutional palette and
drilled posture, Aethiopes can read as a re-skinned Romance or Hellenic.

---

## 3. Elves

### Mythic — Argyrion

**Silhouette and height.** Male 185–199 cm, female 174–187 cm — the tallest
and most attenuated race short of Centaur, matching the sharpest malus
combination in the whole race table (strength−1, conditioning−1,
constitution−2 against elements+3). Build is willowy to the point of looking
underweight by human standards without reading as sickly — elongated limbs,
narrow shoulders, minimal visible muscle. Posture is unnaturally still and
composed. At 50 m: the tallest thing in the crowd that isn't a Centaur, and
the one that doesn't seem to be working to stay upright.

**Palette.** Skin cool porcelain `#F1E6DA`, near-luminous, no ruddiness. Hair
silver `#D8D6D2` or pale gold `#E4D9A8` — the "silvered" register the naming
doc calls for. Eyes silver-grey `#B8C0C4` or pale violet `#B7A8C4` — the one
human-adjacent race group where an unusual eye colour is appropriate, since
Mythic is explicitly the elf race, not a human culture. Culture dyes in
moon-white, pale gold, and washed-out pale blue — nothing saturated. Argyrion
("the Silver Place") is the visual thesis: metal-cool, pale, quiet.

**Features.** Long, narrow faces, high fine cheekbones, pointed ears (see
build note). Men and women are both slender-faced with minimal visible body
hair — no beards; Mythic men are depicted clean-faced, which is itself a
distinguishing marker from every bearded-option human culture. Hair worn
long and unbound or in a single simple plait for both sexes — elaborate
styling reads too "worked," and this culture's whole affect is effortless.
Ornament is minimal worked silver, thin chains, no gemstones — anything
heavier fights the willowy frame. No tattooing; skin is kept visually
"unmarked" as part of the ethereal read.

**Clothing at level 1.** Undyed pale linen or raw silk-look tunic/dress in
moon-white or oat, no silver thread yet, minimal cut, floor- or
ankle-length even at level 1 (this culture doesn't do short hemlines) —
plain but never scruffy; Mythic should look composed even in starting
cloth.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male apparent late-20s, very tall 192 cm, extremely
slender build with narrow shoulders and long limbs, cool pale porcelain
skin with no ruddiness, long straight silver-white hair worn loose,
clean-shaven, pale silver-grey eyes, subtly pointed ear tips, standing
perfectly still composed pose in an undyed pale moon-white linen tunic,
soft diffused studio daylight, neutral pale grey backdrop, realistic skin
texture despite the pale tone (visible pores, not airbrushed), no armor, no
jewellery beyond a thin silver chain, no fantasy glow or particle effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female apparent mid-20s, very tall 180 cm, extremely
slender willowy build, cool pale porcelain skin, long straight pale-gold
hair loose or in a single simple plait, pale violet-grey eyes, subtly
pointed ear tips, standing composed still pose in an ankle-length undyed
pale linen dress, soft diffused studio daylight, neutral pale grey
backdrop, realistic skin texture, no armor, no heavy jewellery, no fantasy
glow or particle effects.

**Build note.** Feasible on MetaHuman for body and proportion, but with two
real gaps to flag: (1) MetaHuman ships **no pointed-ear morph** — every elf
race needs either a custom ear attachment mesh or a modified head asset,
which is extra pipeline work multiplied across all three elf races; (2) at
185–199 cm male, Mythic sits at or past the edge of MetaHuman's default
height slider range and will need the extended/custom skeletal scale
verified before art starts (see §18).

### Sidhe — Tara

**Silhouette and height.** Male 180–193 cm, female 169–182 cm — tall and
agile rather than attenuated, matching finesse+2/awareness+2 against the
same strength−1/conditioning−1/constitution−2 frailty as Mythic, but the
higher finesse/awareness reads as coiled and quick rather than merely thin.
Build is lean-athletic, not underfed — a fencer's or dancer's frame. Posture
is alert, weight on the balls of the feet. At 50 m: tall, but moving before
you finish noticing them.

**Palette.** Skin pale with a cool undertone `#EBDFD4`. Hair raven-black
`#100C0A` or copper-red `#B5551D` — the two extremes, little in between.
Eyes green `#3E7A52` or violet-grey `#8477A0`. Tara's register is "mounds,
dreams, quarters rather than forts" — deep moss greens, dusk purples, and
worked bronze/copper ornament (Celtic-adjacent metalwork, since Sidhe pairs
mythologically with Celtic). No bright saturated colour; everything reads
slightly dusk-lit even in daylight reference.

**Features.** Angular, fox-like facial structure — pointed chin, high sharp
cheekbones, pointed ears. Men wear hair long and loose or in narrow braids
at the temple; little to no facial hair, and what exists is kept very
short. Women wear hair elaborately loose — deliberately unbound and
wild-looking, the opposite of Mythic's composed plait, to mark Sidhe as the
fae-wild elf rather than the serene one. Ornament is bronze/copper spirals
and knotwork, worn at wrist and throat. No tattooing, but subtle natural
skin markings (a dusting of nearly-invisible freckling in an unusual
grey-green tone) are appropriate as a species trait, not applied art.

**Clothing at level 1.** Undyed dark-grey or moss-toned linen, minimal cut,
close to the body (Sidhe clothing is not loose the way Celtic's is — it
should never catch on branches). No bronze ornament yet at level 1.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male apparent late-20s, tall 186 cm, lean athletic
coiled build, pale cool-toned skin, long raven-black hair loose with a
narrow temple braid, no facial hair, green eyes, sharp fox-like cheekbones,
subtly pointed ears, standing alert weight-forward pose in an undyed
dark-moss linen tunic close-fitted to the body, dusk-toned soft daylight,
neutral grey backdrop, realistic skin texture, no armor, no heavy jewellery,
no fantasy glow effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female apparent mid-20s, tall 175 cm, lean agile build,
pale cool-toned skin, long copper-red hair loose and slightly windblown,
violet-grey eyes, sharp cheekbones, subtly pointed ears, standing alert
poised pose in an undyed dark-grey linen wrap close to the body, dusk-toned
soft daylight, neutral grey backdrop, realistic skin texture, no armor, no
heavy jewellery, no fantasy glow effects.

**Build note.** Same MetaHuman gaps as Mythic (no stock pointed-ear morph),
but Sidhe's height range (180–193 cm) sits closer to MetaHuman's normal
bounds than Mythic's, so the skeletal-scale risk is lower. The
"deliberately wild, windblown" hair groom is a higher-effort hair asset
than Mythic's simple straight styles.

### Alfar — Vetrholt

**Silhouette and height.** Male 182–195 cm, female 171–184 cm — tall, and
notably the hardiest of the three elf races: the base profile carries no
strength or constitution malus at all (only conditioning−2, plus
knowledge−1 and calmness−1), which should read physically as a tougher,
more weathered elf than Mythic or Sidhe, not a frailer one. Build is lean
but sinewy, built for cold and distance rather than a duelist's quickness.
Posture is upright and enduring rather than coiled. At 50 m: elf-tall, but
the one that looks like it could actually survive a winter outdoors.

**Palette.** Skin frost-pale `#F3ECE4`, cooler and flatter than Mythic's
luminous porcelain. Hair white-blonde `#EDEAE2` or silver `#D6D6D6`. Eyes
ice-blue `#AEDDE8`. Vetrholt's register is "colder and cleaner than the
Germanic" per the naming doc — pure white, ice-blue, pale grey, with silver
fox or white fur trim as the practical cold-weather answer, echoing
Germanic's fur-trim logic but in a paler, cleaner key.

**Features.** Angular but broader through the jaw than Mythic or Sidhe —
this is the "hunter elf," not the "dream elf." Pointed ears, smaller and
less exaggerated than Sidhe's. Men wear hair cropped shorter than the other
two elf races (practical, cold-weather) or in a single tight braid; short
or no beard — elves stay beardless across all three races as a
species-level convention. Women wear hair in tight practical braids, rarely
loose. Ornament is worked silver in simple geometric (not spiral/knotwork)
patterns, echoing the Old Norse register. No tattooing; skin may show
genuine cold-weather chapping at cheeks/nose, unlike Mythic's untouched
porcelain.

**Clothing at level 1.** Undyed white or pale-grey wool, close-fitted and
layered for cold, no fur trim yet. The plainest of the three elf starting
outfits, appropriately, since Vetrholt is the most utilitarian elf culture.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male apparent early-30s, tall 188 cm, lean sinewy
weather-hardened build, frost-pale skin with slight cold-chapping at cheeks,
white-blonde hair cropped short, no beard, ice-blue eyes, subtly pointed
ears, standing enduring upright pose in undyed white wool layered clothing,
cold flat daylight, neutral pale-grey backdrop, realistic skin texture
including chapping, no armor, no heavy jewellery, no fantasy glow effects.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female apparent late-20s, tall 177 cm, lean hardy build,
frost-pale skin, silver-white hair in a tight practical braid, ice-blue
eyes, subtly pointed ears, standing upright enduring pose in undyed
pale-grey wool layered clothing, cold flat daylight, neutral pale-grey
backdrop, realistic skin texture, no armor, no heavy jewellery, no fantasy
glow effects.

**Build note.** Same pointed-ear gap as the other two elves. Alfar's
no-constitution-malus build is the easiest of the three elves to keep
looking convincingly "tough" rather than fragile — least risk of reading
as underweight.

---

## 4. Hillback Empire

### Hillback Dwarves — Brakmor

**Silhouette and height.** Male 140–155 cm, female 133–147 cm — short and
extremely broad, matching the sharpest positive tilt in the table
(constitution+2, strength+2) against athleticism−1/impulse−2. Build is
dense rather than squat-cartoonish: proportionally adult (head-to-body ratio
stays in adult range, not the oversized-head dwarf-caricature look Daniel's
direction explicitly rules out), just compressed and thick through the
torso and limbs. Posture is planted, low centre of gravity, minimal wasted
movement (impulse−2 reads as deliberate, unhurried). At 50 m: short and
wide as a door, and just as hard to move.

**Palette.** Skin weathered ruddy tan `#C48A5E` — forge and mine work,
outdoor colour on a mountain-dwelling people. Hair dark brown `#2B1D12`,
black, or red `#7A3B1E`; eyes brown `#4A3320` to near-black. Brakmor is a
forge-and-mine culture (Gornruk, "the Ironworks," is the entry settlement),
so the palette is iron-black, undyed heavy leather, dark oxblood-red
accents from forge dye/pigment rather than plant dye, and undyed dense
wool. Little bright colour — practicality and heat-resistance over display.

**Features.** Broad, strong-jawed faces, heavy brow. Men wear beards long,
thick, and often worked (simple braids or clasps, not ornate) — a real and
central marker of adult male status in this culture, but kept realistic in
scale, not floor-length costume-beard. Women do not share the beard
convention; hair worn practical, usually braided close to the head for
forge/mine safety. Ornament is functional metalwork — iron or bronze beard
clasps, simple rings — made by the wearer's own trade more often than
bought. No tattooing; forge scars and soot-staining are treated as
badges, not blemishes.

**Clothing at level 1.** Heavy undyed wool tunic, thick leather trousers or
skirt, no beard clasps yet (earned/crafted), practical hobnailed or thick
leather boots. Dense, plain, built for work rather than show.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male apparent 40s, short 148 cm and extremely broad
dense-muscled build with adult body proportions (not child-like), ruddy
weathered tan skin, thick dark-brown beard with a single simple braid clasp,
brown eyes, heavy brow, standing planted low-centre-of-gravity pose in a
heavy undyed wool tunic and thick leather trousers, warm forge-adjacent
indoor lighting, neutral grey backdrop, realistic skin texture with visible
soot smudging and scarring, no armor, no idealized retouching, no
cartoon-proportioned oversized head.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female apparent late-30s, short 140 cm and broad
dense-muscled build with adult body proportions, ruddy weathered tan skin,
dark hair braided tightly to the head, brown eyes, heavy brow, standing
planted sturdy pose in a heavy undyed wool tunic and thick leather skirt,
warm forge-adjacent indoor lighting, neutral grey backdrop, realistic skin
texture, no armor, no idealized retouching, no cartoon-proportioned
oversized head.

**Build note.** The hardest of the 12 "MetaHuman-feasible" races, and
genuinely borderline. MetaHuman's custom-body workflow supports short
stature, but the specific proportion here — wide ribcage and shoulders
relative to a short overall height, adult (not juvenile) limb ratios — sits
well outside the default preset space and needs hand-tuned skeletal
proportions per sex, checked specifically against the "not cartoony, not
childlike" rule before it's approved. Budget this one extra review pass.

---

## 5. Dew Hollow

### Woodling — Amberknot

**Silhouette and height.** Male 125–138 cm, female 119–132 cm — small forest
folk, matching finesse+2/survival+1/awareness+1 against
strength−1/conditioning−1/discipline−2. Build is slight and nimble, adult
proportions kept carefully adult (this is the race most at risk of reading
as a child if scaled naively — limb-to-torso ratio must stay adult, only
overall scale shrinks). Posture is quick, alert, weight forward on the
toes, restless (discipline−2 shows as fidgeting stillness, never quite
settled). At 50 m: a child-sized adult, moving like they'd rather already
be gone.

**Palette.** Skin tawny-brown `#A9764F`, bark-toned. Hair auburn, gold, or
brown `#7A4B23` — leaf colours, matching Amberknot's "round gold-leaved
thicket-town in the autumn scrub." Eyes amber `#A6752E` or green `#55702E`.
Culture dyes with autumn scrub: amber, russet, gold-leaf yellow, brown —
nothing that would stand out against dry bracken, because Woodlings dress
to disappear into their own territory.

**Features.** Sharp, small features — narrow chin, large watchful eyes
relative to face size (a real feature of small body plans, not a stylization
choice), slightly pointed ear tips (subtler than the elf races — a
Dew-Hollow-specific marker, not borrowed from Sidhe/Alfar/Mythic). Men and
women both wear hair short or practically tied — nothing that snags on
brush. Faint natural bark-like texture or mottling on exposed skin
(subtle — a species trait, camouflage-coded, not tattoo-applied) is
appropriate and distinguishes Woodling from a simply-shrunk human. Ornament
is minimal: a single cord, a carved wood or seed-pod pendant.

**Clothing at level 1.** Undyed brown or russet-toned rough-spun cloth,
minimal cut, no leaf/gold-toned dye yet — level 1 Woodling is drab on
purpose, camouflage before craft.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male (small stature, adult facial and body proportions,
not a child), 131 cm, slight nimble build, tawny bark-toned skin with
faint natural mottling, short auburn hair, amber eyes, subtly pointed ear
tips, standing alert forward-weighted restless pose in undyed russet
rough-spun clothing, dappled autumn-forest daylight, neutral grey backdrop,
realistic skin texture, no armor, no jewellery, no childlike proportions,
no cartoon stylization.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female (small stature, adult proportions, not a child),
125 cm, slight nimble build, tawny bark-toned skin, short gold-brown hair
tied back, green eyes, subtly pointed ear tips, standing alert watchful
pose in undyed brown rough-spun clothing, dappled autumn-forest daylight,
neutral grey backdrop, realistic skin texture, no armor, no jewellery, no
childlike proportions, no cartoon stylization.

**Build note.** Bespoke model expected. The core problem is proportion at
scale: MetaHuman's height slider was not designed to produce a
125–138 cm *adult*, and naive downscaling of an adult mesh plus a low
height value tends to either (a) look like a scaled child, which the
realism rule forbids, or (b) look proportionally wrong (adult torso, doll
limbs). A bespoke or heavily custom-rigged base is the safer bet, plus the
bark-mottling skin detail is a custom shader/texture regardless of skeleton
choice.

### Gobbledrift — Rattledrift

**Silhouette and height.** Male 109–122 cm, female 104–117 cm — the
smallest race in the bible, matching impulse+2/athleticism+1/detail+1
against wisdom−1/discipline−1/strength−2 (the single lowest strength malus
of all 16 races). Build is wiry and spindly, minimal visible muscle,
slightly hunched — a scavenger's posture, low and quick rather than
upright. Movement should read jittery and impulsive, never composed. At
50 m: the smallest, twitchiest silhouette on the roster.

**Palette.** Skin sallow grey-green to grey-tan `#8E8368` — a genuine
skin-tone variant (not a health/cartoon-green cue), kept muted and
naturalistic rather than saturated goblin-green. Hair sparse and dark
`#221E18`. Eyes amber-yellow `#B08A2E` or dark. Rattledrift is a
"biggest and loudest of the Gobbledrift camps... roofed in salvaged sheet"
— the clothing culture follows: patchwork, mismatched scavenged and
re-dyed cloth, soot-black and rust-brown dominant because that's what's
salvageable, not chosen.

**Features.** Angular, sharp-featured faces, prominent ears (larger and
more expressive than any other race — a genuine Gobbledrift trait, kept
proportion-realistic rather than comically oversized), sparse patchy
facial/head hair on men rather than a full beard convention. Both sexes
show a slightly stooped neck-forward posture as a built-in feature, not
just a pose note. Ornament is scavenged and mismatched by nature —
a bent nail, a bit of wire, a button — worn as found-object jewellery
rather than crafted.

**Clothing at level 1.** Patchwork rough cloth in muted browns and greys,
deliberately mismatched (two visibly different fabric scraps is correct,
not a texture error), no found-object jewellery yet at level 1 — that's
collected as the character plays, thematically appropriate for a
scavenger race.

**Reference prompt — male.** Photorealistic reference photo, three-quarter
and profile, adult male (very small stature, adult proportions, not a
child), 115 cm, wiry spindly build with a stooped neck-forward posture,
sallow grey-tan skin, sparse dark patchy hair, amber-yellow eyes,
prominent proportionally-realistic large ears, standing hunched restless
pose in mismatched patchwork brown-grey rough cloth, dim workshop-toned
daylight, neutral grey backdrop, realistic skin texture, no armor, no
cartoon-oversized features, no childlike proportions.

**Reference prompt — female.** Photorealistic reference photo, three-quarter
and profile, adult female (very small stature, adult proportions, not a
child), 110 cm, wiry spindly build, sallow grey-green skin, sparse dark
hair cropped short, dark eyes, prominent proportionally-realistic ears,
standing hunched alert pose in mismatched patchwork rough cloth, dim
workshop-toned daylight, neutral grey backdrop, realistic skin texture, no
armor, no cartoon-oversized features, no childlike proportions.

**Build note.** Bespoke model required, more definitely than Woodling. At
109–122 cm the adult-proportion problem is even more acute, and the
prominent-ear and sallow non-human skin tone push the head well outside
MetaHuman's human head library — a custom head sculpt is needed regardless
of what happens with the body/skeleton.

### Fae — Hollowbell

**Silhouette and height.** Male 155–168 cm, female 148–161 cm — short to
medium for a humanoid but read as tall-and-thin due to extreme slenderness,
matching elements+3/spirit+2 against the same triple malus
(strength−1/athleticism−1/conditioning−1) plus constitution−2 — mechanically
the frailest single stat combination in the table alongside Mythic. Build
is reed-thin, minimal mass, closer to a plant stem than a human frame.
Posture drifts rather than stands — weight barely settled, as if ready to
be moved by a breeze. At 50 m: barely displaces the air around it.

**Palette.** Skin very pale and faintly translucent `#F4EDEA` with a hint of
blue or green undertone visible at the temples and wrists (a subtle
subsurface-scattering cue, not a costume paint job). Hair unusual pale
hues — silvery-lilac `#C9B8D6` or moss-green `#8FAE8A` — appropriate here
specifically because Fae is an explicitly non-human bespoke race, unlike
the human cultures. Eyes large and pale, luminous `#CDEDE6` or `#D8CDEF`.
Hollowbell sits in "the Bloom," named for crystal flowers, and Dewglass is
a still reflecting pool — the palette follows: opalescent pale blue,
lilac, dew-silver, nothing earthy or saturated.

**Features.** Delicate, finely-boned faces, large eyes relative to face
(more pronounced than Woodling's), minimal to no body hair on either sex,
skin with a faint natural sheen rather than matte. Hair worn loose and
long more often than bound — it should move like it's underwater even in
still reference shots. Ornament is naturalistic rather than metal —
worked crystal or glass-like natural formations, dew-drop shapes,
never forged metal. No tattooing; the skin's faint translucency and
undertone do the visual work a marking would elsewhere.

**Clothing at level 1.** Undyed pale grey-white gauze-weight cloth, minimal
cut, no opalescent shimmer yet at level 1 — that belongs to higher-tier
gear. Even the "plain" starting cloth should look slightly finer/thinner
than any human race's linen, consistent with a culture that doesn't do
heavy labour in it.

**Reference prompt — male.** Photorealistic-leaning reference photo (fine
art / high-end fashion photography lighting acceptable given the
otherworldly skin), three-quarter and profile, adult male apparent
late-20s, 161 cm, extremely slender reed-thin build, very pale skin with a
faint cool translucent quality at the temples, long silvery-lilac hair
worn loose, large pale blue-green eyes, standing in a drifting
barely-weighted pose, wearing minimal pale grey-white gauze-weight cloth,
soft diffused overcast light, neutral pale backdrop, skin rendered with
subtle subsurface scattering rather than airbrushed opacity, no armor, no
metal jewellery, no glitter/sparkle particle effects.

**Reference prompt — female.** Photorealistic-leaning reference photo,
three-quarter and profile, adult female apparent mid-20s, 154 cm,
extremely slender reed-thin build, very pale translucent-toned skin, long
moss-green hair worn loose, large pale lilac eyes, standing in a drifting
weightless-looking pose, wearing minimal pale gauze-weight cloth, soft
diffused overcast light, neutral pale backdrop, subtle subsurface
scattering skin rendering, no armor, no metal jewellery, no glitter/sparkle
particle effects.

**Build note.** Bespoke model required — not primarily for proportion (Fae
height is within normal human range) but for materials: the translucent,
faintly-luminous skin needs a custom subsurface-scattering shader beyond
MetaHuman's standard realistic-human skin preset, and the large-eye facial
proportion is outside the standard head library. Body proportion alone
might have survived on MetaHuman; the skin and eyes push it to bespoke.

### Centaur — Longmane

**Silhouette and height.** Quadrupedal — state both numbers. Withers
(shoulder) height male 152–168 cm, female 142–158 cm, in the range of a
large draft/warmblood horse. Total height (crown of head, torso upright)
male 215–232 cm, female 200–217 cm — the tallest race in the bible by a
wide margin, matching athleticism+2/conditioning+2 against
finesse−1/detail−1/elements−2. Build is powerful and heavy-boned
throughout, both the equine body and the human torso — this is the
physically strongest-reading race on the roster, full stop. At 50 m: half
again the height of a mounted rider, and unmistakable in outline before any
other detail resolves.

**Palette.** Equine-half coat colours follow real horse genetics — bay
`#6B3E22`, chestnut `#8B4A2B`, black `#1A1512`, dapple-grey `#A9A9A0`, dun
`#B79A6B` — with natural markings (blaze, socks) exactly as a real horse
would carry them; this is the strongest "ground it in reality" opportunity
in the whole document and should not be skipped. Human-torso skin tone is
independently variable (not tied to coat colour) but defaults to a
sun-worked outdoor tan `#C69C6D` given Longmane sits on an open plateau.
Hair dark brown to black `#2E2013`. Eyes brown `#4A3320`. Clothing/tack
palette is practical leather and rope rather than dyed cloth — Archrun is
a paddock and post-road culture, and Centaurs don't have a torso-heavy
clothing tradition the way bipeds do.

**Features.** Human-torso facial features are broad and strong-jawed,
matching the powerful build; no elf-adjacent features (no pointed ears —
Centaur is not part of the elf-mythology cluster). Hair worn practically
short or tied back, kept clear of tack. Facial hair on males is common and
functional-length, not styled. The equine-human transition at the waist is
the single most important sculpt point in the whole race and needs its
own dedicated reference pass beyond what a text prompt can specify — see
build note. Ornament is functional tack — leather straps, a simple woven
girth-band — never decorative jewellery, consistent with a working-animal
self-image this culture is comfortable with rather than embarrassed by.

**Clothing at level 1.** A simple leather or rope harness/vest across the
human torso (practical, not armor), no dye, no tack ornament yet. Centaurs
need less "clothing" than any biped race by design — most of the visual
surface area is the coat, not cloth.

**Reference prompt — male.** Photorealistic reference photo of a centaur
reference maquette or heavily-tagged photo composite: human torso, adult
male, early 30s, broad powerful build, sun-worked tan skin, short dark
hair tied back, brown eyes, strong jaw, joined at the waist to a
bay-coloured (`#6B3E22`) quadrupedal horse body with a black mane and tail
and a natural white blaze marking, withers height approximately 160 cm,
standing four-square on all four legs in a relaxed stance, wearing only a
simple leather torso harness, natural outdoor daylight on an open
grassland plateau, realistic skin and coat texture with visible musculature
at the join, no armor, no fantasy glow effects, no exaggerated
proportions at the human-equine transition.

**Reference prompt — female.** Photorealistic reference photo of a centaur
reference maquette or heavily-tagged photo composite: human torso, adult
female, late 20s, strong athletic build, sun-worked tan skin, dark hair
tied back, brown eyes, joined at the waist to a dapple-grey (`#A9A9A0`)
quadrupedal horse body with a black mane and tail, withers height
approximately 148 cm, standing four-square relaxed stance, wearing only a
simple leather torso harness, natural outdoor daylight on an open
grassland plateau, realistic skin and coat texture with visible musculature
at the join, no armor, no fantasy glow effects, no exaggerated proportions
at the human-equine transition.

**Build note.** Bespoke model required, unambiguously and by the widest
margin of any race here. This is not a proportion tweak on a bipedal rig —
it needs an entirely custom skeleton (human spine grafted to a
quadrupedal body), a custom four-legged locomotion rig, and a full bespoke
animation set (walk/trot/canter/gallop, plus combat moves that don't exist
in any bipedal library). This is realistically its own production line
with its own schedule, not a task the character-art lane picks up alongside
the other 15 races.

---

## 6. Open questions for Daniel

1. **Is MetaHuman actually the answer, even for the 12 "feasible" races?**
   This document assumed it because it's free and fast, but nothing has
   been decided. If Daniel wants full bespoke sculpts across all 16 for
   visual consistency (so the 4 Dew Hollow races don't look like a
   different game bolted onto 12 MetaHumans), that's a materially
   different budget and timeline, and it should be settled before anyone
   opens the MetaHuman Creator.
2. **Elf ears.** MetaHuman has no stock pointed-ear morph. Mythic, Sidhe,
   and Alfar all need it. Decide: a custom attachment mesh (cheaper,
   riskier at close range) or a fully custom head per elf race (safer,
   slower). This blocks all three elf races equally.
3. **Height range vs. MetaHuman's slider limits.** Mythic tops out at
   199 cm male; Gobbledrift bottoms out at 104 cm female. Neither has been
   tested against MetaHuman's actual bounds. This needs an engineering
   spike, not a design guess, before art starts on either race.
4. **Fae's skin shader.** Realistic-but-translucent skin is a new
   subsurface-scattering material, not a reuse of the standard human skin
   preset. Who owns building it, and does it get built once and shared, or
   once per race that needs something similar?
5. **Centaur is a separate production line.** Custom skeleton, custom
   quadrupedal rig, full bespoke animation set — this cannot ride on the
   same schedule as the other 15 races without either slipping everything
   else or shipping Centaur late/incomplete. Needs its own estimate and
   probably its own owner.
6. **Adaptive-outfit stress test.** Epic's adaptive-clothing system is
   assumed to resize cleanly across a body's height/build sliders. Nobody
   has tested it at the extremes this bible requires (Hillback Dwarf
   breadth, Mythic height, Centaur's torso-only coverage). One test
   garment on one extreme body, before the art lane commits to
   level-1 clothing as "solved."
7. **Every hex value in this document is a proposal, not a locked palette.**
   They're internally consistent and grounded in real dye/material sources,
   but nobody outside this session has signed off on them. Treat this
   bible as a first draft to react to, not a spec to build against
   silently.
8. **Facial markings and invented-language conflicts.** None of the 16
   races in this draft got tattooed script or invented glyphs, deliberately
   — that's territory `names/great-north-places.md` owns (invented tongues
   for Hillback, Woodling, Gobbledrift, Fae, Centaur). If any race later
   wants script-based marking, it needs a naming-doc check-in first so the
   glyphs don't get invented twice, differently, in two documents.
