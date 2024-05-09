from django.db import models
from datetime import date
from .genre import Genre


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    release_date = models.DateField(default=date.today)
    duration = models.IntegerField(default=0)
    movie_url = models.CharField(max_length=200)
    trailer_url = models.CharField(max_length=200)
    trailer_thumbnail_url = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} ({', '.join(genre.name for genre in self.genres.all())})"
