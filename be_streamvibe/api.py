from .models import Movie, Genre, Director, Language
from rest_framework import viewsets, permissions
from .serializers.movie_serializer import MovieSerializer
from .serializers.genre_serializer import GenreSerializer
from .serializers.director_serializer import DirectorSerializer
from .serializers.language_serializer import LanguageSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GenreSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DirectorSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LanguageSerializer

