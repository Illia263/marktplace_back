
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta(serializers.ModelSerializer):

        model = User
        
        fields = ('id', 'uuid', 'username', 'email', 'role', 'balance', 'avatar', 'description', 'dateOfregistration')
class AllPublicUsersSerializer(serializers.ModelSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta(serializers.ModelSerializer):

        model = User
        
        fields = ('uuid', 'username', 'avatar', 'description', 'dateOfregistration')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'uuid', 'username', 'email', 'password', 'role', 'dateOfregistration')
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
        fields = ('uuid', 'username', 'description', 'avatar')

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'description', 'avatar')
    