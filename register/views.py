from django.shortcuts import render, redirect
from .forms import RegisterForm
#from .storeregistration import StoreRegistrationPost

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})
"""
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            userinfo = {'username': response.POST['username'],'password':response.POST['password1'], 'email':response.POST['email']}
            Userdict = StoreRegistrationPost(userinfo)
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})
"""
'''
#This is commented out, because the urls.py path('', include("django.contrib.auth.urls")) draws from
#a built-in django app that creates a default login page. 
def login(response):
    return render(response, "register/login.html", {})
'''
