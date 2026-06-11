from django.urls import path
from .views import OfferListCreateView, OfferDetailView

urlpatterns = [
    path('', OfferListCreateView.as_view(), name='offers-list'),
    path('<uuid:uuid>/', OfferDetailView.as_view(), name='offer')
]