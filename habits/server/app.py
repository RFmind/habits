from flask import Flask, render_template

from habits_api.habits_api import habits_api

def create_app():
    app = Flask(
        __name__,
        static_folder='../static/dist',
        template_folder='../static')
    
    @app.route('/')
    def index(): 
        return render_template('index.html')

    app.register_blueprint(habits_api)
    
    return app
