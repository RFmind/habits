import json

def as_dict(habit):
    result = {}
    fields = ['id', 'name']
    for field in fields:
        if hasattr(habit, field) and getattr(habit, field) is not None:
            result[field] = getattr(habit, field)
    return result

def as_json(data):
    if data is None:
        return None
    if type(data) == list:
        return json.dumps(list(map(as_dict, data)))
    return json.dumps(as_dict(data))

