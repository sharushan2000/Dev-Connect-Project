from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import ContactInformation ,Project


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['email', 'github', 'phone',
                  'address', 'city', 'state', 'country']
        labels = {
            'email': '',
            'github': '',
            'phone': '',
            'address': '',
            'city': '',
            'state': '',
            'country': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Github'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control',    'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control',   'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'git_url']
        labels = {
            'title': '',
            'description': '',
            'git_url': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'git_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Github URL'}),
        }