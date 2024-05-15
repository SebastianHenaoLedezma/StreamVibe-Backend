from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from be_streamvibe.models.support_request import Support_request
from be_streamvibe.serializers.supportRequest_serializer import SupportRequestSerializer


@api_view(['GET', 'POST'])
def list_create_support_request(request):
    if request.method == 'GET':
        support_requests = Support_request.objects.all()
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupportRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete_support_request(request, pk):
    try:
        support_request = Support_request.objects.get(pk=pk)
    except Support_request.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SupportRequestSerializer(support_request)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupportRequestSerializer(support_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        support_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
