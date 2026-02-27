from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        team_marvel, _ = Team.objects.get_or_create(
            name='Team Marvel',
            defaults={'members_count': 0, 'total_activity': 0}
        )
        team_dc, _ = Team.objects.get_or_create(
            name='Team DC',
            defaults={'members_count': 0, 'total_activity': 0}
        )

        # Marvel superheroes
        marvel_heroes = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com'},
            {'name': 'Captain America', 'email': 'captainamerica@marvel.com'},
            {'name': 'Thor', 'email': 'thor@marvel.com'},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com'},
        ]

        # DC superheroes
        dc_heroes = [
            {'name': 'Superman', 'email': 'superman@dc.com'},
            {'name': 'Batman', 'email': 'batman@dc.com'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com'},
            {'name': 'The Flash', 'email': 'theflash@dc.com'},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com'},
        ]

        # Create Marvel users
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel',
                total_activity=0
            )
            marvel_users.append(user)
            team_marvel.members_count += 1

        # Create DC users
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team DC',
                total_activity=0
            )
            dc_users.append(user)
            team_dc.members_count += 1

        team_marvel.save()
        team_dc.save()

        # Create activities
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Yoga']
        for user in marvel_users + dc_users:
            for i in range(3):
                activity = Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_types[i % len(activity_types)],
                    duration=30 + (i * 10),
                    calories_burned=200 + (i * 50),
                    date=datetime.now() - timedelta(days=i)
                )
                user.total_activity += activity.duration
            user.save()
            team_marvel.total_activity += user.total_activity if user.team == 'Team Marvel' else 0
            team_dc.total_activity += user.total_activity if user.team == 'Team DC' else 0

        team_marvel.save()
        team_dc.save()

        # Create workouts
        workouts = [
            {'name': 'Morning Jog', 'description': 'Easy 5km jog', 'duration': 30, 'intensity': 'Low'},
            {'name': 'HIIT Training', 'description': 'High intensity interval training', 'duration': 45, 'intensity': 'High'},
            {'name': 'Yoga Session', 'description': 'Relaxing yoga session', 'duration': 60, 'intensity': 'Low'},
            {'name': 'Strength Training', 'description': 'Full body strength workout', 'duration': 50, 'intensity': 'High'},
            {'name': 'Swimming', 'description': 'Lap swimming', 'duration': 40, 'intensity': 'Medium'},
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        # Create leaderboard
        rank = 1
        all_users = sorted(marvel_users + dc_users, key=lambda u: u.total_activity, reverse=True)
        for user in all_users:
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                rank=rank,
                total_activity=user.total_activity
            )
            rank += 1

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
