from django.contrib import admin
from .models import Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'top')
    fields = ['title', 'subtitle', 'price', 'description', 'button_text', 'button_url', 'top', 'top_text']

