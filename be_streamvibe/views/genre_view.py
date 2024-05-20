from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.genre import Genre

from be_streamvibe.serializers.genre_serializer import GenreSerializer


@api_view(['GET', 'POST'])
def genre(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer_genres = GenreSerializer(genres, many=True)
        return Response(serializer_genres.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_genre(request, pk):
    try:
        genre_info = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response({'message': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

    number_of_movies = request.query_params.get('number_of_movies')

    if number_of_movies:
        number_of_movies = int(number_of_movies)
        serialized_genre = GenreSerializer(genre_info, number_of_movies=number_of_movies)
    else:
        serialized_genre = GenreSerializer(genre_info)

    return Response(serialized_genre.data)
