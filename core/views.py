from django.shortcuts import render, redirect
from core.models import User


def index(request):
    return render(request, 'index.html', {
        #'user':'user,
    })
