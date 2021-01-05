from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import View
from .models import Order
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            print("order", order.cart_item.all(), order.get_total())
            for i in order.cart_item.all():
                print("t", i.product.name)
            context = {"object": order}
            return render(self.request, "order/order_summary.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect(reverse("catalog:product_list"))
