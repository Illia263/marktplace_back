from django.db import models
from games.models import Game, Category
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
class Offer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)

    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    is_auto_delivery = models.BooleanField(default=False)
    secret_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_field = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.seller.username}"