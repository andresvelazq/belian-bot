import json
import os

def addCharacter(name, stats, server):
    """Creates JSON file for server if none, adds character if not already added"""
    mods = []
    for stat in range(len(stats)):
        stats[stat] = int(stats[stat])
        modifier = ((stats[stat] - 10) / 2)
        if modifier < 0 and modifier % 2:
            modifier -= 1
        modifier = int(modifier)
        mods.append(modifier)

    characters = []
    character = {
        "name": name,
        "hp": 0,
        "strength": stats[0],
        "dexterity": stats[1],
        "constitution": stats[2],
        "intelligence": stats[3],
        "wisdom": stats[4],
        "charisma": stats[5],
        "str_save": mods[0],
        "dex_save": mods[1],
        "con_save": mods[2],
        "int_save": mods[3],
        "wis_save": mods[4],
        "cha_save": mods[5],
        "acrobatics": mods[1],
        "animal handling": mods[4],
        "arcana": mods[3],
        "athletics": mods[0],
        "deception": mods[5],
        "history": mods[3],
        "insight": mods[4],
        "intimidation": mods[5],
        "investigation": mods[3],
        "medicine": mods[4],
        "nature": mods[3],
        "perception": mods[4],
        "performance": mods[5],
        "persuasion": mods[5],
        "religion": mods[3],
        "sleight of hand": mods[1],
        "stealth": mods[1],
        "survival": mods[4],
        "attacks": []
    }
   
    if not os.path.isfile(f'.\\servers\\{server}.json'):
        with open(f'.\\servers\\{server}.json', 'w') as f:
            json.dump([character], f)
        return True
    else:   
        with open(f'.\\servers\\{server}.json') as f:
            characters = json.load(f)

    # duplicate check
    for c in characters:
        if c["name"] == character["name"]:
            return False

    characters.append(character)

    with open(f'.\\servers\\{server}.json', 'w') as f:
        json.dump(characters, f)
    return True