from django.shortcuts import render, redirect
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
            form.save()
            name =  form.cleaned_data.get('first_name').capitalize()
            messages.success(request, 'Hello' + ' ' + name + ',' + ' thanks for getting in touch. I will respond to you shortly. ')
            return redirect('home')
    else:
        form = ContactForm()

    context = {'form':form, 'projects':projects,}
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


@admin_only
def updateProject(request, project_id):
    """this function handles post updates"""

    project = Project.objects.get(id=project_id)
    form = projectForm(instance=project)
    if request.method == "POST":
        form = projectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = projectForm(instance=project)

    context = {'form':form,}
    return render(request, 'mains/projects-form.html', context)


@admin_only
def deleteProject(request, project_id):
    """this function handles the removal of projects"""

    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('home')

