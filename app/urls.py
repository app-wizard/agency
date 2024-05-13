
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("home.urls", namespace="home")),
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls", namespace="contact")),
    path('services/', include("service.urls", namespace="service")),
    path('price/', include("price.urls", namespace="price")),
    path('menu/', include("menu.urls", namespace="menu")),
]
