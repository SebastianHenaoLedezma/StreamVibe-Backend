from rest_framework import routers
from django.urls import path
from .api import (MovieViewSet,GenreViewSet, DirectorViewSet,
                  LanguageViewSet, ActorViewSet, UserViewSet,
                  FaqViewSet, SupportRequestViewSet, ReviewViewSet,
                  RatingViewSet, MusicCreatorViewSet
                  )
from .views.movie_view import list_create_movie, retrieve_update_delete_movie
from .views.genre_view import list_create_genre, retrieve_update_delete_genre
from .views.language_view import list_create_language, retrieve_update_delete_language


router = routers.DefaultRouter()

# router.register(r'api/movies', list_create_movie, 'movie-list-create')
# router.register(r'api/movies/<int:pk>', retrieve_update_delete_movie, 'movie-retrive-update-delete')
# router.register('api/genres', GenreViewSet, 'genres')
# router.register('api/directors', DirectorViewSet, 'directors')
# router.register('api/languages', LanguageViewSet, 'languages')
router.register('api/actors', ActorViewSet, 'actors')
router.register('api/music_creator', MusicCreatorViewSet, 'music_creator')
router.register('api/users', UserViewSet, 'users' )
router.register('api/faqs', FaqViewSet, 'faqs' )
router.register('api/supportRequest', SupportRequestViewSet, 'supportRequests' )
router.register('api/reviews', ReviewViewSet)
router.register('api/rating', RatingViewSet, 'ratings')

urlpatterns = [
    path('api/movies/', list_create_movie, name='movie-list-create'),
    path('api/movies/<int:pk>/', retrieve_update_delete_movie, name='movie-retrieve-update-delete'),
    path('api/genres', list_create_genre, name= 'genres-list-create'),
    path('api/genres/<int:pk>', retrieve_update_delete_genre, name='genres-retrieve-update-delete'),
    path('api/languages', list_create_language, name='language-list-create'),
    path('api/languages/<int:pk>', retrieve_update_delete_language, name='language-retrieve-update-delete'),
]

urlpatterns += router.urls

