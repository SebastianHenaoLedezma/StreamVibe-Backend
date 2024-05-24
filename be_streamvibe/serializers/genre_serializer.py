from rest_framework import serializers
from be_streamvibe.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies',)

    def get_movies(self, genre):
        number_of_movies = self.context.get('number_of_movies', None)
        top = self.context.get('top', False)

        if top:
            movies = genre.movie_set.order_by('-ratings__rating')
        else:
            movies = genre.movie_set.all()

        if number_of_movies:
            movies = movies[:number_of_movies]

        movie_data = [
            {
                'id': movie.id,
                'trailer_thumbnail': movie.trailer_thumbnail.url,
                'title': movie.title,
                'duration': movie.duration,
            }
            for movie in movies
        ]
        return movie_data

