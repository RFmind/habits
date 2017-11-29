from flask import Blueprint, jsonify
from app.habits_api.models import Habit

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

@habits_api.route('/', methods=['GET'])
def index_habits():
    return jsonify(Habit.query.all())


