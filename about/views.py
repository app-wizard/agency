from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        'title': "About Us"
    }
    return render(request, "about/about.html",context)