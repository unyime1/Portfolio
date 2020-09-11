from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from blogs.decorators import *
from blogs.models import *
from mains.models import *
from .forms import *


# Create your views here.


@login_required(login_url='home')
def adminDashboard(request):
    """this function handles the admin dashboard page"""
    posts_count = Post.objects.all().count()
    projects_count = Project.objects.all().count()
    testimonials_count = Testimonial.objects.all().count()


    context = {
        'posts_count':posts_count, 'projects_count':projects_count, 'testimonials_count':testimonials_count,

    
    }
    return render(request, 'admins/dashboard.html', context)


@login_required(login_url='home')
def postList(request):
    """this function handles the all posts page"""

    posts = Post.objects.all().order_by('-date_published')

    context = {
        'posts':posts,
    }
    return render(request, 'admins/all_posts.html', context)


@login_required(login_url='home')
def projectList(request):
    """this function handles the all projects page"""

    projects = Project.objects.all()

    context = {
        'projects':projects
    }
    return render(request, 'admins/all_projects.html', context)



@login_required(login_url='home')
def testimonialList(request):
    """this function handles the all testimonials page"""

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials':testimonials
    }
    return render(request, 'admins/all_testimonials.html', context)



@login_required(login_url='home')
def contactList(request):
    """this function handles admin contacts page"""

    contacts = Contact.objects.all().order_by('-date')

    context = {
        'contacts':contacts
    }
    return render(request, 'admins/all_contacts.html', context)



@login_required(login_url='home')
def viewMessage(request, contact_id):
    """this function handles admin message page"""

    contact = Contact.objects.get(id=contact_id)

    context = {
        'contact':contact
    }
    return render(request, 'admins/contact_message.html', context)


@login_required(login_url='home')
def deleteMessage(request, contact_id):
    """this function handles the deletion of contact messages"""

    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    messages.info(request, 'The message has been deleted')
    return redirect('admin_panel')


def userLogout(request):
    """this function handles the logout functionality"""

    logout(request)
    return redirect('home')


def userLogin(request):
    """this function handles the login view"""
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #authenticate the user
            user = authenticate(request, username=username, password=password)

            #login user
            if user is not None:
                login(request, user)
                return redirect('admin_panel')
            else:
                messages.error(request, 'Your username or password is incorrect!')
                return redirect('login')
    
    else:
        form = LoginForm()

    context = {'form':form,}
    return render(request, 'admins/login.html', context)

