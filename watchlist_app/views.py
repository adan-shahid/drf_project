from django.shortcuts import render, HttpResponse
from .models import movie
from django.http import JsonResponse

# Create your views here.

def movieList(request):
    movies = movie.objects.all() #COMPLEX QUERYSET RESULT
    data = {
        'movies':list(movies.values())
        }  #CONVERTING a PYTHON DICTIONARY.
    return JsonResponse(data) #CONVERTING DICT INTO JSON RESPONSE.
