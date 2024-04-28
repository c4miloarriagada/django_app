from rest_framework import serializers
from duocgame.models import Game, Consola

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['idGame', 'name', 'description', 'price', 'category']

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = ['idConsola', 'name', 'manufacturer', 'releaseDate', 'storage', 'price']




