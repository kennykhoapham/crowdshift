from django import forms
from django.forms import ModelForm
from reviews.models import ProfilePhoto, ReviewPhoto
 
class SearchForm(forms.Form):
    search = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'size':'80'}))


class WriteReviewForm(forms.Form):
	title = forms.CharField(label="Title", max_length=60, widget=forms.TextInput(attrs={'size':'40'}))
	body = forms.CharField(widget=forms.Textarea)
	#photo = forms.FileField(required=False)


class AddVehicleForm(forms.Form):
	year = forms.CharField(label="Year", max_length=4, widget=forms.TextInput(attrs={'size':'50'}))
	make = forms.CharField(label="Make", max_length=20, widget=forms.TextInput(attrs={'size':'50'}))
	model = forms.CharField(label="Model", max_length=20, widget=forms.TextInput(attrs={'size':'50'}))


class AddProfilePhotoForm(forms.Form):
	photo = forms.FileField()
	# class Meta:
	# 	model = ProfilePhoto
	# 	exclude = ()