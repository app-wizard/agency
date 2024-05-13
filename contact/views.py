from django.shortcuts import redirect, render

from contact.forms import ContactForm
from price.models import Price
from service.models import Service
from django.utils import timezone


# Create your views here.
def contact(request):
    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")
    context = {
        "title": "Contacts",
        "services": services,
        "prices": price,
    }

    if request.method == 'POST':
        print('tut2')
        form = ContactForm(request.POST)
        print('tut3')
        if form.is_valid():
            form.save()
            render(request, "contact/contact.html", context)
        else:
            render(request, "contact/contact.html", context)
   
    return render(request, "contact/contact.html", context)


