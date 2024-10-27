from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Team, Task
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/teams', methods=['GET', 'POST'])
def manage_teams():
    if request.method == 'POST':
        new_team = Team(name=request.json['name'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team.id), 201
    teams = Team.query.all()
    return jsonify([{'id': team.id, 'name': team.name} for team in teams])

@app.route('/teams/<int:team_id>/tasks', methods=['GET', 'POST'])
def manage_tasks(team_id):
    if request.method == 'POST':
        new_task = Task(title=request.json['title'], description=request.json['description'], team_id=team_id)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.id), 201
    tasks = Task.query.filter_by(team_id=team_id).all()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Créer les tables
    app.run(debug=True)
