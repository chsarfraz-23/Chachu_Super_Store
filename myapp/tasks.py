from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from myapp.models.myapp_models import ApprovedShops


@shared_task
def shop_approval_msg(approved_shop_id: str) -> None:
    approved_shop = ApprovedShops.objects.filter(id=approved_shop_id).first()
    context = {"shop_id": approved_shop_id}
    my_subject = "Shop  Verification "
    html_message = render_to_string("shop_approval_email.html", context)
    plain_message = strip_tags(html_message)
    message = EmailMultiAlternatives(
        body=plain_message,
        subject=my_subject,
        from_email=None,
        to=[approved_shop.email],
    )
    message.attach_alternative(html_message, "text/html")
    message.send()
