from django.shortcuts import render
from rest_framework import generics
from .serializers import OfferSerializer
from .models import Offer
class OfferListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetailView(generics.RetrieveAPIView):
    permission_classes = []
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'uuid'