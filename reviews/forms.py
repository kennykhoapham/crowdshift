from django import forms
from django.forms import ModelForm
 
class SearchForm(forms.Form):
    search = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'size':'80'}))


class WriteReviewForm(forms.Form):
	title = forms.CharField(label="Title", max_length=60, widget=forms.TextInput(attrs={'size':'40'}))
	body = forms.CharField(widget=forms.Textarea)


class CreateVehicleForm(forms.Form):
	year = forms.CharField(label="", max_length=4, widget=forms.NumberInput(attrs={'size':'5'}))
	make = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'size':'10'}))
	model = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'size':'10'}))
