from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import ContactInformation ,Project , Education ,Experience


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control gray-shade', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

        labels = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password1': '',
            'password2': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control gray-shade', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control gray-shade', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control gray-shade', 'placeholder': 'Confirm Password'}),

        }

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



class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'school', 'start_date', 'end_date', 'description']
        labels = {
            'degree': '',
            'school': '',
            'start_date': '',
            'end_date': '',
            'description': ''
        }
        widgets = {
            'degree':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree/Course Name/Field of Study/Diploma/Training/Bootcamp/Workshop/Online Course/Other'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School/College/University/Institute'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date' ,"placeholder": 'Start Date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date',"placeholder": 'End Date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

    
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        labels = {
            'title': '',
            'company': '',
            'start_date': '',
            'end_date': '',
            'description': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date', 'placeholder': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date', 'placeholder': 'End Date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }