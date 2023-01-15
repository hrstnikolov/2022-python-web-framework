from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from auth_demo.auth_app.forms import SignUpForm
from auth_demo.auth_app.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ['email', 'date_joined']
    list_filter = ['is_staff', 'is_superuser']
    ordering = ['email']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'age', 'user']
