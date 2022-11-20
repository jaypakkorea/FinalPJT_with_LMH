from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Rating

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username',)


class ProfileSerializer(serializers.ModelSerializer):

    
    class FollowFollowingSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id','username', 'profile_pic')

    class RatingSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = User
                fields = '__all__'

        class Meta:
            model = Rating
            exclude = ('user',)

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'overview', 'poster_path', 'release_date', 'like_users',)

    # like_articles = ArticleSerializer(many=True)
    followers = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)
    ratings = RatingSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    ratings_count = serializers.IntegerField(source='ratings.count', read_only=True)

    class Meta:
        model = User
        fields = '__all__'



class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')