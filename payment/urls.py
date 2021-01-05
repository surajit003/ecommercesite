from django.conf.urls import url
from . import views

app_name = "payment"
urlpatterns = [
    url(
        r"^pay/(?P<payment_option>[\w-]+)/$",
        views.PaymentView.as_view(),
        name="payment",
    ),
]
