from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    model = Order
    fields = ('id', 'buyer', 'offer', 'price', 'status', 'created_at')
    read_only_fields = ('buyer', 'price', 'status')