import os

from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apifairy import APIFairy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

if os.getenv("FLASK_ENV") == "testing":
    print("ddddddddddd")
    load_dotenv(dotenv_path=".env_test")
else:
    load_dotenv()

database = SQLAlchemy()

db_migration = Migrate()

ma = Marshmallow()

apifairy = APIFairy()

print(os.getenv("CONFIG_TYPE"))


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

    app.config.from_object(config_type)

    initialize_extensions(app)

    register_blueprint(app)
    jwt = JWTManager(app)

    return app


def initialize_extensions(app):
    database.init_app(app)

    db_migration.init_app(app, database)

    ma.init_app(app)

    apifairy.init_app(app)

    import core.models.models
    import core.models.user


def register_blueprint(app):
    from core.api import teams_api_blueprint
    from core.api import tasks_api_blueprint
    from core.api import login_api_blueprint

    app.register_blueprint(teams_api_blueprint, url_prefix="/api")
    app.register_blueprint(tasks_api_blueprint, url_prefix="/api")
    app.register_blueprint(login_api_blueprint, url_prefix="/api")
