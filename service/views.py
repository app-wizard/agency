from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from service.forms import ServiceForm
from service.models import Service

# Create your views here.
def service(request):

    services = Service.objects.all().order_by('id')
    context = {
        'title': "Services",
        'services': services,
    }

    return render(request, "service/service.html",context)

@login_required(login_url="my-login")
def create_service(request):
    if not request.user.is_superuser:
        return redirect("service:services")

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            serv = form.save(commit=False)
            serv.user = request.user
            serv.save()
            return redirect("service:services")
    else:
        form = ServiceForm()

    context = {
        "CreateServiсeForm": form,
    }
    return render(request, "service/create-service.html", context)

@login_required(login_url="my-login")
def update_service(request, pk):
    if not request.user.is_superuser:
        return redirect("service:services")
    
    try:
        serv = Service.objects.get(id=pk)

    except Service.DoesNotExist:
        return redirect("service:services")

    form = ServiceForm(instance=serv)

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=serv)
        if form.is_valid():
            form.save()
            return redirect("service:services")
    context = {
        "UpdateServiсeForm": form,
    }

    return render(request, "service/update-service.html", context)


@login_required(login_url="my-login")
def delete_service(request, pk):
    if not request.user.is_superuser:
        return redirect("service:services")
    
    try:
        serv = Service.objects.get(id=pk)

    except Service.DoesNotExist:
        return redirect("service:services")

    if request.method == "POST":
        serv.delete()
        return redirect("service:services")

    return render(request, "service/delete-service.html")