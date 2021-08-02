from django import forms
from .models import ED

class Increment(forms.ModelForm):
    ED_count = forms.IntegerField(label="", initial=0)
    class Meta:
        model = ED
        fields = ('ED_count',)
        labels = {
        'ED_count': (''),
    }
        # fields = '__all__'

    # increment = forms.IntegerField(min_value=0,max_value=50)

