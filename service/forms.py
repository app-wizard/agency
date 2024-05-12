from .models import Service
from django.forms import ModelForm

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'short_description', 'fontawesome_icon_class']