from core.services.team_service import TeamService
from core.schema.team_schema import CreateTeamSchema, TeamSchema
from flask import abort
from apifairy import response, body

from . import teams_api_blueprint

team_schema = TeamSchema(many=True)  # for a list of teams
single_team_schema = TeamSchema()  # for a tema by id


@teams_api_blueprint.route("/teams", methods=["GET"])
@response(team_schema)
def team():
    return TeamService.get_all_teams()


@teams_api_blueprint.route("/teams", methods=["POST"])
@body(CreateTeamSchema)
@response(single_team_schema)
def create_team(data):
    try:
        new_team = TeamService.create_team(data["name"])
        return new_team
    except Exception as e:
        abort(400, description=f"Erreur lors de la création de l'équipe : {str(e)}")


@teams_api_blueprint.route("/teams/<int:id>", methods=["GET"])
@response(single_team_schema)
def get_team_by_id(id):
    """Récupère une équipe par son ID"""
    team = TeamService.get_detail_team(id)
    if team is None:
        abort(404, description="Team not found")
    return team
