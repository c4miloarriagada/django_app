import requests
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import GameForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser   
from django.views.decorators.csrf import csrf_exempt
from .models import Game
from .serializers import GameSerializer
from .models import UserProfile
from .models import Game
# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        perfil = request.session.get("role")
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "landing_page.html", context)

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
            return render(request, "login.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "login.html")


def shoppingcart(request):
    return render(request, "shopping_cart.html")


@login_required
def admin_panel(request):
    if request.session["role"] != "admin":
        return HttpResponse("No tienes permisos para acceder a esta página")
    return render(request, "admin_panel.html")


def cat_accion(request):
    perfil = request.session.get("role") 
    if request.user.is_authenticated:
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "cat_accion.html", context)


def cat_terror(request):
    perfil = request.session.get("role") 
    if request.user.is_authenticated:
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "cat_terror.html", context)


def dashboard(request):
    juegos = Game.objects.all()
    perfil = request.session.get("role")  
    datos = {'juegos': juegos, 'perfil': perfil}
    if request.user.is_authenticated:
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "dashboard.html", datos)


def checkout(request):
    perfil = request.session.get("role") 
    if request.user.is_authenticated:
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "checkout.html", context)


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
    perfil = request.session.get("role") 
    if request.user.is_authenticated:
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "shopping_cart.html", context)


@login_required
def user_panel(request):
    if request.session["role"] != "cliente":
        return HttpResponse(
            "Solo los clientes puede ver su perfil desde esta pagina, por favor si es administrador dirijase a la pagina de administrador"
        )
    return render(request, "user_panel.html")


def visualizacion(request):
    return render(request, "visualizacion.html")


def info_games(request):
    url_api = 'https://www.freetogame.com/api/games'
    response = requests.get(url_api)
    if response.status_code == 200:
        juegos = response.json()
    else:
        juegos = []

    to_render = {"juegos": juegos}
    return render(request, 'info_juegos.html', to_render)


def wip(request):
    if request.user.is_authenticated:
        perfil = request.session.get("role")
        context = {"perfil": perfil}
    else:  # Si el usuario no está autenticado
        context = {}
    return render(request, "wip.html", context)

@login_required
def form_juegos(request):
    if request.session["role"] != "admin":
        return HttpResponse("No tienes permisos para acceder a esta página") #puse la restriccion, despues lo enlazamos a la pg de admin
    datos = {
        'form': GameForm()
    }
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            datos['mensaje'] = "Juego guardado correctamente"
            return redirect('dashboard')
        else:
            datos['mensaje'] = "Error al guardar el juego"
    return render(request, "form_juegos.html", {'form': GameForm()})

@login_required
def mod_juegos(request, idgame):
    if request.session["role"] != "admin":
        return HttpResponse("No tienes permisos para acceder a esta página")
    juego = Game.objects.get(idGame=idgame)
    datos = {
        'form': GameForm(instance=juego)
    }
    if request.method == "POST":
        form = GameForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            datos['mensaje'] = "Juego modificado correctamente"
            return redirect('dashboard')
        else:
            datos['mensaje'] = "Error al modificar el juego"
    return render(request, "mod_juegos.html", datos)

@login_required
def eliminar_juego(request, idgame):
    if request.session["role"] != "admin":
        return HttpResponse("No tienes permisos para acceder a esta página")
    juego = Game.objects.get(idGame=idgame)
    juego.delete()
    return redirect(to="dashboard")

@csrf_exempt
@api_view(["GET", "POST"])
def game_list(request):
    if request.method == "GET":
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "POST"])
def get_games(request):
    if request.method == "GET":
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
