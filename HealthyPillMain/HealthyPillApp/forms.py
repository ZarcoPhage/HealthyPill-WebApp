from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models.fields import CharField
from django.forms.models import ALL_FIELDS
from django.forms.widgets import HiddenInput
from django.http import request
from HealthyPillApp.models import UserProfile
from django.forms import ModelForm, DateInput
from HealthyPillApp.models import Event
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
  is_specialist = forms.BooleanField(widget=forms.CheckboxInput, required=False)
  phone = forms.CharField(label='número telefónico', required=False, widget=forms.NumberInput)
  class Meta:
    model = UserProfile
    fields = ['username', 'email', 'phone', 'password1', 'password2', 'is_specialist']
    help_texts = {k:'' for k in fields }


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    #user = UserProfile.username
    fields = ['title', 'description','start_time', 'end_time'] #'user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    #self.fields['user'] = User.username