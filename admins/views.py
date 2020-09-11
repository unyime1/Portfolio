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


def postList(request):
    """this function handles the all posts page"""

    posts = Post.objects.all().order_by('-date_published')

    context = {
        'posts':posts,
    }
    return render(request, 'admins/all_posts.html', context)


def projectList(request):
    """this function handles the all projects page"""

    projects = Project.objects.all()

    context = {
        'projects':projects
    }
    return render(request, 'admins/all_projects.html', context)




def testimonialList(request):
    """this function handles the all testimonials page"""

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials':testimonials
    }
    return render(request, 'admins/all_testimonials.html', context)



def contactList(request):
    """this function handles admin contacts page"""

    contacts = Contact.objects.all().order_by('-date')

    context = {
        'contacts':contacts
    }
    return render(request, 'admins/all_contacts.html', context)



def viewMessage(request, contact_id):
    """this function handles admin message page"""

    contact = Contact.objects.get(id=contact_id)

    context = {
        'contact':contact
    }
    return render(request, 'admins/contact_message.html', context)



def deleteMessage(request, contact_id):
    """this function handles the deletion of contact messages"""

    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    messages.info(request, 'The message has been deleted')
    return redirect('admin_panel')
