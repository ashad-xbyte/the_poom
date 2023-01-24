from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'auth/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passd = request.POST['passd']
        cpass = request.POST['cpass']
        des = request.POST['des']

        myuser = User.objects.create_user(username, email, passd)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Success')
        return redirect('user_login')

    return render(request, 'auth/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        passd = request.POST['passd']
        user = authenticate(username=username, password=passd)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'auth/index.html', {'fname':fname})
        else:
            messages.error(request, "Wrong credentials")
            return redirect('home')

    return render(request, 'auth/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out done")
    return redirect('home')