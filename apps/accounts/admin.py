from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]

    fieldsets = (
        (
            "Profile",
            {"fields": ("username", "password")},
        ),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            "Additonal Info",
            {"fields": ("birthday", "photo")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
