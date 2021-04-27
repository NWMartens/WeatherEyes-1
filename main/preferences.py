#don't forget to pip install dnspython
import pymongo
from pymongo import MongoClient


class StorePreferencesPost():
    '''This class will update or store user preferences from the form displayed on the preferences.html page.'''
    def __init__ (self, dictionary, user):
      '''This is the constructor for the class.  There are several global variables:
      self. user = user that is logged into the website\n
      self.dictionary = the dictionary that represents the preferences that is passed to the class

      Values from dictionary:
        self.temp - Temperare unit preferred \n
        selt.timeframe - Hourly or Daily option preferred \n
        self.provider - Service provider preferred \n
        self.munit - Unit of Measurement \n
        self.datatype - Preferred type of weather data - Weather observations, prior forecast, or forecast
      
      self.client - client to connect to MongoDB\n
      self.db - database in MongoDB\n
      self.collection - Collection with database in MongoDB

      Args: 
      dictionary - Dictionary of user preferences from the POST request\n
      user- the active user logged into the website at the time
      '''
      self.user = user
      self.dictionary = dictionary
      self.temp = self.dictionary['TempUnit']
      self.timeframe = self.dictionary['HRorDAY']
      self.provider = self.dictionary['ServiceProvider']
      self.munit = self.dictionary['Munits']
      self.datatype = self.dictionary['datatype']
      self.client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      self.db = self.client["User"]
      self.collection = self.db['Preference']
      if self.collection.find({'username':self.user}).count() ==0:
        self.storemongo()
      else:
        self.updatemongo()

    def storemongo(self):
      '''This class will store the user's preferences in MongoDB if they have not set preferences yet with the active username.'''
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      preferences = {'username':self.user, 'datatype':self.datatype,'ServiceProvider':self.provider,'HRorDAY':self.timeframe,'Munit': self.munit,'TempUnit':self.temp}
      new_data = preferences
      post_id = collection.insert_one(new_data).inserted_id

    def updatemongo(self):
      '''This class will update the user's preferences in MongoDB if previous preferences had been established with the active username'''
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      collection.find_and_modify(query={'username': self.user}, update ={'username':self.user,'datatype':self.datatype,'ServiceProvider':self.provider,'HRorDAY':self.timeframe,'Munit': self.munit,'TempUnit':self.temp})

class Preferences:
    '''This class is pulling user unit preferences. This class is mostly a utility class for updating the units in the WebpageMongo class to then display the correct unit for the user'''
    def __init__(self, username):
        '''This is the construct for the class. There are several global variables.\n
        
        self.username - the active user in the website\n
        self.preferences - the dictionary of the user's preferences\n
        
        Values from dictionary:\n
        self.TempUnit - Temperare unit preferred\n
        self.serviceprovider - Service provider preferred\n
        self.MUnit - Unit of Measurement\n
        selt.HRorDAY - Hourly or Daily option preferred\n
        self.datatype - Preferred type of weather data - Weather observations, prior forecast, or forecast
        
        Args:\n
        username: the active user logged into the website'''
        self.username = username
        self.preferences = []
        self.pullFromMongo()
        for x in self.preferences:
            self.datatype = x['datatype'] 
            self.serviceprovider = x['ServiceProvider'] 
            self.HRorDAY = x['HRorDAY'] 
            self.TempUnit = x['TempUnit'] 
            self.MUnit = x['Munit']

    def pullFromMongo(self):
        '''This method retrieves preference data from MongoDB and updated the self.preferences variable'''
        client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['User']
        collection = db['Preference']
        self.preferences = collection.find({'username':self.username})
        

    def Temp(self):
        '''This method converts the indicated temperature unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "TemperatureK"
        elif TempUnit == 'Celsius':
            return "TemperatureC"
        elif TempUnit == 'Farenheit':
            return "TemperatureF"
            
    def UnitT(self):
        '''This method converts the indicated temperature unit preference into a temperature symbol.
        \n
        Returns:\n
        Preferred unit symbol for temperature as string'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "°K"
        elif TempUnit == 'Celsius':
            return "°C"
        elif TempUnit == 'Farenheit':
            return "°F"
    
    def UnitP(self):
        '''This method returns the indicated precipitation accumulation unit preference.
        \n
        Returns:\n
        Preferred unit of measurement'''
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Millimeters'
        elif munit == 'Inches':
            return 'Inches'

    def MinTemp(self):
        '''This method converts the indicated temperature unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MinTempK"
        elif TempUnit == 'Celsius':
            return "MinTempC"
        elif TempUnit == 'Farenheit':
            return "MinTempF"

    def MaxTemp(self):
        '''This method converts the indicated temperature unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MaxTempK"
        elif TempUnit == 'Celsius':
            return "MaxTempC"
        elif TempUnit == 'Farenheit':
            return "MaxTempF"

    def HighTemp(self):
        '''This method converts the indicated temperature unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "HighTempK"
        elif TempUnit == 'Celsius':
            return "HighTempC"
        elif TempUnit == 'Farenheit':
            return "HighTempF"

    def LowTemp(self):
        '''This method converts the indicated temperature unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "LowTempK"
        elif TempUnit == 'Celsius':
            return "LowTempC"
        elif TempUnit == 'Farenheit':
            return "LowTempF"

    def Rainunit(self):
        '''This method converts the indicated preciptation accumulation unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Rainfall_m'
        elif munit == 'Inches':
            return 'Rainfall_i'

    def Snowunit(self):
        '''This method converts the indicated preciptation accumulation unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Snowfall_m'
        elif munit == 'Inches':
            return 'Snowfall_i'

    def Precipunit(self):
        '''This method converts the indicated preciptation accumulation unit preference into a specific string. 
        \n
        Returns:\n
        The returned value is the key to a value in MongDB'''
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Precipitation_m'
        elif munit == 'Inches':
            return 'Precipitation_i'
    