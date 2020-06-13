from django.forms import ModelForm
from core.models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('message',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('new_comment',)
