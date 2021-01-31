from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor, VendorConfirmationCode
import uuid


@receiver(post_save, sender=Vendor)
def send_email_to_vendor(sender, instance, **kwargs):
    if instance.active != instance._Vendor__original_status:
        # something has changed in the active field
        code = uuid.uuid4()
        if instance.active:
            status = "Approved"
        else:
            status = "Declined"
        vendor, _ = VendorConfirmationCode.objects.get_or_create(vendor=instance)
        if _:
            vendor.confirmation_code = code
            vendor.save()
            signup_link = (
                "127.0.0.1:8084/ecommerce/accounts/signup?confirmation_token={}".format(
                    code
                )
            )
            send_mail(
                "Information about Registration ",
                "Your application has been {}.To sign Up please follow the following link {}".format(
                    status, signup_link
                ),
                "surajit.das0320@gmail.com",
                [instance.email],
                fail_silently=False,
            )
