from django.conf.urls import url
from . import views

app_name = "cart"

urlpatterns = [
    url(
        r"^add-to-cart/(?P<slug>[\w-]+)/$",
        views.add_to_cart,
        name="add_to_cart",
    ),
    url(
        r"^remove-from-cart/(?P<slug>[\w-]+)/$",
        views.remove_from_cart,
        name="remove_from_cart",
    ),
    url(
        r"^remove-item-from-cart/(?P<slug>[\w-]+)/$",
        views.remove_single_item_from_cart,
        name="remove-single-item-from-cart",
    ),
]
