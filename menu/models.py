from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    subscriber_name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)
    paypal_subscription_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscriber_name} - {self.subscription_plan} - {self.subscription_cost}'