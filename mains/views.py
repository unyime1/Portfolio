from django.shortcuts import render

# Create your views here.

def home(request):
    """this function handles the main view"""

    context = {}
    return render(request, 'mains/index.html', context)