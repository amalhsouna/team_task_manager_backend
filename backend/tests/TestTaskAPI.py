import json
from tests import BaseTestCase

class TestTaskAPI(BaseTestCase):
    def test_create_task(self):
        response = self.client.post(
            '/api/tasks',
            data=json.dumps({'name': 'Test Task', 'team_id': 1}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Task created successfully', response.data)
