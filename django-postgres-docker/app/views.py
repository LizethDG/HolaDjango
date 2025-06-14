from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmailUserCreationForm, EmailAuthenticationForm

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect("login")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = EmailAuthenticationForm()
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = EmailUserCreationForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")