
def is_valid(newhabit):

    if newhabit is None:
        return False
    elif 'name' not in newhabit:
        return False
    elif len(newhabit['name']) > 50:
        return False

    return True

