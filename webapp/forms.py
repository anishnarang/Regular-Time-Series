from django import forms

from .models import *

class DetailsForm(forms.ModelForm):
	class Meta:
		model=InputForm
		exclude=[]

class MahaForm(forms.ModelForm):
	class Meta:
        	model=InputMaha
        	exclude=[]

