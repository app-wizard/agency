from django.contrib import admin
from .models import Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """
    Defines the admin interface for the `Price` model.

    The `PriceAdmin` class inherits from `admin.ModelAdmin` 
    and provides a customized admin interface for the `Price` model. 
    It specifies the fields to be displayed in the admin list view 
    (`list_display`) and the fields to be included in the admin edit form (`fields`).
    """

    list_display = ("title", "price", "top")
    fields = [
        "title",
        "subtitle",
        "price",
        "description",
        "button_text",
        "button_url",
        "top",
        "top_text",
    ]

