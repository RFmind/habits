from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import configuration_mode

db = SQLAlchemy()

def create_app(config_mode_name):

    app = Flask(
        __name__,
        static_folder='../../static/dist',
        template_folder='../../static')
    app.config.from_object(configuration_mode[config_mode_name])

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    from app.habits_api.views import habits_api
    app.register_blueprint(habits_api)

    with app.app_context():
        db.create_all()

    return app


