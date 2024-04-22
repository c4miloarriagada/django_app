from rest_framework import serializers
from duocgame.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['idGame', 'name', 'description', 'price', 'category']




