# barbershop/forms.py

from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['usuario', 'barbero', 'servicio', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'barbero': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
        }
