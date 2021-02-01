from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "catalog"

urlpatterns = [
    url(
        r"^product/(?P<slug>[\w-]+)/detail/$",
        views.ProductDetail.as_view(),
        name="product_detail",
    ),
    url(
        r"^category/(?P<slug>[\w-]+)$",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    url(
        r"^product/list/$",
        views.ProductList.as_view(),
        name="product_list",
    ),
    url(
        r"^product/(?P<slug>[\w-]+)/list/$",
        views.ProductListByCompany.as_view(),
        name="product_list_by_company",
    ),
    url(
        r"^index/$",
        login_required(views.Index),
        name="index",
    ),
    url(
        r"^product/create/$",
        views.CreatProduct.as_view(),
        name="product_create",
    ),
    url(
        r"^product/(?P<slug>[\w-]+)/update/$",
        views.ProductUpdate.as_view(),
        name="product_update",
    ),
    url(
        r"^product/(?P<slug>[\w-]+)/delete/$",
        views.ProductDelete.as_view(),
        name="product_delete",
    ),
]
