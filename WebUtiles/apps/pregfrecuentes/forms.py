from django import forms
from .models import *

class PregForm(forms.ModelForm):
     class Meta:
          model = Frecuentes
          fields = ['titulo','contenido']