from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Subscriber(models.Model):
    """
    Represents a subscriber to the newsletter.

    The `Subscriber` model stores the email address of a newsletter subscriber, 
    as well as the date and time when the subscription was created.

    Attributes:
        email (str): The email address of the subscriber.
        created_at (datetime): The date and time when the subscription was created.
    """

    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class EmailTemplate(models.Model):
    """
    Represents an email template for the newsletter.

    The `EmailTemplate` model stores the subject and message content of an email template, as well as the list of subscribers who should receive the email.

    Attributes:
        subject (str): The subject line of the email.
        message (str): The content of the email message, formatted using RichTextField.
        recipients (list of Subscriber): The list of subscribers who should receive the email.
    """

    subject = models.CharField(max_length=254)
    message = RichTextField(blank=True)
    recipients = models.ManyToManyField(Subscriber)

    def __str__(self):
        return str(self.subject)
