from django.shortcuts import render

from price.models import Price

# Create your views here.
def prices(request):
    
    pricings = Price.objects.all()

    context = {
        'title': "Prices",
        'pricings' : pricings,
    }
    return render(request, "price/price.html",context)