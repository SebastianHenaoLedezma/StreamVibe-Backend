from django.db import models
from datetime import date
from .genre import Genre
from .director import Director
from .language import Language
from .actor import Actor


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    release_date = models.DateField(default=date.today)
    duration = models.IntegerField(default=0)
    movie_url = models.CharField(max_length=200)
    trailer_url = models.CharField(max_length=200)
    trailer_thumbnail_url = models.CharField(max_length=200)
    upcoming_movie = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    languages = models.ManyToManyField(Language)
    actors = models.ManyToManyField(Actor)
    

    def __str__(self):
        return (f"{self.title} "
                f"({', '.join(genre.name for genre in self.genres.all())}) "
                f"({', ' .join(director.name for director in self.directors.all())})"
                f"({', ' .join(language.name for language in self.languages.all())})")
