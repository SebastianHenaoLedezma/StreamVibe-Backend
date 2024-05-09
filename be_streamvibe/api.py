from .models import Movie, Genre
from rest_framework import viewsets, permissions
from .serializers.movie_serializer import MovieSerializer
from .serializers.genre_serializer import GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GenreSerializer
