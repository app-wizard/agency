from django.urls import path
from menu import views

app_name = "menu"

urlpatterns = [
    path("", views.menu, name="menu"),
    path('subscription/<plan>', views.subscription_plans, name='subscription-plans'),
    path('create-subscription/<subID>/<plan>/<cost>', views.create_subscription, name='create-subscription'),
    path('delete-subscription/<subID>', views.delete_subscription, name='delete-subscription'),
]
