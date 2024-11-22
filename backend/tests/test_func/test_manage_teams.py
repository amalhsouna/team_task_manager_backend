import unittest
from flask import Flask, jsonify, request
from flask_testing import TestCase
from services.team_service import TeamService

class TestManageTeams(TestCase):
    def test_create_team(self):
        """Test the creation of a new team via POST"""
        response = self.client.post('/teams', json={'name': 'Team A'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], 'Team A')

    def test_get_all_teams(self):
        """Test getting all teams via GET"""
        # Ajouter d'abord quelques équipes
        TeamService.create_team('Team A')
        TeamService.create_team('Team B')

        response = self.client.get('/teams')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]['name'], 'Team A')
        self.assertEqual(response.json[1]['name'], 'Team B')

if __name__ == '__main__':
    unittest.main()