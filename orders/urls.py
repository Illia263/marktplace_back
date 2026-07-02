from .views import CreateOrderView
from django.urls import path
urlpatterns = [
    path('', CreateOrderView.as_view(), name="order")
]
