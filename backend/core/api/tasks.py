from core.services.task_service import TaskService
from core.schema.task_schema import TaskSchema
from apifairy import response

from . import tasks_api_blueprint

task_schema = TaskSchema(many=True) # for many tasks

@tasks_api_blueprint.route("/tasks/<int:id>", methods=["GET"])
@response(task_schema)
def task(id):
    return TaskService.get_tasks_by_team(id)