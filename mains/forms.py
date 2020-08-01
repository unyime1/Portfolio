from django.forms import ModelForm
from django import forms
from .models import *


class ContactForm(ModelForm):
    """this class handles the contact form"""
    first_name = forms.CharField(max_length=100, required=True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=100, required=True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=180, required=True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(max_length=3000, required=True, label='',
                    widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Contact 
        fields = '__all__' 



class projectForm(ModelForm):
    """this form handles the addition of post to site"""
    title = forms.CharField(max_length=300, required=True, label='Title',
                widget=forms.TextInput(attrs={'placeholder': 'Title'}))
 
    category = forms.CharField(max_length=300, required=True, label='Category',
                widget=forms.TextInput(attrs={'placeholder': 'Category'}))

    link = forms.CharField(max_length=300, required=True, label='Link',
                widget=forms.TextInput(attrs={'placeholder': 'Link'}))
    
    image = forms.ImageField()

    class Meta:
        model = Project
        fields = '__all__'