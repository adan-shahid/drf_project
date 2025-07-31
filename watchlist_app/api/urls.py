from django.urls import path
from watchlist_app.api.views import movieListAV, movieDetailAV


urlpatterns = [
    path('list/', movieListAV.as_view(), name="movie-list"),
    path('<int:pk>/', movieDetailAV.as_view(), name="movie_details"),
]
