from rest_framework import serializers
from be_streamvibe.models.movie import Movie
from be_streamvibe.models.genre import Genre
from be_streamvibe.models.rating import Rating
from be_streamvibe.models.language import Language

from be_streamvibe.serializers.director_serializer import DirectorSerializer
from be_streamvibe.serializers.actor_serializer import ActorSerializer
from be_streamvibe.serializers.music_creator_serializer import MusicCreatorSerializer
from be_streamvibe.serializers.review_serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(slug_field='name', queryset=Genre.objects.all(), many=True)
    directors = DirectorSerializer(many=True, read_only=True)
    languages = serializers.SlugRelatedField(slug_field='name', queryset=Language.objects.all(), many=True)
    actors = ActorSerializer(many=True, read_only=True)
    music_creators = MusicCreatorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    ratings = serializers.SlugRelatedField(slug_field='rating', queryset=Rating.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'release_year', 'duration', 'movie_url', 'trailer_url',
            'trailer_thumbnail_url',
            'genres', 'directors', 'languages', 'actors', 'music_creators', 'reviews', 'ratings')
