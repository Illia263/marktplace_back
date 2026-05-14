from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    readonly_fields = ('uuid',)
    fieldsets = UserAdmin.fieldsets + (
        ('Martketplace additional info', {'fields' : ('uuid', 'role', 'balance', 'avatar')}),
    )
    list_display = ['id','username', 'email', 'role', 'balance', 'uuid','is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
admin.site.register(CustomUser, CustomUserAdmin)

