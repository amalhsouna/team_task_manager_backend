from models.models import db, Team

class TeamService:
    @staticmethod
    def create_team(name):
        new_team = Team(name=name)
        db.session.add(new_team)
        db.session.commit()
        return new_team

    @staticmethod
    def get_all_teams():
        return Team.query.all()

    @staticmethod
    def get_detail_team(id):
        return Team.query.get(id)