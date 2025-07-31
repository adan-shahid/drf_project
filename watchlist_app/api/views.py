from watchlist_app.models import movie
from watchlist_app.api.serializers import movieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST', 'PUT'])
def movieList(request):
    if request.method == 'GET':
        movies = movie.objects.all()
        serializer = movieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = movieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
  
@api_view(['GET','PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movies = movie.objects.get(pk=pk)
        except movie.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = movieSerializer(movies)
        return Response(serializers.data)
        
    if request.method == 'PUT':
        movies = movie.objects.get(pk=pk)
        serializer = movieSerializer(movies, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        movies = movie.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
