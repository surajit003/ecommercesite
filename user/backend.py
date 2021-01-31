from allauth.account.auth_backends import AuthenticationBackend
from django.shortcuts import redirect


class MyAuthenticationBackend(AuthenticationBackend):
    def authenticate(self, request, **credentials):
        user = super().authenticate(request, **credentials)
        print("entered")
        if user.is_superuser == True:
            return redirect("vendor:summary")
        else:
            return redirect("catalog:product_list")
