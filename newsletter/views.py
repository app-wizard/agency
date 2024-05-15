from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import SubscriberForm
# Create your views here.

def mailing(request):
    """
    Handles the subscription process for the newsletter mailing list.

    When a user submits the subscription form, this view processes the form data,
    saves the subscriber, and sends a confirmation email to the subscriber.

    If the form is valid, the view renders the subscription success page.
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            context = {
                "email": subscriber.email,
            }
            email_content = render_to_string(
                "newsletter/subscription_thank_you.html", context
            )
            email_subject = "Thank you for subscribing to our newsletter!"
            recipient_list = [subscriber.email]
            from_email = settings.EMAIL_HOST_USER

            send_mail(
                email_subject,
                "",
                from_email,
                recipient_list,
                html_message=email_content,
                fail_silently=False,
            )

            return render(request, "newsletter/subscription_success.html", context)
    else:
        form = SubscriberForm()
    return render(request, "newsletter/subscription_form.html", {"form": form})
