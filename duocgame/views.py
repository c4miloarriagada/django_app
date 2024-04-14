from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import UserProfile

# Create your views here.


def landing_page(request):
    return render(request, "landing_page.html")


def signup(request):
    if request.method == "POST":
        User = get_user_model()
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        address = request.POST.get("address")
        phone = request.POST.get("telefono")
        birthday = request.POST.get("fecha_nacimiento")
        role = "cliente"

        # Crear el usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
        )

        # Crear el perfil de usuario
        UserProfile.objects.create(
            user=user,
            address=address,
            phone=phone,
            birthday=birthday,
            role=role,
        )
        return redirect("/login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session["role"] = profile.role
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "login.html", {"error": "Invalid login"})
    return render(request, "login.html")


def shoppingcart(request):
    return render(request, "shopping_cart.html")


@login_required
def admin_panel(request):
    if request.session["role"] != "admin":
        return HttpResponse("No tienes permisos para acceder a esta página")
    return render(request, "admin_panel.html")


def cat_accion(request):
    return render(request, "cat_accion.html")


def cat_terror(request):
    return render(request, "cat_terror.html")


def dashboard(request):
    return render(request, "dashboard.html")


def checkout(request):
    return render(request, "checkout.html")


@login_required
def profile_modification(request):
    if request.session["role"] != "cliente":
        return HttpResponse(
            "Solo los clientes puede editar su perfil desde esta pagina, por favor si es administrador dirijase a la pagina de administrador"
        )
    return render(request, "profile_modification.html")


@login_required
def restore_pass(request):
    return render(request, "restore_pass.html")


def shopping_cart(request):
    return render(request, "shopping_cart.html")


@login_required
def user_panel(request):
    if request.session["role"] != "cliente":
        return HttpResponse(
            "Solo los clientes puede ver su perfil desde esta pagina, por favor si es administrador dirijase a la pagina de administrador"
        )
    return render(request, "user_panel.html")


def visualizacion(request):
    return render(request, "visualizacion.html")
