from django import forms
from .models import Reports

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ('cn','name','remarks')