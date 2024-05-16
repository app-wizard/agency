# pylint: disable=no-member
from django.shortcuts import render
from contact.forms import ContactForm
from price.models import Price
from service.models import Service



# Create your views here.
def contact(request):
    """
    View function for the contact page. Retrieves the latest 3 prices and all services,
    and renders the contact page with a contact form.

    If the form is submitted and valid, the form data is saved and the 
    contact page is rendered again.
    """
    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")
    context = {
        "title": "SeoAgency: Digital Marketing & Automation Solutions - Contact Us",
        "description": ("Explore SeoAgency's services including SEO, Digital Advertising,"
                        "and Social Media Marketing. Boost your success with our tailored"
                        "solutions. Contact us now!"),
        "services": services,
        "prices": price,
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, "contact/contact_ok.html", context)
        else:
            return render(request, "contact/contact.html", context)

    return render(request, "contact/contact.html", context)
