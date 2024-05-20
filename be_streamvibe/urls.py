from rest_framework import routers
from django.urls import path

from .views.movie_view import all_movie, all_info_movie, random_movie
from .views.genre_view import genre, all_genre
from .views.faq_view import list_create_faq
from .views.rating_view import list_create_rating, retrieve_update_delete_rating
from .views.supportRequest_view import list_create_support_request
from .views.user_view import list_users, create_user, retrieve_user, update_user, delete_user

router = routers.DefaultRouter()

urlpatterns = [
    path('movies/', all_movie, name='movie-list-create'),       # ✅
    path('movies/<int:pk>/', all_info_movie, name='movie-retrieve-update-delete'),      # ✅
    path('movies/random', random_movie, name='random_movie'),       # ✅

    path('genres', genre, name='genres-list-create'),       # ✅
    path('genres/<int:pk>', all_genre, name='genres-retrieve-update-delete'),       # ✅

    path('faqs', list_create_faq, name='faq-list-create'),

    path('ratings', list_create_rating, name='rating-list-create'),   # creo que seria la parte de jorge que debo mostrar o no sabria como decir aunque no creo 
    path('ratings/<int:pk>', retrieve_update_delete_rating, name='rating-retrieve-update-delete'),

    path('suportrequests', list_create_support_request, name='suport-request-list-create'),

    path('users', list_users, name='user-list-create'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>/', retrieve_user, name='retrieve_user'),
    path('users/<int:pk>/update/', update_user, name='update_user'),
    path('users/<int:pk>/delete/', delete_user, name='delete_user'),
]

urlpatterns += router.urls
