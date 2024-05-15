from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.faq import Faq
from be_streamvibe.serializers.faq_serializer import FaqSerializer


@api_view(['GET', 'POST'])
def list_create_faq(request):
    if request.method == 'GET':
        Faqs = Faq.objects.all()
        serializer = FaqSerializer(Faqs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_faq(request, pk):
    try:
        Faq = Faq.objects.get(pk=pk)
    except Faq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FaqSerializer(Faq)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FaqSerializer(Faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
