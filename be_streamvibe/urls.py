from rest_framework import routers
from django.urls import path

from .views.movie_view import list_create_movie, retrieve_update_delete_movie
from .views.genre_view import genre, all_data_genre, all_genre
from .views.faq_view import list_create_faq
from .views.rating_view import list_create_rating, retrieve_update_delete_rating
from .views.supportRequest_view import list_create_support_request
from .views.user_view import list_create_user, retrieve_update_delete_user

router = routers.DefaultRouter()

urlpatterns = [
    path('api/movies/', list_create_movie, name='movie-list-create'),
    path('api/movies/<int:pk>/', retrieve_update_delete_movie, name='movie-retrieve-update-delete'),

    path('api/genres', genre, name='genres-list-create'),
    path('api/genres/<int:pk>', all_genre, name='genres-retrieve-update-delete'),

    path('api/top-genres/<int:pk>', all_data_genre, name='genres-retrieve-update-delete'),

    path('api/faqs', list_create_faq, name='faq-list-create'),

    path('api/ratings', list_create_rating, name='rating-list-create'),   # creo que seria la parte de jorge que debo mostrar o no sabria como decir aunque no creo 
    path('api/ratings/<int:pk>', retrieve_update_delete_rating, name='rating-retrieve-update-delete'),

    path('api/suportrequests', list_create_support_request, name='suport-request-list-create'),

    path('api/users', list_create_user, name='user-list-create'),
    path('api/users/<int:pk>', retrieve_update_delete_user, name='user-retrieve-update-delete'),
]

urlpatterns += router.urls
