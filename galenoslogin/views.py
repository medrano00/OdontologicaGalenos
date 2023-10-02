from django.shortcuts import render, redirect
from .forms import ReservarCitaForm


# Create your views here.

def indexwithlogin(request):
    return render(request, 'galenoslogin/indexwithlogin.html', {})

def reservarCita(request):
    if request.method == 'POST':
        form = ReservarCitaForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            sucursal = form.cleaned_data['sucursal']
            prevision = form.cleaned_data['prevision']
            especialidad = form.cleaned_data['especialidad']
            fecha = form.cleaned_data['fecha']
            return redirect('reservaRealizada')
    else:
        form = ReservarCitaForm()
    return render(request, 'galenoslogin/reservarCita.html', {'form': form})

def reservaRealizada(request):
    return render(request, 'galenoslogin/reservaRealizada.html', {})