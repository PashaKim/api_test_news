from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import CommentSerializer, PostSerializer, UserSerializer
from content.models import Comment, Post


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
