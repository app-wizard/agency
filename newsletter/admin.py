from typing import Any
from django.contrib import admin
from .models import Subscriber, EmailTemplate
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from ckeditor.fields import RichTextField

class EmailTemplateAdminForm(forms.ModelForm):
    """
    Defines a custom Django admin form for the `EmailTemplate` model.

    The `EmailTemplateAdminForm` class inherits from `forms.ModelForm` and provides a custom configuration for the admin interface of the `EmailTemplate` model. It sets the `message` field to use a `forms.Textarea` widget with 10 rows of height.
    """

    class Meta:
        model = EmailTemplate
        fields = '__all__'
        widgets = {
           'message': forms.Textarea(attrs={'rows': 10}),
        }

class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateAdminForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        subject = obj.subject
        html_message = obj.message

        recipients = [subscriber.email for subscriber in obj.recipients.all()]
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            "",
            from_email,
            recipients,
            html_message=html_message,
            fail_silently=False,
        )

admin.site.register(EmailTemplate, EmailTemplateAdmin)

admin.site.register(Subscriber)
