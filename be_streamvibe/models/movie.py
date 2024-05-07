from django.db import models
from datetime import date

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    release_date = models.DateField(default=date.today)
    duration = models.IntegerField(default=0)
    movie_url = models.CharField(max_length=200)
    trailer_url = models.CharField(max_length=200)
    trailer_thumbnail_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    