import json
import os


failed = 0
worked = 1
protected = 2

def addCharacter(name: str, stats: list[int], server: str, user: int) -> bool:
    """Creates JSON file for server if none, adds character if not already added"""
    file = f'.\\servers\\{server}.json'
    mods = []
    # convert stats to integers and calculate modifiers
    for stat in range(len(stats)):
        modifier = ((stats[stat] - 10) / 2)
        if modifier < 0 and modifier % 2:
            modifier -= 1
        modifier = int(modifier)
        mods.append(modifier)

    characters = []
    character = {
        "name": name,
        "created by": user,
        "public": False,
        "max hp": 0,
        "current hp": 0,
        "strength": stats[0],
        "dexterity": stats[1],
        "constitution": stats[2],
        "intelligence": stats[3],
        "wisdom": stats[4],
        "charisma": stats[5],
        "strength save": mods[0],
        "dexterity save": mods[1],
        "constituion save": mods[2],
        "intelligence save": mods[3],
        "wisdom save": mods[4],
        "charisma save": mods[5],
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


def updateSaves(name: str, saves: list[int], server: str, user: int) -> int:
    """Search JSON file for character, then update save values"""
    file = f'.\\servers\\{server}.json'
    
    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2

    update["strength save"] = saves[0]
    update["dexterity save"] = saves[1]
    update["constitution save"] = saves[2]
    update["intelligence save"] = saves[3]
    update["wisdom save"] = saves[4]
    update["charisma save"] = saves[5]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def updateStats(name: str, stats: list[int], server: str, user: int) -> int:
    """Search JSON file for character, then update save values"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(stats)):
        stats[stat] = int(stats[stat])

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update["strength"] = stats[0]
    update["dexterity"] = stats[1]
    update["constitution"] = stats[2]
    update["intelligence"] = stats[3]
    update["wisdom"] = stats[4]
    update["charisma"] = stats[5]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def athletics(name: str, athletics: str, server: str, user: int) -> int:
    """Search JSON file for character, then update athletics bonus"""
    file = f'.\\servers\\{server}.json'
    athletics = int(athletics)

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update["athletics"] = athletics

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def dexs_update(name: str, dex_skills: list[str], server: str, user: int) -> int:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(dex_skills)):
        dex_skills[stat] = int(dex_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update["acrobatics"] = dex_skills[0]
    update["sleight of hand"] = dex_skills[1]
    update["stealth"] = dex_skills[2]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def ints_update(name: str, int_skills: list[str], server: str, user: int) -> int:
    """Search JSON file for character, then update intelligence bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(int_skills)):
        int_skills[stat] = int(int_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2

    update["arcana"] = int_skills[0]
    update["history"] = int_skills[1]
    update["investigation"] = int_skills[2]
    update["nature"] = int_skills[3]
    update["religion"] = int_skills[4]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def wiss_update(name: str, wis_skills: list[str], server: str, user: int) -> int:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(wis_skills)):
        wis_skills[stat] = int(wis_skills[stat])


    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update["animal handling"] = wis_skills[0]
    update["insight"] = wis_skills[1]
    update["medicine"] = wis_skills[2]
    update["perception"] = wis_skills[3]
    update["survival"] = wis_skills[4]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def chas_update(name: str, cha_skills: list[str], server: str, user: int) -> int:
    """Search JSON file for character, then update dexterity bonuses"""
    file = f'.\\servers\\{server}.json'
    for stat in range(len(cha_skills)):
        cha_skills[stat] = int(cha_skills[stat])

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update["deception"] = cha_skills[0]
    update["intimidation"] = cha_skills[1]
    update["performance"] = cha_skills[2]
    update["persuasion"] = cha_skills[3]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def update_HP(name: str, hp: int, server: str, user: int) -> int:
    """Adds max HP stat for a character and matches current HP to it"""
    file = f'.\\servers\\{server}.json'

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2
    
    update['max hp'] = hp
    update['current hp'] = hp

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1


def damage(name: str, damage: int, server: str, user: int) -> tuple[int, int]:
    """Subtracts damage from health"""
    file = f'.\\servers\\{server}.json'

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0, 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0, 0
    
    if update["created by"] != user:
        return 2, 0

    if damage < 0:
        damage *= -1
    new_health = update["current hp"] - damage
    update["current hp"] = new_health if new_health > 0 else 0

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1, new_health


def heal(name: str, heal: int, server: str) -> bool:
    """Adds max HP stat for a character and matches current HP to it"""
    file = f'.\\servers\\{server}.json'

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return False
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return False
    
    if heal < 0:
        heal *= -1
    new_health = update["current hp"] + heal
    update["current hp"] = new_health if new_health < update["max hp"] else update["max hp"]

    with open(file, 'w') as f:
        json.dump(characters, f)

    return True


def update_attack(name: str, attack: str, attack_info: list[int], server: str,
                   user: int) -> int:
    """Adds to or updates a character's list of attacks"""
    file = f'.\\servers\\{server}.json'

    attack_add = {
        "attack": attack,
        "hit mod": attack_info[0],
        "num dice": attack_info[1],
        "dice": attack_info[2],
        "plus": attack_info[3]
    }

    if os.path.isfile(file):
        with open(file) as f:
            characters = json.load(f)
    else:
        return 0
    
    update = next((character for character in characters if character["name"] == name), None)

    if not update:
        return 0
    
    if update["created by"] != user:
        return 2

    with open(file, 'w') as f:
        json.dump(characters, f)

    return 1
