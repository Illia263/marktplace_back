from rest_framework import serializers
from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('uuid', 'title', 'description', 'price', 'stock', 'is_active', 'is_auto_delivery', 'created_at', 'custom_field', 'seller', 'game',  'category', 'secret_data')
        extra_kwargs = {'secret_data' : {'write_only' : True}}
        read_only_fields = ('seller',)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.seller:
            representation['seller'] = {
                'id': instance.seller.id,
                'username' : instance.seller.username,
                'avatar' : instance.seller.avatar.url if instance.seller.avatar else None

            }
        if instance.game:
            representation['game'] = {
                'id' : instance.game.id,
                'title' : instance.game.title,
                'slug' : instance.game.slug
            }
        if instance.category:
            representation['category'] = {
                'id' : instance.category.id,
                'title' : instance.category.title,
                'slug' : instance.category.slug
            }
        return representation