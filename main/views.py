from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

#This is just a test view
def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(response):
    return render(response, "main/home.html", {})

def future_forecast(response):
    return render(response, "main/future_forecast.html", {})

def prior_forecast(response):
    return render(response, "main/prior_forecast.html", {})

def preferences(response):
    return render(response, "main/preferences.html", {})

def observational_inquiry(response):
    return render(response, "main/observational_inquiry.html", {})