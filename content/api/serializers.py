from django.contrib.auth.models import User
from rest_framework import serializers
from content.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name')


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_name', 'title', 'link', 'author', 'amount_of_upvotes', 'created')


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_name', 'content', 'created')
