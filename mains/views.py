from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages 

# Create your views here.

def home(request):
    """this function handles the main view"""

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

    context = {'form':form,}
    return render(request, 'mains/index.html', context)