from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):

	email = forms.EmailField()

	# def clean(self):
	# 	username = self.cleaned_data.get('username')
	# 	if User.objects.filter(username=username).exists():
	# 		raise ValidationError("Username already exists")
	# 	email = self.cleaned_data.get('email')
	# 	if User.objects.filter(email=email).exists():
	# 		raise ValidationError("Email already exists")
	# 	return self.cleaned_data

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
