from django import forms as formulario
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms


class LoginForms(formulario.Form):

    form_user = formulario.CharField(min_length=5, max_length=20, 
                                     widget=formulario.TextInput(attrs={'class': 'form-control'}))
    form_password = formulario.CharField(min_length=8, max_length=64, 
                                         widget=(formulario.PasswordInput(attrs={'class': 'form-control'})))