from django.shortcuts import render

from service.models import Service

# Create your views here.
def service(request):

    services = Service.objects.all()
    context = {
        'title': "Services",
        'services': services,
    }

    return render(request, "service/service.html",context)