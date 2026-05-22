from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserRoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'standart user'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    avatar = models.ImageField(upload_to='avatars/', blank=True, null = True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = models.CharField(
        max_length=10,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.USER
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.username} ({self.get_role_display()}) - Balance: {self.balance}", self.email