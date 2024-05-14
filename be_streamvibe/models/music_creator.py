from django.db import models


class MusicCreator(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField(max_length=250)

    def __str__ (self):
        return self.name
    