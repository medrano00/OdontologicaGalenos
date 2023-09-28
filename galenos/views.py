from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.middleware import csrf

# Create your views here

def index(request):
    return render(request, 'galenos/index.html', {})

def reservarCita(request):
    return render(request, 'galenos/reservarCita.html', {})

class Login(LoginView):
    template_name = 'registration/login.html'