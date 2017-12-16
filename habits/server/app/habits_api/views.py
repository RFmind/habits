import json
from flask import Blueprint, jsonify, request, make_response
from cerberus import Validator

from app import db
from app.habits_api.models import Habit, Activity
from app.habits_api.util import as_json, datetime_as_str

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

@habits_api.route('/', methods=['GET'])
def habits():
    return make_response(as_json(Habit.query.all()), 200)

@habits_api.route('/', methods=['POST'])
def add_habit():
    data = request.get_json(silent=True)
    validator = Validator()
    schema = {'name': {'required': True, 'type': 'string', 'maxlength': 50}}

    if data is None or not validator.validate(data, schema):
        return make_response("Bad Request", 400)

    new_habit = Habit(name=data['name'])
    new_habit.save()

    return make_response(as_json(new_habit), 201)

@habits_api.route('/<id>', methods=['GET'])
def show_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        return make_response("Not Found", 404)

    return make_response(
        as_json(habit),
        200)

@habits_api.route('/<id>', methods=['DELETE'])
def delete_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        return make_response("Not Found", 404)

    habit.delete()
    return make_response(
        as_json(habit),
        200)

@habits_api.route('/<id>', methods=['PUT'])
def update_habit(id):
    habit = Habit.query.get(id)
    
    if habit is None:
        return make_response('Not Found', 404)

    data = request.get_json(silent=True)
    validator = Validator()
    schema = {'name': {'required': True, 'type': 'string', 'maxlength': 50}}

    if data is None or not validator.validate(data, schema):
        return make_response('Bad Request', 400)

    habit.name = data['name']
    db.session.commit()
    return make_response(
        as_json(habit),
        200)

@habits_api.route('/batch-delete/', methods=['POST'])
def batch_delete():
    data = request.get_json(silent=True)

    if data is None or len(data) == 0:
        return make_response('Bad Request', 400)

    result = {'success': [], 'failure': []}

    for habit_id in data:
        habit = Habit.query.get(habit_id)

        if habit is None:
            result['failure'].append(habit_id)
        else:
            habit.delete()
            result['success'].append(habit_id)

    if len(result['success']) == 0:
        return make_response('Not Found', 404)

    return make_response(json.dumps(result), 200)

@habits_api.route('/<id>/trigger/', methods=['GET'])
def trigger_habit(id):
    habit = Habit.query.get(id)

    if habit is None:
        return make_response('Not Found', 404)

    activity = Activity(habit_id=id)
    db.session.add(activity)
    db.session.commit()

    trigger_time_str = datetime_as_str(activity.trigger_time)

    return make_response(
        json.dumps({'trigger_time': '{}'.format(trigger_time_str)}), 
        200)

