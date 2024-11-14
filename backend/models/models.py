
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='team', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def to_dict(self):
            return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'team_id': self.team_id
            }
