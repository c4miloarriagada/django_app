from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token 
from django.shortcuts import render
  


@csrf_exempt
@api_view(['POST'])
def custom_login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario no encontrado')
    
    pass_valido = check_password(password, user.password)   
    if not pass_valido:
        return Response('Contraseña incorrecta')
    
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)
