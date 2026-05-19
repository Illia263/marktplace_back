from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from firebase_admin import auth
from .models import CustomUser

class GoogleLoginView(APIView):
    permission_classes = []

    def post(self, request):
        id_token = request.data.get('id_token')
        if not id_token:
            return Response({'error': 'id_token is requried'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            decoded_token = auth.verify_id_token(id_token)
            email = decoded_token.get('email')
            user, created = CustomUser.objects.get_or_create(email=email)
            if created:
                user.username = email.split('@')[0]
                user.set_unusable_password()
                user.save()
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh' : str(refresh),
                    'access': str(refresh.access_token),
                })
        except Exception as e:
            return Response({'errror': 'Invalid token or Firebase error'}, status=status.HTTP_400_BAD_REQUEST)
