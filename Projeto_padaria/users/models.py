from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class RegistrationForm(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    
