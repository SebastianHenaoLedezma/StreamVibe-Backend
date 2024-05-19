from rest_framework import serializers
from be_streamvibe.models.director import Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name', 'photo_url')
