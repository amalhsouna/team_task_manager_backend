from core.models.models import Task
from core import database as db


class TaskService:
    @staticmethod
    def create_task(title, description, team_id):
        new_task = Task(title=title, description=description, team_id=team_id)
        print(new_task)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_tasks_by_team(team_id):
        return Task.query.filter_by(team_id=team_id).all()
