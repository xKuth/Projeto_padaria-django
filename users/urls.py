from django.urls import path
from django.conf.urls.static import static
from . import views
from Projeto_padaria import settings

urlpatterns = [ 
    path('login', views.logonP, name='logon'),
    path('register', views.registerP, name='register'),
    path('logout', views.LogoutP, name='logout')
]