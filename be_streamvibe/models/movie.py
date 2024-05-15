from django.db import models
from datetime import date
from .genre import Genre
from .director import Director
from .language import Language
from .actor import Actor
from .music_creator import MusicCreator
from cloudinary.models import CloudinaryField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    release_date = models.DateField(default=date.today)
    duration = models.DurationField()
    movie_url = CloudinaryField('video', resource_type='video', default='')
    trailer_url = models.CharField(max_length=200)
    trailer_thumbnail_url = models.CharField(max_length=200)
    upcoming_movie = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    languages = models.ManyToManyField(Language)
    actors = models.ManyToManyField(Actor)
    music_creators = models.ManyToManyField(MusicCreator)
    

    def __str__(self):
        return self.title
