from django.shortcuts import render

# Create your views here.
def account(request):
    context = {
        'title': "Account"
    }
    return render(request, "account/account.html",context)