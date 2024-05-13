from .models import Movie, Genre, Director, Language, Actor, User, Faq, Support_request, Review, Rating
from rest_framework import viewsets, permissions
from .serializers.movie_serializer import MovieSerializer
from .serializers.genre_serializer import GenreSerializer
from .serializers.director_serializer import DirectorSerializer
from .serializers.language_serializer import LanguageSerializer
from .serializers.actor_serializer import ActorSerializer 
from .serializers.user_serializer import UserSerializer
from .serializers.faq_serializer import FaqSerializer
from .serializers.supportRequest_serializer import SupportRequestSerializer
from .serializers.review_serializer import ReviewSerializer
from .serializers.rating_serializer import RatingSerializer


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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FaqSerializer

class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = Support_request.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SupportRequestSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RatingSerializer
