from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.addProjects, name='project'),
    path('product_development/', views.productDevelopment, name='development'),
    path('update_project/<str:project_id>/', views.updateProject, name='update_project'),
    path('delete_project/<str:project_id>/', views.deleteProject, name='delete_project'),
    path('testimonial/', views.addTestimonial, name='testimonial'),
    path('update_testimonial/<str:testimonial_id>/', views.updateTestimonial, name='update_testimonial'),
    path('delete_testimonial/<str:testimonial_id>/', views.deleteTestimonial, name='delete_testimonial'),
]  