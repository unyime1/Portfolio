from django.urls import path


from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add_post/', views.addPost, name='add_post'),
    path('posts/<str:slug_id>/', views.postPage, name='posts'),
] 