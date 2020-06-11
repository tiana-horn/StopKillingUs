from django.shortcuts import render, redirect
from django.conf import settings
from core.models import User, Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'google_map_key': settings.GOOGLE_MAP_KEY,
        'posts': posts,
    })

def privacyPolicy(request):
    return render(request, 'privacy.html')
