from django.contrib import admin
from .models.movie import Movie
from .models.genre import Genre

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
