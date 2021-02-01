from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView
from .models import Company
from .tasks import update_profile
from catalog.models import Category
from allauth.account.views import SignupView
from vendor.models import VendorConfirmationCode
from django.contrib import messages


# Create your views here.
def ProfileView(request, profile_id):
    if request.method == "GET":
        return render(request, "account/profile.html", {"profile_id": profile_id})
    if request.method == "POST":
        try:
            phone_number = request.POST.get("phone_number")
            company_name = request.POST.get("company")
            vendor = request.POST.get("vendor")
            buyer = request.POST.get("buyer")
            if vendor:
                role = "VE"
            if buyer:
                role = "BU"
            update_profile(profile_id, company_name, phone_number, role)
        except Exception as ex:
            return redirect("user:profile", profile_id=profile_id)
        return redirect("user:company_list")


class CompanyListView(ListView):
    model = Company
    template_name = "catalog/company.html"

    def get_context_data(self, **kwargs):
        print("got here")
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = "catalog/company_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class AccountSignupView(SignupView):
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        context = super(AccountSignupView, self).get_context_data(**kwargs)
        context["confirmation_token"] = self.kwargs.get("confirmation_token")
        return context

    def form_valid(self, form):
        if self.kwargs.get("confirmation_token"):
            try:
                vendor_code = VendorConfirmationCode.objects.get(
                    confirmation_code=self.kwargs.get("confirmation_token"), valid=False
                )
                vendor_code.valid = True
                vendor_code.save()
                return super(AccountSignupView, self).form_valid(form)
            except VendorConfirmationCode.DoesNotExist:
                messages.info(
                    self.request, "Invalid Code or Already used for an existing account"
                )
                return redirect(
                    reverse(
                        "user:signup_view",
                        kwargs={
                            "confirmation_token": self.kwargs.get("confirmation_token")
                        },
                    )
                )


def check_user_type_and_redirect(request):
    if request.user.is_superuser:
        return redirect("vendor:summary")
    else:
        return redirect("catalog:index")
