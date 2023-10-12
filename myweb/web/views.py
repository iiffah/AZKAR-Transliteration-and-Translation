from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    return render (request, "index.html")

def translate(request):
    return render (request, "translate.html")

def navbar(request):
    return render (request, "navbar.html")

def login(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == "POST":

            # Attempt to sign user in
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                # login(request, user)
                return redirect('index')
            else:
                messages.error(request,"ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render (request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        # email = request.POST["email"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
      
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = fname
            user.last_name = lname   
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        # login(request, user)
        return redirect('login')
    else:
        return render(request, "register.html")
    
def Contact(request):
    if request.method=='POST':
        first_name=request.POST['name']
        email=request.POST['email']
        Telephone_Number=request.POST['phone']
        message=request.POST['message']
        contact=Contacts.objects.create(first_name=first_name,email=email,Telephone=Telephone_Number,message=message)
        messages.success(request, 'Your message successful')
    return render(request,'contact.html') 

def About(request):
    return render(request,'about.html')

def mnread(request):
    return render (request, "mnread.html")

def mntranslate(request):
    return render (request, "mntranslate.html")

def enread(request):
    return render (request, "enread.html")

def entranslate(request):
    return render (request, "entranslate.html")

