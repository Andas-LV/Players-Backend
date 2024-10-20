from storages.backends.s3boto3 import S3Boto3Storage
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.user.username

class Player(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    avatar_url = models.ImageField(upload_to='players-avatars/', null=True, blank=True, storage=S3Boto3Storage())
    birth_date = models.DateField()
    age = models.IntegerField()
    height_cm = models.IntegerField()
    weight_kgs = models.IntegerField()
    positions = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    overall_rating = models.IntegerField()
    potential = models.IntegerField()
    value_euro = models.IntegerField()
    wage_euro = models.IntegerField()
    preferred_foot = models.CharField(max_length=50)
    international_reputation = models.IntegerField()
    weak_foot = models.IntegerField()
    skill_moves = models.IntegerField()
    body_type = models.CharField(max_length=100)
    release_clause_euro = models.IntegerField()
    national_team = models.CharField(max_length=100, blank=True, null=True)
    national_rating = models.IntegerField(blank=True, null=True)
    national_team_position = models.CharField(max_length=100, blank=True, null=True)
    national_jersey_number = models.IntegerField(blank=True, null=True)
    crossing = models.IntegerField()
    finishing = models.IntegerField()
    heading_accuracy = models.IntegerField()
    short_passing = models.IntegerField()
    volleys = models.IntegerField()
    dribbling = models.IntegerField()
    curve = models.IntegerField()
    freekick_accuracy = models.IntegerField()
    long_passing = models.IntegerField()
    ball_control = models.IntegerField()
    acceleration = models.IntegerField()
    sprint_speed = models.IntegerField()
    agility = models.IntegerField()
    reactions = models.IntegerField()
    balance = models.IntegerField()
    shot_power = models.IntegerField()
    jumping = models.IntegerField()
    stamina = models.IntegerField()
    strength = models.IntegerField()
    long_shots = models.IntegerField()
    aggression = models.IntegerField()
    interceptions = models.IntegerField()
    positioning = models.IntegerField()
    vision = models.IntegerField()
    penalties = models.IntegerField()
    composure = models.IntegerField()
    marking = models.IntegerField()
    standing_tackle = models.IntegerField()
    sliding_tackle = models.IntegerField()

    def __str__(self):
        return self.name

class FavoritePlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_players")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="favorited_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'player')