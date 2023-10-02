from django import forms

class ReservarCitaForm(forms.Form):
        rut = forms.CharField(label='Rut', max_length=100)
        sucursal = forms.ChoiceField(label='Sucursal', choices=[('santiago', 'Santiago'), ('vinadelmar', 'Viña del Mar'), ('puertomontt', 'Puerto Montt')])
        prevision = forms.ChoiceField(label='Prevision', choices=[('fonasa', 'Fonasa'), ('vidatres', 'Vida Tres'), ('particular', 'Particular'), ('colmenagoldencross', 'Colmena Golden Cross'), ('Consalud', 'Consalud'), ('cruzblanca', 'Cruz Blanca'), ('masvida', 'MasVida')])
        especialidad = forms.ChoiceField(label='Especialidad', choices=[('implantologia', 'Implantología'), ('odontologiageneral', 'Odontología General'), ('odontologiageneralinfantil', 'Odontología General Infantil'), ('odontologiageneralformacionortodoncia', 'Odontología General - Formación Ortodoncia'), ('odontopediatriainfantil', 'Odontopediatría - Odontología Infantil'), ('ortodoncia', 'Ortodoncia'), ('ortodonciainvisible', 'Ortodoncia Invisible'), ('rehabilitacionoral', 'Rehabilitación Oral')])
        fecha = forms.DateField(label='Fecha', widget=forms.SelectDateWidget)