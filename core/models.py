from django.db import models

# Create your models here.

class Reserva(models.Model):
    rut = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=100)
    prevision = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    email = models.EmailField()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        return "Reserva de RUT " + self.rut + " con fecha " + str(self.fecha)