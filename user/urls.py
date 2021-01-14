from django.conf.urls import url
from . import views

app_name = "user"

urlpatterns = [
    url(
        r"^profile/(?P<profile_id>[0-9a-f-]+)$",
        views.ProfileView,
        name="user_profile",
    )
]