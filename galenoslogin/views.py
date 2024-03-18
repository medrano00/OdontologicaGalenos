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

def reserva_del(request, pk):
    context = {}
    try:
        reserva = Reserva.objects.get(id=pk)  # Assuming 'id' is the primary key field of the Reserva model

        reserva.delete()
        mensaje = "Bien, datos eliminados..."
        reservas = Reserva.objects.all()  # Retrieve the remaining reservations
        context = {'reservas': reservas, 'mensaje': mensaje}  # Update the context with the remaining reservations
        return render(request, 'galenoslogin/admin.html', context)
    except Reserva.DoesNotExist:
        mensaje = "Error, reserva no existe..."
        reservas = Reserva.objects.all()  # Retrieve all reservations
        context = {'reservas': reservas, 'mensaje': mensaje}  # Update the context with all reservations
        return render(request, 'galenoslogin/admin.html', context)

def reservaRealizada(request):
    return render(request, 'galenoslogin/reservaRealizada.html', {})

def admin(request):
    reservas = Reserva.objects.all()
    return render(request, 'galenoslogin/admin.html', {'reservas': reservas})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservarCitaForm(request.POST)
        if form.is_valid():
            reserva.rut = form.cleaned_data['rut']
            reserva.sucursal = form.cleaned_data['sucursal']
            reserva.prevision = form.cleaned_data['prevision']
            reserva.especialidad = form.cleaned_data['especialidad']
            reserva.fecha = form.cleaned_data['fecha']
            reserva.save()
            return redirect('reservaRealizada')
    else:
        form = ReservarCitaForm(initial={
            'rut': reserva.rut,
            'sucursal': reserva.sucursal,
            'prevision': reserva.prevision,
            'especialidad': reserva.especialidad,
            'fecha': reserva.fecha
        })
    return render(request, 'galenoslogin/editar_reserva.html', {'form': form})