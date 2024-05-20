from rest_framework import serializers
from be_streamvibe.models.review import Review
from be_streamvibe.models.user import User


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'review', 'user_name')

    def get_user_name(self, obj):
        user_id = obj.user_id
        user = User.objects.get(id=user_id)
        return user.name

    def all(self):
        user = User.objects.get.all()
        return {
            'reviews': [review.review for review in user],
            'user_name': [review.user_name for review in user],
            'ratings': [review.ratings for review in user],
        }
