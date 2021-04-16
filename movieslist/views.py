from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieslist.serializers import *
from movieslist.models import *

# @api_view(['GET'])
# def actorviewurl(request):
#     view_urls = {
#         ''
#     }


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorDetailSerializer
    queryset = Actor.objects.all()


class ActorListView(generics.ListAPIView):
    serializer_class = ActorListSerializer
    queryset = Actor.objects.all()


class ActorCreateView(generics.CreateAPIView):
    serializer_class = ActorDetailSerializer


'''aaa'''


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreDetailSerializer
    queryset = Genre.objects.all()


class GenreListView(generics.ListAPIView):
    serializer_class = GenreListSerializer
    queryset = Genre.objects.all()


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreDetailSerializer


'''bbb'''


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


'''ccc'''


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()


class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all()


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailSerializer


'''ddd'''


class MovieShotsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieShotsDetailSerializer
    queryset = MovieShots.objects.all()


class MovieShotsListView(generics.ListAPIView):
    serializer_class = MovieShotsListSerializer
    queryset = MovieShots.objects.all()


class MovieShotsCreateView(generics.CreateAPIView):
    serializer_class = MovieShotsDetailSerializer


'''eee'''


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewDetailSerializer


'''fff'''


class RatingStarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingStarDetailSerializer
    queryset = RatingStar.objects.all()


class RatingStarListView(generics.ListAPIView):
    serializer_class = RatingStarListSerializer
    queryset = RatingStar.objects.all()


class RatingStarCreateView(generics.CreateAPIView):
    serializer_class = RatingStarDetailSerializer


'''jjj'''


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()


class RatingListView(generics.ListAPIView):
    serializer_class = RatingListSerializer
    queryset = Rating.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingDetailSerializer
