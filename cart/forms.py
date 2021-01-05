from django import forms
from .models import CartItem

# this import should already be at the top
class ProductAddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = "__all__"

    # quantity = forms.IntegerField(
    #     widget=forms.TextInput(
    #         attrs={"size": "2", "value": "1", "class": "quantity", "maxlength": "5"}
    #     ),
    #     error_messages={"invalid": "Please enter a valid quantity."},
    #     min_value=1,
    # )
    # product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        print("requestssssss", self.request)
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

        # custom validation to check for cookies

    # def clean(self):
    #     print('self',self.request.test_cookie_worked())
    #     if self.request:
    #         if not self.request.session.test_cookie_worked():
    #             raise forms.ValidationError("Cookies must be enabled.")
    #     return self.cleaned_data


# override the default __init__ so we can set the request
