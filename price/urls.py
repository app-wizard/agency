from django.urls import path
from price import views

app_name = "price"

urlpatterns = [
    path("", views.prices, name="prices"),
]
