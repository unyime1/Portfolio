from django.db import models

# Create your models here.

class Contact(models.Model):
    """this class handles the contact form table"""
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=20000, null=True)

    def __str__(self):
        return str(self.first_name)