from django.urls import path
from watchlist_app.api.views import watchListAV, movieDetailAV, streamPlatformAV, streamPlatformDetailsAV


urlpatterns = [
    path('list/', watchListAV.as_view(), name="movie-list"),
    path('list/<int:pk>/', movieDetailAV.as_view(), name="movie_details"),

    path('streamPlatform/', streamPlatformAV.as_view(), name="stream-platform"),
    path('streamPlatform/<int:pk>/', streamPlatformDetailsAV.as_view(), name="platform-details"),
]
