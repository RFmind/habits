import json
import logging as log
from flask import Blueprint, jsonify, request, make_response, current_app
from cerberus import Validator

from app import db
from app.habits_api.models import Habit, Activity
from app.habits_api.util import as_json, datetime_as_str, activity_as_dict

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

@habits_api.route('/', methods=['GET'])
def habits():
    result = as_json(Habit.query.all())
    log.info('Sending list of habits: {}'.format(result))
    return make_response(result, 200)

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

    log.info('Added a new habit: {}'.format(as_json(new_habit)))
    log.info('Sending 201 Created with new habit: {}'.format(
        as_json(new_habit)))
    return make_response(as_json(new_habit), 201)

@habits_api.route('/<id>', methods=['GET'])
def show_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        log.info('Habit not found. id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response("Not Found", 404)

    log.info('Sending habit: {}'.format(as_json(habit)))
    return make_response(
        as_json(habit),
        200)

@habits_api.route('/<id>', methods=['DELETE'])
def delete_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        log.info('Habit not found. id: {}'.format(id))
        log.info('Sending 404 Not Found')
        return make_response("Not Found", 404)

    habit.delete()
    log.info('Deleted habit: {}'.format(habit))
    return make_response(
        as_json(habit),
        200)

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
    log.info('Habit with id {} updated: {}'.format(
        id, as_json(habit)))
    return make_response(
        as_json(habit),
        200)

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

    log.info('Added activity: {}'.format(activity_as_dict(activity)))
    return make_response(
        json.dumps(activity_as_dict(activity)), 
        200)

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

    dict_activities = list(map(activity_as_dict, activities))
    log.info('Sending activities: {}'.format(dict_activities))
    return make_response(json.dumps(dict_activities), 200)

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

    log.info('Sending activity: {} for habit with id {}'.format(
        activity_as_dict(activity), id))
    return make_response(json.dumps(activity_as_dict(activity)), 200)


