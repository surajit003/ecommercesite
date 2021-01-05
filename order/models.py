from cart.models import CartItem
from django.conf import settings
from common.models import TimeStampedModel
from django.db import models
from checkout.models import Address
from payment.models import Payment

# Create your models here.
class Order(TimeStampedModel):
    cart_item = models.ManyToManyField(CartItem)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        Address,
        related_name="shipping_address",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    billing_address = models.ForeignKey(
        Address,
        related_name="billing_address",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "OrderItems"
        verbose_name = "OrderItem"

    def __str__(self):
        return "{}".format(self.user.username)

    def get_total(self):
        total = 0
        for order_item in self.cart_item.all():
            print("i", order_item.get_final_price(), order_item.product.name)
            total += order_item.get_final_price()
        # if self.coupon:
        #     total -= self.coupon.amount
        print("tota", total)
        return total
