from rest_framework import serializers
from be_streamvibe.models.support_request import Support_request
# from .user_serializer import UserSerializer

class SupportRequestSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Support_request
        fields = ('id', 'name', 'email', 'phone', 'message', 'user')
        