from django import forms
from .models import Threshold


class Fitness_Standard(forms.ModelForm):
    class Meta:
        model = Threshold
        fields = ('Fitness_Standard_per',)
        labels = {
        'Fitness_Standard_per': (''),
        }