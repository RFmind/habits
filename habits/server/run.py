import os
from app import create_app

if __name__ == '__main__':
    settings_mode = os.getenv('SETTINGS_MODE')
    app = create_app(settings_mode)
    app.run()

