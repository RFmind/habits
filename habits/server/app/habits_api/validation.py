
def is_valid(newhabit):
    if newhabit is None:
        return False
    if 'name' not in newhabit:
        return False
    if len(newhabit['name']) > 50:
        return False
    return True

