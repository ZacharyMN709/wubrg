from typing import Literal, Union, get_args


# region Card Type Types
# https://mtg.fandom.com/wiki/Supertype
# https://media.wizards.com/2023/downloads/MagicComp%20Rules%2020230203.txt, from https://magic.wizards.com/en/rules

# From Rule 205.4a
SUPERTYPE = Literal["Basic", "Legendary", "Ongoing", "Snow", "World"]

# From Rule 205.2a
TYPE = Literal[
    "Artifact", "Battle", "Conspiracy", "Creature", "Dungeon", "Enchantment", "Instant", "Land", "Phenomenon", 
    "Plane", "Planeswalker", "Scheme", "Sorcery", "Tribal", "Vanguard"
]

# From Rule 205.3i
LAND_SUBTYPE = Literal[
    "Desert", "Forest", "Gate", "Island", "Lair", "Locus", "Mine", "Mountain", "Plains", "Power-Plant", "Sphere", 
    "Swamp", "Tower", "Urza's"
]

# From Rule 205.3m
CREATURE_SUBTYPE = Literal[
    "Advisor", "Aetherborn", "Alien", "Ally", "Angel", "Antelope", "Ape", "Archer", "Archon", "Army", "Artificer", 
    "Assassin", "Assembly-Worker", "Astartes", "Atog", "Aurochs", "Avatar", "Azra", "Badger", "Balloon", 
    "Barbarian", "Bard", "Basilisk", "Bat", "Bear", "Beast", "Beeble", "Beholder", "Berserker", "Bird", 
    "Blinkmoth", "Boar", "Bringer", "Brushwagg", "Camarid", "Camel", "Caribou", "Carrier", "Cat", "Centaur", 
    "Cephalid", "Child", "Chimera", "Citizen", "Cleric", "Clown", "Cockatrice", "Construct", "Coward", "Crab", 
    "Crocodile", "C'tan", "Custodes", "Cyclops", "Dauthi", "Demigod", "Demon", "Deserter", "Devil", "Dinosaur", 
    "Djinn", "Dog", "Dragon", "Drake", "Dreadnought", "Drone", "Druid", "Dryad", "Dwarf", "Efreet", "Egg", "Elder", 
    "Eldrazi", "Elemental", "Elephant", "Elf", "Elk", "Employee", "Eye", "Faerie", "Ferret", "Fish", "Flagbearer", 
    "Fox", "Fractal", "Frog", "Fungus", "Gamer", "Gargoyle", "Germ", "Giant", "Gith", "Gnoll", "Gnome", "Goat", 
    "Goblin", "God", "Golem", "Gorgon", "Graveborn", "Gremlin", "Griffin", "Guest", "Hag", "Halfling", "Hamster", 
    "Harpy", "Hellion", "Hippo", "Hippogriff", "Homarid", "Homunculus", "Horror", "Horse", "Human", "Hydra", 
    "Hyena", "Illusion", "Imp", "Incarnation", "Inkling", "Inquisitor", "Insect", "Jackal", "Jellyfish", 
    "Juggernaut", "Kavu", "Kirin", "Kithkin", "Knight", "Kobold", "Kor", "Kraken", "Lamia", "Lammasu", "Leech", 
    "Leviathan", "Lhurgoyf", "Licid", "Lizard", "Manticore", "Masticore", "Mercenary", "Merfolk", "Metathran", 
    "Minion", "Minotaur", "Mite", "Mole", "Monger", "Mongoose", "Monk", "Monkey", "Moonfolk", "Mouse", "Mutant", 
    "Myr", "Mystic", "Naga", "Nautilus", "Necron", "Nephilim", "Nightmare", "Nightstalker", "Ninja", "Noble", 
    "Noggle", "Nomad", "Nymph", "Octopus", "Ogre", "Ooze", "Orb", "Orc", "Orgg", "Otter", "Ouphe", "Ox", "Oyster", 
    "Pangolin", "Peasant", "Pegasus", "Pentavite", "Performer", "Pest", "Phelddagrif", "Phoenix", "Phyrexian", 
    "Pilot", "Pincher", "Pirate", "Plant", "Praetor", "Primarch", "Prism", "Processor", "Rabbit", "Raccoon", 
    "Ranger", "Rat", "Rebel", "Reflection", "Rhino", "Rigger", "Robot", "Rogue", "Sable", "Salamander", "Samurai", 
    "Sand", "Saproling", "Satyr", "Scarecrow", "Scion", "Scorpion", "Scout", "Sculpture", "Serf", "Serpent", 
    "Servo", "Shade", "Shaman", "Shapeshifter", "Shark", "Sheep", "Siren", "Skeleton", "Slith", "Sliver", "Slug", 
    "Snake", "Soldier", "Soltari", "Spawn", "Specter", "Spellshaper", "Sphinx", "Spider", "Spike", "Spirit", 
    "Splinter", "Sponge", "Squid", "Squirrel", "Starfish", "Surrakar", "Survivor", "Tentacle", "Tetravite", 
    "Thalakos", "Thopter", "Thrull", "Tiefling", "Treefolk", "Trilobite", "Triskelavite", "Troll", "Turtle", 
    "Tyranid", "Unicorn", "Vampire", "Vedalken", "Viashino", "Volver", "Wall", "Walrus", "Warlock", "Warrior", 
    "Weird", "Werewolf", "Whale", "Wizard", "Wolf", "Wolverine", "Wombat", "Worm", "Wraith", "Wurm", "Yeti", 
    "Zombie", "Zubera"
]

# From Rule 205.3g
ARTIFACT_SUBTYPE = Literal[
    "Attraction", "Blood", "Clue", "Contraption", "Equipment", "Food", "Fortification", "Gold", "Powerstone", 
    "Treasure", "Vehicle"
]

# From Rule 205.3h
ENCHANTMENT_SUBTYPE = Literal["Aura", "Background", "Cartouche", "Class", "Curse", "Rune", "Saga", "Shard", "Shrine"]

# From Rule 205.3j
PLANESWALKER_SUBTYPE = Literal[
    "Ajani", "Aminatou", "Angrath", "Arlinn", "Ashiok", "Bahamut", "Basri", "Bolas", "Calix", "Chandra", "Comet", 
    "Dack", "Dakkon", "Daretti", "Davriel", "Dihada", "Domri", "Dovin", "Ellywick", "Elminster", "Elspeth", 
    "Estrid", "Freyalise", "Garruk", "Gideon", "Grist", "Huatli", "Jace", "Jared", "Jaya", "Jeska", "Kaito", 
    "Karn", "Kasmina", "Kaya", "Kiora", "Koth", "Liliana", "Lolth", "Lukka", "Minsc", "Mordenkainen", "Nahiri", 
    "Narset", "Niko", "Nissa", "Nixilis", "Oko", "Ral", "Rowan", "Saheeli", "Samut", "Sarkhan", "Serra", "Sivitri", 
    "Sorin", "Szat", "Tamiyo", "Tasha", "Teferi", "Teyo", "Tezzeret", "Tibalt", "Tyvar", "Ugin", "Urza", "Venser", 
    "Vivien", "Vraska", "Will", "Windgrace", "Wrenn", "Xenagos", "Yanggu", "Yanling", "Zariel"
]

# From Rule 205.3k
INSTANT_SUBTYPE = Literal["Adventure", "Arcane", "Lesson", "Trap"]

# From Rule 205.3k
SORCERY_SUBTYPE = Literal["Adventure", "Arcane", "Lesson", "Trap"]


SUBTYPE = Union[LAND_SUBTYPE, CREATURE_SUBTYPE, ARTIFACT_SUBTYPE, ENCHANTMENT_SUBTYPE,
                PLANESWALKER_SUBTYPE, INSTANT_SUBTYPE, SORCERY_SUBTYPE]

ANY_TYPE = Union[SUPERTYPE, TYPE, SUBTYPE]
# endregion Card Type Types


# region Card Type Sets
# Extracting the card types from the data type definitions.SUPERTYPES: set[SUPERTYPE] = set(get_args(SUPERTYPE))
TYPES: set[TYPE] = set(get_args(TYPE))
LAND_SUBTYPES: set[LAND_SUBTYPE] = set(get_args(LAND_SUBTYPE))
CREATURE_SUBTYPES: set[CREATURE_SUBTYPE] = set(get_args(CREATURE_SUBTYPE))
ARTIFACT_SUBTYPES: set[ARTIFACT_SUBTYPE] = set(get_args(ARTIFACT_SUBTYPE))
ENCHANTMENT_SUBTYPES: set[ENCHANTMENT_SUBTYPE] = set(get_args(ENCHANTMENT_SUBTYPE))
PLANESWALKER_SUBTYPES: set[PLANESWALKER_SUBTYPE] = set(get_args(PLANESWALKER_SUBTYPE))
INSTANT_SUBTYPES: set[INSTANT_SUBTYPE] = set(get_args(INSTANT_SUBTYPE))
SORCERY_SUBTYPES: set[SORCERY_SUBTYPE] = set(get_args(SORCERY_SUBTYPE))

SUBTYPE_DICT: dict[TYPE, set[SUBTYPE]] = {
    "Land": LAND_SUBTYPES,
    "Creature": CREATURE_SUBTYPES,
    "Artifact": ARTIFACT_SUBTYPES,
    "Enchantment": ENCHANTMENT_SUBTYPES,
    "Planeswalker": PLANESWALKER_SUBTYPES,
    "Instant": INSTANT_SUBTYPES,
    "Sorcery": SORCERY_SUBTYPES
}
# endregion Card Type Sets
