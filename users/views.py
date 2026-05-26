from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from firebase_admin import auth
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CustomUserSerializer, CustomUserCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class GoogleLoginView(APIView):
    permission_classes = []

    def post(self, request):
        id_token = request.data.get('id_token')
        if not id_token:
            return Response({'error': 'id_token is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token.get('uid')
            email = decoded_token.get('email')
            base_name = email.split('@') [0]
            short_uid = uid[:5]
            generated_username = f"{base_name}_{short_uid}"
            user, created = CustomUser.objects.get_or_create(email=email, defaults={"username" : generated_username})
            if created:

                user.set_unusable_password()
                user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(refresh),
                'access': str(refresh.access_token),
                })
        except Exception as e:
            print(e)
            return Response({'error': 'Invalid token or Firebase error'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveAPIView):
    #TODO: fix security
    permission_classes = []
    authentication_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'uuid'

class UserListView(generics.ListAPIView):
    #TODO: fix security
    permission_classes = []
    authentication_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
