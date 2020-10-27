# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Personal info'), {'fields': ('full_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff'),
        }),
    )
    list_display = ('full_name', 'email',)
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email', 'full_name', )
    ordering = ('full_name', 'email')
