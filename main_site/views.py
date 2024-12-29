import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login")
def home(requests):
    return render(requests, 'base.html')

def register_view(requests):
    if requests.method == 'POST':
        username = requests.POST.get('username')
        email = requests.POST.get('email')
        password = requests.POST.get('password')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(requests, "User Created.")



    return render(requests, 'register.html')

def login_view(requests):
    if requests.method == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("password")

        user = authenticate(requests, username=username, password=password)
        if user is not None:
            login(requests, user)
            return redirect("/")

        else:
            messages.error(requests, "User Not Found")
    else:

        return render(requests, 'login.html')

@login_required(login_url="/login")
def logout_view(requests):
    logout(requests)
    return redirect('/login')
