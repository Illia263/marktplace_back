from django.urls import path
from  .views import AllCategoryView, AllGamesView, GameSpecificView
urlpatterns = [
    path('', AllGamesView.as_view(), name='games'),
    path('categories/', AllCategoryView.as_view(), name='categories'),
    path('<slug>/', GameSpecificView.as_view(), name='game')
]

# api/games/ - games
# api/games/categories/ - categories