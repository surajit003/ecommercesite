from django.core.mail import send_mail
from ecommerce.celery_app import celery_app as app
from vendor.models import Vendor


@app.task(name="send_email_for_vendor_registration")
def trigger_email(msg_body, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    send_mail(
        "Information about Registration ",
        msg_body,
        "surajit.das0320@gmail.com",
        [vendor.email],
        fail_silently=False,
    )
