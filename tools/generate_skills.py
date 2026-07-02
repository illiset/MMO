"""Generate Great North skill trees: one CLASS-TYPE (archetype) tree used
levels 1-9, and one CLASS tree per class (level 10+, earned via class quest).

Slice-four classes (Knight, Squire, Bard, Ranger) are hand-authored below.
All other class trees are generated from archetype templates with class
flavor and marked status="draft" for Daniel's review.

Classic layout: tiers unlock by level; skills may require a prerequisite.
Output: data/skills/great-north/archetypes/*.json and classes/*.json
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "data" / "skills" / "great-north"

# (name, tier, kind, cost_type, cost, cooldown, power, description)
# kind: strike|dot|taunt|stance|buff|heal|hot|cleanse|shout|cc|dd|debuff|pet|passive
ARCHETYPE_TEMPLATES = {
    "frontline": [
        ("Strike", 1, "strike", "stamina", 10, 3, 1.0, "A disciplined weapon strike."),
        ("Taunt", 1, "taunt", "stamina", 8, 8, 0.0, "Force the enemy to attack you."),
        ("Guard Stance", 1, "stance", "none", 0, 1, 0.8, "Trade damage for defense."),
        ("Shield Bash", 2, "strike", "stamina", 15, 6, 1.2, "Bash with shield or pommel."),
        ("Intercept", 2, "cc", "stamina", 20, 20, 0.0, "Rush to an ally, absorbing the next blow."),
        ("Rending Cut", 2, "dot", "stamina", 15, 10, 0.9, "Bleed the target over 12s."),
        ("Battle Shout", 3, "shout", "stamina", 10, 30, 0.5, "Rally nearby allies' strength."),
        ("Crushing Blow", 3, "strike", "stamina", 25, 12, 1.8, "A heavy, slow strike."),
        ("Bulwark", 3, "buff", "stamina", 20, 45, 1.0, "Greatly reduce damage taken for 8s."),
        ("Hamstring", 4, "cc", "stamina", 15, 15, 0.6, "Slow the target's movement."),
        ("Riposte", 4, "passive", "none", 0, 0, 0.7, "Counter-attack after parries."),
        ("Challenger's Roar", 4, "taunt", "stamina", 25, 25, 0.0, "Taunt all nearby enemies."),
        ("Executioner", 5, "strike", "stamina", 30, 20, 2.5, "Massive damage to wounded foes."),
        ("Iron Will", 5, "buff", "none", 0, 60, 1.0, "Break and resist crowd control."),
        ("Whirling Blade", 5, "strike", "stamina", 30, 15, 1.4, "Strike all enemies around you."),
        ("Vigilance", 6, "passive", "none", 0, 0, 0.8, "Guard an ally, redirecting damage."),
        ("Sunder Armor", 6, "debuff", "stamina", 20, 10, 0.8, "Reduce the target's armor."),
        ("Last Stand", 6, "buff", "none", 0, 120, 1.5, "Refuse to fall below 1 health for 6s."),
        ("Warlord's Presence", 7, "passive", "none", 0, 0, 1.0, "Aura: nearby allies gain defense."),
        ("Decapitate", 7, "strike", "stamina", 40, 30, 3.2, "A devastating finishing blow."),
    ],
    "healers": [
        ("Mend", 1, "heal", "mana", 12, 2, 1.0, "A quick healing prayer."),
        ("Smite", 1, "dd", "mana", 10, 3, 0.8, "Holy damage to a single foe."),
        ("Renew", 1, "hot", "mana", 15, 4, 0.9, "Heal over 12 seconds."),
        ("Greater Mend", 2, "heal", "mana", 25, 5, 1.8, "A slow, powerful heal."),
        ("Purify", 2, "cleanse", "mana", 15, 8, 0.0, "Remove poisons and disease."),
        ("Ward", 2, "buff", "mana", 20, 15, 1.0, "Absorb incoming damage."),
        ("Circle of Healing", 3, "heal", "mana", 35, 12, 1.2, "Heal all party members nearby."),
        ("Chastise", 3, "cc", "mana", 15, 20, 0.4, "Stun undead and beasts briefly."),
        ("Prayer of Vigor", 3, "buff", "mana", 20, 30, 0.8, "Raise an ally's constitution."),
        ("Intervention", 4, "heal", "mana", 30, 25, 2.2, "Instant emergency heal."),
        ("Martyr's Gift", 4, "heal", "none", 0, 45, 1.5, "Sacrifice health to heal an ally."),
        ("Silence", 4, "cc", "mana", 25, 30, 0.0, "Stop the target from casting."),
        ("Resurrection", 5, "heal", "mana", 50, 60, 0.0, "Return a fallen ally to life."),
        ("Divine Aegis", 5, "buff", "mana", 35, 60, 1.8, "Shield the whole party."),
        ("Judgment", 5, "dd", "mana", 30, 15, 1.6, "Heavy holy damage."),
        ("Beacon of Light", 6, "hot", "mana", 40, 30, 1.4, "A pulsing ground heal."),
        ("Guardian Spirit", 6, "buff", "mana", 40, 120, 2.0, "Prevent an ally's death."),
        ("Exorcism", 6, "dd", "mana", 35, 20, 2.0, "Banish with searing light."),
        ("Font of Life", 7, "passive", "none", 0, 0, 1.0, "Your heals splash to nearby allies."),
        ("Miracle", 7, "heal", "mana", 60, 180, 3.0, "Fully heal the target."),
    ],
    "support": [
        ("Discord", 1, "dd", "mana", 10, 3, 0.7, "A jarring note of force."),
        ("Chant of Swiftness", 1, "buff", "mana", 15, 10, 0.8, "Speed nearby allies' steps."),
        ("Lullaby", 1, "cc", "mana", 15, 15, 0.0, "Sing a single enemy to sleep."),
        ("Chant of Vigor", 2, "buff", "mana", 15, 10, 0.9, "Restore stamina to the party."),
        ("Distract", 2, "debuff", "mana", 12, 12, 0.5, "Lower the target's awareness."),
        ("Mock", 2, "debuff", "mana", 12, 10, 0.6, "Weaken the enemy's resolve."),
        ("War Drums", 3, "buff", "mana", 25, 30, 1.1, "Quicken allies' attacks."),
        ("Dissonance", 3, "dot", "mana", 20, 10, 0.9, "A grating tone that wounds over time."),
        ("Mesmerize", 3, "cc", "mana", 25, 25, 0.0, "Entrance enemies in a cone."),
        ("Chant of Warding", 4, "buff", "mana", 25, 15, 1.0, "Raise allies' magic resistance."),
        ("Cutpurse", 4, "debuff", "mana", 15, 20, 0.4, "Steal a beneficial effect."),
        ("Crescendo", 4, "dd", "mana", 30, 15, 1.5, "A building blast of sound."),
        ("Anthem of the North", 5, "buff", "mana", 35, 60, 1.5, "Empower the party's damage."),
        ("Fade", 5, "stance", "none", 0, 30, 0.0, "Slip from enemies' attention."),
        ("Cacophony", 5, "dd", "mana", 35, 20, 1.3, "Damage all nearby enemies."),
        ("Battle Hymn", 6, "buff", "mana", 40, 45, 1.6, "The party strikes true (crit up)."),
        ("Siren's Pull", 6, "cc", "mana", 30, 30, 0.0, "Draw the enemy to you, dazed."),
        ("Counterpoint", 6, "passive", "none", 0, 0, 0.9, "Your buffs also shield slightly."),
        ("Maestro", 7, "passive", "none", 0, 0, 1.0, "Chants affect one extra target."),
        ("Grand Finale", 7, "dd", "mana", 50, 60, 2.8, "Consume your chants for a blast."),
    ],
    "dps": [
        ("Quick Strike", 1, "strike", "stamina", 8, 2, 0.9, "A fast, cheap attack."),
        ("Aimed Attack", 1, "strike", "stamina", 12, 5, 1.2, "A careful, harder hit."),
        ("Evasion", 1, "stance", "none", 0, 20, 0.6, "Focus on dodging briefly."),
        ("Twin Fangs", 2, "strike", "stamina", 15, 6, 1.3, "Strike twice in a blur."),
        ("Crippling Poison", 2, "dot", "none", 0, 15, 0.8, "Coat weapons; hits slow and sicken."),
        ("Ambush", 2, "strike", "stamina", 20, 12, 1.8, "Bonus damage from behind."),
        ("Deadeye", 3, "buff", "none", 0, 30, 1.0, "Next attacks cannot miss."),
        ("Serrated Edge", 3, "dot", "stamina", 15, 10, 1.0, "A ragged wound that bleeds."),
        ("Tumble", 3, "cc", "stamina", 15, 15, 0.0, "Roll away and break snares."),
        ("Killing Spree", 4, "buff", "stamina", 25, 45, 1.4, "Kills briefly reset cooldowns."),
        ("Expose Weakness", 4, "debuff", "stamina", 15, 12, 0.7, "Open the target to more damage."),
        ("Volley", 4, "strike", "stamina", 25, 15, 1.3, "Strike up to three enemies."),
        ("Assassinate", 5, "strike", "stamina", 35, 25, 2.6, "Aim for the vitals."),
        ("Shadowstep", 5, "cc", "stamina", 20, 20, 0.0, "Appear behind your target."),
        ("Relentless", 5, "passive", "none", 0, 0, 0.9, "Attacks build growing speed."),
        ("Garrote", 6, "cc", "stamina", 25, 25, 0.8, "Silence and bleed from stealth."),
        ("Predator's Focus", 6, "passive", "none", 0, 0, 1.0, "Bonus damage to wounded prey."),
        ("Fan of Blades", 6, "strike", "stamina", 30, 18, 1.5, "Strike all around you."),
        ("Deathmark", 7, "debuff", "stamina", 30, 45, 1.2, "Mark a target to take heavy damage."),
        ("Coup de Grace", 7, "strike", "stamina", 45, 40, 3.4, "Finish what you started."),
    ],
}

# Flavor prefixes for generated (non-slice) class trees.
CLASS_FLAVOR = {
    "zealot": "Fervent", "wizard": "Arcane", "reaver": "Grim",
    "truthspeaker": "Truth's", "volva": "Seer's", "preacher": "Devout",
    "dracomancer": "Drake", "muse": "Inspired", "provacateur": "Cunning",
    "syndicate": "Covert", "philosopher": "Reasoned",
    "knave": "Sly", "jester": "Mocking", "hundr": "Hound's", "equal": "Balanced",
    "draoi": "Wild", "pankrator": "Unarmed", "frontiersman": "Trailworn",
    "relic-master": "Relic", "whisper": "Silent", "veil-tamer": "Veiled",
}

# Hand-authored slice-four class trees (level 10+). Tier N unlocks at level 8+2N.
AUTHORED = {
    "knight": [
        ("Shield Slam", 1, "strike", "stamina", 25, 6, 1.4, "Slam your shield, then whirl into a slash."),
        ("Crusader's Oath", 1, "buff", "none", 0, 30, 1.0, "Steel yourself: brief defense surge."),
        ("Zealous Taunt", 1, "taunt", "stamina", 10, 8, 0.0, "A challenge no foe can ignore."),
        ("Aegis of the North", 2, "buff", "stamina", 25, 45, 1.3, "Plant your shield: party damage shield."),
        ("Pommel Strike", 2, "cc", "stamina", 18, 15, 0.5, "Daze the target with your hilt."),
        ("Holy Edge", 2, "strike", "mana", 20, 10, 1.5, "Blade wreathed in consecrated light."),
        ("Phalanx", 3, "stance", "none", 0, 10, 1.0, "Immovable: heavy defense, slow steps."),
        ("Retribution", 3, "passive", "none", 0, 0, 0.9, "Blocked attacks are answered in kind."),
        ("Banner of Valor", 3, "shout", "stamina", 30, 60, 1.2, "Plant a banner: allies fight harder."),
        ("Shield Charge", 4, "cc", "stamina", 30, 25, 1.1, "Charge through, bowling enemies over."),
        ("Consecrate", 4, "dot", "mana", 30, 20, 1.0, "Sanctify the ground against foes."),
        ("Unbreakable", 4, "buff", "none", 0, 90, 1.8, "The Knight does not kneel: big mitigation."),
        ("Judgment of Steel", 5, "strike", "stamina", 35, 20, 2.2, "A verdict delivered edge-first."),
        ("Guardian's Bond", 5, "passive", "none", 0, 0, 1.0, "Your guarded ally takes even less harm."),
        ("Rally the Line", 5, "shout", "stamina", 35, 90, 1.5, "Mass heal-over-time and courage."),
        ("Bastion", 6, "buff", "stamina", 40, 120, 2.0, "Become the wall: absorb for the party."),
        ("Crusade", 6, "buff", "none", 0, 180, 2.0, "For the North: party-wide offense surge."),
        ("Sundering Slam", 6, "strike", "stamina", 40, 30, 2.4, "Armor means nothing to conviction."),
        ("Paragon of the Realm", 7, "passive", "none", 0, 0, 1.2, "Aura: allies stand taller near you."),
        ("Deliverance", 7, "strike", "stamina", 50, 60, 3.5, "The blow that ends the battle."),
    ],
    "squire": [
        ("Field Dressing", 1, "heal", "mana", 12, 2, 1.1, "Practical battlefield healing."),
        ("Shield of Faith", 1, "buff", "mana", 15, 12, 1.0, "Ward an ally with conviction."),
        ("Rebuke", 1, "dd", "mana", 10, 4, 0.8, "A stinging censure."),
        ("Bind Wounds", 2, "hot", "mana", 18, 6, 1.1, "Steady mending over time."),
        ("Squire's Duty", 2, "cleanse", "mana", 15, 8, 0.0, "Strip ailments from an ally."),
        ("Stand Fast", 2, "buff", "mana", 20, 20, 0.9, "Brace an ally against knockdown."),
        ("Triage", 3, "heal", "mana", 30, 10, 1.6, "Heal the most wounded party member."),
        ("Oath of Service", 3, "passive", "none", 0, 0, 0.8, "Healing a guarded ally costs less."),
        ("Blessed Water", 3, "heal", "mana", 25, 15, 1.3, "Throw a flask: small area heal."),
        ("Knight's Vigil", 4, "buff", "mana", 30, 45, 1.4, "An ally cannot be critically hit."),
        ("Lay on Hands", 4, "heal", "mana", 40, 60, 2.5, "A great and instant mending."),
        ("Censure", 4, "cc", "mana", 25, 30, 0.0, "Command silence from the wicked."),
        ("Field Chapel", 5, "hot", "mana", 40, 40, 1.6, "Consecrate ground that heals allies."),
        ("Devoted Heart", 5, "passive", "none", 0, 0, 1.0, "Your heals crit more often."),
        ("Absolution", 5, "cleanse", "mana", 35, 25, 1.0, "Cleanse the party of one ailment."),
        ("Martyrdom", 6, "heal", "none", 0, 90, 2.0, "Bleed yourself to save another."),
        ("Sanctuary", 6, "buff", "mana", 45, 120, 1.8, "A zone the enemy's blows soften in."),
        ("Litany of Dawn", 6, "heal", "mana", 45, 30, 1.9, "Wave of healing at first light."),
        ("Hearthkeeper", 7, "passive", "none", 0, 0, 1.1, "Out of combat, your party mends fast."),
        ("The Vow Kept", 7, "heal", "mana", 60, 180, 3.2, "No one dies while the Squire stands."),
    ],
    "bard": [
        ("Song of Steel", 1, "buff", "mana", 15, 10, 0.9, "Allies' weapons sing: damage up."),
        ("Biting Verse", 1, "dd", "mana", 10, 3, 0.8, "Words that draw blood."),
        ("Traveler's March", 1, "buff", "mana", 12, 8, 0.9, "The road shortens for your party."),
        ("Song of Mending", 2, "hot", "mana", 20, 8, 1.0, "A melody that knits flesh."),
        ("Heckle", 2, "taunt", "mana", 10, 12, 0.0, "Enrage a foe into recklessness."),
        ("Chord of Stamina", 2, "buff", "mana", 18, 10, 1.0, "The party's endurance swells."),
        ("Ballad of the Fallen", 3, "dot", "mana", 22, 10, 1.0, "Grief made audible; it wounds."),
        ("Encore", 3, "passive", "none", 0, 0, 0.9, "Your songs linger longer."),
        ("Sleep Song", 3, "cc", "mana", 25, 25, 0.0, "A lullaby for unruly monsters."),
        ("Battle Ballad", 4, "buff", "mana", 30, 30, 1.3, "Attack speed for the whole line."),
        ("Sour Note", 4, "debuff", "mana", 18, 12, 0.7, "The enemy falters, defense down."),
        ("Refrain of Vigor", 4, "buff", "mana", 28, 20, 1.2, "Restore the party's stamina."),
        ("The North Remembers", 5, "buff", "mana", 35, 60, 1.5, "An anthem: all stats rise."),
        ("Discordant Blast", 5, "dd", "mana", 35, 18, 1.6, "A chord that shatters shields."),
        ("Silver Tongue", 5, "passive", "none", 0, 0, 0.9, "Vendors, quests, and crowds favor you."),
        ("Song of Sanctuary", 6, "buff", "mana", 40, 90, 1.7, "Shelter written in melody."),
        ("Requiem", 6, "dot", "mana", 40, 30, 1.8, "For enemies: an ending, slowly."),
        ("Crowd Favorite", 6, "passive", "none", 0, 0, 1.0, "Your buffs reach one more ally."),
        ("Virtuoso", 7, "passive", "none", 0, 0, 1.1, "Two songs may play at once."),
        ("The Final Verse", 7, "dd", "mana", 55, 120, 3.0, "Every song ends. So do they."),
    ],
    "ranger": [
        ("Longshot", 1, "strike", "stamina", 12, 4, 1.2, "A patient shot from far away."),
        ("Hunter's Mark", 1, "debuff", "none", 0, 10, 0.6, "Mark prey: it cannot hide, takes more."),
        ("Swift Feet", 1, "stance", "none", 0, 20, 0.7, "Move like wind between shots."),
        ("Barbed Arrow", 2, "dot", "stamina", 15, 8, 1.0, "It stays in. It hurts."),
        ("Snare Trap", 2, "cc", "stamina", 18, 20, 0.0, "Lay a trap that roots the unwary."),
        ("Double Nock", 2, "strike", "stamina", 20, 10, 1.5, "Two arrows, one breath."),
        ("Camouflage", 3, "stance", "none", 0, 30, 0.0, "Fade into the treeline."),
        ("Keen Eye", 3, "passive", "none", 0, 0, 0.9, "Your critical shots strike deeper."),
        ("Warden of Paths", 3, "buff", "stamina", 20, 30, 1.0, "Party moves quicker off-road."),
        ("Pinning Shot", 4, "cc", "stamina", 25, 18, 0.9, "Nail a boot to the ground."),
        ("Wolfpack", 4, "pet", "stamina", 30, 90, 1.3, "Call a wolf of the North to fight."),
        ("Rain of Arrows", 4, "strike", "stamina", 30, 20, 1.4, "Darken the sky over an area."),
        ("Heartseeker", 5, "strike", "stamina", 35, 25, 2.4, "The shot they never hear."),
        ("Windrunner", 5, "passive", "none", 0, 0, 0.9, "Attacking no longer slows your run."),
        ("Master Trapper", 5, "cc", "stamina", 30, 45, 1.0, "Traps arm faster, bite harder."),
        ("Eagle's Descent", 6, "strike", "stamina", 35, 30, 2.0, "Leap-shot from high ground."),
        ("One with the Wild", 6, "buff", "none", 0, 120, 1.6, "The forest fights beside you."),
        ("Piercing Gale", 6, "strike", "stamina", 40, 25, 1.8, "An arrow through every foe in line."),
        ("Apex Predator", 7, "passive", "none", 0, 0, 1.1, "Marked prey fears you: damage aura."),
        ("The Long Hunt", 7, "strike", "stamina", 50, 90, 3.3, "Every hunt ends the same way."),
    ],
}

SLICE = set(AUTHORED)


def slugify(name):
    return "".join(c if c.isalnum() else "-" for c in name.lower()).strip("-").replace("--", "-")


def build_skill(class_id, name, tier, kind, cost_type, cost, cooldown, power, desc, status, tree):
    base_damage = int(14 + tier * 9)
    return {
        "id": f"{class_id}-{slugify(name)}" if tree == "class" else f"{class_id}-t-{slugify(name)}",
        "name": name,
        "tree": tree,
        "tier": tier,
        "levelReq": (8 + 2 * tier) if tree == "class" else max(1, tier * 2 - 1),
        "kind": kind,
        "costType": cost_type,
        "cost": cost,
        "cooldown": cooldown,
        "power": round(power, 2),
        "baseValue": int(base_damage * power) if power > 0 else 0,
        "description": desc,
        "status": status,
    }


def main():
    factions = json.loads((REPO / "data" / "factions" / "great-north.json").read_text(encoding="utf-8"))
    (OUT / "archetypes").mkdir(parents=True, exist_ok=True)
    (OUT / "classes").mkdir(parents=True, exist_ok=True)

    total = 0
    for arch in factions["archetypes"]:
        # Class-type tree (levels 1-9): first 8 archetype template skills.
        arch_skills = [build_skill(arch["id"], *t, status="authored", tree="classtype")
                       for t in ARCHETYPE_TEMPLATES[arch["id"]][:8]]
        (OUT / "archetypes" / f"{arch['id']}.json").write_text(
            json.dumps({"classType": arch["id"], "skills": arch_skills}, indent=2) + "\n",
            encoding="utf-8")
        total += len(arch_skills)

        for cls in arch["classes"]:
            cid = cls["id"]
            if cid in SLICE:
                skills = [build_skill(cid, *t, status="authored", tree="class")
                          for t in AUTHORED[cid]]
            else:
                flavor = CLASS_FLAVOR.get(cid, cls["name"])
                skills = []
                for (name, tier, kind, ct, cost, cd, power, desc) in ARCHETYPE_TEMPLATES[arch["id"]]:
                    skills.append(build_skill(
                        cid, f"{flavor} {name}", tier, kind, ct, cost, cd, power,
                        f"{desc} ({cls['name']} draft.)", status="draft", tree="class"))
            (OUT / "classes" / f"{cid}.json").write_text(
                json.dumps({"classId": cid, "className": cls["name"],
                            "classType": arch["id"], "skills": skills}, indent=2) + "\n",
                encoding="utf-8")
            total += len(skills)

    print(f"generated {total} skills across 4 class-type trees and "
          f"{sum(len(a['classes']) for a in factions['archetypes'])} class trees")


if __name__ == "__main__":
    main()
