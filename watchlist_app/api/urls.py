from django.urls import path
from watchlist_app.api.views import (watchListAV, movieDetailAV,
                                    streamPlatformAV, streamPlatformDetailsAV,
                                    reviewList, reviewDetails,
                                    reviewCreate)


urlpatterns = [
    path('list/', watchListAV.as_view(), name="movie-list"),
    path('list/<int:pk>/', movieDetailAV.as_view(), name="movie_details"),

    path('stream/', streamPlatformAV.as_view(), name="stream-platform"),
    path('stream/<int:pk>/', streamPlatformDetailsAV.as_view(), name="platform-details"),

    # path('review/', reviewList.as_view(), name="review"),
    # path('review/<int:pk>/', reviewDetails.as_view(), name="review-details"),

    path('stream/<int:pk>/review-create/', reviewCreate.as_view(), name="review-create"),
    #ALL THE REVIEWS FOR A PARTICULAR MOVIE.
    path('stream/<int:pk>/review/', reviewList.as_view(), name="reviews"),
    #DETAILS OF INDIVIDUAL REVIEWS.
    path('stream/review/<int:pk>/', reviewDetails.as_view(), name='review-details'),

    
]
