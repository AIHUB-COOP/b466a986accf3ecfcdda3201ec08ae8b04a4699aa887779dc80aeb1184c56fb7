<<<<<<< HEAD
from xml.etree.ElementTree import QName
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import SignUpForm, LoginForm

# Create your views here.

#This request comes from django HTTP request
def user_signup_view(request): 
    success = False
    message = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            student_id = form.cleaned_data.get('studentID')
            raw_password = form.cleaned_data.get("pass1")
            user = authenticate(username=username, password=raw_password)

            message = 'User created - please <a href="/login">login</a>.'
            success = True
        else:
            print(form.errors)
            message = f'Form is not valid -- {form.errors}'
    else:
        form = SignUpForm() 
    
    return render(request,"auth/signup.html", {"form": form, "msg": message, "success": success})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "auth/login.html", {"form": form, "msg": msg})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 1f69843 (created an appl for authentication)
