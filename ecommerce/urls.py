"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

app_name = "ecommerce"
main = [
    url(r"^admin/", admin.site.urls),
    url(r"^vendor/", include("vendor.urls")),
    url(r"^catalog/", include("catalog.urls")),
    url(r"^cart/", include("cart.urls")),
    url(r"^account/", include("user.urls")),
    url(r"^order/", include("order.urls")),
    url(r"^checkout/", include("checkout.urls")),
    url(r"^accounts/", include("allauth.urls")),
    url(r"^payment/", include("payment.urls")),
    url(r"^__debug__/", include(debug_toolbar.urls)),
]

urlpatterns = (
    [url(r"^ecommerce/", include(main))]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Ecommerce Admin"
admin.site.site_title = "Ecommerce Admin Portal"
admin.site.index_title = "Welcome to Ecommerce Admin Portal"


def show_toolbar(request):
    return True


SHOW_TOOLBAR_CALLBACK = show_toolbar
