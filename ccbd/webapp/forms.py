from django import forms

from .models import InputForm

class DetailsForm(forms.ModelForm):
	class Meta:
		model=InputForm
		exclude=[]
