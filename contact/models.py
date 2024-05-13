from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
