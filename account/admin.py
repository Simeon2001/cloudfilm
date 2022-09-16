from django.contrib import admin

from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "is_seller"]
    list_filter = ["is_active", "created_at", "is_seller"]
    list_editable = ["is_active"]
    search_fields = ["email", "name"]
    fieldsets = (
        (
            "Basic Details",
            {"fields": ("email", "name")},
        ),
        (
            "Groups & Permissions",
            {"classes": ("collapse",), "fields": ("groups", "user_permissions")},
        ),
        (
            "User Secret",
            {"classes": ("collapse",), "fields": ("password", "last_login")},
        ),
        (
            "User Status",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_seller",
                    "is_active",
                    "is_verified",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
