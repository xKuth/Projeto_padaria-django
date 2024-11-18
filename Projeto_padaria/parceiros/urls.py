from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaP, name='pagina001'),
]