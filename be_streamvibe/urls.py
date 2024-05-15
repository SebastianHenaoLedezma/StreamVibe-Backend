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
from .views.actor_view import list_create_actor, retrieve_update_delete_actor
from .views.director_view import list_create_director, retrieve_update_delete_director
from .views.faq_view import list_create_faq, retrieve_update_delete_faq
from .views.music_creator_view import list_create_musicCreator, retrieve_update_delete_musicCreator
from .views.rating_view import list_create_rating, retrieve_update_delete_rating
from .views.review_view import list_create_review, retrieve_update_delete_review
from .views.supportRequest_view import list_create_support_request, retrieve_update_delete_support_request
from .views.user_view import list_create_user, retrieve_update_delete_user


router = routers.DefaultRouter()

urlpatterns = [
    path('api/movies/', list_create_movie, name='movie-list-create'),
    path('api/movies/<int:pk>/', retrieve_update_delete_movie, name='movie-retrieve-update-delete'),

    path('api/genres', list_create_genre, name= 'genres-list-create'),
    path('api/genres/<int:pk>', retrieve_update_delete_genre, name='genres-retrieve-update-delete'),

    path('api/languages', list_create_language, name='language-list-create'),
    path('api/languages/<int:pk>', retrieve_update_delete_language, name='language-retrieve-update-delete'),

    path('api/actors', list_create_actor, name='actor-list-create'),
    path('api/actors/<int:pk>', retrieve_update_delete_actor, name='actor-retrieve-update-delete'),

    path('api/directors', list_create_director, name='director-list-create'),
    path('api/directors/<int:pk>', retrieve_update_delete_director, name='director-retrieve-update-delete'),

    path('api/faqs', list_create_faq, name='faq-list-create'),
    path('api/faqs/<int:pk>', retrieve_update_delete_faq, name='faq-retrieve-update-delete'),

    path('api/music_creator', list_create_musicCreator, name='music_creator-list-create'),
    path('api/music_creator/<int:pk>', retrieve_update_delete_musicCreator, name='music_creator-retrieve-update-delete'),

    path('api/ratings', list_create_rating, name='rating-list-create'),
    path('api/ratings/<int:pk>', retrieve_update_delete_rating, name='rating-retrieve-update-delete'),

    path('api/review', list_create_review, name='review-list-create'),
    path('api/review/<int:pk>', retrieve_update_delete_review, name='review-retrieve-update-delete'),

    path('api/suportrequests', list_create_support_request, name='suport-request-list-create'),
    path('api/suportrequests/<int:pk>', retrieve_update_delete_support_request, name='suport-request-retrieve-update-delete'),
    
    path('api/users', list_create_user, name='user-list-create'),
    path('api/users/<int:pk>', retrieve_update_delete_user, name='user-retrieve-update-delete'),
]

urlpatterns += router.urls

