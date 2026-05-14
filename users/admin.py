from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Martketplace additional info', {'fields' : ('role', 'balance', 'avatar')}),
    )
    list_display = ['username', 'email', 'role', 'balance', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
admin.site.register(CustomUser, CustomUserAdmin)

