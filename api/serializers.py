
from rest_framework import serializers
from django.contrib.auth import get_user_model
from contents.models import (
    Post,
    Comment,
    Like,
    Share,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    tags = LikeSerializer(read_only=True, many=True)
    class Meta:
        model = Comment
        fields = ["comment", "post_commented_link", "tags"]


class ShareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Share
        fields = ["post_shared_link", "user"]


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    count_likes = serializers.IntegerField()
    count_loves = serializers.IntegerField()
    count_sads = serializers.IntegerField()
    count_comments = serializers.IntegerField()
    count_shares = serializers.IntegerField()
    
    class Meta:        
        model = Post
        fields = ["id", "title", "post_content", "post_type", "link", "username", "first_name", "last_name", "count_likes", "count_loves", "count_sads", "count_shares", "count_comments"]
        # fields = ["id", "title", "post_content", "post_type", "link", "username", "first_name", "last_name", "tags", "count_likes", "count_loves", "count_sads", "count_shares", "count_comments"]


class PostByLinkSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    comments = CommentSerializer(read_only=True, many=True)
    shares = ShareSerializer(read_only=True, many=True)
    tags = LikeSerializer(read_only=True, many=True)
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    count_likes = serializers.IntegerField()
    count_loves = serializers.IntegerField()
    count_sads = serializers.IntegerField()
    
    class Meta:        
        model = Post
        fields = ["id", "title", "post_content", "post_type", "link", "username", "first_name", "last_name", "tags", "shares", "comments", "count_likes", "count_loves", "count_sads"]