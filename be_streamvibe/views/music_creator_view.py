from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.music_creator import MusicCreator
from be_streamvibe.serializers.music_creator_serializer import MusicCreatorSerializer


@api_view(['GET', 'POST'])
def list_create_musicCreator(request):
    if request.method == 'GET':
        MusicCreators = MusicCreator.objects.all()
        serializer = MusicCreatorSerializer(MusicCreators, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_musicCreator(request, pk):
    try:
        MusicCreator = MusicCreator.objects.get(pk=pk)
    except MusicCreator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MusicCreatorSerializer(MusicCreator)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicCreatorSerializer(MusicCreator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        MusicCreator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
