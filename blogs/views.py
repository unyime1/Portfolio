from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.

def blog(request):
    """this function handles the blog view"""
    posts = Post.objects.all()

    context = {'posts':posts,}
    return render(request, 'blogs/blogs.html', context) 


def addPost(request):
    """this function returns the add post view"""

    form = postForm()
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = postForm()

    context = {'form':form,}
    return render(request, 'blogs/add_post.html', context)

def postPage(request, post_id):
    """this function handles the post pages"""
    post = Post.objects.get(id=post_id)

    context = {'post':post,}
    return render(request, 'blogs/post.html', context)