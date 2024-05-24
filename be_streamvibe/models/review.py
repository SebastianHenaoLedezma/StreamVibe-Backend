from django.db import models

from .user import User
from .rating import Rating


# Create your models here.
class Review(models.Model):
    review = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    ratings = models.ManyToManyField(Rating, default=None, blank=True)

    def __str__(self):
        return self.review

    @staticmethod
    def save_review(review_comment, name):
        review = Review.objects.create(review=review_comment, name=name)
        return review
