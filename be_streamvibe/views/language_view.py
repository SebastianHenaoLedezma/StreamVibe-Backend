from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.language import Language
from be_streamvibe.serializers.language_serializer import LanguageSerializer


@api_view(['GET', 'POST'])
def list_create_language(request):
    if request.method == 'GET':
        genres = Language.objects.all()
        serializer = LanguageSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_language(request, pk):
    try:
        genre = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LanguageSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LanguageSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
