from flask import Blueprint, request, jsonify
from services.team_service import TeamService

team_bp = Blueprint('team_bp', __name__)

@team_bp.route('/teams', methods=['GET', 'POST'])
def manage_teams():
    if request.method == 'POST':
        new_team = TeamService.create_team(request.json['name'])
        return jsonify({'id': new_team.id, 'name': new_team.name}), 201
    teams = TeamService.get_all_teams()
    return jsonify([{'id': team.id, 'name': team.name} for team in teams])

@team_bp.route('/teams/add', methods=['POST'])
def add_team():
    data = request.json
    new_team = TeamService.create_team(data['name'])
    return jsonify({'id': new_team.id, 'name': new_team.name}), 201

@team_bp.route('/teams/<int:id>', methods=['GET'])
def get_team_detail(id):
    team = TeamService.get_detail_team(id) 
    if team is None:
        ConnectionAbortedError(404, description="Team not found")
    return jsonify({
        'id': team.id,
        'name': team.name,
        'task': [task.to_dict() for task in team.tasks] 
    })