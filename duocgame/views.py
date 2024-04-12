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
    return render(request, "shopping_cart.html")


def admin_panel(request):
    return render(request, "admin_panel.html")


def cat_accion(request):
    return render(request, "cat_accion.html")


def cat_terror(request):
    return render(request, "cat_terror.html")


def dashboard(request):
    return render(request, "dashboard.html")


def checkout(request):
    return render(request, "checkout.html")


def login(request):
    return render(request, "login.html")


def profile_modification(request):
    return render(request, "profile_modification.html")


def restore_pass(request):
    return render(request, "restore_pass.html")


def shopping_cart(request):
    return render(request, "shopping_cart.html")


def signup(request):
    return render(request, "singup.html")


def user_panel(request):
    return render(request, "user_panel.html")


def visualizacion(request):
    return render(request, "visualizacion.html")
