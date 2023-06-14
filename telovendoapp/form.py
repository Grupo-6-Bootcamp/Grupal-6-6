from django import forms
from .models import Proveedores
from django.contrib.auth.forms import AuthenticationForm


class FormularioLogin(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, label='Nombre de Usuario', error_messages={
                               'required': 'El usuario es obligatorio'})
    password = forms.CharField(max_length=16, required=True, label='Contraseña',
                               widget=forms.PasswordInput, error_messages={'required': 'La contraseña es obligatoria'})


class FormularioProveedores(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = ('nombre', 'rut', 'direccion', 'telefono', 'email')
        labels = {
            'nombre': 'Nombre',
            'rut': 'Rut',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Email'
        }
