from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.actor import Actor
from be_streamvibe.serializers.actor_serializer import ActorSerializer


@api_view(['GET', 'POST'])
def list_create_actor(request):
    if request.method == 'GET':
        Actors = Actor.objects.all()
        serializer = ActorSerializer(Actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_actor(request, pk):
    try:
        Actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ActorSerializer(Actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorSerializer(Actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
