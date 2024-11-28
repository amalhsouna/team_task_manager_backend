from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Column,
)

from core import database as db

class Team(db.Model):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    tasks = db.relationship("Task", back_populates="team", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Team(name={self.name})>"

class Task(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)
    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team = db.relationship("Team", back_populates="tasks")

    def __repr__(self):
        return f"<Task(title={self.title})>"
