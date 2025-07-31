
from watchlist_app.models import movie
from watchlist_app.api.serializers import movieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
    
   


@api_view(['GET','PUT'])
def movie_details(request, pk):
    if request.method == 'GET':
        movies = movie.objects.get(pk=pk)
        serializers = movieSerializer(movies)
        return Response(serializers.data)

    if request.method == 'PUT':
        serializer = movieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
