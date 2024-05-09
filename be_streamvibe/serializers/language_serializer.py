from rest_framework import serializers
from be_streamvibe.models.language import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')




