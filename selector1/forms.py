from django import forms
from django.http import request
from .models import City

ATTRIBUTES = {}

class BaseForm(forms.ModelForm):
    name        = forms.CharField    ( widget=forms.TextInput     ( attrs=ATTRIBUTES), label=("Nombre"))

    class Meta:
        model   = City
        widgets = {\
                    }
