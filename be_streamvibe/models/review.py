from django.db import models

from .user import User
from .movie import Movie

# Create your models here.
class Review(models.Model):
    review = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.review

