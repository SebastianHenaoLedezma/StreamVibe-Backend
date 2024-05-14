from rest_framework import serializers
from be_streamvibe.models.music_creator import MusicCreator

class MusicCreatorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MusicCreator
        fields = ("id", "name", "photo_url")


