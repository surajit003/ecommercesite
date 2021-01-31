from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = (
            "slug",
            "active",
            "admin_checked",
            "reviewed_by",
            "current_status",
        )
