def verifyStats(stats: list[str]) -> bool:
    """Verifies input stats are valid integers"""
    for stat in stats:
        if not stat.isnumeric():
            return False
    return True
