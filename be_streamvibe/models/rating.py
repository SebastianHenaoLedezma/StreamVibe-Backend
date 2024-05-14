from django.db import models

from .user import User
from .movie import Movie
from .review import Review

# Create your models here.
class Rating(models.Model):
    rating = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.rating

