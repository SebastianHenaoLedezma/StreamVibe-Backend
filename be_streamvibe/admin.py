from django.contrib import admin
from .models.movie import Movie
from .models.genre import Genre


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',)


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)

