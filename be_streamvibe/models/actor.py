from django.db import models
from cloudinary.models import CloudinaryField


class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo_url = CloudinaryField('image', default='')

    def __str__(self):
        return self.name
