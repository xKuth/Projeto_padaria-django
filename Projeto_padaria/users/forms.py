from django import forms 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForms(forms.Form):
    user_form = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Digite o nome de úsuario:'}))
    password_form = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Digite a senha de úsuario:'}))
    
class RegisterForm(forms.Form):

    form_user = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Usuario: ')
    form_password = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Senha: ')
    form_password2 = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Repita a senha: ')
