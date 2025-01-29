from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import LoginForms, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def logonP(request):
    form = LoginForms()
    if request == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authentic = authenticate(request, username=username, password=password)
        if authentic is not None:
            login(request, authentic)
        else:
            return redirect('pagina001.html')
    context = {'formu': form}
    return render(request, 'html/login.html', context)

def registerP(request):
    form = RegisterForm()
    if request == 'POST':
        form = RegisterForm(request.POST)
        if form is not None:
            if form.is_valid():
                user_form = form.cleaned_data('form_user')
                password_form = form.cleaned_data('form_pasword')
                password_form2 = form.cleaned_data('form_password2')
                if password_form == password_form2:
                    form.save()
                    new_user = authenticate(request, username='user_form', password='password_form')
                    login(request, new_user)
            

    context = {'form': form}
    return render(request, 'html/register.html', context)
