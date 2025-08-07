from watchlist_app.models import watchList, streamPlatform, Review
from watchlist_app.api.serializers import (watchListSerializer,
                                            streamPlatformSerializer,
                                            reviewSerializer)
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins
from rest_framework.views import APIView

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from watchlist_app.api.permissions import AdminOrReadonly, ReviewUserOrReadonly



class watchListAV(APIView):
#INSTEAD OF USING THE IF CONDITION, I'VE DEFINED 'GET' METHOD.
    def get(self, request):
        watchlist = watchList.objects.all()
        serializer = watchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = watchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class movieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movies = watchList.objects.get(pk=pk)
        except watchList.DoesNotExist:
            return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = watchListSerializer(movies)
        return Response(serializers.data)
    
    def put(self, request, pk):
        movies = watchList.objects.get(pk=pk)
        serializer = watchListSerializer(movies, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movies = watchList.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#WRITING THE VIEWS FOR STREAMPLATFORM SERIALIZER
class streamPlatformAV(APIView):
    def get(self, request):
        platform = streamPlatform.objects.all()
        serializer = streamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = streamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class streamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            platform = streamPlatform.objects.get(pk=pk)
        except streamPlatform.DoesNotExist:
            return Response({'Error':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = streamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = streamPlatform.objects.get(pk=pk)
        serializer = streamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = streamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# #NOW I AM WRITING THE VIEW FOR 'reviewSerializer'
# class reviewList(mixins.ListModelMixin,
#                        mixins.CreateModelMixin,
#                        generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = reviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class reviewDetails(mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = reviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# NOW WE ARE USING GENERIC CLASS-BASED VIEWS.
class reviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = reviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class reviewCreate(generics.CreateAPIView):
   
    serializer_class = reviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer): #WE USE THIS 'perform_create' to overwrite this create method.
        pk = self.kwargs.get('pk') #ACCESSING THE PRIMARY KEY.
        movie = watchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user )
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
            
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2

        movie.number_rating = movie.number_rating + 1
        movie.save()

        serializer.save(watchlist=movie, review_user=review_user)

class reviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = reviewSerializer
    permission_classes = [ReviewUserOrReadonly]









# @api_view(['GET', 'POST', 'PUT'])
# def movieList(request):
#     if request.method == 'GET':
#         movies = movie.objects.all()
#         serializer = movieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = movieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
  
# @api_view(['GET','PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movies = movie.objects.get(pk=pk)
#         except movie.DoesNotExist:
#             return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializers = movieSerializer(movies)
#         return Response(serializers.data)
        
#     if request.method == 'PUT':
#         movies = movie.objects.get(pk=pk)
#         serializer = movieSerializer(movies, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movies = movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
