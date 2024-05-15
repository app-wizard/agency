from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    """
    Represents a user's subscription to a subscription plan.

    The `Subscription` model stores information about a user's subscription,
    including the subscriber's name, the subscription plan, the subscription cost,
    the PayPal subscription ID, and whether the subscription is currently active.
    The model also has a one-to-one relationship with the `User` model, allowing
    each user to have a single subscription.

    The `__str__` method returns a string representation of the subscription,
    including the subscriber's name, the subscription plan, and the subscription cost.
    """

    subscriber_name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)
    paypal_subscription_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscriber_name} - {self.subscription_plan} - {self.subscription_cost}"
