from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.name 


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    #tag = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        """this function autogenerates the slug from the title"""

        if self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        """this function solves the error associated with empty image fields"""
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    