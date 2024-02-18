import json
import os

def addCharacter(name: str, stats: list[str], server: str) -> bool:
    """Creates JSON file for server if none, adds character if not already added"""
    file = f'.\\servers\\{server}.json'
    mods = []
    # convert stats to integers and calculate modifiers
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
   
    if not os.path.isfile(file):
        with open(file, 'w') as f:
            json.dump([character], f)
        return True
    else:   
        with open(file) as f:
            characters = json.load(f)

    # duplicate check
    for c in characters:
        if c["name"] == character["name"]:
            return False

    characters.append(character)

    with open(file, 'w') as f:
        json.dump(characters, f)
    return True


def updateSaves(name: str, saves: list[str], server: str) -> bool:
    """Search JSON file for character, then update save values"""
    file = f'.\\servers\\{server}.json'
    for save in range(len(saves)):
        saves[save] = int(saves[save])

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["str_save"] = saves[0]
    update["dex_save"] = saves[1]
    update["con_save"] = saves[2]
    update["int_save"] = saves[3]
    update["wis_save"] = saves[4]
    update["cha_save"] = saves[5]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True


def updateStats(name: str, stats: list[str], server: str) -> bool:
    """Search JSON file for character, then update save values"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(stats)):
        stats[stat] = int(stats[stat])

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["strength"] = stats[0]
    update["dexterity"] = stats[1]
    update["constitution"] = stats[2]
    update["intelligence"] = stats[3]
    update["wisdom"] = stats[4]
    update["charisma"] = stats[5]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True

def athletics(name: str, athletics: str, server: str) -> bool:
    """Search JSON file for character, then update athletics bonus"""
    file = f'.\\servers\\{server}.json'
    athletics = int(athletics)

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["athletics"] = athletics

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True


def dexs_update(name: str, dex_skills: list[str], server: str) -> bool:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(dex_skills)):
        dex_skills[stat] = int(dex_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["acrobatics"] = dex_skills[0]
    update["sleight of hand"] = dex_skills[1]
    update["stealth"] = dex_skills[2]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True

def ints_update(name: str, int_skills: list[str], server: str) -> bool:
    """Search JSON file for character, then update intelligence bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(int_skills)):
        int_skills[stat] = int(int_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["arcana"] = int_skills[0]
    update["history"] = int_skills[1]
    update["investigation"] = int_skills[2]
    update["nature"] = int_skills[3]
    update["religion"] = int_skills[4]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True

def wiss_update(name: str, wis_skills: list[str], server: str) -> bool:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(wis_skills)):
        wis_skills[stat] = int(wis_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["animal handling"] = wis_skills[0]
    update["insight"] = wis_skills[1]
    update["medicine"] = wis_skills[2]
    update["perception"] = wis_skills[3]
    update["survival"] = wis_skills[4]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True

def chas_update(name: str, cha_skills: list[str], server: str) -> bool:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(cha_skills)):
        cha_skills[stat] = int(cha_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    update["deception"] = cha_skills[0]
    update["intimidation"] = cha_skills[1]
    update["performance"] = cha_skills[2]
    update["persuasion"] = cha_skills[3]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True