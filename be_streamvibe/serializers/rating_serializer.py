from rest_framework import serializers
from be_streamvibe.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'rating',)
