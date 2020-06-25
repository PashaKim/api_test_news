from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def amount_of_upvotes(self):
        return len(self.upvotes.users.all())

    class Meta:
        ordering = ('upvotes', 'created')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}, {self.author}'

    class Meta:
        ordering = ('created', )


class Upvote(models.Model):
    post = models.OneToOneField(Post, related_name="upvotes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='upvotes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}, {self.amount_of_users}'

    @property
    def amount_of_users(self):
        return len(self.users.all())

    class Meta:
        ordering = ('created', )
