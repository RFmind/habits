from flask import Blueprint

habits_api = Blueprint('habits_api', __name__, url_prefix='/habits')

@habits_api.route('/', methods=['GET'])
def index_habits():
    return '[]'

