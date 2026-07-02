from django.shortcuts import render
from .serializers import OrderSerializer
from rest_framework import generics
from .models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError

class CreateOrderView (generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     def perform_create(self, serializer):
          buyer = self.request.user
          target_offer = serializer.validated_data.get('offer')
          if buyer.balance >= target_offer.price:
               buyer.balance -= target_offer.price
               buyer.save()
          elif buyer.balance < target_offer.price:
               raise ValidationError({"error" : "Not enough funds"})
          
          serializer.save(buyer=buyer, price=target_offer.price)