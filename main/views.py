from django.shortcuts import render
from django.http import HttpResponse
from .forms import PreferencesForm

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

#This is just a test view
def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(response):
    return render(response, "main/home.html", {})

def current_forecast(response):
    return render(response, "main/current_forecast.html", {})

def prior_forecast(response):
    return render(response, "main/prior_forecast.html", {})

def preferences(request):
    if request.method == "POST":
        UserPrefDict = {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']}

        return render(request,'main/thankyou.html', {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']})
    else:
        form = PreferencesForm()
    return render(request, 'main/preferences.html', {'form':form})

def observational_inquiry(response):
    return render(response, "main/observational_inquiry.html", {})