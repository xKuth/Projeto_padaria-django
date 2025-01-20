from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def logonP(request):
    if request == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authentic = authenticate(request, username=username, password=password)
        if authentic is not None:
            login(request, authentic)
        else:
            return redirect('pagina001.html')
    return render(request, 'html/login.html')

def registerP(request):
    return render(request, 'html/register.html')