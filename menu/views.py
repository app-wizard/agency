# pylint: disable=no-member

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from price.models import Price
from service.models import Service
from .models import Subscription
from .paypal import *


@login_required
def menu(request):
    """
    Renders the menu page for authenticated users.

    If the user has an active subscription, the menu page is rendered with the subscription plan 
    details and the available services and prices.

    If the user does not have an active subscription, the menu page is rendered with a message 
    indicating that the user has no subscription.

    Args:
        request (django.http.request.HttpRequest): The HTTP request object.

    Returns:
        django.http.response.HttpResponse: The rendered menu page.
    """
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by("id")[:3]
    try:
        sub_detail = Subscription.objects.get(user=request.user, is_active=True)
        subscription_plan = sub_detail.subscription_plan
        context = {
            "title": "Menu",
            "SubscriptionPlan": subscription_plan,
            "SubscriptionID": sub_detail.paypal_subscription_id,
            "services": service,
            "prices": price,
        }
        return render(request, "menu/menu.html", context)

    except Subscription.DoesNotExist:
        subscription_plan = "No Subscription"
        context = {
            "title": "Menu",
            "SubscriptionPlan": subscription_plan,
            "services": service,
            "prices": price,
        }
        return render(request, "menu/menu.html", context)


@login_required
def subscription_plans(request, plan):
    """
    View function that renders the subscription plans page.

    If the user does not have an active subscription, this view will display the 
    available subscription plans, services, and prices. If the user already has 
    an active subscription, 
    they will be redirected to the menu page.

    Args:
        request (HttpRequest): The HTTP request object.
        plan (str): The subscription plan to display.

    Returns:
        HttpResponse: The rendered subscription plans page, 
        or a redirect to the menu page if the user already 
        has an active subscription.
    """
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by("id")[:3]

    if not Subscription.objects.filter(user=request.user).exists():
        context = {
            "plan": plan,
            "services": service,
            "prices": price,
        }
        return render(request, "menu/subscription-plans.html", context)
    else:
        return redirect("menu:menu")


@login_required(login_url="my-login")
def create_subscription(request, sub_id, plan, cost):
    """
    Creates a new subscription for the authenticated user.

    Args:
        request (django.http.request.HttpRequest): The HTTP request object.
        sub_id (str): The PayPal subscription ID.
        plan (str): The subscription plan.
        cost (float): The subscription cost.

    Returns:
        django.http.response.HttpResponse: A rendered HTML template for the created subscription.
    """
    if Subscription.objects.filter(user=request.user).exists():
        return redirect("menu/menu.html")
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by("id")[:3]

    first_name = request.user.first_name
    last_name = request.user.last_name
    full_name = f"{first_name} {last_name}"

    if full_name.strip() == "":
        full_name = request.user.username

    subscription = Subscription.objects.create(
        user=request.user,
        subscription_plan=plan,
        subscription_cost=cost,
        subscriber_name=full_name,
        paypal_subscription_id=sub_id,
        is_active=True,
    )

    context = {
        "SubscriptionPlan": plan,
        "services": service,
        "prices": price,
    }

    return render(request, "menu/create-subscription.html", context)


@login_required(login_url="my-login")
def delete_subscription(request, sub_id):
    """
    Deletes a subscription for the authenticated user.

    Args:
        request (django.http.request.HttpRequest): The HTTP request object.
        sub_id (str): The PayPal subscription ID.

    Returns:
        django.http.response.HttpResponse: A rendered HTML template for the deleted subscription.
    """
    try:
        access_token = get_access_token()
        cancel_subscription_paypal(access_token, sub_id)
        subscription = Subscription.objects.get(
            user=request.user, paypal_subscription_id=sub_id
        )
        subscription.delete()
        return render(request, "menu/delete-subscription.html")

    except Subscription.DoesNotExist:
        return render(request, "menu/menu.html")

@login_required(login_url="my-login")
def paypal_success(request):
    return render(request, "menu/paypal-success.html")
