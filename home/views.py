from django.shortcuts import render

from home.models import Sliders, About

# Create your views here.


def index(request):
    sliders = Sliders.objects.all()
    about = About.objects.first()
    context = {"title": "SeoAgency", "sliders": sliders, 'about' : about,}
    return render(request, "home/index.html", context)
