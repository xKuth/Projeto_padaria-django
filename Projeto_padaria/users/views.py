from django.shortcuts import render

# Create your views here.
def logonP(request):
    return render(request, 'html/login.html')