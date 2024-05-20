from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.movie import Movie
from be_streamvibe.serializers.movie_serializer import MovieSerializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def all_data_movie(request, pk):
    try:
        movies = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = [MovieSerializer.process_data(movie) for movie in movies]
        return Response(serializer)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
