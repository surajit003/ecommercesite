from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile_number", "company", "active")
    prepopulated_fields = {"slug": ("name",)}
