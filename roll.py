from random import randint


def onedymod(y: int, mod: int) -> int:
    """Roll one dice with y faces and add a modifier"""
    result = randint(1,y) 
    print(f'{result} + {mod}') # for testing purposes, will remove later
    return result + mod


def xdy(x: int, y: int) -> list[int]:
    """Roll x number of dice with y faces each"""
    results = []
    for dice in range(x):
        results.append(randint(1,y))
    return results
