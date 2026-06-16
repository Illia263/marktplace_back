from django.shortcuts import render
from .serializers import GameSerializer, CategorySerializer
from rest_framework import generics
from .models import Game, Category

class AllGamesView(generics.ListAPIView):
    permission_classes = []
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class AllCategoryView(generics.ListAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GameSpecificView(generics.RetrieveAPIView):
    permission_classes = []
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'slug'