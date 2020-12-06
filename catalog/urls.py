from django.conf.urls import url
from . import views

app_name = "catalog"

urlpatterns = [
    url(
        r"^product/(?P<slug>[\w-]+)$",
        views.ProductDetail.as_view(),
        name="product_detail",
    ),
]
