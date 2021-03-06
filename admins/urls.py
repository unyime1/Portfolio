from django.urls import path

from . import views 

urlpatterns = [ 
    path('my-login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('panel/admin_panel/', views.adminDashboard, name='admin_panel'),
    path('panel/all_posts/', views.postList, name='all_posts'),
    path('panel/all_testimonials/', views.testimonialList, name='all_testimonials'),
    path('panel/all_projects/', views.projectList, name='all_projects'),
    path('panel/admin_contacts/', views.contactList, name='admin_contacts'),
    path('panel/message/<str:contact_id>/', views.viewMessage, name='message'),
    path('panel/delete_message/<str:contact_id>/', views.deleteMessage, name='delete_message'),
]  