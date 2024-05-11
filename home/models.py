from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Sliders(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
    # image = models.ImageField(upload_to='Home/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = "Slider Section"