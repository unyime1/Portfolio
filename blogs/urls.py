from django.urls import path


from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add_post/', views.addPost, name='add_post'),
    path('posts/<str:slug_id>/', views.postPage, name='posts'),
    path('update/<str:post_id>/', views.updatePost, name='update_post'),
    path('delete/<str:post_id>/', views.deletePost, name='delete_post'),
] 