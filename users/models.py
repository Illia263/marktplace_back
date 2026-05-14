from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserRoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'standart user'

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null = True)
    role = models.CharField(
        max_length=10,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.USER
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()}) - Balance: {self.balance}"