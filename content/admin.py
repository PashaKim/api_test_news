from django.contrib import admin
from .models import Post, Comment, Upvote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'amount_of_upvotes', 'created')
    # prepopulated_fields = {"link": ("title",)}
    raw_id_fields = ('author',)
    list_filter = ('created', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created')
    raw_id_fields = ('post', 'author',)
    list_filter = ('created',)


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'amount_of_users')
    fields = ('post', 'users', 'amount_of_users')
    readonly_fields = ('amount_of_users', )
    raw_id_fields = ('post',)
    filter_horizontal = ('users',)
