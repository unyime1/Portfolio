from django.shortcuts import render, redirect

from .forms import *

# Create your views here.

def blog(request):
    """this function handles the blog view"""

    context = {}
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

