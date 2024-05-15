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
    list_display = ('title', 'display_genres', 'display_directors')
    search_fields = ('title',)
    filter_horizontal = ('genres', 'directors', 'languages', 'actors', 'music_creators',)
    list_filter = ('genres', 'directors', 'languages',)

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    display_genres.short_description = 'Genres'

    def display_directors(self, obj):
        return ", ".join([director.name for director in obj.directors.all()])
    display_directors.short_description = 'Directors'

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'movie',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'user', 'get_related_object')
    search_fields = ('rating', 'review__user__name')
    list_filter = ('rating', 'user')

    def get_related_object(self, obj):
        if obj.movie:
            return obj.movie.title
        elif obj.review:
            return obj.review.user
        else:
            return None

    get_related_object.short_description = 'Movie/Review'

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')



# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Actor)
admin.site.register(MusicCreator)
admin.site.register(User, UserAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Support_request)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating, RatingAdmin)