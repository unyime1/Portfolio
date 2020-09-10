from django.db import models

# Create your models here.

class Contact(models.Model):
    """this class handles the contact form table"""
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    """this class handles the contact form table"""
    title = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/') 
    

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



class Testimonial(models.Model):
    """this class handles the contact form table"""
    name = models.CharField(max_length=500, null=True, blank=True)
    business = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/') 
    content = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        """this function solves the error associated with empty image fields"""
        try: 
            url = self.image.url
        except:
            url = ''
        return url


class ProductDevelopment(models.Model):
    """this class handles the product development table"""
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    project_title = models.CharField(max_length=500, null=True, blank=True)
    project_description = models.CharField(max_length=5000, null=True, blank=True)
    budget = models.CharField(max_length=500, null=True, blank=True)
    currency = models.CharField(max_length=500, null=True, blank=True)
    
    