from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, FilesN
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, File_1


# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            messages.info(request, 'Your login request has been sent to Admin for approval')
            return redirect('register')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
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
            elif user is not None and user.is_sales:
                login(request, user)
                return redirect('sales')
            elif user is not None and user.is_production:
                login(request, user)
                return redirect('production')
            elif user is not None and user.is_devloper:
                login(request, user)
                return redirect('devloper')
            elif user is not None and user.is_client:
                login(request, user)
                return redirect('client')
            else:
                msg= 'invalid credentials'
        else:
            messages.info(request, 'Your  request yet not approved')

        messages.info(request, 'Invalid credentials OR your request may be not approved')
    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required
def admin(request):
    form = (request.POST or None)
    if request.method == 'POST':
        form = FilesN(request.POST, request.FILES)
        print("sahi he")
        if form.is_valid():
            form.save()
            messages.info(request, 'File uploaded')
            return redirect('adminpage')
        else:
            messages.info(request, 'Failed')
            print(form.errors)
    else:
        # print("galat he")
        form = FilesN()
        # messages.info(request, 'invalid form')
    return render(request,'admin.html', {'form': form})

@login_required
def sales(request):
    return render(request,'sales.html')

@login_required
def production(request):
    return render(request,'production.html')

@login_required
def devloper(request):
    ab = File_1.objects.values_list('title', 'file')
    print(ab)
    context = {'ab': ab[0]}

    # filepath = ab.file
    # filename = ab.title
    form = FilesN(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    # context = {'filepath': filepath,
    #            'form': form,
    #            'filename': filename
    #            }
    return render(request, 'devloper.html', context)

@login_required
def client(request):
    return render(request,'client.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'index.html')
    # Redirect to a success page.
