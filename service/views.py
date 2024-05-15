# pylint: disable=no-member
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from price.models import Price
from service.forms import ServiceForm
from service.models import Service

# Create your views here.
def service(request):
    """
    Renders the service page with a list of services and their corresponding prices.

    This view function is responsible for displaying the service page, which includes
    a list of services and their corresponding prices. The service and price data is
    retrieved from the database and passed to the template for rendering.

    Args:
        request (django.http.request.HttpRequest): The HTTP request object.

    Returns:
        django.http.response.HttpResponse: The rendered service page.
    """
    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")
    context = {
        "title": "Our Solutions - SEO, Digital Advertising, SMM",
        "description": ("Explore Our Solutions in SEO, Digital Advertising,"
                        "Social Media Marketing, Automation, and Web & App Development"
                        "to boost your business efficiency and online presence. Contact us today!"),
        "services": services,
        "prices": price,
    }

    return render(request, "service/service.html", context)


@login_required(login_url="my-login")
def create_service(request):
    """
    Creates a new service in the system.

    This view function handles the creation of a new service. 
    It checks if the user is a superuser, and if so, it retrieves
    the latest 3 prices and all existing services. It then creates
    a ServiceForm instance and handles the form submission. If the form
    is valid, it saves the new service, sets the user who created it,
    and redirects the user to the services list page.

    Args:
        request (django.http.request.HttpRequest): The HTTP request object.

    Returns:
        django.http.response.HttpResponse: The HTTP response object,
        which renders the create-service.html template with the necessary context.
    """
    if not request.user.is_superuser:
        return redirect("service:services")

    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")

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
        "services": services,
        "prices": price,
    }
    return render(request, "service/create-service.html", context)


@login_required(login_url="my-login")
def update_service(request, pk):
    """
    Updates an existing service in the system.

    This view handles the update of a service. It first checks if the current user
    is a superuser, and if not, redirects them to the services page.
    It then retrieves the latest 3 prices and all services, ordered by their IDs.

    The view then attempts to retrieve the service with the provided `pk` (primary key).
    If the service does not exist, the user is redirected to the services page.

    If the request method is POST, the view creates a `ServiceForm` instance with the request
    data and the existing service instance. If the form is valid, the service is updated and
    the user is redirected to the services page.

    The view then renders the `update-service.html` template, passing the `ServiceForm` instance,
    the list of services, and the list of prices to the context.
    """
    if not request.user.is_superuser:
        return redirect("service:services")

    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")

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
        "services": services,
        "prices": price,
    }

    return render(request, "service/update-service.html", context)


@login_required(login_url="my-login")
def delete_service(request, pk):
    """
    Deletes an existing service from the system.

    This view handles the deletion of a service. It first checks if the current user
    is a superuser, and if not, redirects them to the services page.

    The view then retrieves the latest 3 prices and all services, ordered by their IDs.

    The view attempts to retrieve the service with the provided `pk` (primary key).
    If the service does not exist, the user is redirected to the services page.

    If the request method is POST, the view deletes the service and redirects the user
    to the services page.

    The view then renders the `delete-service.html` template, passing the list of
    services and the list of prices to the context.
    """
    if not request.user.is_superuser:
        return redirect("service:services")

    price = Price.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("id")

    try:
        serv = Service.objects.get(id=pk)

    except Service.DoesNotExist:
        return redirect("service:services")

    if request.method == "POST":
        serv.delete()
        return redirect("service:services")

    context = {
        "services": services,
        "prices": price,
    }
    return render(request, "service/delete-service.html", context)
