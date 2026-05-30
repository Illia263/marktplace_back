from django.urls import path, include
from  .views import GoogleLoginView, UserDetailView, UserListView, UserUpdateView, RegistrationView,ResendView,ResetPasswordView, ResetPasswordConfirmationView,UserSelfUpdateView, ActivationAccountView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('google/', GoogleLoginView.as_view(), name='google-login'),
    path('profiles/<uuid:uuid>/', UserDetailView.as_view(), name='user-details' ),
    path('profiles/<uuid:uuid>/edit/', UserUpdateView.as_view(), name='admin-edit'),
    path('profiles/', UserListView.as_view(), name='user-list'),
    path('registration/',RegistrationView.as_view(), name='user-registration' ),
    path('login/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('login/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('activation/resend/', ResendView.as_view(), name='resend-confirmation'),
    path('password_reset/request/', ResetPasswordView.as_view(), name='password-reset'),
    path('password_reset/confirmation/', ResetPasswordConfirmationView.as_view(), name='password-reset-confirmation'),
    path('my_profile/', UserSelfUpdateView.as_view(), name='my_profile-edit'),
    path('activation/', ActivationAccountView.as_view(), name='email-activation')
]
# регистрация - http:localhost:8000/api/auth/users/ (post) (username, email, password, re_password) - /api/auth/registration/

# активация - /api/auth/users/activation/ (uid,token) (post) - /api/auth/activation/

# скинуть еще раз эмэйл с подтверждением юзера - /api/auth/users/resend_activation/  (email) (post) -  /api/auth/activation/resend/

# логин - http:localhost:8000/api/auth/jwt/create/ (post) - /api/auth/login/

# рефреш токен - http:localhost:8000/api/auth/jwt/refresh/ - /api/auth/login/refresh

# запрос на восстанавление  пароля - /api/auth/users/reset_password/  (email) (post) - /api/auth/password_reset/request/

# подтверждения нового пароля - /api/auth/users/reset_password_confirm/ (email) (post) - /api/auth/password_reset/confirmation/

# мой профиль - http:localhost:8000/api/auth/users/me/ (get) (put/patch) - /api/auth/my_profile/ 

# для смені профиля админом - api/auth/profiles/<uuid:uuid>/edit/

# все юзері - /api/auth/profiles/ (get)

# конкретні юзер - /api/auth/profiles/{uuid} (get)