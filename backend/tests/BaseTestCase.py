from flask_testing import TestCase
from app import create_app, db

class BaseTestCase(TestCase):
    def create_app(self):
        # Configure une application Flask pour les tests
        app = create_app('testing')  # Le mode "testing" doit être configuré dans config.py
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
