# Formulario de registro y autenticación estándar para el inicio de sesión.
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Pedido

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado. Por favor, use uno diferente.')
        return email

class PedidoForm(forms.ModelForm):
    numero_tarjeta = forms.CharField(
        max_length=16, 
        min_length=16, 
        label="Número de Tarjeta",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    codigo_cvv = forms.CharField(
        max_length=3, 
        min_length=3, 
        label="Código CVV",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'telefono', 'direccion_entrega', 'numero_tarjeta', 'codigo_cvv']
        labels = {
            'nombre_cliente': 'Nombre del Cliente',
            'telefono': 'Número de Teléfono',
            'direccion_entrega': 'Dirección de Entrega',
        }
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_entrega': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # Método de validación para el campo 'telefono'
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        # Verifica que el teléfono tenga exactamente 12 caracteres
        if len(telefono) != 12:
            raise forms.ValidationError("El número de teléfono debe tener 12 caracteres.")
        
        # Verifica que el primer carácter sea un '+'
        if not telefono.startswith('+'):
            raise forms.ValidationError("El número de teléfono debe comenzar con '+'.")
        
        # Verifica que los demás caracteres sean solo números
        if not re.match(r'^\+\d{11}$', telefono):
            raise forms.ValidationError("El número de teléfono debe contener solo números después de '+'.")
        
        return telefono