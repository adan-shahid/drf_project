# from django.shortcuts import render, HttpResponse
# from .models import movie
# from django.http import JsonResponse

# # Create your views here.

# def movieList(request):
#     movies = movie.objects.all() #COMPLEX QUERYSET RESULT
#     data = {
#         'movies':list(movies.values())
#         }  #CONVERTING a PYTHON DICTIONARY.
#     return JsonResponse(data) #CONVERTING DICT INTO JSON RESPONSE.
# #WE HAVE MULTIPLE OBJECTS IN OUR DATABASE, AND WE WANT TO ACCESS SINGLE OBJECT,
# #FOR THAT WE NEED TO CREATE A SPECIFIC URL.

# def movie_details(request,pk):
#     movie_list = movie.objects.get(pk=pk)
#     data = {
#         'name': movie_list.name,
#         'description':movie_list.description,
#         'active': movie_list.is_active
#     }
#     return JsonResponse(data)
