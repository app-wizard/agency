from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    """
    Configures the newsletter Django app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "newsletter"
