from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario')
    contraseña = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
