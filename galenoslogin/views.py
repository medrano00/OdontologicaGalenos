from django.shortcuts import render

# Create your views here.

def indexwithlogin(request):
    return render(request, 'galenoslogin/indexwithlogin.html', {})

def reservarCita(request):
    return render(request, 'galenoslogin/reservarCita.html', {})