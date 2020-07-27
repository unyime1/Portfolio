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
    title = models.CharField(max_length=600, null=True, blank=True, unique=True)
    subtitle = models.CharField(max_length=600, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, null=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.CharField(max_length=20000000, null=True, blank=True)
    slug = models.SlugField(max_length=600, null=True, blank=True, unique=True)
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
            url = self.image.url
        except:
            url = ''
        return url

    

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    comment_content = models.CharField(max_length=1000, null=True, blank=True)
    comment_reply = models.CharField(max_length=600, null=True, blank=True)
    

    def __str__(self):
        return self.name