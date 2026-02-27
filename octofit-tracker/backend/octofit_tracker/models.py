from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    total_activity = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members_count = models.IntegerField(default=0)
    total_activity = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'


class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class Leaderboard(models.Model):
    user_email = models.EmailField()
    user_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    rank = models.IntegerField()
    total_activity = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    intensity = models.CharField(max_length=20)

    class Meta:
        db_table = 'workouts'
