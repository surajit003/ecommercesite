from catalog.models import Product
from common.models import TimeStampedModel
from django.db import models
from django.conf import settings

# Create your models here.
class CartItem(TimeStampedModel):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "CartItems"
        verbose_name = "CartItem"

    def __str__(self):
        return "{} of {}".format(self.quantity, self.product.name)

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def get_total_item_price(self):
        return self.quantity * self.product.old_price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.price

    def get_amount_saved(self):
        print("amount")
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
