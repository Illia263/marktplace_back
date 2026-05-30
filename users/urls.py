from django.urls import path, include
from  .views import GoogleLoginView, UserDetailView, UserListView, UserUpdateView, RegistrationView,ResendView,ResetPasswordView, ResetPasswordConfirmationView,UserSelfUpdateView, ActivationAccountView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('google/', GoogleLoginView.as_view(), name='google-login'),
    path('<uuid:uuid>/', UserDetailView.as_view(), name='user-details' ),
    path('<uuid:uuid>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('all_profiles/', UserListView.as_view(), name='user-list'),
    path('registration/',RegistrationView.as_view(), name='user-registration' ),
    path('login/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('login/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('activation/resend/', ResendView.as_view(), name='resend-confirmation'),
    path('password_reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('new_password/confirmation/', ResetPasswordConfirmationView.as_view(), name='password-reset-confirmation'),
    path('edit/me/', UserSelfUpdateView.as_view(), name='my_profile-edit'),
    path('activation/', ActivationAccountView.as_view(), name='email-activation')
]
