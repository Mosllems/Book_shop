from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "age", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "phone_number", "address")}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', "age", "phone_number", "address"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
