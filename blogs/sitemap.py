from django.conf import Settings
from django.contrib import sitemaps
from django.urls import reverse
from django.utils.text import slugify

from .models import Post

class PostSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = "https"
    
    def items(self):
        posts = Post.objects.all().order_by('-date_published')
        return posts

    def lastmod(self, item):
        mod_date = item.date_published
        mod_date

    def location(self, item):
        url = '/' + 'posts/' + slugify(item.title)
        return url


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = "https"

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)
