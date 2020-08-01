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


class Project(models.Model):
    """this class handles the contact form table"""
    title = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True) #, upload_to='images/'
    

    def __str__(self):
        return str(self.title)

    @property
    def imageURL(self):
        """this function solves the error associated with empty image fields"""
        try:
            url = self.image.url
        except:
            url = ''
        return url