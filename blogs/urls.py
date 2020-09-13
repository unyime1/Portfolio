from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap, StaticViewSitemap

from . import views

sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSitemap,
}



urlpatterns = [
    #autogenerate sitemap
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #robots.txt
    path("robots.txt", TemplateView.as_view(template_name="blogs/robots.txt", content_type="text/plain")),
    path('blog/', views.blog, name='blog'),
    path('add_post/', views.addPost, name='add_post'),
    path('posts/<str:slug_id>/', views.postPage, name='posts'),
    path('update_posts/<str:post_id>/', views.updatePost, name='update_post'),
    path('delete_posts/<str:post_id>/', views.deletePost, name='delete_post'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),

] 