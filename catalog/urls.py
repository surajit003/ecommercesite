from django.conf.urls import url
from . import views

app_name = "catalog"

urlpatterns = [
    url(
        r"^product/(?P<slug>[\w-]+)$",
        views.ProductDetail.as_view(),
        name="product_detail",
    ),
    url(
        r"^category/(?P<slug>[\w-]+)$",
        views.CategoryDetail.as_view(),
        name="category_detail",
    ),
]
