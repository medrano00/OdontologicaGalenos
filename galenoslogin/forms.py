from django import forms
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = (-s) % 11
    return str(dv) if dv < 10 else 'K'

def clean_rut_format(rut):
    """
    This function cleans the RUT format by removing dots and hyphens.
    """
    rut = rut.replace('.', '').replace('-', '').upper()
    if len(rut) < 2:
        raise ValueError("RUT demasiado corto.")
    return rut[:-1], rut[-1]

class ReservarCitaForm(forms.Form):
    rut = forms.CharField(label='Rut', max_length=12)  # Asegúrate de que el max_length sea adecuado.
    sucursal = forms.ChoiceField(label='Sucursal', choices=[
        ('santiago', 'Santiago'),
        ('vinadelmar', 'Viña del Mar'),
        ('puertomontt', 'Puerto Montt')
    ])
    prevision = forms.ChoiceField(label='Previsión', choices=[
        ('fonasa', 'Fonasa'),
        ('vidatres', 'Vida Tres'),
        ('particular', 'Particular'),
        ('colmenagoldencross', 'Colmena Golden Cross'),
        ('consalud', 'Consalud'),
        ('cruzblanca', 'Cruz Blanca'),
        ('masvida', 'MasVida')
    ])
    especialidad = forms.ChoiceField(label='Especialidad', choices=[
        ('implantologia', 'Implantología'),
        ('odontologiageneral', 'Odontología General'),
        ('odontologiageneralinfantil', 'Odontología General Infantil'),
        ('odontologiageneralformacionortodoncia', 'Odontología General - Formación Ortodoncia'),
        ('odontopediatriainfantil', 'Odontopediatría - Odontología Infantil'),
        ('ortodoncia', 'Ortodoncia'),
        ('ortodonciainvisible', 'Ortodoncia Invisible'),
        ('rehabilitacionoral', 'Rehabilitación Oral')
    ])
    fecha = forms.DateField(label='Fecha', widget=forms.SelectDateWidget)
    email = forms.EmailField(label='Email')

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        try:
            body, dv = clean_rut_format(rut)
            if digito_verificador(body) != dv:
                raise forms.ValidationError("El RUT ingresado no es válido.")
        except ValueError as e:
            raise forms.ValidationError(str(e))
        except:
            raise forms.ValidationError("El formato del RUT es incorrecto.")
        return rut
