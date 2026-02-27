
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

# Basic tests for model creation
class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Testers', total_activity=10)
        self.assertEqual(user.name, 'Test')

    def test_team_creation(self):
        team = Team.objects.create(name='Testers', members_count=1, total_activity=10)
        self.assertEqual(team.name, 'Testers')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity_type='Running', duration=30, calories_burned=200)
        self.assertEqual(activity.activity_type, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', user_name='Test', team='Testers', rank=1, total_activity=10)
        self.assertEqual(lb.rank, 1)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=30, intensity='Low')
        self.assertEqual(workout.name, 'Test Workout')