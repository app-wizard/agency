
from django.contrib import admin
from django.urls import include, path
from .views import handler404, handler500, handler403, handler405

urlpatterns = [
    path('', include("home.urls", namespace="home")),
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls", namespace="contact")),
    path('services/', include("service.urls", namespace="service")),
    path('price/', include("price.urls", namespace="price")),
    path('menu/', include("menu.urls", namespace="menu")),
    path('newsletter/', include("newsletter.urls", namespace="newsletter")),
]

handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'
handler403 = 'app.views.handler403'
handler405 = 'app.views.handler405'