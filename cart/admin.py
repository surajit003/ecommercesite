from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.CartItem)
class CartItem(admin.ModelAdmin):
    list_display = (
        "id",
        "cart_id",
        "product",
    )
