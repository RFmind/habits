from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    static_folder='../../static/dist',
    template_folder='../../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

from app.habits_api.views import habits_api
app.register_blueprint(habits_api)

db.create_all()
