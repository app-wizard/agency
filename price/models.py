from django.db import models
from ckeditor.fields import RichTextField

class Price(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)  # This field uses CKEditor
    button_text = models.CharField(max_length=300, blank=True, null=True)
    button_url = models.CharField(max_length=1000, blank=True, null=True)
    top = models.BooleanField(default=False)
    top_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.title) or ""
