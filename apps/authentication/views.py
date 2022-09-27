from xml.etree.ElementTree import QName
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import SignUpForm 

# Create your views here.

#This request comes from django HTTP request
def user_signup_view(request): 
    success = False
    message = None
    if request.method == "POST":
        pass
    else:
        form = SignUpForm() 
    
    return render(request,"auth/signup.html", {"form": form, "msg": message, "success": success})


def login_view(request):
    pass
