from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=600, null=True, blank=True, unique=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    subtitle = models.CharField(max_length=600, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, null=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.CharField(max_length=20000000, null=True, blank=True)
    slug = models.SlugField(max_length=600, null=True, blank=True, unique=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    comment_content = models.CharField(max_length=1000, null=True, blank=True)
    comment_reply = models.CharField(max_length=600, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL)