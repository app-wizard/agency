from django.urls import path
from service import views

app_name = "service"

urlpatterns = [
    path("", views.service, name="services"),
    path('create-service', views.create_service, name='create-service'),
    path('update-service/<str:pk>', views.update_service, name='update-service'),
    path('delete-service/<str:pk>', views.delete_service, name='delete-service'),
]
