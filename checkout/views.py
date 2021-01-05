from django.shortcuts import render, redirect
from .forms import CheckoutForm
from django.views.generic import View

# Create your views here.


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        return render(self.request, "checkout/checkout.html", {"form": form})

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print("form is valid")
            return redirect("checkout:check-out")
