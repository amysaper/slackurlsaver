import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "urls.config.DevelopmentConfig")
app.config.from_object(config_path)

import api
print(api.__file__)

import database
print(database.__file__)
#import views

print(app.config["DATABASE_URI"])

from database import Base, engine
Base.metadata.create_all(engine)




