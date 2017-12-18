import os
import logging
from app import create_app

if __name__ == '__main__':
    settings_mode = os.getenv('SETTINGS_MODE')
    port_env = os.getenv('PORT')
    if port_env is None:
        port_env = 4000

    logging.basicConfig(level=logging.INFO)
    app = create_app(settings_mode)
    app.run(host='0.0.0.0', port=port_env)

