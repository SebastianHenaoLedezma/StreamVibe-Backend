from rest_framework import serializers
from be_streamvibe.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField(method_name='get_movies')

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

    @staticmethod
    def get_movies(genre, top=False, number_of_movies=None):
        movies = genre.movie_set.order_by('-ratings__rating') if top else genre.movie_set.all()
        movies = movies[:number_of_movies] if number_of_movies else movies
        movie_urls = [movie.trailer_thumbnail.url for movie in movies]
        return movie_urls
