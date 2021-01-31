from . import views
from django.conf.urls import url

app_name = "vendor"

urlpatterns = [
    url(r"^interest/$", views.InterestView.as_view(), name="interest"),
    url(r"^thank-you/$", views.ThankYouView, name="thank-you"),
    url(r"^summary/$", views.SummaryView.as_view(), name="summary"),
    url(
        r"^(?P<slug>[\w-]+)/$",
        views.VendorDetail.as_view(),
        name="vendor_detail",
    ),
    url(
        r"^status/change-status/$",
        views.change_status_of_vendor,
        name="change-status",
    ),
    url(
        r"^assign/status/$",
        views.mark_ticket_status,
        name="ticket_status",
    ),
]
