from rest_framework import routers
from django.urls import path

from .views.movie_view import all_movie, all_info_movie, random_movie, must_watch_movies, new_release_movies
from .views.genre_view import genre, get_genre, genre_top, get_genre_top
from .views.faq_view import list_create_faq
from .views.rating_view import list_create_rating, retrieve_update_delete_rating
from .views.supportRequest_view import list_create_support_request
from .views.user_view import list_users, create_user, retrieve_user, update_user, delete_user, login_user
from .views.review_view import list_reviews, create_review, retrieve_review, update_review, delete_review

router = routers.DefaultRouter()

urlpatterns = [
    path('api/movies/', all_movie, name='movie-list-create'),  # ✅
    path('api/movies/<int:pk>/', all_info_movie, name='movie-retrieve-update-delete'),  # ✅
    path('api/movies-random/', random_movie, name='movie-random'),  # ✅
    path('api/movies-new-releases/', new_release_movies, name='new-release-movies'),  # ✅
    path('api/movies-must-watch/', must_watch_movies, name='movie-must-watch'),  # ✅

    path('api/genres/', genre, name='genre-list-create'),  # ✅
    path('api/genres/<int:pk>/', get_genre, name='genre-retrieve-update-delete'),  # ✅
    path('api/genres-top/', genre_top, name='genre-top-list'),  # ✅
    path('api/genres-top/<int:pk>/', get_genre_top, name='genre-top-retrieve'),  # ✅

    path('api/faqs/', list_create_faq, name='faq-list-create'),  # ✅

    path('api/ratings/', list_create_rating, name='rating-list-create'),  # ✅ ❓
    path('api/ratings/<int:pk>/', retrieve_update_delete_rating, name='rating-retrieve-update-delete'),  # ✅ ❓

    path('api/reviews/', list_reviews, name='list_reviews'),
    path('api/movies/<int:movie_id>/reviews/', create_review, name='create_review'),
    path('api/reviews/<int:pk>/', retrieve_review, name='retrieve_review'),
    path('api/reviews-update/<int:pk>/<int:user_id>/', update_review, name='update_review'),
    path('api/reviews-delete/<int:pk>/', delete_review, name='delete_review'),

    path('api/support-requests/', list_create_support_request, name='support-request-list-create'),  # ❓

    path('api/users/', list_users, name='user-list'),  # ✅
    path('api/users-create/', create_user, name='user-create'),  # ✅
    path('api/users-login/', login_user, name='user-login'),
    path('api/users/<int:pk>/', retrieve_user, name='user-retrieve'),
    path('api/users/<int:pk>/update/', update_user, name='user-update'),
    path('api/users/<int:pk>/delete/', delete_user, name='user-delete'),
]

urlpatterns += router.urls
