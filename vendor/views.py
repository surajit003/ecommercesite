from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from .forms import VendorForm
from .models import Vendor

# Create your views here.
class InterestView(CreateView):
    form_class = VendorForm
    model = Vendor
    template_name = "vendor/interest.html"
    success_url = "/ecommerce/accounts/login/"
