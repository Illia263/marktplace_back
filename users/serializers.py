from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        
        fields = ('id', 'uuid', 'username', 'email', 'role', 'balance', 'avatar', 'description')

class CustomUserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('id', 'uuid', 'username', 'email', 'password', 'role')