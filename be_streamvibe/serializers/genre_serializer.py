from rest_framework import serializers
from be_streamvibe.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    movies = serializers.ListField(read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

    @staticmethod
    def process_data(genre, top=False, number_of_movies=None):
        movies = genre.movie_set.order_by('-ratings__rating') if top else genre.movie_set.all()
        movies = movies[:number_of_movies] if number_of_movies else movies
        movies_data = [movie.trailer_thumbnail_url.url for movie in movies]

        return {
            'id': genre.id,
            'name': genre.name,
            'movies': movies_data
        }
