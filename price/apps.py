from django.apps import AppConfig


class PriceConfig(AppConfig):
    """
    The PriceConfig class is an AppConfig subclass that configures the 'price' Django app.

    The default_auto_field attribute specifies the default primary key field type for models
    in this app, which is set to a BigAutoField.

    The name attribute specifies the name of the app, which is 'price'.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "price"
