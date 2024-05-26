import random
from datetime import date

from django.utils import timezone

from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from be_streamvibe.models import User, Rating
from be_streamvibe.models.movie import Movie
from be_streamvibe.serializers.movie_serializer import MovieSerializer
from be_streamvibe.serializers.movie_dual_serializer import MovieDualSerializer


@api_view(['GET', 'POST'])
def all_movie(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_info_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serialized_movie = MovieSerializer(movie)
    return Response(serialized_movie.data)


@api_view(['GET'])
def random_movie(request):
    movie_count = Movie.objects.count()
    if movie_count == 0:
        return Response({'message': 'No movies found'}, status=status.HTTP_404_NOT_FOUND)
    random_index = random.randint(0, movie_count - 1)
    movie = Movie.objects.all()[random_index]
    serialized_movie = MovieSerializer(movie)
    return Response(serialized_movie.data)


@api_view(['GET'])
def must_watch_movies(request):
    top_movies = Movie.objects.annotate(total_rating=Sum('ratings__rating')).order_by('-total_rating')[:4]

    if not top_movies:
        return Response({'message': 'No movies found'}, status=status.HTTP_404_NOT_FOUND)

    serialized_movies = MovieDualSerializer(top_movies, many=True)
    return Response(serialized_movies.data)


@api_view(['GET'])
def new_release_movies(request):
    today = date.today()
    new_movies = Movie.objects.filter(release_date__gt=today, release_date__isnull=False)
    serializer = MovieDualSerializer(new_movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serialized_movie = MovieSerializer(movie)
    return Response(serialized_movie.data)


@api_view(['PUT'])
def update_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def update_rating_movie(request, pk, user_id):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    rating = request.data.get('rating')
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    rating = Rating.create_or_update_movie(movie, rating, user)
    movie.ratings.add(rating)
    return Response(status=status.HTTP_200_OK)
