from django.contrib import admin
from .models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    fieldset = (None, {"fields": ("social_name", "username")})
    list_display = ("social_name", "username", "social_url", "created_at")
    list_filter = ("created_at",)
