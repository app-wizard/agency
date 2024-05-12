from django.shortcuts import render

from home.models import Sliders, About
from price.models import Price
from service.models import Service

# Create your views here.


def index(request):
    sliders = Sliders.objects.all()
    about = About.objects.first()
    service = Service.objects.all()
    price = Price.objects.all().order_by('id')[:3]

    context = {"title": "SeoAgency", "sliders": sliders, 'about' : about, "services": service, "prices": price,}
    return render(request, "home/index.html", context)
