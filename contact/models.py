from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    Represents a contact submitted through a contact form.

    The `Contact` model stores the following information about a contact:
    - `name`: The name of the contact.
    - `email`: The email address of the contact.
    - `phone`: The phone number of the contact (optional).
    - `message`: The message submitted by the contact.
    - `created_at`: The date the contact was created.

    The `__str__` method returns the name of the contact as a string representation.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
