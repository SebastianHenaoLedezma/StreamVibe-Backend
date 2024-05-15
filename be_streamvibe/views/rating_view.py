from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.rating import Rating
from be_streamvibe.serializers.rating_serializer import RatingSerializer


@api_view(['GET', 'POST'])
def list_create_rating(request):
    if request.method == 'GET':
        Ratings = Rating.objects.all()
        serializer = RatingSerializer(Ratings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_rating(request, pk):
    try:
        Rating = Rating.objects.get(pk=pk)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RatingSerializer(Rating)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RatingSerializer(Rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
