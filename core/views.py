from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.conf import settings
from core.models import User, Post
from core.forms import PostForm, CommentForm
from django.contrib.auth.views import login_required
from django.http import Http404
from django.contrib.auth import authenticate, login




def index(request):
    posts = Post.objects.all()
    form_class = PostForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
    return render(request, 'index.html', {
        'google_map_key': settings.GOOGLE_MAP_KEY,
        'posts': posts,
    })

@login_required
def create_post(request):
    form_class = PostForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commmit=False)
            post.author = request.User
            post.save()
            return redirect('post_detail', pk=post_id)
    else: 
        form = form_class()
    return render(request, 'posts/create_post.html',{
          "form": form,
     })

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.User
            comment.post = post 
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()

    return render(request,'posts/post_detail.html', {
        'post': post,
        'form': CommentForm(),
        'comments': post.comments.all(),
    })

def edit_post(request, post_id):
     post = Post.objects.get(pk=post_id)
     if post.author != request.user:
          raise Http404

     form_class = PostForm

     if request.method == 'POST':
          form = form_class(data=request.POST, instance=post)
          if form.is_valid():
               form.save()
               return redirect("post_detail", pk=post_id)
     else:
          form = form_class(instance=post)
          return render(request, 'posts/edit_post.html', {
               "post": post,
               "form": form,
          })



def privacyPolicy(request):
    return render(request, 'privacy.html')
