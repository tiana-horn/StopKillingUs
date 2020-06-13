from django.contrib import admin
from core.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('message','author','created_at')

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('new_comment', 'author',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
