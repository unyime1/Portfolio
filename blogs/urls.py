from django.urls import path


from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add_post/', views.addPost, name='add_post'),
] 