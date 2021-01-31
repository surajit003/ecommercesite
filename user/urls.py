from django.conf.urls import url
from . import views

app_name = "user"

urlpatterns = [
    url(
        r"^(?P<profile_id>[0-9a-f-]+)/$",
        views.ProfileView,
        name="profile",
    ),
    url(
        r"^company/all/$",
        views.CompanyListView.as_view(),
        name="company_list",
    ),
    url(
        r"^company/(?P<slug>[\w-]+)/$",
        views.CompanyDetailView.as_view(),
        name="company_detail",
    ),
]
