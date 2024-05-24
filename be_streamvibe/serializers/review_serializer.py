from rest_framework import serializers
from be_streamvibe.models.review import Review
from be_streamvibe.models.user import User


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'review', 'name', 'user_name')

    def get_user_name(self, obj):
        user = obj.user
        if user:
            return user.name
        return None

    def all(self):
        user = User.objects.get.all()
        return {
            'reviews': [review.review for review in user],
            'user_name': [review.user_name for review in user],
            'ratings': [review.ratings for review in user],
        }
