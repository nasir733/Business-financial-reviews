from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your modelfs here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']
    fieldsets = (
        (
            (('User'), {
                'fields': ('username', 'password', 'email', 'user_type', 'profile_pic',)
            }),

            (('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }),
        ))


admin.site.register(CustomUser, CustomUserAdmin)
