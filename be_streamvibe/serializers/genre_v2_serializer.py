from rest_framework import serializers
from be_streamvibe.models.genre import Genre
from be_streamvibe.serializers.movie_serializer import MovieSerializer


class TopGenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')
