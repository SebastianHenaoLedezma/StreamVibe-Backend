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
    def save_review(review_comment, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        review = Review.objects.create(review=review_comment, user=user)
        return review
