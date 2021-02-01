from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor, VendorConfirmationCode
import uuid
from django.conf import settings
from .tasks import trigger_email


@receiver(post_save, sender=Vendor)
def send_email_to_vendor(sender, instance, **kwargs):
    if instance.active != instance._Vendor__original_status:
        # something has changed in the active field
        code = uuid.uuid4()
        signup_link = "{}/ecommerce/account/signup/{}/".format(
            settings.SERVER_URL, code
        )
        if instance.active:
            status = "Approved"
            msg_body = "Your application has been {}.To sign Up please follow the following link {}".format(
                status, signup_link
            )
        else:
            status = "Declined"
            msg_body = "Your application has been {}.Please reach out to us for any enquiries".format(
                status, "{}".format(settings.SUPPORT_EMAIL)
            )
        vendor, _ = VendorConfirmationCode.objects.get_or_create(vendor=instance)
        if _:
            vendor.confirmation_code = code
            vendor.save()
            trigger_email.delay(msg_body, instance)
