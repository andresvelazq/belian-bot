import json
import os


def saving_throw(name: str, save: str, server: str) -> int:
    """Returns the modifier of a character's saving throw"""
    file = f'.\\servers\\{server}.json'
    save = save + ' save'

    with open(file) as f:
        characters = json.load(f)
    
    get = next((character for character in characters if character["name"] == name), None)

    if not get:
        print("I can't find this character.")

    return get[save]


def skill_mod(name: str, skill: str, server: str) -> int:
    """Returns the modifier of a character's saving throw"""
    file = f'.\\servers\\{server}.json'

    with open(file) as f:
        characters = json.load(f)
    
    get = next((character for character in characters if character["name"] == name), None)

    if not get:
        print("I can't find this character.")

    return get[skill]


def attack(name: str, attack: str, server: str) -> dict:
    """Returns the attack's information if it exists"""
    file = f'.\\servers\\{server}.json'

    with open(file) as f:
        characters = json.load(f)

    get = next((character for character in characters if character["name"] == name), None)

    if not get:
        print("No character")

    attack = next((atk for atk in get["attacks"] == attack), None)

    if not attack:
        print("No attack")

    return attack
