from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, DetailView
from .forms import VendorForm
from .models import Vendor


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


class VendorDetail(DetailView):
    model = Vendor
    template_name = "vendor/detail.html"
