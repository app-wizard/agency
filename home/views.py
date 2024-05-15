# pylint: disable=no-member

from django.shortcuts import render
from home.models import Sliders, About
from price.models import Price
from service.models import Service

# Create your views here.


def index(request):
    """
    Renders the home page of the SeoAgency website.

    This view function retrieves the necessary data from the database 
    and passes it to the home/index.html template for rendering. The data includes:
    - Sliders: All instances of the Sliders model
    - About: The first instance of the About model
    - Services: All instances of the Service model
    - Prices: The first 3 instances of the Price model, ordered by ID

    The function returns the rendered HTML response for the home page.
    """
    sliders = Sliders.objects.all()
    about = About.objects.first()
    service = Service.objects.all()
    price = Price.objects.all().order_by("id")[:3]

    context = {
        'title': "SeoAgency: Leading Digital Marketing And Software Development Services",
        "description": ("Empower your business with AgencySeo's innovative digital solutions"
                        "in SEO, social media marketing, and custom software development." 
                        " Contact us today!") ,
        "sliders": sliders,
        "about": about,
        "services": service,
        "prices": price,
    }
    return render(request, "home/index.html", context)
