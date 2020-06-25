from django.contrib.auth.models import User
from rest_framework import serializers
from content.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'link', 'author', 'amount_of_upvotes', 'created')


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created')
