from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages 
from blogs.decorators import *

# Create your views here.

def home(request):
    """this function handles the main view"""
    projects = Project.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()

            messages.info(request, 'Hello ' + name.title() + ', your message has been sent. I will get back to you shortly.')
            return redirect('home')
    else:
        form = ContactForm()
    context = {'projects':projects, 'form':form, }
    return render(request, 'mains/index.html', context)


@login_required(login_url='home')
def addProjects(request):
    """this function handles the add project view"""
    form = projectForm()
    template_tag = "Add"
    
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()

            messages.success(request, 'Your project is saved')
            return redirect('admin_panel')
    else:
        form = projectForm()

    context = {'form':form, 'template_tag':template_tag}
    return render(request, 'mains/projects-form.html', context)



@login_required(login_url='home')
def updateProject(request, project_id):
    """this function handles project updates"""

    project = Project.objects.get(id=project_id)
    form = projectForm(instance=project)
    template_tag = "Update"

    if request.method == "POST":
        form = projectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been updated')
            return redirect('admin_panel')
    else:
        form = projectForm(instance=project)

    context = {'form':form, 'template_tag':template_tag}
    return render(request, 'mains/projects-form.html', context)



@login_required(login_url='home')
def deleteProject(request, project_id):
    """this function handles the removal of projects"""

    project = Project.objects.get(id=project_id)
    project.delete()
    messages.success(request, 'Your project has been deleted')
    return redirect('admin_panel')


@login_required(login_url='home')
def addTestimonial(request):
    """this function handles the addition of testimonials"""
    form = testimonialForm()
    template_tag = "Add"
    
    if request.method == 'POST':
        form = testimonialForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Your testimonial is saved')
            return redirect('admin_panel')    
    else:
        form = testimonialForm()

    context = {'form':form, 'template_tag':template_tag}
    return render(request, 'mains/testimonial.html', context)



@login_required(login_url='home')
def updateTestimonial(request, testimonial_id):
    """this function handles the update of testimonials"""

    testimonial = Testimonial.objects.get(id=testimonial_id)
    form = testimonialForm(instance=testimonial)
    template_tag = "Update"

    if request.method == "POST":
        form = testimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your testimonial has been updated')
            return redirect('admin_panel')
    else:
        form = testimonialForm(instance=testimonial)

    context = {'form':form, 'template_tag':template_tag}
    return render(request, 'mains/testimonial.html', context)



@login_required(login_url='home')
def deleteTestimonial(request, testimonial_id):
    """this function handles the removal of testimonials"""

    testimonial = Testimonial.objects.get(id=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Your testimonial has been deleted')
    return redirect('admin_panel')


def productDevelopment(request):
    """this function handles the product development view"""

    form = productDevelopmentForm()
    if request.method == "POST":
        form = productDevelopmentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            form.save()
            messages.success(request, 'Hello ' + str(full_name.title()) + ', I have just received your request. I will get back to you shortly. ')
            return redirect('development')
    else:
        form = productDevelopmentForm()

    context = {'form':form,}
    return render(request, 'mains/development-form.html', context)
