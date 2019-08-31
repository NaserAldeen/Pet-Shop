from django import forms
from .models import *

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['available']
