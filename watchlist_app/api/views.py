
from watchlist_app.models import movie
from watchlist_app.api.serializers import movieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movieList(request):
    movies = movie.objects.all()
    serializers = movieSerializer(movies, many=True)
    return Response(serializers.data)


def movie_details(request, pk):
    pass