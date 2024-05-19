from django.db import models
from .genre import Genre
from .director import Director
from .language import Language
from .actor import Actor
from .music_creator import MusicCreator
from .review import Review
from .rating import Rating
from cloudinary.models import CloudinaryField
import datetime


def get_current_year():
    return datetime.date.today().year


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField(default=get_current_year)
    duration = models.DurationField()
    movie_url = CloudinaryField('video', resource_type='video', blank=True, null=True)
    trailer_url = models.CharField(max_length=200)          # TODO: change to CloudinaryField
    trailer_thumbnail_url = CloudinaryField('image', default='')
    upcoming_movie = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    languages = models.ManyToManyField(Language)
    actors = models.ManyToManyField(Actor)
    music_creators = models.ManyToManyField(MusicCreator)
    reviews = models.ManyToManyField(Review, default=[], blank=True)
    ratings = models.ManyToManyField(Rating, default=[], blank=True)

    def __str__(self):
        return self.title
