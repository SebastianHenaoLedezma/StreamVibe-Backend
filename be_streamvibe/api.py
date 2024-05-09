from .models import Movie, Genre, Director, Language, Actor
from rest_framework import viewsets, permissions
from .serializers.movie_serializer import MovieSerializer
from .serializers.genre_serializer import GenreSerializer
from .serializers.director_serializer import DirectorSerializer
from .serializers.language_serializer import LanguageSerializer
from .serializers.actor_serializer import ActorSerializer 


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

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ActorSerializer
