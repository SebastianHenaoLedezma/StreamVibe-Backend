from rest_framework import serializers
from be_streamvibe.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
