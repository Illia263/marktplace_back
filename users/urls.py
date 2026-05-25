from django.urls import path, include
from  .views import GoogleLoginView, UserDetailView, UserListView


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('google/', GoogleLoginView.as_view(), name='google-login'),
    path('<uuid:uuid>/', UserDetailView.as_view(), name='user-deatils' ),
    path('all_profiles/', UserListView.as_view(), name='user-list'),
]
