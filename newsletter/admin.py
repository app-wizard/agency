from django.contrib import admin
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from ckeditor.fields import RichTextField

from .models import Subscriber, EmailTemplate
class EmailTemplateAdminForm(forms.ModelForm):
    """
    Defines a custom Django admin form for the `EmailTemplate` model.

    The `EmailTemplateAdminForm` class inherits from `forms.ModelForm` 
    and provides a custom configuration for the admin interface of the 
    `EmailTemplate` model. It sets the `message` field to use a `forms.
    Textarea` widget with 10 rows of height.
    """

    class Meta:
        model = EmailTemplate
        fields = '__all__'
        widgets = {
           'message': forms.Textarea(attrs={'rows': 10}),
        }


class EmailTemplateAdmin(admin.ModelAdmin):
    """
    Defines the admin interface for the EmailTemplate model.

    The EmailTemplateAdmin class extends the Django admin.ModelAdmin class to provide a custom
    save_model method. This method is called when an EmailTemplate object is saved through the
    Django admin interface.

    The save_model method performs the following actions:
    1. Calls the parent class's save_model method to save the EmailTemplate object.
    2. Retrieves the subject and message fields from the saved EmailTemplate object.
    3. Retrieves a list of email addresses for all Subscriber objects associated 
    with the EmailTemplate.
    4. Sends an email to the retrieved email addresses using the Django send_mail function, with the
       subject and message fields from the EmailTemplate object.
    """

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
