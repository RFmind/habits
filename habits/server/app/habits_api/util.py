import json
import datetime

def as_dict(habit, include_activities):
    result = {}
    fields = ['id', 'name']
    for field in fields:
        if hasattr(habit, field) and getattr(habit, field) is not None:
            result[field] = getattr(habit, field)
    if include_activities:
        result['activities'] = list(
            map(activity_as_dict, getattr(habit, 'activities')))
    return result

def as_json(data, include_activities = False):
    if data is None:
        return None
    if type(data) == list:
        return json.dumps(
            list(map(lambda d: as_dict(d, include_activities), data)))
    return json.dumps(as_dict(data, include_activities))

def datetime_as_str(data):
    if isinstance(data, datetime.datetime):
        return data.strftime('%Y-%m-%dT%H:%M:%S')

def activity_as_dict(activity):
    if activity is None:
        return None
    return {'trigger_time': datetime_as_str(activity.trigger_time)}
