
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta(serializers.ModelSerializer):

        model = User
        
        fields = ('id', 'uuid', 'username', 'email', 'role', 'balance', 'avatar', 'description', 'date_joined')
class AllPublicUsersSerializer(serializers.ModelSerializer):
    class Meta(serializers.ModelSerializer):

        model = User
        
        fields = ('uuid', 'username', 'avatar', 'description', 'date_joined')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uuid', 'username', 'email', 'password', 'role', 'date_joined')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'description', 'avatar', 'date_joined')

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'description', 'avatar', 'balance', 'date_joined', 'email')
    