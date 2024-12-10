import unittest
from flask_testing import TestCase
from core import create_app, database as db
from core.services.team_service import TeamService
from core.models.models import Task

class TestManageTasks(TestCase):

    def create_app(self):
        """
        Creates an instance of the Flask application with the development configuration.
        """
        app = create_app()  
        app.config['TESTING'] = True  # Enables test mode (e.g., disables CSRF)
        return app

    def setUp(self):
        """
        Sets up prerequisites for each test. Modifications will be explicitly added without resetting the database.
        """
        self.client = self.app.test_client()

        # Add an object to the database
        task = Task(title="Initial Task", desciption="descrition of task")
        db.session.add(task)
        db.session.commit()

    def tearDown(self):
        """
        Cleans up specific test objects to avoid corrupting the existing database.
        """
        teams = Task.query.filter(Task.title.in_(["Initial Task", "Team A", "Team B"])).all()
        for team in teams:
            db.session.delete(team)
        db.session.commit()

    def test_create_team(self):
        """
        Tests the creation of a new team via POST.
        """
        response = self.client.post('/api/teams/1/tasks', json={'title': 'title f task'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], 'Team A')

    def test_get_all_teams(self):
        """
        Tests retrieving all teams via GET.
        """
        # Add teams using TeamService
        TeamService.create_team('Team A')
        TeamService.create_team('Team B')

        response = self.client.get('/api/teams')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)  # Includes "Initial Task", "Team A", "Team B"
        self.assertEqual(response.json[1]['name'], 'Team A')
        self.assertEqual(response.json[2]['name'], 'Team B')


if __name__ == '__main__':
    unittest.main()