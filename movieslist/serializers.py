from rest_framework import serializers

from movieslist.models import *


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


'''aaa'''


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'name'


class GenreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


'''bbb'''


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


'''ccc'''


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


'''ddd'''


class MovieShotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = ('id','image')


class MovieShotsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieShots
        fields = '__all__'


'''eee'''


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'text')


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


'''fff'''


class RatingStarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingStar
        fields = '__all__'


class RatingStarDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingStar
        fields = '__all__'


'''jjj'''


class RatingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id' , 'star')


class RatingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
