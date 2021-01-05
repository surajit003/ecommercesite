from django.conf.urls import url
from . import views

app_name = "checkout"

urlpatterns = [
    url(
        r"^check-out/$",
        views.CheckoutView.as_view(),
        name="check-out",
    ),
]
