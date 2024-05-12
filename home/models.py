from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Sliders(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = "Slider Section"


class About(models.Model):
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    ranking_number = models.IntegerField(blank=True, null=True)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    
    image = CloudinaryField('image', blank=True, null=True)
    # image2 = CloudinaryField('image2', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Section"