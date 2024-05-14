from django.contrib import admin
from .models.movie import Movie
from .models.genre import Genre
from .models.director import Director
from .models.language import Language
from .models.actor import Actor
from .models.music_creator import MusicCreator
from .models.user import User
from .models.faq import Faq
from .models.support_request import Support_request
from .models.review import Review
from .models.rating import Rating


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres', 'directors', 'languages', 'actors', 'music_creators',)


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Language)
admin.site.register(Actor)
admin.site.register(MusicCreator)
admin.site.register(User)
admin.site.register(Faq)
admin.site.register(Support_request)
admin.site.register(Review)
admin.site.register(Rating)