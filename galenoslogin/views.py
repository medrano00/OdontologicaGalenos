from django.shortcuts import render, redirect
from .forms import ReservarCitaForm
from .models import Reserva

# Create your views here.

def indexwithlogin(request):
    return render(request, 'galenoslogin/indexwithlogin.html', {})

def reservarCita(request):
    if request.method == 'POST':
        form = ReservarCitaForm(request.POST)
        if form.is_valid():
            reserva = Reserva(
                rut = form.cleaned_data['rut'],
                sucursal = form.cleaned_data['sucursal'],
                prevision = form.cleaned_data['prevision'],
                especialidad = form.cleaned_data['especialidad'],
                fecha = form.cleaned_data['fecha']
            )
            reserva.save()
            return redirect('reservaRealizada')
    else:
        form = ReservarCitaForm()
    return render(request, 'galenoslogin/reservarCita.html', {'form': form})

def reservaRealizada(request):
    return render(request, 'galenoslogin/reservaRealizada.html', {})

def admin(request):
    reservas = Reserva.objects.all()
    return render(request, 'galenoslogin/admin.html', {'reservas': reservas})