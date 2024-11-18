from django.shortcuts import render
# Create your views here.


def PaginaP(request):
    return render(request, 'html/pagina01.html')