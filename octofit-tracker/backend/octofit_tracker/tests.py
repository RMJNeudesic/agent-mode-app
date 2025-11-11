from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='marvel', is_superhero=True)
        self.assertEqual(user.email, 'test@hero.com')
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', type='run', duration=30, date='2025-11-11')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        self.assertEqual(workout.name, 'Pushups')

class SimpleAPITest(APITestCase):
    """Tests for simple REST API endpoints"""
    
    def test_health_check_get(self):
        """Test the health check endpoint returns 200 and correct data"""
        url = reverse('health-check')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertIn('message', response.data)
        self.assertIn('version', response.data)
    
    def test_echo_post(self):
        """Test the echo endpoint returns the data sent"""
        url = reverse('echo')
        test_data = {
            'name': 'Test User',
            'message': 'Hello, World!'
        }
        response = self.client.post(url, test_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['received'], test_data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Echo successful')
    
    def test_echo_empty_post(self):
        """Test the echo endpoint handles empty data"""
        url = reverse('echo')
        response = self.client.post(url, {}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['received'], {})
    
    def test_health_check_wrong_method(self):
        """Test that health check only accepts GET requests"""
        url = reverse('health-check')
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_echo_wrong_method(self):
        """Test that echo only accepts POST requests"""
        url = reverse('echo')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
