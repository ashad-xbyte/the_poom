from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm


def home(request):
    return render(request, 'auth/index.html')

def register(request):
    msg = None
    if request.method == "POST":
        # username = request.POST['username']
        # fullname = request.POST['fname']
        # email = request.POST['email']
        # passd = request.POST['passd']
        # cpass = request.POST['cpass']
        #
        # myuser = User.objects.create_user(username, email, passd)
        # myuser.full_name = fullname
        #
        # myuser.save()
        #
        # messages.success(request, 'Success')
        # return redirect('user_login')
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('user_login')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'auth/register.html', {'form': form, 'msg':msg})


def user_login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     passd = request.POST['passd']
    #     user = authenticate(username=username, password=passd)
    #     if user is not None:
    #         login(request, user)
    #         fullname = user.first_name
    #         return render(request, 'auth/index.html', {'fullname':fullname})
    #     else:
    #         messages.error(request, "Wrong credentials")
    #         return redirect('home')
    #
    # return render(request, 'auth/user_login.html')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request,'admin.html')

def sales(request):
    return render(request,'sales.html')

def production(request):
    return render(request,'production.html')

def devloper(request):
    return render(request,'devloper.html')

def client(request):
    return render(request,'client.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out done")
    return redirect('home')