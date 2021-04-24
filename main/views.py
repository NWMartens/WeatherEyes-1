from django.shortcuts import render
from django.http import HttpResponse
from .forms import PreferencesForm, PastFCForm, forecast_inquiry_conversion
from .preferences import StorePreferencesPost
from .WebpageMongo import WebpageMongo

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

def image(response):
  return render (response,"main/weatherEyes.png")


def preferences(request):
      if request.method == "POST":
        UserPrefDict = {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']}
        user = request.user.username
        Userdict = StorePreferencesPost(UserPrefDict, user)
        return render(request,'main/thankyou.html', {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']})
      else:
        form = PreferencesForm()
      return render(request, 'main/preferences.html', {'form':form})

def observational_inquiry(response):
    return render(response, "main/observational_inquiry.html", {})

def prior_forecast(request):
      if request.method =='POST':
        form = PastFCForm(request.POST)
      
        if form.is_valid():
          # Fetch sanitized input 
          _provider = form.cleaned_data['provider']
          _inquiry_type = form.cleaned_data['inquiry_type']
          _start_date = form.cleaned_data['start_date']
          _start_time = form.cleaned_data['start_time']
          _AM_or_PM = form.cleaned_data['AM_or_PM']
          
          # Convert sanitized input corresponding options 
          provider = forecast_inquiry_conversion().provider_switch(_provider)
          inquiry_type = forecast_inquiry_conversion().inquiry_switch(_inquiry_type)
          datetime_tup = forecast_inquiry_conversion().date_switch(_start_date, _start_time, _AM_or_PM)
          #date = Apr 24 2021
          #Jan012021
          #time = 11AM
          if datetime_tup != None:
            my_date = datetime_tup[0]
            my_time = datetime_tup[1]
          WM = WebpageMongo()
          month = my_date[:3]
          day = my_date[3:5]
          year = my_date[5:]
          my_date_mod = month + " " + day + " " + year
          my_time_mod = my_time[:2]+my_time[5:]
          data = WM.Forecast_Inquiry(my_date_mod, my_time_mod, provider, inquiry_type)
        args = {'form': form, 'provider': provider, 'inquiry_type': inquiry_type, 'my_date' : my_date, 'my_time': my_time}
        return render(request, 'main/prior_forecast.html', args)
      
      else:
        context = {}
        form = PastFCForm()
        context['form'] = form
        return render(request, 'main/prior_forecast.html', {'form':form})
