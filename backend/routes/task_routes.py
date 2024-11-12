
from flask import Blueprint, request, jsonify
from services.task_service import TaskService

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/teams/<int:team_id>/tasks', methods=['GET', 'POST'])
def manage_tasks(team_id):
    if request.method == 'POST':
        new_task = TaskService.create_task(
            request.json['title'], 
            request.json['description'], 
            team_id
        )
        return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description}), 201
    tasks = TaskService.get_tasks_by_team(team_id)
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])
