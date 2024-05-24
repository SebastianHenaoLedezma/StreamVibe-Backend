from django.db.models import Sum, Avg
from rest_framework import serializers
from be_streamvibe.models.movie import Movie


class MovieDualSerializer(serializers.ModelSerializer):
    trailer_image_url = serializers.SerializerMethodField(method_name='get_trailer_image')
    total_rating = serializers.SerializerMethodField(method_name='get_total_rating')
    average_rating = serializers.SerializerMethodField(method_name='get_average_rating')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'trailer_image_url', 'duration', 'total_rating', 'average_rating', 'upcoming_movie']

    @staticmethod
    def get_trailer_image(movie):
        return movie.trailer_thumbnail.url if movie.trailer_thumbnail else None

    @staticmethod
    def get_total_rating(movie):
        total_rating = movie.ratings.aggregate(total=Sum('rating'))['total']
        return total_rating if total_rating is not None else 0

    @staticmethod
    def get_average_rating(movie):
        average_rating = movie.ratings.aggregate(average=Avg('rating'))['average']
        return round(average_rating, 1) if average_rating is not None else 0
    