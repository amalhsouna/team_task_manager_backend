from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.models import db
from routes.team_routes import team_bp
from routes.task_routes import task_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
migrate = Migrate(app, db)

# Enregistrer les Blueprints
app.register_blueprint(team_bp)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Créer les tables
    app.run(debug=True)