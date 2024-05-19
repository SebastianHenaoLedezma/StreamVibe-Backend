
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.genre import Genre
from be_streamvibe.models.movie import Movie

from be_streamvibe.serializers.genre_serializer import GenreSerializer
from be_streamvibe.serializers.genre_v2_serializer import TopGenreSerializer
from be_streamvibe.serializers.movie_serializer import MovieSerializer


@api_view(['GET', 'POST'])
def genre(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serialized_genres = [GenreSerializer.process_data(genre) for genre in genres]
        return Response(serialized_genres)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_genre(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response({'message': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

    number_of_movies = request.query_params.get('number_of_movies')

    if number_of_movies:
        number_of_movies = int(number_of_movies)
        serialized_genre = GenreSerializer.process_data(genre, number_of_movies=number_of_movies)
    else:
        serialized_genre = GenreSerializer.process_data(genre)

    return Response(serialized_genre)

@api_view(['GET'])
def all_data_genre(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serialized_genres = [GenreSerializer.process_data(genre) for genre in genres]
        return Response(serialized_genres)


@api_view(['GET', 'PUT', 'DELETE'])
def all_data_genre(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response({'message': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopGenreSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopGenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
