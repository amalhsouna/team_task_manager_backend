from flask import Blueprint

teams_api_blueprint = Blueprint("teams_api", __name__)

tasks_api_blueprint = Blueprint("tasks_api", __name__)

login_api_blueprint = Blueprint("auth_user_api", __name__)

from . import auth_user

from . import tasks

from . import teams
