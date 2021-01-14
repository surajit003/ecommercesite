from django.shortcuts import render

# Create your views here.
def ProfileView(request, profile_id):
    if request.method == "GET":
        print("entered")
        return render(request, "account/profile.html", {"profile_id": profile_id})
