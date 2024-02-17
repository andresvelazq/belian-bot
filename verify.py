def verifyStats(stats):
    for stat in stats:
        if not stat.isnumeric():
            return False
    return True