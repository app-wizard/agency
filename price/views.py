# pylint: disable=no-member
from django.shortcuts import render
from price.models import Price
from service.models import Service

# Create your views here.
def prices(request):
    """
    View function that renders the prices page, displaying a list of all services and their associated prices.

    The function retrieves all Service and Price objects from the database, orders them by their respective IDs, and passes them to the template context. The template is then rendered with the provided context.
    """
    services = Service.objects.all().order_by("id")
    pricings = Price.objects.all().order_by("id")
    context = {
        "title": "Optimize Your Success with SeoAgency",
        "description": "Choose from SeoAgency's tailored SEO and digital marketing subscription plans ranging from Economy to Business packages to boost your website's performance and growth.",
        "pricings": pricings,
        "services": services,
        "prices": pricings,
    }
    return render(request, "price/price.html", context)
