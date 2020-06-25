from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    link = models.SlugField(max_length=250, unique=True)
    upvotes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('upvotes', 'created')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def __str__(self):
        return f'{self.post}, {self.author}'

    class Meta:
        ordering = ('created', )
