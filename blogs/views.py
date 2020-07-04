from django.shortcuts import render

# Create your views here.

def blog(request):
    """this function handles the blog view"""

    context = {}
    return render(request, 'blogs/blog.html', context)