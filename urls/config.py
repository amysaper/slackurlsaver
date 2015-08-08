import os

class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/urlsaver"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/urlsaver-test"
    DEBUG = True

class HerokuConfig(object):
    DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG = True
