
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Column,
)

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    tasks = db.relationship('Task', backref='team', lazy=True)

    def __repr__(self):
        return f"<Team(name={self.name})>"

class Task(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)
    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"<Task(name={self.name})>"
