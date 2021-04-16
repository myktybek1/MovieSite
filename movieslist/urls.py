from django.contrib import admin
from django.urls import path
from movieslist.views import *

urlpatterns = [
    path('actor/create/', ActorCreateView.as_view()),
    path('actorall/', ActorListView.as_view()),
    path('actor/detail/<int:pk>/', ActorDetailView.as_view()),

    path('genre/create/', GenreCreateView.as_view()),
    path('genreall/', GenreListView.as_view()),
    path('genre/detail/<int:pk>', GenreDetailView.as_view()),

    path('category/create/', CategoryCreateView.as_view()),
    path('categoryall/', CategoryListView.as_view()),
    path('category/detail/<int:pk>', CategoryDetailView.as_view()),

    path('movie/create/', MovieCreateView.as_view()),
    path('movieall/', MovieListView.as_view()),
    path('movie/detail/<int:pk>', MovieDetailView.as_view()),

    path('movieshots/create/', MovieShotsCreateView.as_view()),
    path('movieshotsall/', MovieShotsListView.as_view()),
    path('movieshots/detail/<int:pk>', MovieShotsDetailView.as_view()),

    path('review/create/', ReviewCreateView.as_view()),
    path('reviewall/', ReviewListView.as_view()),

    # path('review/detail/<int:pk>', ReviewDetailView.as_view()),

    path('ratingstar/create/', RatingStarCreateView.as_view()),
    # path('ratingstarall/', RatingStarListView.as_view()),
    path('ratingstar/detail/<int:pk>', RatingStarDetailView.as_view()),

    path('rating/create/', RatingCreateView.as_view()),
    # path('ratingall/', RatingListView.as_view()),
    path('rating/detail/<int:pk>', RatingDetailView.as_view()),

]