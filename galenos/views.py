from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.middleware import csrf
from django.contrib import messages
from django.contrib.auth import authenticate, login
from galenoslogin.views import indexwithlogin
from django.http import JsonResponse
from .forms import LoginForm

# Create your views here

def index(request):
    return render(request, 'galenos/index.html', {})

def reservarCita(request):
    return render(request, 'galenos/reservarCita.html', {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contraseña']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexwithlogin')  # Redirect to the 'indexwithlogin' page
            else:
                return JsonResponse({'status': 'invalid'})
    else:
        form = LoginForm()
    return render(request, 'galenos/login.html', {'form': form})

