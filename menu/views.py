from django.shortcuts import render

# Create your views here.
def menu(request):
    context = {
        'title': "Menu"
    }
    return render(request, "menu/menu.html",context)