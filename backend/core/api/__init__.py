from flask import Blueprint

teams_api_blueprint = Blueprint("teams_api", __name__)

tasks_api_blueprint = Blueprint("tasks_api", __name__)

from . import tasks

from . import teams
