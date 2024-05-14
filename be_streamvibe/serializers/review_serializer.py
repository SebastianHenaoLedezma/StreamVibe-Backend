from rest_framework import serializers
from be_streamvibe.models.review import Review
# from .user_serializer import UserSerializer
# from .movie_serializer import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ('id', 'review', 'movie', 'user')
        