from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput) # widget is used to encrypt the password

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class UserForm1(UserCreationForm):
    class Meta:
        model=User
        fields=['username']
