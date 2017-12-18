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
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


configuration_mode = {
    'TEST': TestConfig,
    'DEV': DevConfig,
    'PROD': ProdConfig
}
