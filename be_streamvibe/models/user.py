from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=125)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
