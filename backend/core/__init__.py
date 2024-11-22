import os

from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apifairy import APIFairy


load_dotenv()

database = SQLAlchemy()

db_migration = Migrate()

ma = Marshmallow()

apifairy = APIFairy()

def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)

    app.config.from_object(config_type)

    initialize_extensions(app)

    register_blueprint(app)

    return app

def initialize_extensions(app):
    database.init_app(app)

    db_migration.init_app(app, database)

    ma.init_app(app)

    apifairy.init_app(app)

    import core.models.models

def register_blueprint(app):
    from core.api import teams_api_blueprint
    from core.api import tasks_api_blueprint

    app.register_blueprint(teams_api_blueprint, url_prefix="/api")
    app.register_blueprint(tasks_api_blueprint, url_prefix="/api")