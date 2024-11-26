from core.services.task_service import TaskService
from core.schema.task_schema import TaskSchema, CreateTaskSchema
from apifairy import response, body
from flask import abort

from . import tasks_api_blueprint

task_schema = TaskSchema(many=True) # for many tasks
single_task_schema = TaskSchema() # for a task by id team

@tasks_api_blueprint.route("/tasks/<int:id>", methods=["GET"])
@response(task_schema)
def task(id):
    return TaskService.get_tasks_by_team(id)

@tasks_api_blueprint.route("/teams/<int:id>/tasks", methods=["POST"])
@body(CreateTaskSchema)
@response(single_task_schema)
def create_task(data, id):
    try:
        new_task = TaskService.create_task(data["title"], data["description"], id)
        return new_task
    except Exception as e:
        abort(400, description=f"Erreur lors de la création de task pour un equipe : {str(e)}")