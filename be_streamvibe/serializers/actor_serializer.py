from rest_framework import serializers
from be_streamvibe.models.actor import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("photo_url",)
