from cart.models import CartItem
from django.conf import settings
from common.models import TimeStampedModel
from django.db import models


# Create your models here.
class Order(TimeStampedModel):
    cart_item = models.ManyToManyField(CartItem)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "CartItems"
        verbose_name = "CartItem"

    def __str__(self):
        return "{}".format(self.user.username)
