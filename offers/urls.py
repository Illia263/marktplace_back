from django.urls import path
from .views import OfferListCreateView, OfferDetailView, GameByNameAndCategoryView, GameByNameView
urlpatterns = [
    path('', OfferListCreateView.as_view(), name='offers-list'),
    path('<uuid:uuid>/', OfferDetailView.as_view(), name='offer'),
    path('<slug:game_slug>/<slug:category_slug>/', GameByNameAndCategoryView.as_view(), name='offers-by-game-category'),
    path('<slug:game_slug>/', GameByNameView.as_view(), name='game-by-name'),
]