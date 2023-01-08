from django.shortcuts import render
from rest_framework import viewsets 
from .models import User, Game, Word
from .serializers import UserSerializer, GameSerializer, WordSerializer, CreateWordSerializer, CreateGameSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
    def perform_create(self, serializer):
        serializer.save()
    

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    #test = Word.objects.distinct('player')
    #def get_queryset(self):
        #return self.queryset.filter(id=1)

class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save()

class CreateWordViewSet(viewsets.ModelViewSet):
    serializer_class = CreateWordSerializer
    queryset = Word.objects.all()

class CreateGameViewSet(viewsets.ModelViewSet):
    serializer_class = CreateGameSerializer
    queryset = Game.objects.all()

        