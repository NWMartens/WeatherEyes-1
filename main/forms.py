from django import forms
import datetime as dt #added

DataType = [('Weather Observations', 'Weather Observations'), ('Prior Forecast','Prior Forecast'), ('Forecast', 'Forecast')]
Providers = [('AccuWeather', 'AccuWeather'),('NatWeather', 'National Weather Service'),('WeatherCom', 'Weather.com')]
TimeFrame = [('Hourly', 'Hourly'), ('Daily','Daily')]
MUnits = [('Millimeters', 'Millimeters'), ('Inches', 'Inches')]
Temperature = [('Celsius', 'Celsius'), ('Farenheit', 'Farenheit'),('Kelvin', 'Kelvin')]

class CurrForeForm (forms.Form):
  HRorDAY = forms.CharField(label='Would you like the most recently collected hourly or by day information?', widget=forms.Select(choices=TimeFrame))


class PreferencesForm(forms.Form):
    datatype = forms.CharField(label='What type of weather data would you like on your homescreen?', widget=forms.Select(choices=DataType))
    ServiceProvider = forms.CharField(label='If applicable, what weather provider would you like the above information from? *Please note that weather observations only has one provider, National Weather Service', widget=forms.Select(choices=Providers))
    HRorDAY = forms.CharField(label='Would you like the most recently collected hourly or by day information?', widget=forms.Select(choices=TimeFrame))
    Munits = forms.CharField(label='Would you like the precipitation accumulation data to be presented in millimeters or inches?', widget=forms.Select(choices=MUnits))
    TempUnit = forms.CharField(label='Would you like temperature data to be in Celsius, Farenheit, or Kelvin?', widget=forms.Select(choices=Temperature))



# Form for observational data
DATE_RANGE = [('Single day', 'Single day'), ('Range of days', 'Range of days')]
OBSERVATION_YEARS = ['2019', '2020', '2021']
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}'.format(x)) for x in range(1, 24)]
#added

class ObsInqForm(forms.Form):
  """
  Creates forms for user to request data for past observations by selecting from a drop down menu that appears on the Observational Inquiry web page
  """
  HRorDAY = forms.CharField(label='Select the type (hourly or daily) of your inquiry', widget=forms.Select(choices=TimeFrame))
  range_choice = forms.CharField(label='Select your desired range for inquiry', widget=forms.Select(choices=DATE_RANGE))
  start_date = forms.DateField(label='Start date',widget=forms.SelectDateWidget(years=OBSERVATION_YEARS))
  end_date = forms.DateField(label='End date', widget=forms.SelectDateWidget(years=OBSERVATION_YEARS))
  start_time = forms.ChoiceField(label='Start time', #initial = '11', 
                                  choices = [('1', '1'), 
                                                  ('2', '2'), 
                                                  ('3', '3'), 
                                                  ('4', '4'),
                                                  ('5', '5'), 
                                                  ('6', '6'), 
                                                  ('7', '7'), 
                                                  ('8', '8'), 
                                                  ('9', '9'),
                                                  ('10', '10'), 
                                                  ('11', '11'), 
                                                  ('12', '12')])
  start_am_or_pm = forms.ChoiceField(label = 'AM or PM', choices=[('AM','AM'),
                                                      ('PM','PM')])
  end_time = forms.ChoiceField(label='End time', #initial = '11', 
                                  choices = [('1', '1'), 
                                                  ('2', '2'), 
                                                  ('3', '3'), 
                                                  ('4', '4'),
                                                  ('5', '5'), 
                                                  ('6', '6'), 
                                                  ('7', '7'), 
                                                  ('8', '8'), 
                                                  ('9', '9'),
                                                  ('10', '10'), 
                                                  ('11', '11'), 
                                                  ('12', '12')])
  end_am_or_pm = forms.ChoiceField(label = 'AM or PM', choices=[('AM','AM'),
                                                      ('PM','PM')])



#  Form for priorforecast data (yihui)

class Provider(forms.Form):
    provider = forms.ChoiceField(label = 'Provider', choices = [("AccuWeather", "AccuWeather"), 
                                                                ("WeatherCom", "Weather.com"),
                                                                ('NatWeather','NatWeather')])
    
class Frequency(forms.Form):
    datatype = forms.ChoiceField(label = 'Choose hourly or daily', choices=[('Daily','Daily'),
                                                                            ('Hourly','Hourly')])
  

class StartDate(forms.Form):
    #time_initial = datetime.date(2021,4,24)
    startdate = forms.DateField(label = "Start date" ,
                                #initial = time_initial,
                                widget=forms.SelectDateWidget(years=["2020", "2021"]), 
                               )

    
class StartTime(forms.Form):
    starttime = forms.ChoiceField(label='Start time', #initial = '11', 
                                  choices = [('1', '1'), 
                                                  ('2', '2'), 
                                                  ('3', '3'), 
                                                  ('4', '4'),
                                                  ('5', '5'), 
                                                  ('6', '6'), 
                                                  ('7', '7'), 
                                                  ('8', '8'), 
                                                  ('9', '9'),
                                                  ('10', '10'), 
                                                  ('11', '11'), 
                                                  ('12', '12')])
  
    
class AMorPM(forms.Form):
    am_or_pm = forms.ChoiceField(label = 'AM or PM', choices=[('AM','AM'),
                                                      ('PM','PM')])

    
class Range(forms.Form):     #s: single, r: range
    sr = forms.ChoiceField(label = 'Choose single or range', choices=[('single','Single'),  
                                                  ('range','Range')])

class SDateForm(forms.Form):
    s_day = forms.DateField(label = "Start date" ,widget=forms.SelectDateWidget(years=["2019", "2020", "2021"]))

class EDateForm(forms.Form):
    e_day = forms.DateField(label = "End date" ,widget=forms.SelectDateWidget(years=["2019", "2020", "2021"]))


# PROVIDER_CHOICES =[('Option 1','AccuWeather',), ('Option 2', 'WeatherCom'), ('Option 3', 'NatWeather')]
# INQUIRY_TYPE = [('Option 1','Hourly'), ('Option 2','Daily')]
# YEARS = ['2020', '2021']
# TIMES = [('Option 1', '1'), ('Option 2', '2'), ('Option 3', '3'), ('Option 4', '4'),
# ('Option 5', '5'), ('Option 6', '6'), ('Option 7', '7'), ('Option 8', '8'), ('Option 9', '9'),
# ('Option 10', '10'), ('Option 11', '11'), ('Option 12', '12')]
# AorP = [('Option 1', 'AM'), ('Option 2', 'PM')]

# class PastFCForm(forms.Form):
#   """
#   Creates a form with relevant options (in drop down menus) for past forecast inquiry
#   """
#   provider = forms.ChoiceField(choices=PROVIDER_CHOICES)
#   inquiry_type = forms.ChoiceField(choices=INQUIRY_TYPE)
#   start_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
#   start_time = forms.ChoiceField(choices=TIMES)
#   AM_or_PM = forms.ChoiceField(choices=AorP)

# class forecast_inquiry_conversion():
#   """
#   Gives one the ability to switch "options" from the above Django Forms to the value that the option represents
#   """

#   def __init__(self):
#     pass
  
#   def provider_switch(self, key):
#     """
#     Creates a dictionary of key/value pairs for provider options from the provider form
#     """
#     provider_dict = {}
#     for i in range(len(PROVIDER_CHOICES)):
#       option = 'Option ' + str(i+1)
#       value = PROVIDER_CHOICES[i][1]    # Retrieve value of the 'Option i' key fron PROVIDER_CHOICES list
#       provider_dict[option] = value
#     if key in provider_dict:
#       # Key was found
#       value = provider_dict[key]
#       return value
#     else:
#       # Key not found
#       return None
    
#   def inquiry_switch(self, key):
#     """
#     Creates a dictionary of key/value pairs for the different inquiry type options from the inquiry type form
#     """
#     inqtype_dict = {}
#     for i in range(len(INQUIRY_TYPE)):
#       option = 'Option ' + str(i+1)
#       value = INQUIRY_TYPE[i][1]
#       inqtype_dict[option] = value
#     if key in inqtype_dict:
#       # Key was found
#       value = inqtype_dict[key]
#       return value
#     else:
#       return None

#   def date_switch(self, _date, start_time, AM_or_PM):
#     """
#     Converts date and time into desired format that we have in our database.  Date input from the form will be in the form yyyy-mm-dd (note that month may be abbreviated if name of month is longer than 5 chars)
#     """
#     months_dict = {'01': 'Jan',
#                            '02': 'Feb',
#                            '03': 'Mar',
#                            '04': 'Apr',
#                            '05': 'May',
#                            '06': 'Jun',
#                            '07': 'Jul',
#                            '08': 'Aug',
#                            '09': 'Sep',
#                            '10': 'Oct',
#                            '11': 'Nov',
#                            '12': 'Dec'}
#     time_dict = {}
#     for i in range(len(TIMES)):
#       option = TIMES[i][0]
#       value = TIMES[i][1]
#       time_dict[option] = value
#     _date = str(_date)
#     print("Here is the date", _date)

#     split_date = _date.split('-')    # Splits date into list [month, day, , year] note that day has a trailing comma
    
#     # First, extract month
#     _month = split_date[1]
#     if _month in months_dict:
#       month = months_dict[_month]   # Key was found
    
#     else:
#       month = ''
#       print("Key was not found")

#     # Next, extract day
#     day = split_date[2]
    
#     # Third, extract year
#     year = split_date[0]

#     # Next, pull time information
#     if AM_or_PM == 'Option 1':
#       AM_or_PM = 'AM'
#     elif AM_or_PM == 'Option 2':
#       AM_or_PM = 'PM'
#     else:
#       AM_or_PM = ''
#     if start_time in time_dict:
#       time_ = time_dict[start_time] + ':00'
#     else:
#       time_ = ''
#       print("time key not found")
#     my_date = month + day + year
#     when = time_ + AM_or_PM
#     if my_date != '' and when != '':
#       return (my_date, when) 
#     else:
#       return None
