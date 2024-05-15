from django.db import models
from ckeditor.fields import RichTextField

class Price(models.Model):
    """
    Represents a pricing model for a product or service.

    The `Price` model has the following fields:

    - `title`: The title of the pricing model, up to 200 characters.
    - `subtitle`: The subtitle of the pricing model, up to 100 characters.
    - `price`: The price of the product or service, up to 200 characters.
    - `description`: A rich text field for a detailed description of the pricing model.
    - `button_text`: The text to display on the call-to-action button, up to 300 characters.
    - `button_url`: The URL to link the call-to-action button to, up to 1000 characters.
    - `top`: A boolean field indicating whether this pricing model should be displayed at 
    the top of the list.
    - `top_text`: Additional text to display for the pricing model when it is at the top of 
    the list, up to 100 characters.

    The `__str__` method returns the title of the pricing model, or an empty string if the title 
    is not set.
    """

    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)  # CKEditor
    button_text = models.CharField(max_length=300, blank=True, null=True)
    button_url = models.CharField(max_length=1000, blank=True, null=True)
    top = models.BooleanField(default=False)
    top_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.title) or ""
