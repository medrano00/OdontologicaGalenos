from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.middleware import csrf
from django.contrib import messages
from django.contrib.auth import authenticate, login
from galenoslogin.views import indexwithlogin
# Create your views here

def index(request):
    return render(request, 'galenos/index.html', {})

def reservarCita(request):
    return render(request, 'galenos/reservarCita.html', {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(indexwithlogin)
        else:
            messages.error(request, 'Usuario o contraseña inválido')
    return render(request, 'login.html')
