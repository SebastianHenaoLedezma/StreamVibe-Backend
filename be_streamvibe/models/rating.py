from django.db import models

from .user import User


# Create your models here.
class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating}"

    @staticmethod
    def create_or_update(review, stars, user):
        rating = Rating.objects.filter(review=review, user=user).first()
        if not rating:
            return Rating.objects.create(rating=stars, user=user)
        rating.rating = stars
        rating.save()
        return rating
