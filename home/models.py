from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Sliders(models.Model):
    """
    Defines a Sliders model that represents a slider image with a title, 
    subtitle, button text, and button URL.

    The Sliders model has the following fields:
    - image: A CloudinaryField that stores the image for the slider.
    - title: A CharField that stores the title of the slider.
    - subtitle: A CharField that stores the subtitle of the slider.
    - button_text: A CharField that stores the text for the slider's button.
    - button_url: A CharField that stores the URL for the slider's button.

    The model also defines a string representation of the slider using the title field,
    and sets the verbose name plural to "Slider Section".
    """

    image = CloudinaryField("image", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Slider Section"


class About(models.Model):
    """
    Defines an About model that represents information about the website or organization.

    The About model has the following fields:
    - subtitle: A CharField that stores a subtitle for the about section.
    - title: A CharField that stores the title for the about section.
    - short_description: A CharField that stores a short description for the about section.
    - long_description: A TextField that stores a long description for the about section.
    - ranking_number: An IntegerField that stores a ranking number for the about section.
    - tag_line: A CharField that stores a tag line for the about section.
    - experience: A CharField that stores information about the experience for the about section.
    - image: A CloudinaryField that stores an image for the about section.

    The model also defines a string representation of the about section using the title field,
    and sets the verbose name plural to "About Section".
    """

    subtitle = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    ranking_number = models.IntegerField(blank=True, null=True)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)

    image = CloudinaryField("image", blank=True, null=True)
    # image2 = CloudinaryField('image2', blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        """
        Sets the verbose name plural for the About model to "About Section".
        """
        verbose_name_plural = "About Section"
