from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Post

class postForm(ModelForm):
    """this form handles the addition of post to site"""
    title = forms.CharField(max_length=600, required=True, label='Title',
                widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    slug = forms.CharField(max_length=600, required=True, label='Slug',
                widget=forms.TextInput(attrs={'placeholder': 'Slug'}))
    subtitle = forms.CharField(max_length=600, required=True, label='Subtitle',
                widget=forms.TextInput(attrs={'placeholder': 'Subtitle'}))
    
    featured_image = forms.ImageField()

    content = forms.CharField(max_length=20000000, required=True, label='Content',
                widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'subtitle', 'featured_image', 'content']