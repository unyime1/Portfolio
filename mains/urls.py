from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.addProjects, name='project'),
    path('update/<str:project_id>/', views.updateProject, name='update_project'),
    path('delete/<str:project_id>/', views.deleteProject, name='delete_project'),
] 