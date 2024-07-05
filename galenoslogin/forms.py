from django import forms

def val_rut(value):
        run = str(value)
        #verifica largo del rut
        if not (9 <= len(run) <= 10):
                raise forms.ValidationError("El RUT debe tener entre 9 y 10 caracteres")
        
        #verifica si hay guion
        if run[-2] != '-':
                raise forms.ValidationError("El antepenúltimo carácter debe ser un guion ('-')")
        
        #verifica si el ultimo character es valido
        if not (run[-1].isdigit() or run[-1].lower() == 'k'):
                raise forms.ValidationError("El último carácter debe ser un dígito o 'k' (insensible a mayúsculas)")

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
