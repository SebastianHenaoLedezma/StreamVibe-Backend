from django.contrib import admin
from .models.movie import Movie
from .models.genre import Genre
from .models.director import Director
from .models.language import Language


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres', 'directors', 'languages',)


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Language)

