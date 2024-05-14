from rest_framework import serializers
from be_streamvibe.models.movie import Movie
from be_streamvibe.models.genre import Genre
from be_streamvibe.models.director import Director
from be_streamvibe.models.language import Language
from be_streamvibe.models.actor import Actor
from be_streamvibe.models.music_creator import MusicCreator


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    directors = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), many=True)
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    music_creators = serializers.PrimaryKeyRelatedField(queryset=MusicCreator.objects.all(), many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'duration', 'movie_url', 'trailer_url', 'trailer_thumbnail_url', 'genres', 'directors', 'languages', 'actors', 'music_creators',)
        