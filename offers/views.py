from django.shortcuts import render
from rest_framework import generics
from .serializers import OfferSerializer
from .models import Offer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class OfferListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'category', 'is_active']
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class OfferDetailView(generics.RetrieveAPIView):
    permission_classes = []
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'uuid'

class GameByNameAndCategoryView(generics.ListAPIView):
   
    serializer_class = OfferSerializer
    permission_classes = []

    def get_queryset(self):
        game_slug = self.kwargs['game_slug']
        category_slug = self.kwargs['category_slug']
        return Offer.objects.filter(
            game__slug=game_slug,
            category__slug=category_slug,
            is_active=True  
        )

class GameByNameView(generics.ListAPIView):
    permission_classes = []
    serializer_class = OfferSerializer
    def get_queryset(self):
        game_slug = self.kwargs['game_slug']
        return Offer.objects.filter(
            game__slug=game_slug,
            is_active=True
        )


