from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.director import Director
from be_streamvibe.serializers.director_serializer import DirectorSerializer


@api_view(['GET', 'POST'])
def list_create_director(request):
    if request.method == 'GET':
        Directors = Director.objects.all()
        serializer = DirectorSerializer(Directors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_director(request, pk):
    try:
        Director = Director.objects.get(pk=pk)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DirectorSerializer(Director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(Director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
