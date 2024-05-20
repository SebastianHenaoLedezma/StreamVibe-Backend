from django.db import models

from .user import User


# Create your models here.
class Support_request(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField(default=0)
    message = models.TextField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
