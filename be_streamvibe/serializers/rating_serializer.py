from rest_framework import serializers
from be_streamvibe.models.rating import Rating
# from .user_serializer import UserSerializer
# from .movie_serializer import MovieSerializer

class RatingSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # movie = MovieSerializer()

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'review', 'movie', 'user')
        