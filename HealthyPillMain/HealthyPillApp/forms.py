from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from HealthyPillApp.models import UserProfile


class UserRegisterForm(UserCreationForm):

	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)


	class Meta:
		model = UserProfile
		fields = ['username', 'email', 'password1', 'password2',]
		help_texts = {k:'' for k in fields }
