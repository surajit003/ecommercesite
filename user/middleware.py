from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile
from django.shortcuts import reverse, HttpResponseRedirect


class CheckUserhasAlreadyAddedCompany(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            print("profile", profile, profile.profile_id, profile.company)
            if not profile.company:
                while not (
                    request.path
                    == reverse(
                        "user:profile", kwargs={"profile_id": profile.profile_id}
                    )
                ):
                    return HttpResponseRedirect(
                        reverse(
                            "user:profile", kwargs={"profile_id": profile.profile_id}
                        )
                    )
            else:
                return None
