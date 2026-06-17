from rest_framework import serializers
from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('uuid', 'title', 'description', 'price', 'stock', 'is_active', 'is_auto_delivery', 'created_at', 'custom_field', 'seller', 'game',  'category', 'secret_data')
        extra_kwargs = {'secret_data' : {'write_only' : True}}
