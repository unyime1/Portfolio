from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .forms import *
from .models import *
from .decorators import *

# Create your views here.

def blog(request):
    """this function handles the blog view"""
    posts = Post.objects.all().order_by('-date_published')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)

    context = {'posts':posts, 'post_page':post_page,}
    return render(request, 'blogs/blogs.html', context) 


@admin_only
def addPost(request):
    """this function returns the add post view"""

    form = postForm()
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been published')
            return redirect('blog')
    else:
        form = postForm()

    context = {'form':form,}
    return render(request, 'blogs/add_post.html', context)


@admin_only
def updatePost(request, post_id):
    """this function handles post updates"""

    post = Post.objects.get(id=post_id)
    form = postForm(instance=post)
    if request.method == "POST":
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been updated')
            return redirect('blog')
    else:
        form = postForm(instance=post)

    context = {'form':form,}
    return render(request, 'blogs/add_post.html', context)


@admin_only
def deletePost(request, post_id):
    """this function handles the removal of posts"""

    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Your post has been deleted')
    return redirect('blog')
    

def postPage(request, slug_id):
    """this function handles the post pages"""
    post = Post.objects.get(slug=slug_id)

    context = {'post':post,}
    return render(request, 'blogs/post.html', context)


def aboutPage(request):
    """this function handles the about page"""

    context = {}
    return render(request, 'blogs/about.html', context)


def contactPage(request):
    """this function handles the contact me page"""

    context = {}
    return render(request, 'blogs/contact.html', context)


