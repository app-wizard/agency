from django.shortcuts import render

from price.models import Price
from service.models import Service

# Create your views here.
def prices(request):
    services = Service.objects.all().order_by('id')
    pricings = Price.objects.all().order_by('id')
    context = {
        'title': "Prices",
        'pricings' : pricings,
        'services': services,
        'prices': pricings,
    }
    return render(request, "price/price.html",context)