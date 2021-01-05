from django.conf.urls import url
from . import views

app_name = "order"

urlpatterns = [
    url(
        r"^order-summary/$",
        views.OrderSummaryView.as_view(),
        name="order_summary",
    ),
]
