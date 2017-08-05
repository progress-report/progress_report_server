import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP = 'app.py'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'not-very-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # fallback to `progress_report`
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/progress_report')

class TestingConfig(Config):
    TESTING = True
