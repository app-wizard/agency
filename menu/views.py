from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from price.models import Price
from service.models import Service
from .models import Subscription
from .paypal import *


@login_required
def menu(request):
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by('id')[:3]
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
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by('id')[:3]

    if not Subscription.objects.filter(user=request.user).exists():
        context = {
            "plan": plan,
            'services': service,
            'prices': price,
        }
        return render(request, "menu/subscription-plans.html", context)
    else:
        return redirect("menu:menu")

@login_required(login_url="my-login")
def create_subscription(request, subID, plan, cost):

    if Subscription.objects.filter(user=request.user).exists():
        return redirect("menu/menu.html")
    service = Service.objects.all()[:4]
    price = Price.objects.all().order_by('id')[:3]

    firstName = request.user.first_name
    lastName = request.user.last_name
    fullName = f"{firstName} {lastName}"

    if fullName.strip() == "":
        fullName = request.user.username

    subscription = Subscription.objects.create(
        user=request.user,
        subscription_plan=plan,
        subscription_cost=cost,
        subscriber_name=fullName,
        paypal_subscription_id=subID,
        is_active=True,
    )

    context = {
        "SubscriptionPlan": plan,
        'services': service,
        'prices': price,
    }

    return render(request, "menu/create-subscription.html", context)


@login_required(login_url="my-login")
def delete_subscription(request, subID):
    try:
        access_token = get_access_token()
        cancel_subscription_paypal(access_token, subID)
        subscription = Subscription.objects.get(
            user=request.user, paypal_subscription_id=subID
        )
        subscription.delete()
        return render(request, "menu/delete-subscription.html")
    
    except:
        print('EXEPT')
        return render(request, "menu/menu.html")
