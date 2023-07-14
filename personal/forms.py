from dataclasses import fields
from django import forms
from .models import *

class PersonalForm(forms.ModelForm):
    class Meta:
        model = personal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['area'].empty_label = "Selecciona"
        self.fields['estudio'].empty_label = "Selecciona"
        self.fields['Carrera'].empty_label = "Selecciona"
        self.fields['Carrera'].choices = [('', "Selecciona"), ] + list(self.fields['Carrera'].choices)[1:]
        self.fields['ap'].required = True
        self.fields['am'].required = True
