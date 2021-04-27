import pymongo
from pymongo import MongoClient 
from .WebpageMongo import WebpageMongo
import datetime


class HomepagePref():
    """The HomepagePref Class pulls user preferences that have been set in MongoDB to then feed an object into the View.py file to ultimately be displayed on the homepage."""
    def __init__(self, username):
      """This is the constructor for the class. The constructor calls on method getpref() to begin. There are several global variables:\n
      self.user - username associate with logged-in user\n
      self.preferences - preferences that have been pulled from MongoDB\n
      self.timeframe - Hourly or Daily aspect of preferences\n
      self.provider - Weather Service Provider aspect of preferences\n
      self.datatype - Type of weather data (observation, prior forecast, forecast) aspect of preferences
      \n
      Args:\n
        Username: username associated with the logged-in user"""
      self.user = username
      self.preferences = None
      self.timeframe = None
      self.provider = None
      self.datatype = None
      self.getpref()
  
    
    def converttime(self,time):
        '''Converttime method is for converting the current time into the time an hour ago. The method also formats according to the standard format for other classes within the website.
        \n

        Args:\n
          time: the current time based on a datetimenow() filter
          \n
        Returns:\n
          Time an hour ago into a standard string format for the website purposes'''
        hour = time[11:13]
        numhour = int(hour)
        if numhour == 0:
          numhour = 23
        else:
          numhour = numhour-1
        if numhour - 12 < 0:
            amorpm = 'AM'
        else:
            amorpm = 'PM'
        modhour = numhour%12
        if modhour == 0:
            modhour = 12
        else:
            modhour = modhour
        strhour = str(modhour)
        formattime = strhour + amorpm
        return formattime

    def convertdateyesterday (self, date):
        '''Convertdateyesterday method is for converting the date of "today" to "yesterday"'s date in a standard string format for the purpose of the website.
        \n
        Args:\n
          Date: "Today"'s date from the datetimenow() function
          \n
        Returns:\n
          Date: String format that is standard for the website purposes'''
        date = date[:10]
        months = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"June","07":"July", "08":"Aug", "09":"Sept", "10":"Oct", "11":"Nov", "12":"Dec"} 
        year = date[:4]
        month = date [5:7]
        day = date[8:]
        day = int(day)
        if day ==1:
          month = int(month)
          if month in [1,2,4,6,8,9,11]:
            if month == 1:
              month = 12
            else:
              month = month - 1
            day = 31
          elif month in [5,7,10,12]:
            month = month -1
            day = 30
          elif month == 3:
            day = 28
        else:
          day = day -1
        monthabr = months.get(month)
        date = str(monthabr)+ " "+ str(day) + " " + str(year)
        return date
    
    def convertdatetoday (self, date):
        '''Convertdatetodaymethod is for converting the date of "today" into a standard string format for the purpose of the website.
        \n
        Args:\n
          Date: "Today"'s date from the datetimenow() function
          \n
        Returns:\n
          Date: String format that is standard for the website purposes'''
        date = date[:10]
        months = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"June","07":"July", "08":"Aug", "09":"Sept", "10":"Oct", "11":"Nov", "12":"Dec"} 
        year = date[:4]
        month = date [5:7]
        day = date[8:]
        monthabr = months.get(month)
        date = monthabr+" " + day+ " " + year
        return date
    
    def getpref(self):
      '''This method retrieves preference data based on user from MongoDB. This method calls displaypref() with arguments'''
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      if collection.find({'username':self.user}).count() == 0:
        return "You have not set preferences yet, please use the Update Preferences button below to set preferences"
      else:
        preferences = collection.find({'username':self.user})
        for x in preferences:
            datatype = x['datatype'] 
            ServiceProvider = x['ServiceProvider'] 
            HRorDAY = x['HRorDAY']
        self.displaypref(datatype, ServiceProvider, HRorDAY)
      
    def displaypref (self,datatype,ServiceProvider, HRorDAY):
      '''This method parses through preferences to update global variables to be called from Views.py.
      \n
      Args:\n
        datatype: The type of data the user prefers (either weather observations, prior forecast, or forecast)\n
        ServiceProvider: The service provider user selected to be applied to either prior forecast or forecast\n
        HRorDay: User preferences of hourly or daily data. For Weather Observations, data returns yesterday or an hour prior observations'''
      if datatype == "Weather Observations":
        self.datatype = "Weather Observations"
        WM = WebpageMongo(self.user)
        timenow = str(datetime.datetime.now() -datetime.timedelta(hours =4))
        if HRorDAY == "Hourly":
          timeanhourago = self.converttime(timenow)
          if len(str(timeanhourago)) < 4:
            numtime = timeanhourago[:1]
            amorpm = timeanhourago[1:]
          else:
            numtime = timeanhourago[:2]
            amorpm = timeanhourago[2:]
          time = str(numtime) + ' '+str(amorpm)
          if timeanhourago == '11PM':
            date = self.convertdateyesterday(timenow)
          else:
            date = self.convertdatetoday(timenow)
          dateandtime = str(date) + ' '+ str(time)
          self.timeframe = 'Hourly'
          self.preferences = WM.Single_Day_Inquiry_Hourly_Obs(dateandtime)
        else:
          date = self.convertdateyesterday(timenow)
          print(date)
          self.timeframe = 'Daily'
          self.preferences = WM.Single_Day_Inquriy_Obs(date)
      elif datatype == "Prior Forecast":
        WM = WebpageMongo(self.user)
        timenow = str(datetime.datetime.now() -datetime.timedelta(hours =4))
        timeanhourago = self.converttime(timenow)
        if len(timeanhourago) == 4:
          am_pm = timeanhourago[2:]
          time = timeanhourago[:2]
        if len(timeanhourago) == 3:
          am_pm = timeanhourago[1:]
          time = timeanhourago[:1]
        if timeanhourago == '12AM':
          date = self.convertdateyesterday(timenow)
        else:
          date = self.convertdatetoday(timenow)
        self.datatype = 'Prior Forecast'
        if ServiceProvider == "AccuWeather":
          self.provider = 'AccuWeather'
          if HRorDAY == "Hourly":
            self.timeframe = 'Hourly'
            self.preferences = WM.Forecast_Inquiry_M2(date, time, am_pm,"AccuWeather", "Hourly")
          else:
            self.timeframe = 'Daily'
            self.preferences = WM.Forecast_Inquiry_M2(date, time, am_pm, "AccuWeather", "Daily")
        elif ServiceProvider == "NatWeather":
          self.provider = 'NatWeather'
          if HRorDAY == "Hourly":
            self.timeframe = 'Hourly'
            self.preferences = WM.Forecast_Inquiry_M2(date,time, am_pm ,"NatWeather", "Hourly")
          else:
            self.timeframe = 'Daily'
            self.preferences = WM.Forecast_Inquiry_M2(date,time, am_pm ,"NatWeather", "Daily")
        else:
          self.provider = 'WeatherCom'
          if HRorDAY == "Hourly":
            self.timeframe = 'Hourly'
            self.preferences = WM.Forecast_Inquiry_M2(date,time, am_pm,"WeatherCom", "Hourly")
          else:
            self.timeframe = 'Daily'
            self.preferences = WM.Forecast_Inquiry_M2(date,time, am_pm,"WeatherCom", "Daily")
      else:
        self.datatype = 'Forecast'
        WM = WebpageMongo(self.user)
        data = WM.Current_Forecast()
        ah = data[0]
        ad = data[1]
        nh = data[2]
        nd = data [3]
        wh = data[4]
        wd = data[5]
        if ServiceProvider == "AccuWeather":
          self.provider = 'AccuWeather'
          if HRorDAY == "Hourly":
            self.timeframe = "Hourly"
            self.preferences = ah
          else:
            self.timeframe = "Daily"
            self.preferences = ad

        elif ServiceProvider == "NatWeather":
          self.provider = 'NatWeather'
          if HRorDAY == "Hourly":
            self.preferences = nh
            self.timeframe = "Hourly"
          else:
            self.preferences=  nd
            self.timeframe = "Daily"
        else:
          if HRorDAY == "Hourly":
            self.provider = 'WeatherCom'
            self.preferences = wh
            self.timeframe = "Hourly"
          else:
            self.preferences= wd
            self.timeframe = "Daily"