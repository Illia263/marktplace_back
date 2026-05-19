from django.urls import path, include
from  .views import GoogleLoginView
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('google/', GoogleLoginView.as_view(), name='google-login'),
]
