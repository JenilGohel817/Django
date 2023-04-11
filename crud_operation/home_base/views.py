from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        return redirect('signin')

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            name = user.first_name
            messages.success(request, 'profile Login successfully.')
            return render(request, "index.html", {'name': name})
        else:
            return redirect('signin')

    return render(request, "login.html")


def sign_out(request):
    logout(request)
    return redirect('index')
