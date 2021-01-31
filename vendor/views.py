from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, DetailView
from .forms import VendorForm
from .models import Vendor
from django.http.response import JsonResponse


# Create your views here.
class InterestView(CreateView):
    form_class = VendorForm
    model = Vendor
    template_name = "vendor/interest.html"

    def get_success_url(self):
        return reverse("vendor:thank-you")


def ThankYouView(request):
    return render(request, "vendor/thankyou.html")


class SummaryView(ListView):
    model = Vendor
    template_name = "vendor/summary.html"

    def get_queryset(self):
        return Vendor.objects.filter(active=False, admin_checked=False)


class VendorDetail(DetailView):
    model = Vendor
    template_name = "vendor/detail.html"


def change_status_of_vendor(request):
    if request.method == "POST" and request.is_ajax():
        id = request.POST.get("id")
        status = request.POST.get("status")
        if status == "active":
            active = True
        if status == "inactive":
            active = False
        vendor = Vendor.objects.get(id=id)
        vendor.active = active
        vendor.admin_checked = True
        vendor.reviewed_by = request.user
        vendor.save()
        return JsonResponse({"status": 204, "response": "Success"}, safe=False)
