from django.urls import path
from django.conf.urls.static import static
from . import views
from Projeto_padaria import settings

urlpatterns = [
    path('', views.PaginaP, name='pagina001'),
] 