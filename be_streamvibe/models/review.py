from django.db import models

from .user import User
from .rating import Rating


# Create your models here.
class Review(models.Model):
    review = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.ManyToManyField(Rating, default=None, blank=True)

    def __str__(self):
        return self.review
