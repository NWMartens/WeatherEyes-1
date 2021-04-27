from django.shortcuts import render
from django.http import HttpResponse
from .forms import PreferencesForm, ObsInqForm, CurrForeForm
from .forms import Frequency, Provider, StartDate, StartTime, AMorPM
from .forms import Frequency, Range, SDateForm, EDateForm
from .preferences import StorePreferencesPost
from .WebpageMongo import WebpageMongo
from .homepage import HomepagePref


# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

#This is just a test view
def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(response):
    user = response.user.username
    data = HomepagePref(user)
    return render(response, "main/home.html", {'display':data.preferences, 'Timeframe':data.timeframe, 'provider': data.provider, 'datatype':data.datatype})

def current_forecast(response, HRorDAY):
  user = response.user.username
  WM = WebpageMongo(user)
  data = WM.Current_Forecast()
  ah = data[0]
  ad = data[1]
  nh = data[2]
  nd = data[3]
  wh = data[4]
  wd = data[5]
  
  return render(response, "main/current_forecast.html", {
      'datatype':HRorDAY,

      'WeatherComDailyData': wd,
      'WeatherComHourlyData': wh,

      'AccuWeatherDailyData': ad,
      'AccuWeatherHourlyData': ah,

      'NatWeatherDailyData': nd,
      'NatWeatherHourlyData': nh
      })

def currentinquiry(request):
    if request.method == "POST":
        CurrForeDict = {'HRorDAY': request.POST['HRorDAY']}
        # Userdict = StorePreferencesPost(UserPrefDict, user)
        return current_forecast(request, request.POST['HRorDAY'])
    else:
        form = CurrForeForm()
        return render(request, 'main/currentinquiry.html', {'form':form})


def preferences(request):
      if request.method == "POST":
        UserPrefDict = {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']}
        user = request.user.username
        Userdict = StorePreferencesPost(UserPrefDict, user)
        return render(request,'main/thankyou.html', {'datatype': request.POST['datatype'], 'ServiceProvider': request.POST['ServiceProvider'],'HRorDAY': request.POST['HRorDAY'], 'Munits': request.POST['Munits'],'TempUnit': request.POST['TempUnit']})
      else:
        form = PreferencesForm()
      return render(request, 'main/preferences.html', {'form':form})

def observational_inquiry(request):
    #return render(response, "mysite/WeatherEyes-1/main/observational_inquiry.html", {})
    if request.method == 'POST':
      form = ObsInqForm(request.POST)
      
      if form.is_valid():
        HRorDAY = form.cleaned_data['HRorDAY']
        range_choice = form.cleaned_data['range_choice']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        start_am_or_pm = form.cleaned_data['start_am_or_pm']
        end_am_or_pm = form.cleaned_data['end_am_or_pm']
        WM = WebpageMongo('hanna')
        data= WM.detinqtype(HRorDAY, range_choice, start_date, end_date, start_time, end_time, start_am_or_pm, end_am_or_pm)
      
      # args = {'form': form, 'HRorDAY': HRorDAY, 'range_choice':range_choice, 'start_date': start_date, 'end_date': end_date}
      return render(request, 'main/observation.html', {
        'data':data,
        'HRorDAY': HRorDAY,
        'range_choice':range_choice, 
        'start_date': start_date, 
        'end_date': end_date})
    
    else:
        context = {}
        form = ObsInqForm()
        context['form'] = form
        return render(request, 'main/observational_inquiry.html', context)


def prior_forecast(request):
    if request.method == 'POST':
        filled_form1 = Provider(request.POST)
        filled_form2 = Frequency(request.POST)
        filled_form3 = StartDate(request.POST)
        filled_form4 = StartTime(request.POST)
        filled_form5 = AMorPM(request.POST)
        if filled_form1.is_valid() and filled_form2.is_valid() and filled_form3.is_valid() and filled_form4.is_valid() and filled_form5.is_valid():
            provider = filled_form1.cleaned_data['provider']
            datatype1 = filled_form2.cleaned_data['datatype']
            startdate = filled_form3.cleaned_data['startdate'].strftime("%b %d %Y")
            starttime = filled_form4.cleaned_data['starttime']
            am_or_pm = filled_form5.cleaned_data['am_or_pm']
            # print(provider, datatype, startdate, starttime+am_or_pm)
            # print(type(provider), type(datatype), type(startdate))
            WM = WebpageMongo('hanna')
            start = str(starttime) + " " + am_or_pm
            data = WM.Forecast_Inquiry_M2(startdate, starttime , am_or_pm ,  provider, datatype1)
            return render(request, "main/prior_forecast.html", {
            'data':data,
            'datatype': datatype1})
        else:
            provider_form = Provider()
            fre_form = Frequency()
            start_date = StartDate()
            start_time = StartTime()
            am_or_pm_form = AMorPM()
            return render(request, "main/prior_forecast.html", {
                "fre_form":fre_form, 
                "start_date":start_date,
                "provider_form":provider_form,
                "start_time":start_time,
                "am_or_pm_form":am_or_pm_form,
            })
    else:
        provider_form = Provider()
        fre_form = Frequency()
        start_date = StartDate()
        start_time = StartTime()
        am_or_pm_form = AMorPM()
        return render(request, "main/prior_forecast.html", {
            "fre_form":fre_form, 
            "start_date":start_date,
            "provider_form":provider_form,
            "start_time":start_time,
            "am_or_pm_form":am_or_pm_form,
        })
    

   