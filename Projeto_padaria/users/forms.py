from django.contrib.auth.forms import UserCreationForm
from django import forms as formualro_login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms



class LoginForms(forms.Form):
    user_form = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Digite o nome de úsuario:'}))
    password_form = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Digite a senha de úsuario:'}))
    
class RegisterForm(UserCreationForm):

    username = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Digite o nome de úsuario:'}))
    password1 = forms.CharField(min_length=8, max_length=64, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Digite uma senha valida:'}))
    password2 = forms.CharField(min_length=8, max_length=64, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Repita sua senha:'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

