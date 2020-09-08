from django.urls import path

from . import views 

urlpatterns = [ 
    path('panel/admin_panel/', views.adminDashboard, name='admin_panel'),
    #path('panel/all_posts/', views.postList, name='all_posts'),
    #path('panel/all_testimonials/', views.testimonialList, name='all_testimonials'),
    #path('panel/all_projects/', views.projectList, name='all_projects'),
]  