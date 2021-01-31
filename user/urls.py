from django.conf.urls import url
from django.contrib.auth.decorators import login_required

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
    url(
        r"^signup/(?P<confirmation_token>[0-9a-f-]+)/$",
        views.AccountSignupView.as_view(),
        name="signup_view",
    ),
    url(
        r"^verify/user-type/$",
        login_required(views.check_user_type_and_redirect),
        name="verify_user_type",
    ),
]
