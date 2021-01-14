from django.shortcuts import render, redirect
from .tasks import update_profile


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
            update_profile.delay(profile_id, company_name, phone_number, role)
        except Exception as ex:
            return redirect("user:profile", profile_id=profile_id)
        return redirect("catalog:product_list")
