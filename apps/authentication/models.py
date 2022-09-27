<<<<<<< HEAD
<<<<<<< HEAD
# Create your models here.
"""
Since we are using Django default User models for authentication, Using models.py file for defining Signup and Login Forms.

This code can be written in a new python file eg: forms.py
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Signup Form creation -> Will be Used in Views

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "User Name",
            "class": "form-control",
        }
        )
    )
    studentID = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Student/Staff ID",
            "class": "form-control",
        }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "form-control",
        }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter your Password",
            "class": "form-control",
        }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Re-enter your Password",
            "class": "form-control",
        }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'studentID', 'email', 'password1', 'password2')



#Login Form creation -> will be used in views @sharath


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
        }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
        }
        )
    )
=======
from django.db import models

# Create your models here.
>>>>>>> 1f69843 (created an appl for authentication)
=======
# Create your models here.
"""
Since we are using Django default User models for authentication, Using models.py file for defining Signup and Login Forms.

This code can be written in a new python file eg: forms.py
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Signup Form creation -> Will be Used in Views

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "User Name",
            "class": "form-control",
        }
        )
    )
    studentID = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Student/Staff ID",
            "class": "form-control",
        }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "form-control",
        }
        )
    )
    pass1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter your Password",
            "class": "form-control",
        }
        )
    )
    pass2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Re-enter your Password",
            "class": "form-control",
        }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'studentID', 'email', 'pass1', 'pass2')



#Login Form creation -> will be used in views @sharath
>>>>>>> 8e54605 (TEM-7 created Views and Forms for Signup)
