import json
import logging as log
from flask import Blueprint, jsonify, request, make_response, current_app
from cerberus import Validator

from app import db
from app.habits_api.models import Habit, Activity
from app.habits_api.encoders import HabitEncoder, DeepHabitEncoder

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

@habits_api.route('/', methods=['GET'])
def habits():
    habits = Habit.query.all()
    habits_json = json.dumps(habits, cls=DeepHabitEncoder)

    log.info('Sending list of habits: {}'.format(habits_json))
    return make_response(habits_json, 200)

@habits_api.route('/', methods=['POST'])
def add_habit():
    data = request.get_json(silent=True)
    validator = Validator()
    schema = {'name': {'required': True, 'type': 'string', 'maxlength': 50}}

    if data is None or not validator.validate(data, schema):
        log.info('Received bad data from user: {}'.format(request.data))
        log.info('Sending 400 Bad Request')
        return make_response("Bad Request", 400)

    new_habit = Habit(name=data['name'])
    new_habit.save()
    new_habit_json = json.dumps(new_habit, cls=HabitEncoder)

    log.info('Added a new habit: {}'.format(new_habit))
    log.info('Sending 201 Created with new habit: {}'.format(new_habit))
    return make_response(new_habit_json, 201)

@habits_api.route('/<id>', methods=['GET'])
def show_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        log.info('Habit not found. id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response("Not Found", 404)

    habit_json = json.dumps(habit, cls=HabitEncoder)

    log.info('Sending habit: {}'.format(habit))
    return make_response(habit_json, 200)

@habits_api.route('/<id>', methods=['DELETE'])
def delete_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        log.info('Habit not found. id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response("Not Found", 404)

    habit.delete()
    habit_json = json.dumps(habit, cls=HabitEncoder)

    log.info('Deleted habit: {}'.format(habit))
    return make_response(habit_json, 200)

@habits_api.route('/<id>', methods=['PUT'])
def update_habit(id):
    habit = Habit.query.get(id)
    
    if habit is None:
        log.info('Habit not found. id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    data = request.get_json(silent=True)
    validator = Validator()
    schema = {'name': {'required': True, 'type': 'string', 'maxlength': 50}}

    if data is None or not validator.validate(data, schema):
        log.info('Received bad data from user: {}'.format(request.data))
        log.info('Sending 400 Bad Request')
        return make_response('Bad Request', 400)

    habit.name = data['name']
    db.session.commit()
    habit_json = json.dumps(habit, cls=HabitEncoder)

    log.info('Habit with id {} updated: {}'.format(id, habit))
    return make_response(habit_json, 200)

@habits_api.route('/batch-delete/', methods=['POST'])
def batch_delete():
    data = request.get_json(silent=True)

    if data is None or len(data) == 0:
        log.info('Received bad data from user: {}'.format(request.data))
        log.info('Sending 400 Bad Request')
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
        log.info('No habits found, ids: {}'.format(data))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    log.info('Batch deleted some/all of the habits, results: {}'.format(result))
    return make_response(json.dumps(result), 200)

@habits_api.route('/<id>/trigger/', methods=['GET'])
def trigger_habit(id):
    habit = Habit.query.get(id)

    if habit is None:
        log.info('Habit not found, id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    activity = Activity(habit_id=id)
    db.session.add(activity)
    db.session.commit()

    activity_json = json.dumps(activity.as_dict())

    log.info('Added activity: {}'.format(activity_json))
    return make_response(activity_json, 200)

@habits_api.route('/<id>/activities/', methods=['GET'])
def list_triggers(id):
    habit = Habit.query.get(id)

    if habit is None:
        log.info('Habit not found, id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    activities = habit.activities

    if activities is None:
        log.info('No activities found')
        log.info('Sending 404 Not Found')
        return make_response(json.dumps([]), 200)

    activities_json = json.dumps(
        list(map(lambda a: a.as_dict(), activities)))

    log.info('Sending activities: {}'.format(activities_json))
    return make_response(activities_json, 200)

@habits_api.route('/<idh>/activities/<ida>', methods=['GET'])
def get_activity_by_id(idh, ida):
    habit = Habit.query.get(idh)

    if habit is None:
        log.info('Habit not found, id: {}'.format(idh))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    activity = Activity.query.get(ida)

    if activity is None:
        log.info('Activity not found, id: {}'.format(ida))
        log.info('Sending 404 Not Found')
        return make_response('Not Found', 404)

    activity_json = json.dumps(activity.as_dict())

    log.info('Sending activity: {} for habit with id {}'.format(
        activity_json, id))
    return make_response(activity_json, 200)

