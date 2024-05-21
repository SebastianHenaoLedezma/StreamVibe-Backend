from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=125)
    verified = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name
