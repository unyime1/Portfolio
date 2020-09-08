from django.shortcuts import render, redirect
from django.contrib import messages 
from blogs.decorators import *
from blogs.models import *
from mains.models import *

# Create your views here.



def adminDashboard(request):
    """this function handles the admin dashboard page"""
    posts_count = Post.objects.all().count()
    projects_count = Project.objects.all().count()
    testimonials_count = Testimonial.objects.all().count()


    context = {
        'posts_count':posts_count, 'projects_count':projects_count, 'testimonials_count':testimonials_count,

    
    }
    return render(request, 'admins/dashboard.html', context)


