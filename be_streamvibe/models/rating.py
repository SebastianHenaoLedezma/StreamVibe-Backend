from django.db import models

from .user import User
from .movie import Movie
from .review import Review

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.movie_id and self.review_id:
            raise ValueError("Rating cannot be associated with both a movie and a review.")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.rating}"

