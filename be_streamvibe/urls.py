from rest_framework import routers
from django.urls import path

from .views.movie_view import all_movie, all_info_movie, random_movie, must_watch_movies
from .views.genre_view import genre, all_genre
from .views.faq_view import list_create_faq
from .views.rating_view import list_create_rating, retrieve_update_delete_rating
from .views.supportRequest_view import list_create_support_request
from .views.user_view import list_users, create_user, retrieve_user, update_user, delete_user

router = routers.DefaultRouter()

urlpatterns = [
    path('movies/', all_movie, name='movie-list-create'),  # ✅
    path('movies/<int:pk>/', all_info_movie, name='movie-retrieve-update-delete'),  # ✅
    path('movies/random/', random_movie, name='movie-random'),
    path('movies/must-watch/', must_watch_movies, name='movie-must-watch'),

    path('genres/', genre, name='genre-list-create'),  # ✅
    path('genres/<int:pk>/', all_genre, name='genre-retrieve-update-delete'),  # ✅

    path('faqs/', list_create_faq, name='faq-list-create'),  # ✅

    path('ratings/', list_create_rating, name='rating-list-create'),  # ✅
    path('ratings/<int:pk>/', retrieve_update_delete_rating, name='rating-retrieve-update-delete'),  # ✅

    path('support-requests/', list_create_support_request, name='support-request-list-create'),

    path('users/', list_users, name='user-list'),
    path('users/create/', create_user, name='user-create'),
    path('users/<int:pk>/', retrieve_user, name='user-retrieve'),
    path('users/<int:pk>/update/', update_user, name='user-update'),
    path('users/<int:pk>/delete/', delete_user, name='user-delete'),
]

urlpatterns += router.urls
