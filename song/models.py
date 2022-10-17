from django.db import models
import uuid


# Create your models here.
class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.FileField(max_length=200, blank=True, null=True)
    durations = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title


# from django import forms

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Like(models.Model):
    objects = None
    user_id = models.CharField(max_length=200)
    song_title = models.TextField()
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id
