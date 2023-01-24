from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'auth/index.html')

def register(request):
    return render(request, 'auth/register.html')

def login(request):
    return render(request, 'auth/login.html')

def logout(request):
    pass    