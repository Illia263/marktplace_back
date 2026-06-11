from django.urls import path
from  .views import AllCategoryView, AllGamesView
urlpatterns = [
    path('', AllGamesView.as_view(), name='games'),
    path('categories/', AllCategoryView.as_view(), name='categories')

]

# api/games/ - games
# api/games/categories/ - categories