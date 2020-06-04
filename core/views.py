from django.shortcuts import render, redirect
from core.models import User


def index(request):
    return render(request, 'index.html', {
        #'user':'user,
    })

def privacyPolicy(request):
    return render(request, 'privacy.html')
