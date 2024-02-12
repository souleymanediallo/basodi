from django.contrib import admin
from .models import Profile, CustomUser, Address
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "last_name", "phone", "active", "created"]
    search_fields = ["user__email", "last_name", "phone", "active", "created"]
    list_filter = ["active", "created"]
    list_editable = ["active"]
    list_per_page = 10

admin.site.register(Profile, ProfileAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "firstname", "zip_code", "is_active", "is_admin", "is_staff"]
    search_fields = ["email", "firstname", "is_active", "is_admin", "is_staff"]
    list_filter = ["is_active", "is_admin", "is_staff"]
    list_editable = ["is_active"]
    list_per_page = 10

admin.site.register(CustomUser, CustomUserAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "longitude", "latitude", "district", "department", "commune", "region"]
    search_fields = ["user__email", "city", "longitude", "latitude", "district", "department", "commune", "region"]
    list_filter = ["city", "longitude", "latitude", "district", "department", "commune", "region"]
    list_per_page = 10

admin.site.register(Address, AddressAdmin)