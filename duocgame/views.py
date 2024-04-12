from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.



def landing_page(request):
    return render(request, "landing_page.html")

def singup(request):
    return render(request, "singup.html")

def login(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        contraseña = request.POST.get("contraseña")
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            return render(request, "landing_page.html")
        else:
            return render(request, "login.html")       
    return render(request, "login.html")

def shoppingcart(request):
    return render(request, "shoppingcart.html")