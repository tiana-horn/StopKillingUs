from django.shortcuts import render, redirect
from django.conf import settings
from core.models import User


def index(request):
    return render(request, 'index.html', {
        'google_map_key': settings.GOOGLE_MAP_KEY,

    })

def privacyPolicy(request):
    return render(request, 'privacy.html')
