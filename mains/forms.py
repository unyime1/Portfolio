from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import *



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




class testimonialForm(ModelForm):
    """this form handles the addition of post to site"""
    name = forms.CharField(max_length=600, required=True, label='Name',
                widget=forms.TextInput(attrs={'placeholder': 'Name'}))
 
    business = forms.CharField(max_length=600, required=True, label='Business',
                widget=forms.TextInput(attrs={'placeholder': 'Business'}))
    
    image = forms.ImageField()

    content = forms.CharField(max_length=20000000, required=True, label='Content',
                widget=SummernoteWidget())

    class Meta:
        model = Testimonial
        fields = '__all__'


CURRENCY = (
    ('Currency', 'Currency'),
    ('Naira', 'Naira'),
    ('Dollars', 'Dollars'),
    ('Euros', 'Euros'),
    ('Pounds', 'Pounds'),
)

class productDevelopmentForm(ModelForm):
    """this form handles the product development form"""
    full_name = forms.CharField(max_length=300, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Full Name(required)'}))
 
    phone_number = forms.CharField(max_length=300, required=True, label='',
                widget=forms.TextInput(attrs={'type':'number','placeholder': 'Phone Number(required)'}))
    
    email = forms.EmailField(max_length=300, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Email(required)'}))
    
    project_title = forms.CharField(max_length=400, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'What type of web product do you need?(required)'}))
    
    project_description = forms.CharField(max_length=4000, required=False, label='',
                widget=forms.Textarea(attrs={'placeholder': 'What features do you want your product to have?(optional)'}))
 
    budget = forms.CharField(max_length=400, required=True, label='',
                widget=forms.TextInput(attrs={'type':'number','placeholder': 'Enter your budget(required)'}))

    currency = forms.ChoiceField(choices=CURRENCY, label='', required=False)
 
    class Meta:
        model = ProductDevelopment
        fields = '__all__'

    def clean_currency(self):
        """this function handles currency cleaning"""
        currency = self.cleaned_data['currency']
        
        if currency == "Currency":
            raise forms.ValidationError(_('Please select a valid currency'))
        else:
            return currency


class ContactForm(ModelForm):
    """this form handles the addition of post to site"""
    name = forms.CharField(max_length=600, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Name(required)'}))
 
    email = forms.EmailField(max_length=600, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Email(required)'}))
    
    subject = forms.CharField(max_length=600, required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Subject(required)'}))
    
    message = forms.CharField(max_length=600, required=True, label='',
                widget=forms.Textarea(attrs={'placeholder': 'Message(required)'}))

    class Meta:
        model = Contact
        fields = '__all__'