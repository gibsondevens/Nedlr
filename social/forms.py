from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Image

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email",)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ("religion", "bio",)

class UploadImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ("profile", "pic",)
		widgets = {
			'profile': forms.HiddenInput()
		}