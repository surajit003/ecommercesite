from django.contrib import admin
from .models import Address

# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "street_address",
        "apartment_address",
        "country",
        "zip",
        "address_type",
        "default",
    ]
    list_filter = ["default", "address_type", "country"]
    search_fields = ["user", "street_address", "apartment_address", "zip"]
