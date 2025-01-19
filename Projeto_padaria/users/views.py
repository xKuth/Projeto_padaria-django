from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import user

# Create your views here.

def logonP(request):
    if request.User
    
    username = request.POST['username']
    password = request.POST['password']
    authentic = authenticate(request, username=username, password=password)

    if authentic is not None:
        login(request, authentic)
    return render(request, 'html/login.html')

def registerP(request):
    return render(request, 'html/register.html')