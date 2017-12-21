import os

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    def __init__(self):
        os_dburl = os.getenv('OPENSHIFT_POSTGRESQL_DB_URL') + '/habits_prod'
        db_url = os.getenv('DATABASE_URL')
        self.SQLALCHEMY_DATABASE_URI = db_url if os_dburl is None else os_dburl

configuration_mode = {
    'TEST': TestConfig,
    'DEV': DevConfig,
    'PROD': ProdConfig
}
