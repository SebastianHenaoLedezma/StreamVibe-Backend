from django.db.models import Avg
from rest_framework import serializers

from be_streamvibe.models import Actor, Review, Director, MusicCreator, User
from be_streamvibe.models.movie import Movie
from be_streamvibe.models.genre import Genre
from be_streamvibe.models.rating import Rating
from be_streamvibe.models.language import Language

from be_streamvibe.serializers.director_serializer import DirectorSerializer
from be_streamvibe.serializers.actor_serializer import ActorSerializer
from be_streamvibe.serializers.music_creator_serializer import MusicCreatorSerializer
from be_streamvibe.serializers.review_serializer import ReviewSerializer
from be_streamvibe.serializers.genre_serializer import GenreSerializer
from be_streamvibe.serializers.language_serializer import LanguageSerializer


class ActorSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField(method_name='get_photo_url')

    class Meta:
        model = Actor
        fields = ('id', 'name', 'photo_url')

    @staticmethod
    def get_photo_url(actor):
        return actor.photo_url.url


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'verified')
        extra_kwargs = {
            'verified': {'required': False}
        }


class ReviewSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(method_name='get_average_rating')
    user_name = serializers.SerializerMethodField(method_name='get_user_name')
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Review
        fields = ('id', 'name', 'user_name', 'review', 'average_rating', 'user')

    @staticmethod
    def get_average_rating(review):
        average_rating = round(review.ratings.values_list('rating', flat=True).aggregate(Avg('rating')).get('rating__avg') or 0)
        return average_rating

    @staticmethod
    def get_user_name(review):
        if review.user:
            return review.user.name
        return ""

    @staticmethod
    def get_user(review):
        return UserSerializer(review.user).data


class DirectorSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField(method_name='get_photo_url')

    class Meta:
        model = Director
        fields = ('id', 'name', 'photo_url')

    @staticmethod
    def get_photo_url(director):
        return director.photo_url.url


class MusicCreatorSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField(method_name='get_photo_url')

    class Meta:
        model = MusicCreator
        fields = ('id', 'name', 'photo_url')

    @staticmethod
    def get_photo_url(music_creator):
        return music_creator.photo_url.url


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    movie_url = serializers.SerializerMethodField(method_name='get_movie_url')
    trailer_url = serializers.SerializerMethodField(method_name='get_trailer_url')
    trailer_image_url = serializers.SerializerMethodField(method_name='get_trailer_image')
    genres = serializers.SerializerMethodField(method_name='get_genres')
    directors = serializers.SerializerMethodField(method_name='get_directors')
    languages = serializers.SerializerMethodField(method_name='get_languages')
    actors = serializers.SerializerMethodField(method_name='get_actors')
    music_creators = serializers.SerializerMethodField(method_name='get_music_creators')
    reviews = serializers.SerializerMethodField(method_name='get_reviews')
    ratings = serializers.SerializerMethodField(method_name='get_ratings')

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'release_year', 'release_date', 'duration', 'movie_url', 'trailer_url',
            'trailer_image_url',
            'genres', 'directors', 'languages', 'actors', 'music_creators', 'reviews', 'ratings')

    @staticmethod
    def get_movie_url(movie):
        return movie.movie.url if movie.movie else None

    @staticmethod
    def get_trailer_url(movie):
        return movie.trailer.url if movie.trailer else None

    @staticmethod
    def get_trailer_image(movie):
        return movie.trailer_thumbnail.url if movie.trailer_thumbnail else None

    @staticmethod
    def get_genres(movie):
        return GenreSerializer(movie.genres.all(), many=True).data

    @staticmethod
    def get_directors(movie):
        return DirectorSerializer(movie.directors.all(), many=True).data

    @staticmethod
    def get_languages(movie):
        return LanguageSerializer(movie.languages.all(), many=True).data

    @staticmethod
    def get_actors(movie):
        return ActorSerializer(movie.actors.all(), many=True).data

    @staticmethod
    def get_music_creators(movie):
        return MusicCreatorSerializer(movie.music_creators.all(), many=True).data

    @staticmethod
    def get_reviews(movie):
        return ReviewSerializer(movie.reviews.all(), many=True).data

    @staticmethod
    def get_ratings(movie):
        average_rating = movie.ratings.values_list('rating', flat=True).aggregate(Avg('rating')).get('rating__avg')
        return average_rating
