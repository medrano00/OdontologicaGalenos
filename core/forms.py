from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Usuario')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Contraseña')

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
        rut = forms.CharField(label='Rut', max_length=100, validators=[val_rut])
        sucursal = forms.ChoiceField(label='Sucursal', choices=[('santiago', 'Santiago'), ('vinadelmar', 'Viña del Mar'), ('puertomontt', 'Puerto Montt')])
        prevision = forms.ChoiceField(label='Prevision', choices=[('fonasa', 'Fonasa'), ('vidatres', 'Vida Tres'), ('particular', 'Particular'), ('colmenagoldencross', 'Colmena Golden Cross'), ('Consalud', 'Consalud'), ('cruzblanca', 'Cruz Blanca'), ('masvida', 'MasVida')])
        especialidad = forms.ChoiceField(label='Especialidad', choices=[('implantologia', 'Implantología'), ('odontologiageneral', 'Odontología General'), ('odontologiageneralinfantil', 'Odontología General Infantil'), ('odontologiageneralformacionortodoncia', 'Odontología General - Formación Ortodoncia'), ('odontopediatriainfantil', 'Odontopediatría - Odontología Infantil'), ('ortodoncia', 'Ortodoncia'), ('ortodonciainvisible', 'Ortodoncia Invisible'), ('rehabilitacionoral', 'Rehabilitación Oral')])
        fecha = forms.DateField(label='Fecha', widget=forms.SelectDateWidget)
        email = forms.EmailField(label='Email')