from django.db.models import Sum
from rest_framework import serializers
from be_streamvibe.models.movie import Movie


class MovieRatingsSerializer(serializers.ModelSerializer):
    trailer_image_url = serializers.SerializerMethodField(method_name='get_trailer_image')
    total_rating = serializers.SerializerMethodField(method_name='get_total_rating')

    class Meta:
        model = Movie
        fields = ['title', 'trailer_image_url', 'duration',
                  'total_rating']  # Asegúrate de que estos campos existen en el modelo Movie

    @staticmethod
    def get_trailer_image(movie):
        return movie.trailer_thumbnail.url if movie.trailer_thumbnail else None

    @staticmethod
    def get_total_rating(movie):
        total_rating = movie.ratings.aggregate(total=Sum('rating'))['total']
        return total_rating if total_rating is not None else 0
