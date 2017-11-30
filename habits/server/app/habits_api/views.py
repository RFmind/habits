from flask import Blueprint, jsonify, request, make_response
from app.habits_api.models import Habit
from app import db

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

def habit_to_dict(habit):
    result = {}
    result['id'] = habit.id
    if hasattr(habit, 'name'):
        result['name'] = habit.name
    return result

def habit_to_json(habit):
    return jsonify(habit_to_dict(habit))

def habits_to_json(habits):
    return jsonify(list(map(habit_to_dict, habits)))

@habits_api.route('/', methods=['GET', 'POST'])
def habits():
    if request.method == 'GET':
        response = make_response(habits_to_json(Habit.query.all()), 200)
        return response
    else:
        data = request.get_json(silent=True)
        if data is None:
            return make_response("Bad Request", 400)
 
        new_habit = Habit(data['id'], data['name'])
        new_habit.save()

        return make_response(habit_to_json(new_habit), 201)

@habits_api.route('/<id>', methods=['GET'])
def show_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        return make_response("Not Found", 404)

    return make_response(
        habit_to_json(habit),
        200)

@habits_api.route('/<id>', methods=['DELETE'])
def delete_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        return make_response("Not Found", 404)

    return make_response(
        habit_to_json(habit),
        200)

