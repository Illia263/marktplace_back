from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from firebase_admin import auth
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import CustomUserSerializer, CustomUserCreateSerializer, PublicUserSerializer, UpdateUserSerializer, AllPublicUsersSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from core.permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
user = get_user_model()
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
    
    permission_classes = []
    authentication_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = PublicUserSerializer
    lookup_field = 'uuid'

class UserListView(generics.ListAPIView):
  
    permission_classes = [IsAdminOrReadOnly]
  
    queryset = CustomUser.objects.all()
    serializer_class = AllPublicUsersSerializer

class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = 'uuid'

class UserSelfUpdateView(generics.RetrieveUpdateAPIView):
        permission_classes = [IsAuthenticated]

        serializer_class = UpdateUserSerializer

        def get_object(self):
            return self.request.user

class RegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer
    permission_classes = []
    def perform_create(self, serializer):
        user = serializer.save()
        uid = urlsafe_base64_encode(force_bytes(user.uuid))
        token = default_token_generator.make_token(user)
        activation_link = f"http://localhost:3000/activate/{uid}/{token}/"
        html_body = render_to_string('email/activation.html', {'link' : activation_link})
        
        send_mail(subject='activation', message=activation_link, from_email='adminmarket@gmail.com', recipient_list=[user.email], html_message=html_body)


class ResendView(APIView):
    permission_classes = []
    def post(self, request):
        user_email = request.data.get('email')
        
        try:
            user = CustomUser.objects.get(email=user_email)
            if user.is_active is False:
                uid = urlsafe_base64_encode(force_bytes(user.uuid))
                token = default_token_generator.make_token(user)
                activation_link = f"http://localhost:3000/activate/{uid}/{token}/"
                html_body = render_to_string('email/activation.html', {'link' : activation_link})
                
                send_mail(subject='activation', message=activation_link, from_email='adminmarket@gmail.com', recipient_list=[user.email], html_message=html_body)
                return Response({'message' : 'Mail re-sent successfully'})
            else:
                return Response({'error' : 'user is already active'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error' : 'User email is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        
class ActivationAccountView(APIView):
    permission_classes = []
    def post(self, reqest):
        uid = reqest.data.get('uid')
        token = reqest.data.get('token')
        try:
            uuid = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(uuid=uuid)
            user_check = default_token_generator.check_token(user, token)
            if  user_check:
                user.is_active = True
                user.save()
                return Response({'message' : 'Account activated successfully'})
            else: 
                return Response({'message' : 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError, OverflowError, CustomUser.DoesNotExist) as e:
            return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
class ResetPasswordView(APIView): 
    permission_classes = []
    def post(self, request):
        user_email = request.data.get('email')
        try:
            user = CustomUser.objects.get(email=user_email)
            if user.is_active is True:
                uid = urlsafe_base64_encode(force_bytes(user.uuid))
                token = default_token_generator.make_token(user)
                new_password_link = f"http://localhost:3000/new_password/{uid}/{token}/"
                html_body = render_to_string('email/new.html', {'link' : new_password_link})
                
                send_mail(subject='new', message=new_password_link, from_email='adminmarket@gmail.com', recipient_list=[user.email], html_message=html_body)
                return Response({'message' : 'Password reset link sent successfully'})
            else:
                return Response({'error' : 'Account is not active'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error' : 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
class ResetPasswordConfirmationView(APIView):
    permission_classes = []
    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        try:
            uuid = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(uuid=uuid)
            user_check = default_token_generator.check_token(user, token)
            if  user_check:
                user.set_password(new_password)
                user.save()
                return Response({'message' : 'Password was changed successfully'})
            else: 
                return Response({'message' : 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError, OverflowError, CustomUser.DoesNotExist) as e:
            return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
            


        