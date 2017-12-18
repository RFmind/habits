import os
from app import create_app

if __name__ == '__main__':
    settings_mode = os.getenv('SETTINGS_MODE')
    port_env = os.getenv('PORT')
    if port_env is None:
        port_env = 4000

    app = create_app(settings_mode)
    app.run(host='0.0.0.0', port=port_env)

