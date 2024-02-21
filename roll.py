from random import randint


def oned20mod(mod: int) -> int:
    """Roll one dice with y faces and add a modifier"""
    result = randint(1,20) 
    if result == 20:
        return 100 # critical success
    elif result == 1:
        return -100 # critical failure

    return result + mod


def xdy(x: int, y: int) -> list[int]:
    """Roll x number of dice with y faces each"""
    results = []
    for dice in range(x):
        results.append(randint(1,y))
    return results
