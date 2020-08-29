from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages 
from blogs.decorators import *

# Create your views here.

def home(request):
    """this function handles the main view"""
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        #get both the username and password
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()

        
        messages.info(request, 'Hello ' + name.title() + ', your message has been sent. I will get back to you shortly.')
        return redirect('home')

    context = {'projects':projects, 'testimonials':testimonials,}
    return render(request, 'mains/index.html', context)


def addProjects(request):
    """this function handles the add project view"""
    form = projectForm()
    
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('project')
            messages.success(request, 'Your project is saved')
    else:
        form = projectForm()

    context = {'form':form,}
    return render(request, 'mains/projects-form.html', context)



def updateProject(request, project_id):
    """this function handles post updates"""

    project = Project.objects.get(id=project_id)
    form = projectForm(instance=project)
    if request.method == "POST":
        form = projectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = projectForm(instance=project)

    context = {'form':form,}
    return render(request, 'mains/projects-form.html', context)



def deleteProject(request, project_id):
    """this function handles the removal of projects"""

    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('home')


def addTestimonial(request):
    """this function handles the addition of testimonials"""
    form = testimonialForm()
    
    if request.method == 'POST':
        form = testimonialForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('testimonial')
            messages.success(request, 'Your testimonial is saved')
    else:
        form = testimonialForm()

    context = {'form':form,}
    return render(request, 'mains/testimonial.html', context)



def updateTestimonial(request, testimonial_id):
    """this function handles the update of testimonials"""

    testimonial = Testimonial.objects.get(id=testimonial_id)
    form = testimonialForm(instance=testimonial)
    if request.method == "POST":
        form = testimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial')
    else:
        form = testimonialForm(instance=testimonial)

    context = {'form':form,}
    return render(request, 'mains/testimonial.html', context)



def deleteTestimonial(request, testimonial_id):
    """this function handles the removal of testimonials"""

    testimonial = Testimonial.objects.get(id=testimonial_id)
    testimonial.delete()
    return redirect('home')

