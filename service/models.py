from django.db import models

# Create your models here.
# Services Model
class Service(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=250, blank=True, null=True)
    fontawesome_icon_class = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Service Section"