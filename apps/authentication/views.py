from xml.etree.ElementTree import QName
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import SignUpForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

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

    message = None

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")
    
    form = AuthenticationForm()
	
    # return render(request=request, template_name="main/login.html", context={"login_form":form})
    return render(request,"auth/login.html", {"form": form, "msg": message})
