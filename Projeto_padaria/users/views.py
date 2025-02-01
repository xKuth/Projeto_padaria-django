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
        form = LoginForms(request.POST)
        if form.is_valid:
            username = request.Post.get('user_form')
            password = request.Post.get('password_form')
            authentic = authenticate(request, username='user_form', password='password_form')
        if authentic is not None:
            login(request, authentic)
        else:
            return redirect('register')
    context = {'formu': form}
    return render(request, 'html/login.html', context)


def registerP(request):
    if request.method == 'POST':
        form_req = RegisterForm(request.POST)
        if form_req is not None:
            print('passou aki', form_req)
            if form_req.is_valid():
                user_form = request.POST.get('username')
                password_form = request.POST.get('password1')
                password_form2 = request.POST.get('password2')
                print('pegou todos elementos')
                print(user_form, password_form, password_form2)
                if password_form == password_form2:
                    print('senha igual')
                    user_save = form.save(commit=False)
                    new_user = authenticate(request, username=user_form, password=password_form)
                    login(request, user_save)
                    if new_user:
                        redirect('pagina001')
            else:
                print('formulario nao e valido')
                redirect('/')
            
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'html/register.html', context)
