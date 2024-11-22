from flask_restx import Resource
from core.services import team_service
from flask import jsonify

from . import teams_api_blueprint

@teams_api_blueprint.route("/teams", methods=["GET"])
class Teams(Resource):
    def get(self, id):
        team = team_service.get_detail_team(id)
        if team is None:
            return {'message': 'Team not found'}, 404
        return jsonify({
            'id': team.id,
            'name': team.name,
            'task': [task.to_dict() for task in team.tasks]
        })
