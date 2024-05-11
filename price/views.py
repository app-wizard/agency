from django.shortcuts import render

# Create your views here.
def prices(request):
    context = {
        'title': "Prices"
    }
    return render(request, "price/price.html",context)