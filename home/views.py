from django.shortcuts import render

from home.models import Sliders

# Create your views here.


def index(request):
    sliders = Sliders.objects.all()
    context = {"title": "SeoAgency", "sliders": sliders}
    return render(request, "home/index.html", context)
