from django import forms
from.models import Subscriber

class SubscriberForm(forms.ModelForm):
    """
    Defines a Django form for subscribing to a newsletter.

    The `SubscriberForm` class is a Django `ModelForm` that represents 
    the `Subscriber` model. It has a single field, `email`, 
    which allows users to enter their email address to subscribe to the newsletter.
    """

    class Meta:
        """
        The `Meta` class defines the configuration options for the `SubscriberForm` 
        Django form. It specifies that the form should use the `Subscriber` model, 
        and that the only field to be included in the form is the `email` field.
        """

        model = Subscriber
        fields = ["email"]
