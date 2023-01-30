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
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_admin:
                    login(request, user)
                    return redirect('adminpage')
                elif user.is_sales:
                    login(request, user)
                    return redirect('sales')
                elif user.is_production:
                    login(request, user)
                    return redirect('production')
                elif user.is_devloper:
                    login(request, user)
                    return redirect('devloper')
                elif user.is_client:
                    login(request, user)
                    return redirect('client')
                else:
                    messages.info(request, 'Your  request yet not approved')
            else:
                messages.info(request, 'Invalid credentials!')
        else:
            messages.info(request, 'Invalid Username!')

    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required
def admin(request):
    u1 = request.user
    u2 = request.user.roles
    model = User
    if model.objects.filter(username=u1) & model.objects.filter(is_admin=1):
        form = (request.POST or None)
        if request.method == 'POST':
            form = FilesN(request.POST, request.FILES)
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
        return render(request, 'admin.html', {'form': form})
    else:
        return render(request, 'login_error.html')


@login_required
def sales(request):
    return render(request, 'sales.html')


@login_required
def production(request):
    model = User
    u1 = request.user
    if model.objects.filter(username=u1) & model.objects.filter(is_production=1):
        fileall = File_1.objects.filter(is_production_file=1)
        context = {'fileall': fileall}
        return render(request, 'production.html', context)
    else:
        return render(request, 'login_error.html')


@login_required
def devloper(request):
    model = User
    u1 = request.user
    if model.objects.filter(username=u1) & model.objects.filter(is_devloper=1):
        fileall = File_1.objects.filter(is_devloper_file=1)
        context = {'fileall': fileall}
        return render(request, 'devloper.html', context)
    else:
        return render(request, 'login_error.html')


@login_required
def client(request):
    return render(request, 'client.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'index.html')
    # Redirect to a success page.

@login_required
def upload_file(request):
    u1 = request.user
    u2 = request.user.roles
    model = User
    form = (request.POST or None)
    if request.method == 'POST':
        form = FilesN(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'File uploaded')
        else:
            messages.info(request, 'Failed')
            print(form.errors)
    else:
        # print("galat he")
        form = FilesN()
        # messages.info(request, 'invalid form')
    return render(request, 'upload_file.html', {'form': form, 'u2': u2})