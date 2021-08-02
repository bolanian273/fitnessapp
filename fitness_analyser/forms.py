from django import forms


CHART_CHOICES = (
	('', '-------------'),
	('#1', 'Bar Chart'),
	('#2', 'Line Chart'),

	)


class FitnessGraphForm(forms.Form):
	date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="")
	date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="")
	chart_type = forms.ChoiceField(choices=CHART_CHOICES, label = "")