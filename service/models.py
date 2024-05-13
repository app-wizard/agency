from django.db import models

# Create your models here.
# Services Model
class Service(models.Model):
    """
    Represents a service offered by the application. Each service has a name,
    a short description, and an optional FontAwesome icon class.

    Attributes:
        name (str): The name of the service.
        short_description (str): A brief description of the service.
        fontawesome_icon_class (str): The CSS class for the FontAwesome 
        icon associated with the service.
    """

    name = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=250, blank=True, null=True)
    fontawesome_icon_class = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Specifies the plural name for the Service model in the Django admin interface.
        """
        verbose_name_plural = "Service Section"
