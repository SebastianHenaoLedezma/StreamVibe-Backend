from rest_framework import serializers
from be_streamvibe.models.movie import Movie
from be_streamvibe.models.genre import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'duration', 'movie_url', 'trailer_url', 'trailer_thumbnail_url', 'genres')