import pymongo
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['EMS']
ems_collection = db['Ems_1']



def home(request):
    return render(request, 'auth/index.html')

def register(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passd = request.POST['pass']
        cpass = request.POST['cpass']
        des = request.POST['des']

        myuser = User.objects.create_user(fname, lname, email)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Success')
        return redirect('signin')



def login(request):
    return render(request, 'auth/login.html')

def logout(request):
    pass    