
from models.models import db, Task

class TaskService:
    @staticmethod
    def create_task(title, description, team_id):
        new_task = Task(title=title, description=description, team_id=team_id)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_tasks_by_team(team_id):
        return Task.query.filter_by(team_id=team_id).all()
