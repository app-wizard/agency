from django.shortcuts import render

# Create your views here.
def services(request):
    context = {
        'title': "Services"
    }
    return render(request, "service/service.html",context)