from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from be_streamvibe.models import Movie, Rating, User
from be_streamvibe.models.review import Review
from be_streamvibe.serializers.review_serializer import ReviewSerializer


@api_view(['GET'])
def list_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    review = Review.save_review(request.data.get('review'), request.data.get('user_id'))
    movie.reviews.add(review)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def retrieve_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_review(request, pk, user_id):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Verificar si el usuario que está actualizando la review es el mismo que la creó
    if review.user != user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    serializer = ReviewSerializer(review, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Imprimir errores del serializer
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
