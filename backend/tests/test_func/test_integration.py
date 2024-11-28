from flask_testing import TestCase
from app import create_app, db
from core.models.models import Task

class TestTaskIntegration(TestCase):
    def create_app(self):
        return create_app('TestingConfig')

    def setUp(self):
        db.create_all()
        self.client = self.app.test_client()
        task = Task(title="Initial Task", description="Setup description")
        db.session.add(task)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_task_lifecycle(self):
        # Vérifier que la tâche initiale existe
        response = self.client.get('/api/tasks')
        self.assertEqual(len(response.json['tasks']), 1)

        # Ajouter une nouvelle tâche
        data = {'title': 'New Task', 'description': 'New description'}
        post_response = self.client.post('/api/tasks', json=data)
        self.assertEqual(post_response.status_code, 201)

        # Vérifier qu'il y a deux tâches
        get_response = self.client.get('/api/tasks')
        self.assertEqual(len(get_response.json['tasks']), 2)
