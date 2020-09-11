from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, widget=forms.PasswordInput)


