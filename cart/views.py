from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from catalog.models import Product
from .models import CartItem
from order.models import Order
from django.utils import timezone
from django.contrib import messages


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = CartItem.objects.get_or_create(
        product=product, user=request.user, ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_item.filter(product__slug=product.slug):
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, "Item Quantity Updated")
            return redirect("order:order_summary")
        else:
            messages.info(request, "This Item was added to cart")
            order.cart_item.add(cart_item)
            return redirect("order:order_summary")
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.cart_item.add(cart_item)
    return redirect("catalog:product_detail", slug=slug)


def remove_from_cart(request, slug):
    print("entered")
    product = get_object_or_404(Product, slug=slug)
    cart_item = CartItem.objects.filter(
        product=product, user=request.user, ordered=False
    )[0]
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print("or", order)
        if order.cart_item.filter(product__slug=product.slug):
            print("got here")
            order.cart_item.remove(cart_item)
            messages.info(request, "This Item was removed from your cart")
            return redirect("catalog:product_detail", slug=slug)
        else:
            messages.info(request, "This Item is not in your cart")
            return redirect("catalog:product_detail", slug=slug)
    else:
        messages.info(request, "No order exists with that Item")
        return redirect("catalog:product_detail", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.cart_item.filter(product__slug=product.slug).exists():
            order_item = CartItem.objects.filter(
                product=product, user=request.user, ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.cart_item.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("order:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)
