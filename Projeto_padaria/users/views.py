from django.shortcuts import render

# Create your views here.
def logonP(request):
    return render(request, 'html/login.html')

def registerP(request):
    return render(request, 'html/register.html')