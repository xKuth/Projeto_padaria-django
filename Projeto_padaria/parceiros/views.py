from django.shortcuts import render
# Create your views here.


def PaginaP(request):
    return render(request, 'html/pagina01.html')


def suppliersP(request):
    return render(request, 'html/supplier.html')

def infoP(request):
    return render(request, 'html/info.html')