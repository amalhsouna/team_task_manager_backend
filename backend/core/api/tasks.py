
from flask import request, jsonify
from core.services import task_service
from flask_restx import Resource, fields

from . import tasks_api_blueprint
# Création du namespace pour les tâches

@tasks_api_blueprint.route("/tasks", methods=["GET"])
class Tasks(Resource):
    def manage_tasks(team_id):
        if request.method == 'POST':
            new_task = task_service.create_task(
                request.json['title'], 
                request.json['description'], 
                team_id
            )
            return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description}), 201
        tasks = TaskService.get_tasks_by_team(team_id)
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])
