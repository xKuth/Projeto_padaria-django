from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import LoginForms, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def logonP(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(data=request.POST)
        if form.is_valid():
            nome = request.POST.get('user_form')
            senha = request.POST.get('password_form')
            user = authenticate(username=nome, password=senha)
            if user:
                login(request, user)
                return redirect('pagina001')
            else:
                return redirect('register')
    context = {'formu': form}
    return render(request, 'html/login.html', context)


def registerP(request):
    if request.method == 'POST':
        form_req = RegisterForm(data=request.POST)
        if form_req is not None:
            if form_req.is_valid():
                user_form = request.POST.get('username')
                password_form = request.POST.get('password1')
                password_form2 = request.POST.get('password2')
                print(user_form, password_form, password_form2)
                if password_form == password_form2:
                    new_user = authenticate(username=user_form, password=password_form)
                    login(request, new_user)
                    form_req.save()
                    if new_user:
                        redirect('pagina001')
            else:
                redirect('/')
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'html/register.html', context)


def LogoutP(request):
    logout(request)
    return redirect('/')

